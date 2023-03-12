


from PyQt5 import QtCore, QtGui, QtWidgets
from assets.medias.qrcs import jojo_BG, mha_BG, mob_BG, tye_BG
from assets.files.ARRAYS import *
from assets.files._backUpFiles import backupAllFiles

import sys, os, csv
import StartWindow

class Ui_BrowseWindow(object):
    def setupUi(self, BrowseWindow):

        ''' FUNCTIONS '''
        def closeApp():
            sys.exit()

        def enterStartWindow():

            # Showing new window
            self.ui = StartWindow.Ui_StartWindow()
            self.window = QtWidgets.QMainWindow()
            self.ui.setupUi(self.window)
            self.window.show()

            # Hiding current window
            BrowseWindow.hide()

            print("Routing to StartWindow!")

        def logoutUser():

            # Removing current user
            currentUser.clear()

            # Routes back to StartWindow
            if len(currentUser) == 0:
                enterStartWindow()

        BrowseWindow.setObjectName("BrowseWindow")
        BrowseWindow.resize(900, 800)
        BrowseWindow.setMinimumSize(QtCore.QSize(900, 800))
        BrowseWindow.setMaximumSize(QtCore.QSize(900, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/imgs/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BrowseWindow.setWindowIcon(icon)
        BrowseWindow.setStyleSheet("background-color: rgb(25, 25, 25);")
        self.centralwidget = QtWidgets.QWidget(BrowseWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BrowseWindow_ExitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.BrowseWindow_ExitBtn.clicked.connect(closeApp)
        self.BrowseWindow_ExitBtn.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.BrowseWindow_ExitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BrowseWindow_ExitBtn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: none;\n"
"    font-size: 19px;\n"
"    color:  rgb(255, 66, 69);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(255, 66, 69);\n"
"    color: white;\n"
"}")
        self.BrowseWindow_ExitBtn.setObjectName("BrowseWindow_ExitBtn")
        self.BrowseWindow_LogoutBtn = QtWidgets.QPushButton(self.centralwidget)
        self.BrowseWindow_LogoutBtn.clicked.connect(logoutUser)
        self.BrowseWindow_LogoutBtn.setGeometry(QtCore.QRect(20, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.BrowseWindow_LogoutBtn.setFont(font)
        self.BrowseWindow_LogoutBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BrowseWindow_LogoutBtn.setStyleSheet("QPushButton {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 19px;\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: grey;\n"
"    color: black;\n"
"}")
        self.BrowseWindow_LogoutBtn.setObjectName("BrowseWindow_LogoutBtn")
        self.BrowseWindow_MainHeadingLabel = QtWidgets.QLabel(self.centralwidget)
        self.BrowseWindow_MainHeadingLabel.setGeometry(QtCore.QRect(180, 90, 541, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.BrowseWindow_MainHeadingLabel.setFont(font)
        self.BrowseWindow_MainHeadingLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    background: none;\n"
"    color: white;\n"
"}")
        self.BrowseWindow_MainHeadingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BrowseWindow_MainHeadingLabel.setObjectName("BrowseWindow_MainHeadingLabel")
        self.BrowseWindow_MainTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.BrowseWindow_MainTextLabel.setGeometry(QtCore.QRect(180, 110, 541, 111))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        self.BrowseWindow_MainTextLabel.setFont(font)
        self.BrowseWindow_MainTextLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    background: none;\n"
"    color: white;\n"
"}")
        self.BrowseWindow_MainTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BrowseWindow_MainTextLabel.setWordWrap(True)
        self.BrowseWindow_MainTextLabel.setObjectName("BrowseWindow_MainTextLabel")
        self.BrowseWindow_SearchLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.BrowseWindow_SearchLineEdit.setGeometry(QtCore.QRect(150, 240, 611, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.BrowseWindow_SearchLineEdit.setFont(font)
        self.BrowseWindow_SearchLineEdit.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(184, 184, 184);\n"
"    border: none;\n"
"    color: black;\n"
"    padding-top: 4px;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    border-radius: 20px;\n"
"}")
        self.BrowseWindow_SearchLineEdit.setText("")
        self.BrowseWindow_SearchLineEdit.setObjectName("BrowseWindow_SearchLineEdit")
        self.BrowseWindow_ScrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.BrowseWindow_ScrollArea.setGeometry(QtCore.QRect(50, 320, 801, 431))
        self.BrowseWindow_ScrollArea.setStyleSheet("QScrollArea {\n"
"    border: 1px solid rgb(230, 230, 230);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: black;\n"
"    border-radius: 5px;\n"
"    width: 15px;\n"
"    margin: 15px 0 0;\n"
"}\n"
"\n"
"\n"
"/* Handle */\n"
"QScrollBar::handle:vertical {\n"
"    background-color: rgb(255, 66, 69);\n"
"}\n"
"QScrollBar::handle:vertical::hover {\n"
"    background-color: rgb(255, 10, 22)\n"
"}\n"
"\n"
"/* Top Btn */\n"
"QScrollBar::sub-line:vertical {\n"
"    background-color: grey;\n"
"}")
        self.BrowseWindow_ScrollArea.setWidgetResizable(True)
        self.BrowseWindow_ScrollArea.setObjectName("BrowseWindow_ScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 784, 500))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.BrowseWindow_SeriesHolderFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.BrowseWindow_SeriesHolderFrame.setMinimumSize(QtCore.QSize(0, 500))
        self.BrowseWindow_SeriesHolderFrame.setStyleSheet("QFrame {\n"
"    background-color: white;\n"
"}")
        self.BrowseWindow_SeriesHolderFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BrowseWindow_SeriesHolderFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BrowseWindow_SeriesHolderFrame.setObjectName("BrowseWindow_SeriesHolderFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.BrowseWindow_SeriesHolderFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.BrowseWindow_SeriesHolderFrameLayout = QtWidgets.QGridLayout()
        self.BrowseWindow_SeriesHolderFrameLayout.setObjectName("BrowseWindow_SeriesHolderFrameLayout")
        self.BrowseWindow_Row2 = QtWidgets.QHBoxLayout()
        self.BrowseWindow_Row2.setSpacing(0)
        self.BrowseWindow_Row2.setObjectName("BrowseWindow_Row2")
        self.BrowseWindow_Series3 = QtWidgets.QWidget(self.BrowseWindow_SeriesHolderFrame)
        self.BrowseWindow_Series3.setStyleSheet("QWidget {\n"
"    border: 2px solid rgba(214, 214, 214, 0.1);\n"
"    background-color: rgba(214, 214, 214, 0.1);\n"
"}")
        self.BrowseWindow_Series3.setObjectName("BrowseWindow_Series3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.BrowseWindow_Series3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.BrowseWindow_Series3Layout = QtWidgets.QHBoxLayout()
        self.BrowseWindow_Series3Layout.setSpacing(0)
        self.BrowseWindow_Series3Layout.setObjectName("BrowseWindow_Series3Layout")
        self.BrowseWindow_Series3ImgLabel = QtWidgets.QLabel(self.BrowseWindow_Series3)
        self.BrowseWindow_Series3ImgLabel.setMinimumSize(QtCore.QSize(12, 200))
        self.BrowseWindow_Series3ImgLabel.setMaximumSize(QtCore.QSize(150, 200))
        self.BrowseWindow_Series3ImgLabel.setStyleSheet("QLabel {\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}")
        self.BrowseWindow_Series3ImgLabel.setText("")
        self.BrowseWindow_Series3ImgLabel.setPixmap(QtGui.QPixmap(":/newPrefix/imgs/series/mob.jpg"))
        self.BrowseWindow_Series3ImgLabel.setScaledContents(True)
        self.BrowseWindow_Series3ImgLabel.setObjectName("BrowseWindow_Series3ImgLabel")
        self.BrowseWindow_Series3Layout.addWidget(self.BrowseWindow_Series3ImgLabel)
        self.BrowseWindow_Series3CntFrame = QtWidgets.QFrame(self.BrowseWindow_Series3)
        self.BrowseWindow_Series3CntFrame.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}")
        self.BrowseWindow_Series3CntFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BrowseWindow_Series3CntFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BrowseWindow_Series3CntFrame.setObjectName("BrowseWindow_Series3CntFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.BrowseWindow_Series3CntFrame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.BrowseWindow_Series3CntFrameLayout = QtWidgets.QVBoxLayout()
        self.BrowseWindow_Series3CntFrameLayout.setSpacing(0)
        self.BrowseWindow_Series3CntFrameLayout.setObjectName("BrowseWindow_Series3CntFrameLayout")
        self.BrowseWindow_Series3NameLabel = QtWidgets.QLabel(self.BrowseWindow_Series3CntFrame)
        self.BrowseWindow_Series3NameLabel.setStyleSheet("QLabel {\n"
"    border: none;\n"
"    padding-left: 10px;\n"
"}")
        self.BrowseWindow_Series3NameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BrowseWindow_Series3NameLabel.setObjectName("BrowseWindow_Series3NameLabel")
        self.BrowseWindow_Series3CntFrameLayout.addWidget(self.BrowseWindow_Series3NameLabel)
        self.BrowseWindow_Series3DescLabel = QtWidgets.QLabel(self.BrowseWindow_Series3CntFrame)
        self.BrowseWindow_Series3DescLabel.setStyleSheet("QLabel {\n"
"    border: none;\n"
"    padding-left: 10px;\n"
"}")
        self.BrowseWindow_Series3DescLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BrowseWindow_Series3DescLabel.setObjectName("BrowseWindow_Series3DescLabel")
        self.BrowseWindow_Series3CntFrameLayout.addWidget(self.BrowseWindow_Series3DescLabel)
        self.BrowseWindow_Series3TogglePushBtn = QtWidgets.QPushButton(self.BrowseWindow_Series3CntFrame)
        self.BrowseWindow_Series3TogglePushBtn.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BrowseWindow_Series3TogglePushBtn.setFont(font)
        self.BrowseWindow_Series3TogglePushBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BrowseWindow_Series3TogglePushBtn.setStyleSheet("QPushButton {\n"
"    background-color:  rgb(255, 66, 69);\n"
"    color: white;\n"
"    padding-top: 3px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(255, 10, 22)\n"
"}")
        self.BrowseWindow_Series3TogglePushBtn.setObjectName("BrowseWindow_Series3TogglePushBtn")
        self.BrowseWindow_Series3CntFrameLayout.addWidget(self.BrowseWindow_Series3TogglePushBtn)
        self.horizontalLayout_4.addLayout(self.BrowseWindow_Series3CntFrameLayout)
        self.BrowseWindow_Series3Layout.addWidget(self.BrowseWindow_Series3CntFrame)
        self.horizontalLayout_10.addLayout(self.BrowseWindow_Series3Layout)
        self.BrowseWindow_Row2.addWidget(self.BrowseWindow_Series3)
        self.BrowseWindow_Series4 = QtWidgets.QWidget(self.BrowseWindow_SeriesHolderFrame)
        self.BrowseWindow_Series4.setStyleSheet("QWidget {\n"
"    border: 2px solid rgba(214, 214, 214, 0.1);\n"
"    background-color: rgba(214, 214, 214, 0.1);\n"
"}")
        self.BrowseWindow_Series4.setObjectName("BrowseWindow_Series4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.BrowseWindow_Series4)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.BrowseWindow_Series4Layout = QtWidgets.QHBoxLayout()
        self.BrowseWindow_Series4Layout.setSpacing(0)
        self.BrowseWindow_Series4Layout.setObjectName("BrowseWindow_Series4Layout")
        self.BrowseWindow_Series4ImgLabel = QtWidgets.QLabel(self.BrowseWindow_Series4)
        self.BrowseWindow_Series4ImgLabel.setMinimumSize(QtCore.QSize(12, 200))
        self.BrowseWindow_Series4ImgLabel.setMaximumSize(QtCore.QSize(150, 200))
        self.BrowseWindow_Series4ImgLabel.setStyleSheet("QLabel {\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}")
        self.BrowseWindow_Series4ImgLabel.setText("")
        self.BrowseWindow_Series4ImgLabel.setPixmap(QtGui.QPixmap(":/newPrefix/imgs/series/tye.jpg"))
        self.BrowseWindow_Series4ImgLabel.setScaledContents(True)
        self.BrowseWindow_Series4ImgLabel.setObjectName("BrowseWindow_Series4ImgLabel")
        self.BrowseWindow_Series4Layout.addWidget(self.BrowseWindow_Series4ImgLabel)
        self.BrowseWindow_Series4CntFrame = QtWidgets.QFrame(self.BrowseWindow_Series4)
        self.BrowseWindow_Series4CntFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BrowseWindow_Series4CntFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BrowseWindow_Series4CntFrame.setObjectName("BrowseWindow_Series4CntFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.BrowseWindow_Series4CntFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.BrowseWindow_Series4CntFrameLayout = QtWidgets.QVBoxLayout()
        self.BrowseWindow_Series4CntFrameLayout.setSpacing(0)
        self.BrowseWindow_Series4CntFrameLayout.setObjectName("BrowseWindow_Series4CntFrameLayout")
        self.BrowseWindow_Series4NameLabel = QtWidgets.QLabel(self.BrowseWindow_Series4CntFrame)
        self.BrowseWindow_Series4NameLabel.setStyleSheet("QLabel {\n"
"    border: none;\n"
"    padding-left: 10px;\n"
"}")
        self.BrowseWindow_Series4NameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BrowseWindow_Series4NameLabel.setObjectName("BrowseWindow_Series4NameLabel")
        self.BrowseWindow_Series4CntFrameLayout.addWidget(self.BrowseWindow_Series4NameLabel)
        self.BrowseWindow_Series4DescLabel = QtWidgets.QLabel(self.BrowseWindow_Series4CntFrame)
        self.BrowseWindow_Series4DescLabel.setStyleSheet("QLabel {\n"
"    border: none;\n"
"    padding-left: 10px;\n"
"}")
        self.BrowseWindow_Series4DescLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BrowseWindow_Series4DescLabel.setObjectName("BrowseWindow_Series4DescLabel")
        self.BrowseWindow_Series4CntFrameLayout.addWidget(self.BrowseWindow_Series4DescLabel)
        self.BrowseWindow_Series4TogglePushBtn = QtWidgets.QPushButton(self.BrowseWindow_Series4CntFrame)
        self.BrowseWindow_Series4TogglePushBtn.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BrowseWindow_Series4TogglePushBtn.setFont(font)
        self.BrowseWindow_Series4TogglePushBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BrowseWindow_Series4TogglePushBtn.setStyleSheet("QPushButton {\n"
"    background-color:  rgb(255, 66, 69);\n"
"    color: white;\n"
"    padding-top: 3px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(255, 10, 22)\n"
"}")
        self.BrowseWindow_Series4TogglePushBtn.setObjectName("BrowseWindow_Series4TogglePushBtn")
        self.BrowseWindow_Series4CntFrameLayout.addWidget(self.BrowseWindow_Series4TogglePushBtn)
        self.verticalLayout_2.addLayout(self.BrowseWindow_Series4CntFrameLayout)
        self.BrowseWindow_Series4Layout.addWidget(self.BrowseWindow_Series4CntFrame)
        self.horizontalLayout_9.addLayout(self.BrowseWindow_Series4Layout)
        self.BrowseWindow_Row2.addWidget(self.BrowseWindow_Series4)
        self.BrowseWindow_SeriesHolderFrameLayout.addLayout(self.BrowseWindow_Row2, 1, 0, 1, 1)
        self.BrowseWindow_Row1 = QtWidgets.QHBoxLayout()
        self.BrowseWindow_Row1.setObjectName("BrowseWindow_Row1")
        self.BrowseWindow_Series1 = QtWidgets.QWidget(self.BrowseWindow_SeriesHolderFrame)
        self.BrowseWindow_Series1.setStyleSheet("QWidget {\n"
"    border: 2px solid rgba(214, 214, 214, 0.1);\n"
"    background-color: rgba(214, 214, 214, 0.1);\n"
"}")
        self.BrowseWindow_Series1.setObjectName("BrowseWindow_Series1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.BrowseWindow_Series1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.BrowseWindow_Series1Layout = QtWidgets.QHBoxLayout()
        self.BrowseWindow_Series1Layout.setSpacing(0)
        self.BrowseWindow_Series1Layout.setObjectName("BrowseWindow_Series1Layout")
        self.BrowseWindow_Series1ImgLabel = QtWidgets.QLabel(self.BrowseWindow_Series1)
        self.BrowseWindow_Series1ImgLabel.setMinimumSize(QtCore.QSize(12, 200))
        self.BrowseWindow_Series1ImgLabel.setMaximumSize(QtCore.QSize(150, 200))
        self.BrowseWindow_Series1ImgLabel.setStyleSheet("QLabel {\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}")
        self.BrowseWindow_Series1ImgLabel.setText("")
        self.BrowseWindow_Series1ImgLabel.setPixmap(QtGui.QPixmap(":/newPrefix/imgs/series/jojo.jpg"))
        self.BrowseWindow_Series1ImgLabel.setScaledContents(True)
        self.BrowseWindow_Series1ImgLabel.setObjectName("BrowseWindow_Series1ImgLabel")
        self.BrowseWindow_Series1Layout.addWidget(self.BrowseWindow_Series1ImgLabel)
        self.BrowseWindow_Series1CntFrame = QtWidgets.QFrame(self.BrowseWindow_Series1)
        self.BrowseWindow_Series1CntFrame.setStyleSheet("QFrame {\n"
"    text-align: center;\n"
"}")
        self.BrowseWindow_Series1CntFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BrowseWindow_Series1CntFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BrowseWindow_Series1CntFrame.setObjectName("BrowseWindow_Series1CntFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.BrowseWindow_Series1CntFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.BrowseWindow_Series1CntFrameLayout = QtWidgets.QVBoxLayout()
        self.BrowseWindow_Series1CntFrameLayout.setSpacing(0)
        self.BrowseWindow_Series1CntFrameLayout.setObjectName("BrowseWindow_Series1CntFrameLayout")
        self.BrowseWindow_Series1NameLabel = QtWidgets.QLabel(self.BrowseWindow_Series1CntFrame)
        self.BrowseWindow_Series1NameLabel.setStyleSheet("QLabel {\n"
"    border: none;\n"
"    padding-left: 10px;\n"
"}")
        self.BrowseWindow_Series1NameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BrowseWindow_Series1NameLabel.setObjectName("BrowseWindow_Series1NameLabel")
        self.BrowseWindow_Series1CntFrameLayout.addWidget(self.BrowseWindow_Series1NameLabel)
        self.BrowseWindow_Series1DescLabel = QtWidgets.QLabel(self.BrowseWindow_Series1CntFrame)
        self.BrowseWindow_Series1DescLabel.setStyleSheet("QLabel {\n"
"    border: none;\n"
"    padding-left: 10px;\n"
"}")
        self.BrowseWindow_Series1DescLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BrowseWindow_Series1DescLabel.setObjectName("BrowseWindow_Series1DescLabel")
        self.BrowseWindow_Series1CntFrameLayout.addWidget(self.BrowseWindow_Series1DescLabel)
        self.BrowseWindow_Series1TogglePushBtn = QtWidgets.QPushButton(self.BrowseWindow_Series1CntFrame)
        self.BrowseWindow_Series1TogglePushBtn.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BrowseWindow_Series1TogglePushBtn.setFont(font)
        self.BrowseWindow_Series1TogglePushBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BrowseWindow_Series1TogglePushBtn.setStyleSheet("QPushButton {\n"
"    background-color:  rgb(255, 66, 69);\n"
"    color: white;\n"
"    padding-top: 3px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(255, 10, 22)\n"
"}")
        self.BrowseWindow_Series1TogglePushBtn.setObjectName("BrowseWindow_Series1TogglePushBtn")
        self.BrowseWindow_Series1CntFrameLayout.addWidget(self.BrowseWindow_Series1TogglePushBtn)
        self.verticalLayout_4.addLayout(self.BrowseWindow_Series1CntFrameLayout)
        self.BrowseWindow_Series1Layout.addWidget(self.BrowseWindow_Series1CntFrame)
        self.horizontalLayout_3.addLayout(self.BrowseWindow_Series1Layout)
        self.BrowseWindow_Row1.addWidget(self.BrowseWindow_Series1)
        self.BrowseWindow_Series2 = QtWidgets.QWidget(self.BrowseWindow_SeriesHolderFrame)
        self.BrowseWindow_Series2.setStyleSheet("QWidget {\n"
"    border: 2px solid rgba(214, 214, 214, 0.1);\n"
"    background-color: rgba(214, 214, 214, 0.1);\n"
"}")
        self.BrowseWindow_Series2.setObjectName("BrowseWindow_Series2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.BrowseWindow_Series2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.BrowseWindow_Series2Layout = QtWidgets.QHBoxLayout()
        self.BrowseWindow_Series2Layout.setSpacing(0)
        self.BrowseWindow_Series2Layout.setObjectName("BrowseWindow_Series2Layout")
        self.BrowseWindow_Series2ImgLabel = QtWidgets.QLabel(self.BrowseWindow_Series2)
        self.BrowseWindow_Series2ImgLabel.setMinimumSize(QtCore.QSize(12, 200))
        self.BrowseWindow_Series2ImgLabel.setMaximumSize(QtCore.QSize(150, 200))
        self.BrowseWindow_Series2ImgLabel.setStyleSheet("QLabel {\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}")
        self.BrowseWindow_Series2ImgLabel.setText("")
        self.BrowseWindow_Series2ImgLabel.setPixmap(QtGui.QPixmap(":/newPrefix/imgs/series/mha.jpg"))
        self.BrowseWindow_Series2ImgLabel.setScaledContents(True)
        self.BrowseWindow_Series2ImgLabel.setObjectName("BrowseWindow_Series2ImgLabel")
        self.BrowseWindow_Series2Layout.addWidget(self.BrowseWindow_Series2ImgLabel)
        self.BrowseWindow_Series2CntFrame = QtWidgets.QFrame(self.BrowseWindow_Series2)
        self.BrowseWindow_Series2CntFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BrowseWindow_Series2CntFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BrowseWindow_Series2CntFrame.setObjectName("BrowseWindow_Series2CntFrame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.BrowseWindow_Series2CntFrame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.BrowseWindow_Series2CntFrameLayout = QtWidgets.QVBoxLayout()
        self.BrowseWindow_Series2CntFrameLayout.setSpacing(0)
        self.BrowseWindow_Series2CntFrameLayout.setObjectName("BrowseWindow_Series2CntFrameLayout")
        self.BrowseWindow_Series2NameLabel = QtWidgets.QLabel(self.BrowseWindow_Series2CntFrame)
        self.BrowseWindow_Series2NameLabel.setStyleSheet("QLabel {\n"
"    border: none;\n"
"    padding-left: 10px;\n"
"}")
        self.BrowseWindow_Series2NameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BrowseWindow_Series2NameLabel.setObjectName("BrowseWindow_Series2NameLabel")
        self.BrowseWindow_Series2CntFrameLayout.addWidget(self.BrowseWindow_Series2NameLabel)
        self.BrowseWindow_Series2DescLabel = QtWidgets.QLabel(self.BrowseWindow_Series2CntFrame)
        self.BrowseWindow_Series2DescLabel.setStyleSheet("QLabel {\n"
"    border: none;\n"
"    padding-left: 10px;\n"
"}")
        self.BrowseWindow_Series2DescLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BrowseWindow_Series2DescLabel.setObjectName("BrowseWindow_Series2DescLabel")
        self.BrowseWindow_Series2CntFrameLayout.addWidget(self.BrowseWindow_Series2DescLabel)
        self.BrowseWindow_Series2TogglePushBtn = QtWidgets.QPushButton(self.BrowseWindow_Series2CntFrame)
        self.BrowseWindow_Series2TogglePushBtn.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BrowseWindow_Series2TogglePushBtn.setFont(font)
        self.BrowseWindow_Series2TogglePushBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BrowseWindow_Series2TogglePushBtn.setStyleSheet("QPushButton {\n"
"    background-color:  rgb(255, 66, 69);\n"
"    color: white;\n"
"    padding-top: 3px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(255, 10, 22)\n"
"}")
        self.BrowseWindow_Series2TogglePushBtn.setObjectName("BrowseWindow_Series2TogglePushBtn")
        self.BrowseWindow_Series2CntFrameLayout.addWidget(self.BrowseWindow_Series2TogglePushBtn)
        self.verticalLayout_5.addLayout(self.BrowseWindow_Series2CntFrameLayout)
        self.BrowseWindow_Series2Layout.addWidget(self.BrowseWindow_Series2CntFrame)
        self.horizontalLayout_6.addLayout(self.BrowseWindow_Series2Layout)
        self.BrowseWindow_Row1.addWidget(self.BrowseWindow_Series2)
        self.BrowseWindow_SeriesHolderFrameLayout.addLayout(self.BrowseWindow_Row1, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.BrowseWindow_SeriesHolderFrameLayout)
        self.verticalLayout.addWidget(self.BrowseWindow_SeriesHolderFrame)
        self.BrowseWindow_ScrollArea.setWidget(self.scrollAreaWidgetContents)
        BrowseWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(BrowseWindow)
        QtCore.QMetaObject.connectSlotsByName(BrowseWindow)

    def retranslateUi(self, BrowseWindow):
        _translate = QtCore.QCoreApplication.translate
        BrowseWindow.setWindowTitle(_translate("BrowseWindow", "AnimexUI - Browse"))
        self.BrowseWindow_ExitBtn.setText(_translate("BrowseWindow", "✖"))
        self.BrowseWindow_LogoutBtn.setText(_translate("BrowseWindow", "LOGOUT"))
        self.BrowseWindow_MainHeadingLabel.setText(_translate("BrowseWindow", "Browse A Series."))
        self.BrowseWindow_MainTextLabel.setText(_translate("BrowseWindow", "You can browse a series either by clicking on its picture; or you can search it up by name."))
        self.BrowseWindow_SearchLineEdit.setPlaceholderText(_translate("BrowseWindow", "Ex: Jojo"))
        self.BrowseWindow_Series3NameLabel.setText(_translate("BrowseWindow", "TextLabel"))
        self.BrowseWindow_Series3DescLabel.setText(_translate("BrowseWindow", "TextLabel"))
        self.BrowseWindow_Series3TogglePushBtn.setText(_translate("BrowseWindow", "START VIEWING"))
        self.BrowseWindow_Series4NameLabel.setText(_translate("BrowseWindow", "TextLabel"))
        self.BrowseWindow_Series4DescLabel.setText(_translate("BrowseWindow", "TextLabel"))
        self.BrowseWindow_Series4TogglePushBtn.setText(_translate("BrowseWindow", "START VIEWING"))
        self.BrowseWindow_Series1NameLabel.setText(_translate("BrowseWindow", "TextLabel"))
        self.BrowseWindow_Series1DescLabel.setText(_translate("BrowseWindow", "TextLabel"))
        self.BrowseWindow_Series1TogglePushBtn.setText(_translate("BrowseWindow", "START VIEWING"))
        self.BrowseWindow_Series2NameLabel.setText(_translate("BrowseWindow", "TextLabel"))
        self.BrowseWindow_Series2DescLabel.setText(_translate("BrowseWindow", "TextLabel"))
        self.BrowseWindow_Series2TogglePushBtn.setText(_translate("BrowseWindow", "START VIEWING"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BrowseWindow = QtWidgets.QMainWindow()
    ui = Ui_BrowseWindow()
    ui.setupUi(BrowseWindow)
    # BrowseWindow.show()

    print("You cannot run the app from this window.. Run StartWindow.py!")
    # backupAllFiles()

    sys.exit()
