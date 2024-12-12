import json
import os
import re
import subprocess
import time
from .server import Server 
from .py_threading import Worker
from PySide6.QtCore import QThreadPool
import requests

class Functions:
    def __init__(self) -> None:
        self.server = Server()
        self.threadPool = QThreadPool()
        self.ngrokAddress = None

    def serverConnTrigger(self, hostType: int):
        self.ngrokAddress = None
        time.sleep(1)
        if self.server.alive:
            self.runPS(r'Stop-Process -n "ngrok"')
            self.server.killServer()
        else:
            serverWorker = Worker(self.server.hostServer)
            if hostType:
                ip_port = self.setNgrok()
                if ip_port:
                    self.threadPool.start(serverWorker)
                    self.ngrokAddress = ip_port
                else:
                    self.server.signals.serverError.emit("I can't start the server check your internet connection!")
            else:
                self.threadPool.start(serverWorker)

    def lineUpCmd(self, cmd: tuple[str, dict]) -> bool:
        clientId = cmd[1]['clientid']
        for key in self.server.sel.get_map().values():
            packet = key.data
            if packet:
                if clientId == packet.clientInfo["ID"]:
                    cmd[1].pop('clientid')
                    self.server.askClient(clientId, cmd)
                    return True
                else:
                    return False
    
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
        except subprocess.CalledProcessError:
            return ''

    def setNgrok(self) -> tuple:
        cwd = os.getcwd()
        ngrokPath = cwd + r"\bin\modules\server\ngrok.exe"
        if os.path.exists(ngrokPath):
            self.runPS(r'Stop-Process -n "ngrok"')
            authentication = f"{ngrokPath} authtoken 26pI4oQ5vZ9ARZ2O8smZzKhnNtv_37oRKopTZJcgJXS1u9xhs"
            self.runPS(authentication)
            forwardPort = ngrokPath + " tcp 63999"
            ngrokWorker = Worker(self.runPS, 0, forwardPort)
            self.threadPool.start(ngrokWorker)
            tunnels = requests.get("http://localhost:4040/api/tunnels").text
            result = json.loads(tunnels)
            if result["tunnels"]:
                pubUrl = result['tunnels'][0]['public_url']
                ip_port = re.findall(r"tcp://(.+):(\d+)$", pubUrl)[0]
                return ip_port
        self.runPS(r'Stop-Process -n "ngrok"')
        return ()
