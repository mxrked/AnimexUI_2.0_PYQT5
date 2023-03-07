


from PyQt5 import QtCore, QtGui, QtWidgets
from assets.medias.qrcs import deku_BG
from assets.files.ARRAYS import accounts, currentUser
from assets.files._backUpFiles import backupAllFiles

import sys
import StartWindow, BrowseWindow

class Ui_LoginAccountWindow(object):
    def setupUi(self, LoginAccountWindow):

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
            LoginAccountWindow.hide()

            print("Routing to StartWindow!")

        def enterBrowseWindow():
            # Showing new window
            self.ui = BrowseWindow.Ui_BrowseWindow()
            self.window = QtWidgets.QMainWindow()
            self.ui.setupUi(self.window)
            self.window.show()

            # Hiding current window
            LoginAccountWindow.hide()

            print("Routing to BrowseWindow!")

        def clearInputs():
            self.LoginAccountWindow_UsernameLineEdit.setText("")
            self.LoginAccountWindow_EmailAddressLineEdit.setText("")
            self.LoginAccountWindow_PasswordLineEdit.setText("")

            self.LoginAccountWindow_UsernameLineEdit.setStyleSheet("QLineEdit {\n"
                "    border: none;\n"
                "    background-color: rgb(189, 189, 189);\n"
                "    padding-left: 10px;\n"
                "    padding-right: 10px;\n"
                "}\n"
                "\n"
                "QLineEdit::focus {\n"
                "    border: 2px solid rgb(119, 196, 255)\n"
                "}")
            self.LoginAccountWindow_EmailAddressLineEdit.setStyleSheet("QLineEdit {\n"
                "    border: none;\n"
                "    background-color: rgb(189, 189, 189);\n"
                "    padding-left: 10px;\n"
                "    padding-right: 10px;\n"
                "}\n"
                "\n"
                "QLineEdit::focus {\n"
                "    border: 2px solid rgb(119, 196, 255)\n"
                "}")
            self.LoginAccountWindow_PasswordLineEdit.setStyleSheet("QLineEdit {\n"
                "    border: none;\n"
                "    background-color: rgb(189, 189, 189);\n"
                "    padding-left: 10px;\n"
                "    padding-right: 10px;\n"
                "}\n"
                "\n"
                "QLineEdit::focus {\n"
                "    border: 2px solid rgb(119, 196, 255)\n"
                "}")

        def loginUser():

            # Getting each of the input texts
            usernameText = self.LoginAccountWindow_UsernameLineEdit.text()
            emailText = self.LoginAccountWindow_EmailAddressLineEdit.text()
            passwordText = self.LoginAccountWindow_PasswordLineEdit.text()

            # Checking if inputs match one of the accounts
            for account in accounts:

                # Checking for invalids
                if account.getUsername() != usernameText:
                    self.LoginAccountWindow_UsernameLineEdit.setStyleSheet("QLineEdit {\n"
                "    border: 2px solid red;\n"
                "    background-color: rgb(189, 189, 189);\n"
                "    padding-left: 10px;\n"
                "    padding-right: 10px;\n"
                "}\n"
                "\n"
                "QLineEdit::focus {\n"
                "    border: 2px solid rgb(119, 196, 255)\n"
                "}")
                else:
                    self.LoginAccountWindow_UsernameLineEdit.setStyleSheet("QLineEdit {\n"
                "    border: none;\n"
                "    background-color: rgb(189, 189, 189);\n"
                "    padding-left: 10px;\n"
                "    padding-right: 10px;\n"
                "}\n"
                "\n"
                "QLineEdit::focus {\n"
                "    border: 2px solid rgb(119, 196, 255)\n"
                "}")

                if account.getEmail() != emailText:
                    self.LoginAccountWindow_EmailAddressLineEdit.setStyleSheet("QLineEdit {\n"
                "    border: 2px solid red;\n"
                "    background-color: rgb(189, 189, 189);\n"
                "    padding-left: 10px;\n"
                "    padding-right: 10px;\n"
                "}\n"
                "\n"
                "QLineEdit::focus {\n"
                "    border: 2px solid rgb(119, 196, 255)\n"
                "}")
                else:
                    self.LoginAccountWindow_EmailAddressLineEdit.setStyleSheet("QLineEdit {\n"
                "    border: none;\n"
                "    background-color: rgb(189, 189, 189);\n"
                "    padding-left: 10px;\n"
                "    padding-right: 10px;\n"
                "}\n"
                "\n"
                "QLineEdit::focus {\n"
                "    border: 2px solid rgb(119, 196, 255)\n"
                "}")

                if account.getPassword() != passwordText:
                    self.LoginAccountWindow_PasswordLineEdit.setStyleSheet("QLineEdit {\n"
                "    border: 2px solid red;\n"
                "    background-color: rgb(189, 189, 189);\n"
                "    padding-left: 10px;\n"
                "    padding-right: 10px;\n"
                "}\n"
                "\n"
                "QLineEdit::focus {\n"
                "    border: 2px solid rgb(119, 196, 255)\n"
                "}")
                else:
                    self.LoginAccountWindow_PasswordLineEdit.setStyleSheet("QLineEdit {\n"
                "    border: none;\n"
                "    background-color: rgb(189, 189, 189);\n"
                "    padding-left: 10px;\n"
                "    padding-right: 10px;\n"
                "}\n"
                "\n"
                "QLineEdit::focus {\n"
                "    border: 2px solid rgb(119, 196, 255)\n"
                "}")

                # Checking username
                if account.getUsername() == usernameText:

                    # Checking email
                    if account.getEmail() == emailText:

                        # Checking password
                        if account.getPassword() == passwordText:

                            currentUser.clear()
                            currentUser.append(account)

                            clearInputs() # Clearing inputs

                            print("Routing to BrowseWindow")
                            print("Welcome, " + currentUser[0].getUsername())

            # Displaying invalids when there are no accounts
            if len(accounts) == 0:
                self.LoginAccountWindow_UsernameLineEdit.setStyleSheet("QLineEdit {\n"
                "    border: 2px solid red;\n"
                "    background-color: rgb(189, 189, 189);\n"
                "    padding-left: 10px;\n"
                "    padding-right: 10px;\n"
                "}\n"
                "\n"
                "QLineEdit::focus {\n"
                "    border: 2px solid rgb(119, 196, 255)\n"
                "}")
                self.LoginAccountWindow_EmailAddressLineEdit.setStyleSheet("QLineEdit {\n"
                "    border: 2px solid red;\n"
                "    background-color: rgb(189, 189, 189);\n"
                "    padding-left: 10px;\n"
                "    padding-right: 10px;\n"
                "}\n"
                "\n"
                "QLineEdit::focus {\n"
                "    border: 2px solid rgb(119, 196, 255)\n"
                "}")
                self.LoginAccountWindow_PasswordLineEdit.setStyleSheet("QLineEdit {\n"
                "    border: 2px solid red;\n"
                "    background-color: rgb(189, 189, 189);\n"
                "    padding-left: 10px;\n"
                "    padding-right: 10px;\n"
                "}\n"
                "\n"
                "QLineEdit::focus {\n"
                "    border: 2px solid rgb(119, 196, 255)\n"
                "}")

            # Routes user after login successfully!
            if len(currentUser) > 0:
                enterBrowseWindow()

        LoginAccountWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Hides the title bar
        LoginAccountWindow.setObjectName("LoginAccountWindow")
        LoginAccountWindow.resize(900, 610)
        LoginAccountWindow.setMinimumSize(QtCore.QSize(900, 610))
        LoginAccountWindow.setMaximumSize(QtCore.QSize(900, 610))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/imgs/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginAccountWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(LoginAccountWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LoginAccountWindow_MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.LoginAccountWindow_MainFrame.setGeometry(QtCore.QRect(0, 0, 511, 701))
        self.LoginAccountWindow_MainFrame.setStyleSheet("QFrame {\n"
"    background-color: rgb(25, 25, 25);\n"
"    border-image: none;\n"
"}")
        self.LoginAccountWindow_MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LoginAccountWindow_MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LoginAccountWindow_MainFrame.setObjectName("LoginAccountWindow_MainFrame")
        self.LoginAccountWindow_ExitBtn = QtWidgets.QPushButton(self.LoginAccountWindow_MainFrame)
        self.LoginAccountWindow_ExitBtn.clicked.connect(closeApp)
        self.LoginAccountWindow_ExitBtn.setGeometry(QtCore.QRect(60, 20, 31, 31))
        self.LoginAccountWindow_ExitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LoginAccountWindow_ExitBtn.setStyleSheet("QPushButton {\n"
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
        self.LoginAccountWindow_ExitBtn.setObjectName("LoginAccountWindow_ExitBtn")
        self.LoginAccountWindow_BackBtn = QtWidgets.QPushButton(self.LoginAccountWindow_MainFrame)
        self.LoginAccountWindow_BackBtn.clicked.connect(enterStartWindow)
        self.LoginAccountWindow_BackBtn.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.LoginAccountWindow_BackBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LoginAccountWindow_BackBtn.setStyleSheet("QPushButton {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 19px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: grey;\n"
"    color: black;\n"
"}")
        self.LoginAccountWindow_BackBtn.setObjectName("LoginAccountWindow_BackBtn")
        self.LoginAccountWindow_MainHeadingLabel = QtWidgets.QLabel(self.LoginAccountWindow_MainFrame)
        self.LoginAccountWindow_MainHeadingLabel.setGeometry(QtCore.QRect(40, 120, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.LoginAccountWindow_MainHeadingLabel.setFont(font)
        self.LoginAccountWindow_MainHeadingLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    background: none;\n"
"    color: white;\n"
"}")
        self.LoginAccountWindow_MainHeadingLabel.setObjectName("LoginAccountWindow_MainHeadingLabel")
        self.LoginAccountWindow_MainTextLabel = QtWidgets.QLabel(self.LoginAccountWindow_MainFrame)
        self.LoginAccountWindow_MainTextLabel.setGeometry(QtCore.QRect(40, 170, 401, 81))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        self.LoginAccountWindow_MainTextLabel.setFont(font)
        self.LoginAccountWindow_MainTextLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    background: none;\n"
"    color: white;\n"
"}")
        self.LoginAccountWindow_MainTextLabel.setWordWrap(True)
        self.LoginAccountWindow_MainTextLabel.setObjectName("LoginAccountWindow_MainTextLabel")
        self.LoginAccountWindow_UsernameLineEdit = QtWidgets.QLineEdit(self.LoginAccountWindow_MainFrame)
        self.LoginAccountWindow_UsernameLineEdit.setGeometry(QtCore.QRect(190, 310, 271, 41))
        self.LoginAccountWindow_UsernameLineEdit.setStyleSheet("QLineEdit {\n"
"    border: none;\n"
"    background-color: rgb(189, 189, 189);\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"QLineEdit::focus {\n"
"    border: 2px solid rgb(119, 196, 255)\n"
"}")
        self.LoginAccountWindow_UsernameLineEdit.setText("")
        self.LoginAccountWindow_UsernameLineEdit.setObjectName("LoginAccountWindow_UsernameLineEdit")
        self.LoginAccountWindow_EmailAddressLineEdit = QtWidgets.QLineEdit(self.LoginAccountWindow_MainFrame)
        self.LoginAccountWindow_EmailAddressLineEdit.setGeometry(QtCore.QRect(190, 370, 271, 41))
        self.LoginAccountWindow_EmailAddressLineEdit.setStyleSheet("QLineEdit {\n"
"    border: none;\n"
"    background-color: rgb(189, 189, 189);\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"QLineEdit::focus {\n"
"    border: 2px solid rgb(119, 196, 255)\n"
"}")
        self.LoginAccountWindow_EmailAddressLineEdit.setText("")
        self.LoginAccountWindow_EmailAddressLineEdit.setObjectName("LoginAccountWindow_EmailAddressLineEdit")
        self.LoginAccountWindow_PasswordLineEdit = QtWidgets.QLineEdit(self.LoginAccountWindow_MainFrame)
        self.LoginAccountWindow_PasswordLineEdit.setGeometry(QtCore.QRect(190, 430, 271, 41))
        self.LoginAccountWindow_PasswordLineEdit.setStyleSheet("QLineEdit {\n"
"    border: none;\n"
"    background-color: rgb(189, 189, 189);\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"QLineEdit::focus {\n"
"    border: 2px solid rgb(119, 196, 255)\n"
"}")
        self.LoginAccountWindow_PasswordLineEdit.setText("")
        self.LoginAccountWindow_PasswordLineEdit.setObjectName("LoginAccountWindow_PasswordLineEdit")
        self.LoginAccountWindow_UsernameLabel = QtWidgets.QLabel(self.LoginAccountWindow_MainFrame)
        self.LoginAccountWindow_UsernameLabel.setGeometry(QtCore.QRect(40, 320, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.LoginAccountWindow_UsernameLabel.setFont(font)
        self.LoginAccountWindow_UsernameLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    background: none;\n"
"    color: white;\n"
"}\n"
"")
        self.LoginAccountWindow_UsernameLabel.setObjectName("LoginAccountWindow_UsernameLabel")
        self.LoginAccountWindow_EmailAddressLabel = QtWidgets.QLabel(self.LoginAccountWindow_MainFrame)
        self.LoginAccountWindow_EmailAddressLabel.setGeometry(QtCore.QRect(40, 380, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.LoginAccountWindow_EmailAddressLabel.setFont(font)
        self.LoginAccountWindow_EmailAddressLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    background: none;\n"
"    color: white;\n"
"}\n"
"")
        self.LoginAccountWindow_EmailAddressLabel.setObjectName("LoginAccountWindow_EmailAddressLabel")
        self.LoginAccountWindow_PasswordLabel = QtWidgets.QLabel(self.LoginAccountWindow_MainFrame)
        self.LoginAccountWindow_PasswordLabel.setGeometry(QtCore.QRect(40, 440, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.LoginAccountWindow_PasswordLabel.setFont(font)
        self.LoginAccountWindow_PasswordLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    background: none;\n"
"    color: white;\n"
"}\n"
"")
        self.LoginAccountWindow_PasswordLabel.setObjectName("LoginAccountWindow_PasswordLabel")
        self.LoginAccountWindow_BtnsFrame = QtWidgets.QFrame(self.LoginAccountWindow_MainFrame)
        self.LoginAccountWindow_BtnsFrame.setGeometry(QtCore.QRect(30, 480, 201, 111))
        self.LoginAccountWindow_BtnsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LoginAccountWindow_BtnsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LoginAccountWindow_BtnsFrame.setObjectName("LoginAccountWindow_BtnsFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.LoginAccountWindow_BtnsFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LoginAccountWindow_LoginBtn = QtWidgets.QPushButton(self.LoginAccountWindow_BtnsFrame)
        self.LoginAccountWindow_LoginBtn.clicked.connect(loginUser)
        self.LoginAccountWindow_LoginBtn.setMinimumSize(QtCore.QSize(85, 40))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.LoginAccountWindow_LoginBtn.setFont(font)
        self.LoginAccountWindow_LoginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LoginAccountWindow_LoginBtn.setStyleSheet("QPushButton {\n"
"    border-radius: 6px;\n"
"    background-color: rgb(255, 66, 69);\n"
"    color: white;\n"
"    padding-top: 3px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(255, 10, 22)\n"
"}")
        self.LoginAccountWindow_LoginBtn.setObjectName("LoginAccountWindow_LoginBtn")
        self.horizontalLayout.addWidget(self.LoginAccountWindow_LoginBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.LoginAccountWindow_ClearBtn = QtWidgets.QPushButton(self.LoginAccountWindow_BtnsFrame)
        self.LoginAccountWindow_ClearBtn.clicked.connect(clearInputs)
        self.LoginAccountWindow_ClearBtn.setMinimumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.LoginAccountWindow_ClearBtn.setFont(font)
        self.LoginAccountWindow_ClearBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LoginAccountWindow_ClearBtn.setStyleSheet("QPushButton {\n"
"    border-radius: 6px;\n"
"    background-color: rgb(255, 66, 69);\n"
"    color: white;\n"
"    padding-top: 3px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(255, 10, 22)\n"
"}")
        self.LoginAccountWindow_ClearBtn.setObjectName("LoginAccountWindow_ClearBtn")
        self.horizontalLayout.addWidget(self.LoginAccountWindow_ClearBtn)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.LoginAccountWindow_BgFrame = QtWidgets.QFrame(self.centralwidget)
        self.LoginAccountWindow_BgFrame.setGeometry(QtCore.QRect(510, -10, 391, 621))
        self.LoginAccountWindow_BgFrame.setStyleSheet("QFrame {\n"
"    background-image: url(:/newPrefix/imgs/deku_BG.jpg);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}")
        self.LoginAccountWindow_BgFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LoginAccountWindow_BgFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LoginAccountWindow_BgFrame.setObjectName("LoginAccountWindow_BgFrame")
        self.LoginAccountWindow_BgDarkenFrame = QtWidgets.QFrame(self.LoginAccountWindow_BgFrame)
        self.LoginAccountWindow_BgDarkenFrame.setGeometry(QtCore.QRect(0, 0, 401, 671))
        self.LoginAccountWindow_BgDarkenFrame.setStyleSheet("QFrame {\n"
"    background: none;\n"
"    background-color: rgba(0, 0, 0, .4);\n"
"}")
        self.LoginAccountWindow_BgDarkenFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LoginAccountWindow_BgDarkenFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LoginAccountWindow_BgDarkenFrame.setObjectName("LoginAccountWindow_BgDarkenFrame")
        LoginAccountWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginAccountWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginAccountWindow)

    def retranslateUi(self, LoginAccountWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginAccountWindow.setWindowTitle(_translate("LoginAccountWindow", "AnimexUI - Login Account"))
        self.LoginAccountWindow_ExitBtn.setText(_translate("LoginAccountWindow", "✖"))
        self.LoginAccountWindow_BackBtn.setText(_translate("LoginAccountWindow", "🠜"))
        self.LoginAccountWindow_MainHeadingLabel.setText(_translate("LoginAccountWindow", "Account Login."))
        self.LoginAccountWindow_MainTextLabel.setText(_translate("LoginAccountWindow", "Provide below, with the basic information that is needed to login to your account."))
        self.LoginAccountWindow_UsernameLineEdit.setPlaceholderText(_translate("LoginAccountWindow", "ex: animelover1337"))
        self.LoginAccountWindow_EmailAddressLineEdit.setPlaceholderText(_translate("LoginAccountWindow", "ex: burner101@gmail.com"))
        self.LoginAccountWindow_PasswordLineEdit.setPlaceholderText(_translate("LoginAccountWindow", "ex: YarYarDaze123"))
        self.LoginAccountWindow_UsernameLabel.setText(_translate("LoginAccountWindow", "Username:"))
        self.LoginAccountWindow_EmailAddressLabel.setText(_translate("LoginAccountWindow", "Email Address:"))
        self.LoginAccountWindow_PasswordLabel.setText(_translate("LoginAccountWindow", "Password:"))
        self.LoginAccountWindow_LoginBtn.setText(_translate("LoginAccountWindow", "LOGIN"))
        self.LoginAccountWindow_ClearBtn.setText(_translate("LoginAccountWindow", "RESET"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginAccountWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginAccountWindow()
    ui.setupUi(LoginAccountWindow)
    # LoginAccountWindow.show()

    print("You cannot run the app from this window.. Run StartWindow.py!")
    backupAllFiles()

    sys.exit()
