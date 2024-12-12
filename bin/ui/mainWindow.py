# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowFtingI.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QPlainTextEdit,
    QProgressBar, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(765, 528)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.styles = QFrame(self.centralwidget)
        self.styles.setObjectName(u"styles")
        self.styles.setStyleSheet(u"#styles.QFrame {\n"
"background-color: rgb(33, 35, 55);\n"
"}\n"
"#frameCmdPrompt.QFrame {\n"
"	border: 1px solid rgb(255, 0, 81);\n"
"	border-radius: 10px;\n"
"}\n"
"#cmdPromptLineEditFrame.QFrame {\n"
"	background-color: rgb(48, 51, 80);\n"
"	border-radius: 10px;\n"
"}\n"
"/*_______________Fixed_Styles______________*/\n"
"/*QLineEdit*/\n"
"QLineEdit {\n"
"	border: 2px solid rgb(103, 103, 103);\n"
"	border-radius: 5px;\n"
"	background-color: Transparent;\n"
"	color: rgb(121, 121, 121);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
"QLineEdit:focus {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 2px solid rgb(189, 255, 0);\n"
"}\n"
"/*QPushButton*/\n"
"\n"
"/*QScrollBar*/\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 255, 0);\n"
"    min-widt"
                        "h: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"	border: none;\n"
"    background: transparent;\n"
"	width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"	border: none;\n"
"    background: transparent;\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 4px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 255, 0);\n"
"    m"
                        "in-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: transparent;\n"
"     height: 10px;\n"
"    border-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: transparent;\n"
"    height: 10px;\n"
"    border-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"/*QTabWidget*/\n"
"QTabWidget::pane { \n"
"	top:-1px;\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"	border: none;\n"
"	top:-1px; \n"
"}\n"
"QTabBar::tab {\n"
"	background-color: transparent;\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);\n"
"	width: 150px; "
                        "height: 30px;\n"
" }\n"
"QTabBar::tab:selected {\n"
"	border-top: 2px solid  rgb(189, 255, 0);\n"
" }\n"
"/*QComboBox*/\n"
"QComboBox{\n"
"	background-color: Transparent;\n"
"	color: rgb(230, 230, 230);\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"	border: 2px solid rgb(103, 103, 103);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	color: rgb(230, 230, 230);\n"
"	border: 2px solid rgb(189, 255, 0);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/all/bin/images/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(230, 230, 230);\n"
"	background-color: rgb(3"
                        "3, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"QProgressBar {\n"
"    background: rgb(112, 118, 130);\n"
"	color: rgb(233, 12, 89);\n"
"	font: 7pt \"Roboto\";\n"
"	text-align: right;\n"
"    border-radius: 4px;\n"
"	margin-right: 20px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(189, 255, 0);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QLabel {\n"
"	border-radius: 5px;\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"/*QPlainTextEdit*/\n"
"QPlainTextEdit {\n"
"	font: 10pt \"Terminal\";\n"
"	border: 2px solid rgb(103, 103, 103);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(47, 48, 50);\n"
"	color: rgb(121, 121, 121);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 2px solid rgb(189, 255, 0);\n"
"	background-color: rgb(14, 14, 15);\n"
"}\n"
"/*QListWidget*/\n"
"QListWidget"
                        " {\n"
"	font: 10pt \"Terminal\";\n"
"	border: 2px solid rgb(103, 103, 103);\n"
"	border-radius: 5px;\n"
"	background-color: Transparent;\n"
"	color: rgb(121, 121, 121);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
"QListWidget:focus {\n"
"	color: rgb(230, 230, 230);\n"
"	border: 2px solid rgb(189, 255, 0);\n"
"}")
        self.styles.setFrameShape(QFrame.StyledPanel)
        self.styles.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.styles)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topFrame = QFrame(self.styles)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setMaximumSize(QSize(16777215, 70))
        self.topFrame.setStyleSheet(u"")
        self.topFrame.setFrameShape(QFrame.NoFrame)
        self.topFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.topFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.topFrame)
        self.logo.setObjectName(u"logo")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QSize(110, 0))
        self.logo.setMaximumSize(QSize(110, 16777215))
        self.logo.setStyleSheet(u"image: url(:/all/bin/images/cat.png);")
        self.logo.setPixmap(QPixmap(u":/images/images/icons/logo.svg"))
        self.logo.setScaledContents(False)
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.logo)

        self.frame = QFrame(self.topFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 16pt \"Roboto\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(182, 182, 182);\n"
"font: 10pt \"Roboto\";")

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout_3.addWidget(self.topFrame)

        self.midFrame = QFrame(self.styles)
        self.midFrame.setObjectName(u"midFrame")
        self.midFrame.setFrameShape(QFrame.NoFrame)
        self.midFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.midFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frameCmdPrompt = QFrame(self.midFrame)
        self.frameCmdPrompt.setObjectName(u"frameCmdPrompt")
        self.frameCmdPrompt.setStyleSheet(u"")
        self.frameCmdPrompt.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_9 = QVBoxLayout(self.frameCmdPrompt)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.cmdPromptHeaderFame = QFrame(self.frameCmdPrompt)
        self.cmdPromptHeaderFame.setObjectName(u"cmdPromptHeaderFame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cmdPromptHeaderFame.sizePolicy().hasHeightForWidth())
        self.cmdPromptHeaderFame.setSizePolicy(sizePolicy1)
        self.cmdPromptHeaderFame.setMinimumSize(QSize(0, 15))
        self.cmdPromptHeaderFame.setMaximumSize(QSize(16777215, 15))
        self.horizontalLayout_7 = QHBoxLayout(self.cmdPromptHeaderFame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.cmdPrompt_Header = QLabel(self.cmdPromptHeaderFame)
        self.cmdPrompt_Header.setObjectName(u"cmdPrompt_Header")
        self.cmdPrompt_Header.setStyleSheet(u"\n"
"QLabel {\n"
"	color: rgb(230, 230, 230);\n"
"	font: 10pt \"Terminal\";\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"	background-image: url(:/all/bin/images/cil-terminal.png);\n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	background-origin: content;\n"
"}")
        self.cmdPrompt_Header.setTextFormat(Qt.PlainText)
        self.cmdPrompt_Header.setScaledContents(False)
        self.cmdPrompt_Header.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.cmdPrompt_Header.setMargin(0)
        self.cmdPrompt_Header.setIndent(25)
        self.cmdPrompt_Header.setOpenExternalLinks(False)

        self.horizontalLayout_7.addWidget(self.cmdPrompt_Header)


        self.verticalLayout_9.addWidget(self.cmdPromptHeaderFame)

        self.scrollArea_cmdPrompt = QScrollArea(self.frameCmdPrompt)
        self.scrollArea_cmdPrompt.setObjectName(u"scrollArea_cmdPrompt")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea_cmdPrompt.sizePolicy().hasHeightForWidth())
        self.scrollArea_cmdPrompt.setSizePolicy(sizePolicy2)
        self.scrollArea_cmdPrompt.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.scrollArea_cmdPrompt.setFrameShape(QFrame.NoFrame)
        self.scrollArea_cmdPrompt.setFrameShadow(QFrame.Plain)
        self.scrollArea_cmdPrompt.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_cmdPrompt.setWidgetResizable(True)
        self.scrollArea_cmdPrompt.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.scroll_cmdPrompt = QWidget()
        self.scroll_cmdPrompt.setObjectName(u"scroll_cmdPrompt")
        self.scroll_cmdPrompt.setGeometry(QRect(0, 0, 419, 286))
        self.scroll_cmdPrompt.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.scroll_cmdPrompt)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.vbox_cmdPrompt = QVBoxLayout()
        self.vbox_cmdPrompt.setSpacing(0)
        self.vbox_cmdPrompt.setObjectName(u"vbox_cmdPrompt")
        self.cmdPrompt_VSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vbox_cmdPrompt.addItem(self.cmdPrompt_VSpacer)


        self.verticalLayout_10.addLayout(self.vbox_cmdPrompt)

        self.scrollArea_cmdPrompt.setWidget(self.scroll_cmdPrompt)

        self.verticalLayout_9.addWidget(self.scrollArea_cmdPrompt)

        self.line_ = QFrame(self.frameCmdPrompt)
        self.line_.setObjectName(u"line_")
        self.line_.setStyleSheet(u"border-top: 1px solid rgb(93, 93, 93);")
        self.line_.setFrameShadow(QFrame.Plain)
        self.line_.setFrameShape(QFrame.HLine)

        self.verticalLayout_9.addWidget(self.line_)

        self.cmdPromptBottomFrame = QFrame(self.frameCmdPrompt)
        self.cmdPromptBottomFrame.setObjectName(u"cmdPromptBottomFrame")
        sizePolicy1.setHeightForWidth(self.cmdPromptBottomFrame.sizePolicy().hasHeightForWidth())
        self.cmdPromptBottomFrame.setSizePolicy(sizePolicy1)
        self.cmdPromptBottomFrame.setMinimumSize(QSize(0, 60))
        self.cmdPromptBottomFrame.setMaximumSize(QSize(16777215, 60))
        self.cmdPromptBottomFrame.setStyleSheet(u"")
        self.verticalLayout_12 = QVBoxLayout(self.cmdPromptBottomFrame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, -1, -1, 9)
        self.cmdPromptLineEditFrame = QFrame(self.cmdPromptBottomFrame)
        self.cmdPromptLineEditFrame.setObjectName(u"cmdPromptLineEditFrame")
        self.cmdPromptLineEditFrame.setMaximumSize(QSize(16777215, 16777215))
        self.cmdPromptLineEditFrame.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.cmdPromptLineEditFrame)
        self.horizontalLayout_8.setSpacing(9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(6, 7, 6, 6)
        self.btn_addFile = QPushButton(self.cmdPromptLineEditFrame)
        self.btn_addFile.setObjectName(u"btn_addFile")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_addFile.sizePolicy().hasHeightForWidth())
        self.btn_addFile.setSizePolicy(sizePolicy3)
        self.btn_addFile.setMinimumSize(QSize(30, 30))
        self.btn_addFile.setMaximumSize(QSize(30, 30))
        self.btn_addFile.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_addFile.setStyleSheet(u"QPushButton {\n"
"	border-radius: 15px;\n"
"	background-color:  transparent;\n"
"	background-repeat: no-reperat;\n"
"	image: url(:/all/bin/images/msgAddFile.png);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:  rgb(103, 110, 121);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:  rgb(85, 90, 99);\n"
"}")

        self.horizontalLayout_8.addWidget(self.btn_addFile, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.cmdPromptPlainText = QPlainTextEdit(self.cmdPromptLineEditFrame)
        self.cmdPromptPlainText.setObjectName(u"cmdPromptPlainText")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.cmdPromptPlainText.sizePolicy().hasHeightForWidth())
        self.cmdPromptPlainText.setSizePolicy(sizePolicy4)
        self.cmdPromptPlainText.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: Transparent;\n"
