import random
import socket
import selectors
import traceback
import json

from .py_packet import ServerPacket
from PySide6.QtCore import QObject, Signal

class Server:
    def __init__(self) -> None:
        self.sel = None
        self.serverSocket = None
        self.ADDRESS = ("0.0.0.0", 63999)
        self.alive = False
        self.signals = ServerSignals()
        
    def hostServer(self):
        self.sel = selectors.DefaultSelector()
        self.serverSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)  # IPV4|TCP
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try: 
            self.serverSocket.bind(self.ADDRESS)
            self.serverSocket.listen()
            self.serverSocket.setblocking(False)
        except socket.error as err:
            self.alive = False
            self.signals.serverStatue.emit(False)
            print("[Server](hostServer):", err)
        else:
            self.signals.serverStatue.emit(True)
            self.alive = True
            self.sel.register(self.serverSocket, events=selectors.EVENT_READ, data=None)
            self.startEventLoop()

    def startEventLoop(self):
        while self.alive:
            events = self.sel.select(timeout=1)  # this line blocks
            for key, mask in events:
                if key.data == None:
                    self.acceptConn(key.fileobj)
                else:
                    packet = key.data
                    try:
                        packet.handleClient(mask)
                    except Exception as err:
                        print(traceback.format_exc())
                        print("[Server](startEventLoop):", err)
                        packet.closeConn()
        # cleanUp
        self.sel.close()
        self.signals.serverStatue.emit(False)
    
    def acceptConn(self, request: socket.socket):
        try:
            clientSocket, clientAddress = request.accept()
        except socket.error as err:
            print('[Server](acceptConn)->', err)
        else:
            packet = ServerPacket(clientSocket, clientAddress, self.sel, self.signals)
            self.sel.register(clientSocket, events=selectors.EVENT_READ, data=packet)  # register the socket for read events only (for now)
            clientId = self.createId()
            packet.clientInfo["ID"] = clientId
            packet.createPacket("str", b'getHostName')

    def killServer(self):
        if self.alive:
            self.alive = False
            try:
                self.sel.unregister(self.serverSocket)
            except Exception as err:
                print("[Server](killServer)> Error:", err)

            try:
                self.serverSocket.close()
            except OSError as err:
                print("[Server](killServer)> Error:", err)
            finally:
                # Delete reference to socket object for garbage collection
                self.serverSocket = None

    def askClient(self, clientId: str, data: tuple):
        keys = self.sel.get_map().values()
        for key in keys:
            packet = key.data
            if packet:
                if packet.clientInfo["ID"] == clientId:
                    packedData = json.dumps(data).encode('utf-8')
                    packet.createPacket(dataType='json', data=packedData, encoding='utf-8')
                    break

    def createId(self) -> str:
        clientId = f"{random.randrange(100, 999)}.{random.randrange(100, 999)}.{random.randrange(100, 999)}"
        clientIdsList = [key.data.clientInfo["ID"] for key in self.sel.get_map().values() if key.data]
        if clientId in clientIdsList:
            self.createId()
        else:
            return clientId
        
class ServerSignals(QObject):
    serverStatue = Signal(bool)
    serverError = Signal(str)
    clientJoined = Signal(dict)
    clientEscaped = Signal(dict)
    cmdResult = Signal(tuple)