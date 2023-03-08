

from PyQt5 import QtCore, QtGui, QtWidgets
from assets.files.ARRAYS import currentUser
from assets.files._backUpFiles import backupAllFiles
from assets.files.OBJECTS import *

import StartWindow
import sys

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

        print(jojo.getImg())

        BrowseWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Hides the title bar
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
        self.BrowseWindow_ScrollArea.setGeometry(QtCore.QRect(50, 320, 801, 451))
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



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BrowseWindow = QtWidgets.QMainWindow()
    ui = Ui_BrowseWindow()
    ui.setupUi(BrowseWindow)
    # BrowseWindow.show()

    print("You cannot run the app from this window.. Run StartWindow.py!")
    backupAllFiles()

    sys.exit()