"	border: none;\n"
"	color: rgb(241, 241, 241);\n"
"	\n"
"	font: 11pt \"Roboto\";\n"
"}")
        self.cmdPromptPlainText.setFrameShape(QFrame.NoFrame)
        self.cmdPromptPlainText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.cmdPromptPlainText.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.cmdPromptPlainText.setTabChangesFocus(False)
        self.cmdPromptPlainText.setReadOnly(False)
        self.cmdPromptPlainText.setOverwriteMode(False)
        self.cmdPromptPlainText.setMaximumBlockCount(0)
        self.cmdPromptPlainText.setBackgroundVisible(False)
        self.cmdPromptPlainText.setCenterOnScroll(False)

        self.horizontalLayout_8.addWidget(self.cmdPromptPlainText)

        self.btn_sendIt = QPushButton(self.cmdPromptLineEditFrame)
        self.btn_sendIt.setObjectName(u"btn_sendIt")
        sizePolicy3.setHeightForWidth(self.btn_sendIt.sizePolicy().hasHeightForWidth())
        self.btn_sendIt.setSizePolicy(sizePolicy3)
        self.btn_sendIt.setMinimumSize(QSize(30, 30))
        self.btn_sendIt.setMaximumSize(QSize(30, 30))
        self.btn_sendIt.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sendIt.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:  transparent;\n"
"	background-repeat: no-reperat;\n"
"	image: url(:/all/bin/images/icons8-send-24hover.png);\n"
"}\n"
"QPushButton:pressed {\n"
"	image: url(:/all/bin/images/icons8-send-24.png);\n"
"}")

        self.horizontalLayout_8.addWidget(self.btn_sendIt)


        self.verticalLayout_12.addWidget(self.cmdPromptLineEditFrame)


        self.verticalLayout_9.addWidget(self.cmdPromptBottomFrame)


        self.horizontalLayout.addWidget(self.frameCmdPrompt)

        self.midRightFrame = QFrame(self.midFrame)
        self.midRightFrame.setObjectName(u"midRightFrame")
        self.midRightFrame.setMinimumSize(QSize(300, 0))
        self.midRightFrame.setMaximumSize(QSize(300, 16777215))
        self.midRightFrame.setStyleSheet(u"background-color: rgb(33, 35, 55);")
        self.midRightFrame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.midRightFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.midRightFrame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.toolsTab = QWidget()
        self.toolsTab.setObjectName(u"toolsTab")
        self.verticalLayout_5 = QVBoxLayout(self.toolsTab)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.toolsTab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 292, 478))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.plainTextEdit_description = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit_description.setObjectName(u"plainTextEdit_description")
        self.plainTextEdit_description.setMinimumSize(QSize(0, 200))
        self.plainTextEdit_description.setMaximumSize(QSize(16777215, 200))
        self.plainTextEdit_description.setFrameShape(QFrame.NoFrame)
        self.plainTextEdit_description.setFrameShadow(QFrame.Plain)

        self.gridLayout_2.addWidget(self.plainTextEdit_description, 3, 0, 1, 1)

        self.listWidget_tools = QListWidget(self.scrollAreaWidgetContents_2)
        QListWidgetItem(self.listWidget_tools)
        QListWidgetItem(self.listWidget_tools)
        QListWidgetItem(self.listWidget_tools)
        QListWidgetItem(self.listWidget_tools)
        self.listWidget_tools.setObjectName(u"listWidget_tools")
        self.listWidget_tools.setMinimumSize(QSize(0, 200))
        self.listWidget_tools.setMaximumSize(QSize(16777215, 200))
        self.listWidget_tools.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 11pt \"Roboto\";")
        self.listWidget_tools.setFrameShape(QFrame.NoFrame)
        self.listWidget_tools.setFrameShadow(QFrame.Plain)
        self.listWidget_tools.setFlow(QListView.TopToBottom)
        self.listWidget_tools.setProperty("isWrapping", False)
        self.listWidget_tools.setResizeMode(QListView.Fixed)
        self.listWidget_tools.setLayoutMode(QListView.SinglePass)
        self.listWidget_tools.setSpacing(2)

        self.gridLayout_2.addWidget(self.listWidget_tools, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 5, 0, 1, 1)

        self.label_12 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 20))
        self.label_12.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)

        self.label_14 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 20))
        self.label_14.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_14, 2, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_5.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.toolsTab, "")
        self.hostTab = QWidget()
        self.hostTab.setObjectName(u"hostTab")
        self.verticalLayout_11 = QVBoxLayout(self.hostTab)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.hostTab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 300, 371))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 20))
        self.label_13.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_13, 3, 0, 1, 1)

        self.btn_hostServer = QPushButton(self.scrollAreaWidgetContents)
        self.btn_hostServer.setObjectName(u"btn_hostServer")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_hostServer.sizePolicy().hasHeightForWidth())
        self.btn_hostServer.setSizePolicy(sizePolicy5)
        self.btn_hostServer.setMinimumSize(QSize(0, 35))
        self.btn_hostServer.setMaximumSize(QSize(274, 35))
        self.btn_hostServer.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(92, 108, 255);\n"
"	border-radius: 5px;\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"	border-left: 2px solid  rgb(233, 12, 89);\n"
"\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(71, 82, 196);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(60, 69, 165);\n"
"}")
        self.btn_hostServer.setIconSize(QSize(24, 24))
        self.btn_hostServer.setCheckable(False)
        self.btn_hostServer.setChecked(False)
        self.btn_hostServer.setAutoRepeat(False)
        self.btn_hostServer.setAutoExclusive(False)

        self.gridLayout.addWidget(self.btn_hostServer, 0, 0, 1, 2)

        self.listWidget_Clients = QListWidget(self.scrollAreaWidgetContents)
        self.listWidget_Clients.setObjectName(u"listWidget_Clients")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.listWidget_Clients.sizePolicy().hasHeightForWidth())
        self.listWidget_Clients.setSizePolicy(sizePolicy6)
        self.listWidget_Clients.setMinimumSize(QSize(274, 150))
        self.listWidget_Clients.setMaximumSize(QSize(274, 150))
        self.listWidget_Clients.setStyleSheet(u"color: rgb(230, 230, 230);\n"
"font: 10pt \"Terminal\";")
        self.listWidget_Clients.setFrameShape(QFrame.NoFrame)
        self.listWidget_Clients.setFrameShadow(QFrame.Plain)
        self.listWidget_Clients.setSpacing(2)

        self.gridLayout.addWidget(self.listWidget_Clients, 4, 0, 1, 2)

        self.btn_createSpy = QPushButton(self.scrollAreaWidgetContents)
        self.btn_createSpy.setObjectName(u"btn_createSpy")
        self.btn_createSpy.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.btn_createSpy.sizePolicy().hasHeightForWidth())
        self.btn_createSpy.setSizePolicy(sizePolicy5)
        self.btn_createSpy.setMinimumSize(QSize(0, 35))
        self.btn_createSpy.setMaximumSize(QSize(274, 35))
        self.btn_createSpy.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(92, 108, 255);\n"
"	border-radius: 5px;\n"
"	font: 700 11pt \"Roboto\";\n"
"	color: rgb(255, 255, 255);\n"
"	border-left: 2px solid  rgb(233, 12, 89); /*rgb(189, 255, 0);*/\n"
"	text-align: left;\n"
"	padding-left: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(71, 82, 196);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(60, 69, 165);\n"
"}")
        self.btn_createSpy.setIconSize(QSize(24, 24))
        self.btn_createSpy.setCheckable(False)
        self.btn_createSpy.setChecked(False)
        self.btn_createSpy.setAutoRepeat(False)
        self.btn_createSpy.setAutoExclusive(False)

        self.gridLayout.addWidget(self.btn_createSpy, 6, 0, 1, 1)

        self.cbox_hostType = QComboBox(self.scrollAreaWidgetContents)
        self.cbox_hostType.addItem("")
        self.cbox_hostType.addItem("")
        self.cbox_hostType.setObjectName(u"cbox_hostType")
        self.cbox_hostType.setMinimumSize(QSize(274, 0))
        self.cbox_hostType.setMaximumSize(QSize(274, 16777215))
        self.cbox_hostType.setStyleSheet(u"")

        self.gridLayout.addWidget(self.cbox_hostType, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 20))
        self.label_15.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_15, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_11.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.hostTab, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.horizontalLayout.addWidget(self.midRightFrame)


        self.verticalLayout_3.addWidget(self.midFrame)

        self.bottomFrame = QFrame(self.styles)
        self.bottomFrame.setObjectName(u"bottomFrame")
        self.bottomFrame.setMaximumSize(QSize(16777215, 40))
        self.bottomFrame.setFrameShape(QFrame.NoFrame)
        self.bottomFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.bottomFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_2 = QFrame(self.bottomFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_2)

        self.Hspacer = QSpacerItem(544, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.Hspacer)

        self.bottomFrame_checkBox_cpuToggle = QRadioButton(self.bottomFrame)
        self.bottomFrame_checkBox_cpuToggle.setObjectName(u"bottomFrame_checkBox_cpuToggle")
        self.bottomFrame_checkBox_cpuToggle.setMaximumSize(QSize(21, 21))
        self.bottomFrame_checkBox_cpuToggle.setCursor(QCursor(Qt.PointingHandCursor))
        self.bottomFrame_checkBox_cpuToggle.setStyleSheet(u"QRadioButton::indicator {\n"
"    border: 2px solid rgb(103, 103, 103);\n"
"	width: 16px;\n"
"	height: 16px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid rgb(141, 141, 141);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(186, 251, 0);\n"
"}")

        self.horizontalLayout_3.addWidget(self.bottomFrame_checkBox_cpuToggle)

        self.label_11 = QLabel(self.bottomFrame)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)
        self.label_11.setMaximumSize(QSize(16777215, 20))
        self.label_11.setStyleSheet(u"")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_11)

        self.CPUprogressBar = QProgressBar(self.bottomFrame)
        self.CPUprogressBar.setObjectName(u"CPUprogressBar")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.CPUprogressBar.sizePolicy().hasHeightForWidth())
        self.CPUprogressBar.setSizePolicy(sizePolicy7)
        self.CPUprogressBar.setMinimumSize(QSize(225, 8))
        self.CPUprogressBar.setMaximumSize(QSize(225, 8))
        self.CPUprogressBar.setStyleSheet(u"")
        self.CPUprogressBar.setMinimum(0)
        self.CPUprogressBar.setMaximum(100)
        self.CPUprogressBar.setValue(0)
        self.CPUprogressBar.setTextVisible(True)
        self.CPUprogressBar.setInvertedAppearance(False)
        self.CPUprogressBar.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_3.addWidget(self.CPUprogressBar)


        self.verticalLayout_3.addWidget(self.bottomFrame)


        self.verticalLayout.addWidget(self.styles)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Spy-Cat", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"v1.0.0 (64-bit)", None))
        self.cmdPrompt_Header.setText(QCoreApplication.translate("MainWindow", u"Command Prompt", None))
#if QT_CONFIG(tooltip)
        self.btn_addFile.setToolTip(QCoreApplication.translate("MainWindow", u"add file", None))
#endif // QT_CONFIG(tooltip)
        self.btn_addFile.setText("")
#if QT_CONFIG(tooltip)
        self.cmdPromptPlainText.setToolTip(QCoreApplication.translate("MainWindow", u"send:ctrl+enter", None))
#endif // QT_CONFIG(tooltip)
        self.cmdPromptPlainText.setPlainText("")
        self.cmdPromptPlainText.setPlaceholderText(QCoreApplication.translate("MainWindow", u">>>", None))
#if QT_CONFIG(tooltip)
        self.btn_sendIt.setToolTip(QCoreApplication.translate("MainWindow", u"ctrl+enter", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_sendIt.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.btn_sendIt.setText("")
#if QT_CONFIG(shortcut)
        self.btn_sendIt.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)

        __sortingEnabled = self.listWidget_tools.isSortingEnabled()
        self.listWidget_tools.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_tools.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"FreeClient clientId=?", None));
        ___qlistwidgetitem1 = self.listWidget_tools.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PS clientId=?, psFile=?", None));
        ___qlistwidgetitem2 = self.listWidget_tools.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"GetChromeDump clientId=?", None));
        ___qlistwidgetitem3 = self.listWidget_tools.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"GetWifiDump clientId=?", None));
        self.listWidget_tools.setSortingEnabled(__sortingEnabled)

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.toolsTab), QCoreApplication.translate("MainWindow", u"Tools", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Clients", None))
        self.btn_hostServer.setText(QCoreApplication.translate("MainWindow", u"Host", None))
        self.btn_createSpy.setText(QCoreApplication.translate("MainWindow", u"Create Spy", None))
        self.cbox_hostType.setItemText(0, QCoreApplication.translate("MainWindow", u"LAN/WAN", None))
        self.cbox_hostType.setItemText(1, QCoreApplication.translate("MainWindow", u"Internet", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Host type", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hostTab), QCoreApplication.translate("MainWindow", u"Host", None))
#if QT_CONFIG(tooltip)
        self.bottomFrame_checkBox_cpuToggle.setToolTip(QCoreApplication.translate("MainWindow", u"Toggle CpuUsage", None))
#endif // QT_CONFIG(tooltip)
        self.bottomFrame_checkBox_cpuToggle.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.CPUprogressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
    # retranslateUi

