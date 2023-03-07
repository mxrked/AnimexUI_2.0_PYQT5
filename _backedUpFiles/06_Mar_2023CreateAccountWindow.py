import re

from PyQt5 import QtCore, QtGui, QtWidgets
from assets.medias.qrcs import jotaro_BG
from assets.files.CLASSES import Account
from assets.files.ARRAYS import *
from assets.files._backUpFiles import backupAllFiles

import sys
import StartWindow


class Ui_CreateAccountWindow(object):

    def setupUi(self, CreateAccountWindow):


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
            CreateAccountWindow.hide()

            print("Routing to StartWindow!")

        def clearInputs():

            self.CreateAccountWindow_UsernameLineEdit.setText(None)
            self.CreateAccountWindow_EmailAddressLineEdit.setText(None)
            self.CreateAccountWindow_PasswordLineEdit.setText(None)
            self.CreateAccountWindow_ConfirmPasswordLineEdit.setText(None)

            self.CreateAccountWindow_UsernameLineEdit.setStyleSheet("QLineEdit {\n"
                "    border: none;\n"
                "    background-color: rgb(189, 189, 189);\n"
                "    padding-left: 10px;\n"
                "    padding-right: 10px;\n"
                "}\n"
                "\n"
                "QLineEdit::focus {\n"
                "    border: 2px solid rgb(119, 196, 255)\n"
                "}")
            self.CreateAccountWindow_EmailAddressLineEdit.setStyleSheet("QLineEdit {\n"
                "    border: none;\n"
                "    background-color: rgb(189, 189, 189);\n"
                "    padding-left: 10px;\n"
                "    padding-right: 10px;\n"
                "}\n"
                "\n"
                "QLineEdit::focus {\n"
                "    border: 2px solid rgb(119, 196, 255)\n"
                "}")
            self.CreateAccountWindow_PasswordLineEdit.setStyleSheet("QLineEdit {\n"
                "    border: none;\n"
                "    background-color: rgb(189, 189, 189);\n"
                "    padding-left: 10px;\n"
                "    padding-right: 10px;\n"
                "}\n"
                "\n"
                "QLineEdit::focus {\n"
                "    border: 2px solid rgb(119, 196, 255)\n"
                "}")
            self.CreateAccountWindow_ConfirmPasswordLineEdit.setStyleSheet("QLineEdit {\n"
                "    border: none;\n"
                "    background-color: rgb(189, 189, 189);\n"
                "    padding-left: 10px;\n"
                "    padding-right: 10px;\n"
                "}\n"
                "\n"
                "QLineEdit::focus {\n"
                "    border: 2px solid rgb(119, 196, 255)\n"
                "}")

        def createAccount():

            # Declaring a new Account object
            newAccount = Account(None, None, None)

            # Getting each of the input texts
            usernameText = self.CreateAccountWindow_UsernameLineEdit.text()
            emailText = self.CreateAccountWindow_EmailAddressLineEdit.text()
            passwordText = self.CreateAccountWindow_PasswordLineEdit.text()
            confirmPasswordText = self.CreateAccountWindow_ConfirmPasswordLineEdit.text()

            # Creating accounts
            if len(accounts) == 0:

                # If username is valid
                if usernameText != "" and usernameText != None:

                    print("Valid Username.")
                    validUsername.clear()
                    validUsername.append(True) # Marking as valid

                    self.CreateAccountWindow_UsernameLineEdit.setStyleSheet("QLineEdit {\n"
                "    border: none;\n"
                "    background-color: rgb(189, 189, 189);\n"
                "    padding-left: 10px;\n"
                "    padding-right: 10px;\n"
                "}\n"
                "\n"
                "QLineEdit::focus {\n"
                "    border: 2px solid rgb(119, 196, 255)\n"
                "}")

                # If username is invalid
                if usernameText == "" or usernameText == None:

                    print("Invalid Username..")
                    validUsername.clear()
                    validUsername.append(False) # Marking as invalid

                    self.CreateAccountWindow_UsernameLineEdit.setStyleSheet("QLineEdit {\n"
                "    border: 2px solid red;\n"
                "    background-color: rgb(189, 189, 189);\n"
                "    padding-left: 10px;\n"
                "    padding-right: 10px;\n"
                "}\n"
                "\n"
                "QLineEdit::focus {\n"
                "    border: 2px solid rgb(119, 196, 255)\n"
                "}")

                # If email is valid
                emailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                if re.fullmatch(emailRegex, emailText):

                    print("Valid Email.")
                    validEmail.clear()
                    validEmail.append(True) # Marking as valid

                    self.CreateAccountWindow_EmailAddressLineEdit.setStyleSheet("QLineEdit {\n"
                "    border: none;\n"
                "    background-color: rgb(189, 189, 189);\n"
                "    padding-left: 10px;\n"
                "    padding-right: 10px;\n"
                "}\n"
                "\n"
                "QLineEdit::focus {\n"
                "    border: 2px solid rgb(119, 196, 255)\n"
                "}")

                # If email is invalid
                if not re.fullmatch(emailRegex, emailText):

                    print("Invalid Email..")
                    validEmail.clear()
                    validEmail.append(False) # Marking as invalid

                    self.CreateAccountWindow_EmailAddressLineEdit.setStyleSheet("QLineEdit {\n"
                "    border: 2px solid red;\n"
                "    background-color: rgb(189, 189, 189);\n"
                "    padding-left: 10px;\n"
                "    padding-right: 10px;\n"
                "}\n"
                "\n"
                "QLineEdit::focus {\n"
                "    border: 2px solid rgb(119, 196, 255)\n"
                "}")

                # If passwords are valid
                if passwordText != "" and passwordText != None and confirmPasswordText != "" and confirmPasswordText != None:

                    # Checking if passwords match
                    if passwordText == confirmPasswordText:

                        print("The passwords are the same.")
                        validPassword.clear()
                        validPassword.append(True)

                        self.CreateAccountWindow_PasswordLineEdit.setStyleSheet("QLineEdit {\n"
                    "    border: none;\n"
                    "    background-color: rgb(189, 189, 189);\n"
                    "    padding-left: 10px;\n"
                    "    padding-right: 10px;\n"
                    "}\n"
                    "\n"
                    "QLineEdit::focus {\n"
                    "    border: 2px solid rgb(119, 196, 255)\n"
                    "}")
                        self.CreateAccountWindow_ConfirmPasswordLineEdit.setStyleSheet("QLineEdit {\n"
                    "    border: none;\n"
                    "    background-color: rgb(189, 189, 189);\n"
                    "    padding-left: 10px;\n"
                    "    padding-right: 10px;\n"
                    "}\n"
                    "\n"
                    "QLineEdit::focus {\n"
                    "    border: 2px solid rgb(119, 196, 255)\n"
                    "}")

                    else:

                        print("The passwords do not match..")
                        validPassword.clear()
                        validPassword.append(False)

                        self.CreateAccountWindow_PasswordLineEdit.setStyleSheet("QLineEdit {\n"
                    "    border: 2px solid red;\n"
                    "    background-color: rgb(189, 189, 189);\n"
                    "    padding-left: 10px;\n"
                    "    padding-right: 10px;\n"
                    "}\n"
                    "\n"
                    "QLineEdit::focus {\n"
                    "    border: 2px solid rgb(119, 196, 255)\n"
                    "}")
                        self.CreateAccountWindow_ConfirmPasswordLineEdit.setStyleSheet("QLineEdit {\n"
                    "    border: 2px solid red;\n"
                    "    background-color: rgb(189, 189, 189);\n"
                    "    padding-left: 10px;\n"
                    "    padding-right: 10px;\n"
                    "}\n"
                    "\n"
                    "QLineEdit::focus {\n"
                    "    border: 2px solid rgb(119, 196, 255)\n"
                    "}")

                # If passwords are invalid
                if passwordText == "" or passwordText == None or confirmPasswordText == "" or confirmPasswordText == None:

                    print("Invalid Passwords..")
                    validPassword.clear()
                    validPassword.append(False) # Marking as invalid

                    self.CreateAccountWindow_PasswordLineEdit.setStyleSheet("QLineEdit {\n"
                "    border: 2px solid red;\n"
                "    background-color: rgb(189, 189, 189);\n"
                "    padding-left: 10px;\n"
                "    padding-right: 10px;\n"
                "}\n"
                "\n"
                "QLineEdit::focus {\n"
                "    border: 2px solid rgb(119, 196, 255)\n"
                "}")
                    self.CreateAccountWindow_ConfirmPasswordLineEdit.setStyleSheet("QLineEdit {\n"
                "    border: 2px solid red;\n"
                "    background-color: rgb(189, 189, 189);\n"
                "    padding-left: 10px;\n"
                "    padding-right: 10px;\n"
                "}\n"
                "\n"
                "QLineEdit::focus {\n"
                "    border: 2px solid rgb(119, 196, 255)\n"
                "}")

                # Creating account when all is valid
                if validUsername[0] == True:
                    if validEmail[0] == True:
                        if validPassword[0] == True:

                            # Appending to object
                            newAccount.setUsername(usernameText)
                            newAccount.setEmail(emailText)
                            newAccount.setPassword(passwordText)

                            # Clearing inputs
                            self.CreateAccountWindow_UsernameLineEdit.setText("")
                            self.CreateAccountWindow_EmailAddressLineEdit.setText("")
                            self.CreateAccountWindow_PasswordLineEdit.setText("")
                            self.CreateAccountWindow_ConfirmPasswordLineEdit.setText("")

                            # Reseting valid arrays
                            validUsername.clear()
                            validEmail.clear()
                            validPassword.clear()

                            validUsername.append(False)
                            validEmail.append(False)
                            validPassword.append(False)

                            # Adding account to accounts
                            accounts.append(newAccount)

                            # Routing user back to StartWindow
                            enterStartWindow()

            if len(accounts) >= 1:

                for account in accounts: # Checking for if any of the other accounts match the one being created

                    # If username is valid
                    if account.getUsername() != usernameText:
                        if usernameText != "" and usernameText != None:

                            print("Valid Username.")
                            validUsername.clear()
                            validUsername.append(True) # Marking as valid

                            self.CreateAccountWindow_UsernameLineEdit.setStyleSheet("QLineEdit {\n"
                        "    border: none;\n"
                        "    background-color: rgb(189, 189, 189);\n"
                        "    padding-left: 10px;\n"
                        "    padding-right: 10px;\n"
                        "}\n"
                        "\n"
                        "QLineEdit::focus {\n"
                        "    border: 2px solid rgb(119, 196, 255)\n"
                        "}")
                    else:
                        print("This username is already in use..")
                        validUsername.clear()
                        validUsername.append(False) # Marking as invalid

                    # If username is invalid
                    if usernameText == "" or usernameText == None:

                        print("Invalid Username..")
                        validUsername.clear()
                        validUsername.append(False) # Marking as invalid

                        self.CreateAccountWindow_UsernameLineEdit.setStyleSheet("QLineEdit {\n"
                    "    border: 2px solid red;\n"
                    "    background-color: rgb(189, 189, 189);\n"
                    "    padding-left: 10px;\n"
                    "    padding-right: 10px;\n"
                    "}\n"
                    "\n"
                    "QLineEdit::focus {\n"
                    "    border: 2px solid rgb(119, 196, 255)\n"
                    "}")

                    # If email is valid
                    emailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                    if account.getEmail() != emailText:
                        if re.fullmatch(emailRegex, emailText):

                            print("Valid Email.")
                            validEmail.clear()
                            validEmail.append(True) # Marking as valid

                            self.CreateAccountWindow_EmailAddressLineEdit.setStyleSheet("QLineEdit {\n"
                        "    border: none;\n"
                        "    background-color: rgb(189, 189, 189);\n"
                        "    padding-left: 10px;\n"
                        "    padding-right: 10px;\n"
                        "}\n"
                        "\n"
                        "QLineEdit::focus {\n"
                        "    border: 2px solid rgb(119, 196, 255)\n"
                        "}")
                    else:
                        print("This email is already in use..")
                        self.CreateAccountWindow_EmailAddressLineEdit.setStyleSheet("QLineEdit {\n"
                    "    border: 2px solid red;\n"
                    "    background-color: rgb(189, 189, 189);\n"
                    "    padding-left: 10px;\n"
                    "    padding-right: 10px;\n"
                    "}\n"
                    "\n"
                    "QLineEdit::focus {\n"
                    "    border: 2px solid rgb(119, 196, 255)\n"
                    "}")

                        validEmail.clear()
                        validEmail.append(False) # Marking as invalid

                    # If email is invalid
                    if not re.fullmatch(emailRegex, emailText):

                        print("Invalid Email..")
                        validEmail.clear()
                        validEmail.append(False) # Marking as invalid

                        self.CreateAccountWindow_EmailAddressLineEdit.setStyleSheet("QLineEdit {\n"
                    "    border: 2px solid red;\n"
                    "    background-color: rgb(189, 189, 189);\n"
                    "    padding-left: 10px;\n"
                    "    padding-right: 10px;\n"
                    "}\n"
                    "\n"
                    "QLineEdit::focus {\n"
                    "    border: 2px solid rgb(119, 196, 255)\n"
                    "}")

                    # If passwords are valid
                    if passwordText != "" and passwordText != None and confirmPasswordText != "" and confirmPasswordText != None:

                        # Checking if passwords match
                        if passwordText == confirmPasswordText:

                            print("The passwords are the same.")
                            validPassword.clear()
                            validPassword.append(True)

                            self.CreateAccountWindow_PasswordLineEdit.setStyleSheet("QLineEdit {\n"
                        "    border: none;\n"
                        "    background-color: rgb(189, 189, 189);\n"
                        "    padding-left: 10px;\n"
                        "    padding-right: 10px;\n"
                        "}\n"
                        "\n"
                        "QLineEdit::focus {\n"
                        "    border: 2px solid rgb(119, 196, 255)\n"
                        "}")
                            self.CreateAccountWindow_ConfirmPasswordLineEdit.setStyleSheet("QLineEdit {\n"
                        "    border: none;\n"
                        "    background-color: rgb(189, 189, 189);\n"
                        "    padding-left: 10px;\n"
                        "    padding-right: 10px;\n"
                        "}\n"
                        "\n"
                        "QLineEdit::focus {\n"
                        "    border: 2px solid rgb(119, 196, 255)\n"
                        "}")

                        else:

                            print("The passwords do not match..")
                            validPassword.clear()
                            validPassword.append(False)

                            self.CreateAccountWindow_PasswordLineEdit.setStyleSheet("QLineEdit {\n"
                    "    border: 2px solid red;\n"
                    "    background-color: rgb(189, 189, 189);\n"
                    "    padding-left: 10px;\n"
                    "    padding-right: 10px;\n"
                    "}\n"
                    "\n"
                    "QLineEdit::focus {\n"
                    "    border: 2px solid rgb(119, 196, 255)\n"
                    "}")
                        self.CreateAccountWindow_ConfirmPasswordLineEdit.setStyleSheet("QLineEdit {\n"
                    "    border: 2px solid red;\n"
                    "    background-color: rgb(189, 189, 189);\n"
                    "    padding-left: 10px;\n"
                    "    padding-right: 10px;\n"
                    "}\n"
                    "\n"
                    "QLineEdit::focus {\n"
                    "    border: 2px solid rgb(119, 196, 255)\n"
                    "}")

                    # If passwords are invalid
                    if passwordText == "" or passwordText == None or confirmPasswordText == "" or confirmPasswordText == None:

                        print("Invalid Passwords..")
                        validPassword.clear()
                        validPassword.append(False) # Marking as invalid


                        self.CreateAccountWindow_PasswordLineEdit.setStyleSheet("QLineEdit {\n"
                    "    border: 2px solid red;\n"
                    "    background-color: rgb(189, 189, 189);\n"
                    "    padding-left: 10px;\n"
                    "    padding-right: 10px;\n"
                    "}\n"
                    "\n"
                    "QLineEdit::focus {\n"
                    "    border: 2px solid rgb(119, 196, 255)\n"
                    "}")

                # Creating account when all is valid
                if validUsername[0] == True:
                    if validEmail[0] == True:
                        if validPassword[0] == True:

                            # Appending to object
                            newAccount.setUsername(usernameText)
                            newAccount.setEmail(emailText)
                            newAccount.setPassword(passwordText)

                            # Clearing inputs
                            self.CreateAccountWindow_UsernameLineEdit.setText("")
                            self.CreateAccountWindow_EmailAddressLineEdit.setText("")
                            self.CreateAccountWindow_PasswordLineEdit.setText("")
                            self.CreateAccountWindow_ConfirmPasswordLineEdit.setText("")

                            # Reseting valid arrays
                            validUsername.clear()
                            validEmail.clear()
                            validPassword.clear()

                            validUsername.append(False)
                            validEmail.append(False)
                            validPassword.append(False)

                            # Adding account to accounts
                            accounts.append(newAccount)


                            # Routing user back to StartWindow
                            enterStartWindow()

                # # Appending to object
                # newAccount.setUsername(usernameText)
                # newAccount.setEmail(emailText)
                # newAccount.setPassword(passwordText)
                #
                # # Clearing inputs
                # self.CreateAccountWindow_UsernameLineEdit.setText("")
                # self.CreateAccountWindow_EmailAddressLineEdit.setText("")
                # self.CreateAccountWindow_PasswordLineEdit.setText("")
                # self.CreateAccountWindow_ConfirmPasswordLineEdit.setText("")
                #
                # # Reseting valid arrays
                # validUsername.clear()
                # validEmail.clear()
                # validPassword.clear()
                #
                # validUsername.append(False)
                # validEmail.append(False)
                # validPassword.append(False)
                #
                # # Adding account to accounts
                # accounts.append(newAccount)
                #
                # # Routing user back to StartWindow
                # enterStartWindow()


        for account in accounts:
            print(account.getUsername() + "," + account.getEmail() + "," + account.getPassword())


        CreateAccountWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Hides the title bar
        CreateAccountWindow.setObjectName("CreateAccountWindow")
        CreateAccountWindow.resize(900, 670)
        CreateAccountWindow.setMinimumSize(QtCore.QSize(900, 670))
        CreateAccountWindow.setMaximumSize(QtCore.QSize(900, 670))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/imgs/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CreateAccountWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(CreateAccountWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CreateAccountWindow_MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.CreateAccountWindow_MainFrame.setGeometry(QtCore.QRect(0, 0, 611, 701))
        self.CreateAccountWindow_MainFrame.setStyleSheet("QFrame {\n"
"    background-color: rgb(25, 25, 25);\n"
"    border-image: none;\n"
"}")
        self.CreateAccountWindow_MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CreateAccountWindow_MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CreateAccountWindow_MainFrame.setObjectName("CreateAccountWindow_MainFrame")
        self.CreateAccountWindow_ExitBtn = QtWidgets.QPushButton(self.CreateAccountWindow_MainFrame)
        self.CreateAccountWindow_ExitBtn.clicked.connect(closeApp)
        self.CreateAccountWindow_ExitBtn.setGeometry(QtCore.QRect(60, 20, 31, 31))
        self.CreateAccountWindow_ExitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CreateAccountWindow_ExitBtn.setStyleSheet("QPushButton {\n"
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
        self.CreateAccountWindow_ExitBtn.setObjectName("CreateAccountWindow_ExitBtn")
        self.CreateAccountWindow_BackBtn = QtWidgets.QPushButton(self.CreateAccountWindow_MainFrame)
        self.CreateAccountWindow_BackBtn.clicked.connect(enterStartWindow)
        self.CreateAccountWindow_BackBtn.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.CreateAccountWindow_BackBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CreateAccountWindow_BackBtn.setStyleSheet("QPushButton {\n"
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
        self.CreateAccountWindow_BackBtn.setObjectName("CreateAccountWindow_BackBtn")
        self.CreateAccountWindow_MainHeadingLabel = QtWidgets.QLabel(self.CreateAccountWindow_MainFrame)
        self.CreateAccountWindow_MainHeadingLabel.setGeometry(QtCore.QRect(40, 120, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.CreateAccountWindow_MainHeadingLabel.setFont(font)
        self.CreateAccountWindow_MainHeadingLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    background: none;\n"
"    color: white;\n"
"}")
        self.CreateAccountWindow_MainHeadingLabel.setObjectName("CreateAccountWindow_MainHeadingLabel")
        self.CreateAccountWindow_MainTextLabel = QtWidgets.QLabel(self.CreateAccountWindow_MainFrame)
        self.CreateAccountWindow_MainTextLabel.setGeometry(QtCore.QRect(40, 170, 401, 81))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        self.CreateAccountWindow_MainTextLabel.setFont(font)
        self.CreateAccountWindow_MainTextLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    background: none;\n"
"    color: white;\n"
"}")
        self.CreateAccountWindow_MainTextLabel.setWordWrap(True)
        self.CreateAccountWindow_MainTextLabel.setObjectName("CreateAccountWindow_MainTextLabel")
        self.CreateAccountWindow_UsernameLineEdit = QtWidgets.QLineEdit(self.CreateAccountWindow_MainFrame)
        self.CreateAccountWindow_UsernameLineEdit.setGeometry(QtCore.QRect(190, 310, 271, 41))
        self.CreateAccountWindow_UsernameLineEdit.setStyleSheet("QLineEdit {\n"
"    border: none;\n"
"    background-color: rgb(189, 189, 189);\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"QLineEdit::focus {\n"
"    border: 2px solid rgb(119, 196, 255)\n"
"}")
        self.CreateAccountWindow_UsernameLineEdit.setText("")
        self.CreateAccountWindow_UsernameLineEdit.setObjectName("CreateAccountWindow_UsernameLineEdit")
        self.CreateAccountWindow_EmailAddressLineEdit = QtWidgets.QLineEdit(self.CreateAccountWindow_MainFrame)
        self.CreateAccountWindow_EmailAddressLineEdit.setGeometry(QtCore.QRect(190, 370, 271, 41))
        self.CreateAccountWindow_EmailAddressLineEdit.setStyleSheet("QLineEdit {\n"
"    border: none;\n"
"    background-color: rgb(189, 189, 189);\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"QLineEdit::focus {\n"
"    border: 2px solid rgb(119, 196, 255)\n"
"}")
        self.CreateAccountWindow_EmailAddressLineEdit.setText("")
        self.CreateAccountWindow_EmailAddressLineEdit.setObjectName("CreateAccountWindow_EmailAddressLineEdit")
        self.CreateAccountWindow_PasswordLineEdit = QtWidgets.QLineEdit(self.CreateAccountWindow_MainFrame)
        self.CreateAccountWindow_PasswordLineEdit.setGeometry(QtCore.QRect(190, 430, 271, 41))
        self.CreateAccountWindow_PasswordLineEdit.setStyleSheet("QLineEdit {\n"
"    border: none;\n"
"    background-color: rgb(189, 189, 189);\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"QLineEdit::focus {\n"
"    border: 2px solid rgb(119, 196, 255)\n"
"}")
        self.CreateAccountWindow_PasswordLineEdit.setText("")
        self.CreateAccountWindow_PasswordLineEdit.setObjectName("CreateAccountWindow_PasswordLineEdit")
        self.CreateAccountWindow_UsernameLabel = QtWidgets.QLabel(self.CreateAccountWindow_MainFrame)
        self.CreateAccountWindow_UsernameLabel.setGeometry(QtCore.QRect(40, 320, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.CreateAccountWindow_UsernameLabel.setFont(font)
        self.CreateAccountWindow_UsernameLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    background: none;\n"
"    color: white;\n"
"}\n"
"")
        self.CreateAccountWindow_UsernameLabel.setObjectName("CreateAccountWindow_UsernameLabel")
        self.CreateAccountWindow_EmailAddressLabel = QtWidgets.QLabel(self.CreateAccountWindow_MainFrame)
        self.CreateAccountWindow_EmailAddressLabel.setGeometry(QtCore.QRect(40, 380, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.CreateAccountWindow_EmailAddressLabel.setFont(font)
        self.CreateAccountWindow_EmailAddressLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    background: none;\n"
"    color: white;\n"
"}\n"
"")
        self.CreateAccountWindow_EmailAddressLabel.setObjectName("CreateAccountWindow_EmailAddressLabel")
        self.CreateAccountWindow_PasswordLabel = QtWidgets.QLabel(self.CreateAccountWindow_MainFrame)
        self.CreateAccountWindow_PasswordLabel.setGeometry(QtCore.QRect(40, 440, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.CreateAccountWindow_PasswordLabel.setFont(font)
        self.CreateAccountWindow_PasswordLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    background: none;\n"
"    color: white;\n"
"}\n"
"")
        self.CreateAccountWindow_PasswordLabel.setObjectName("CreateAccountWindow_PasswordLabel")
        self.CreateAccountWindow_ConfirmPasswordLineEdit = QtWidgets.QLineEdit(self.CreateAccountWindow_MainFrame)
        self.CreateAccountWindow_ConfirmPasswordLineEdit.setGeometry(QtCore.QRect(190, 490, 271, 41))
        self.CreateAccountWindow_ConfirmPasswordLineEdit.setStyleSheet("QLineEdit {\n"
"    border: none;\n"
"    background-color: rgb(189, 189, 189);\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"QLineEdit::focus {\n"
"    border: 2px solid rgb(119, 196, 255)\n"
"}")
        self.CreateAccountWindow_ConfirmPasswordLineEdit.setText("")
        self.CreateAccountWindow_ConfirmPasswordLineEdit.setObjectName("CreateAccountWindow_ConfirmPasswordLineEdit")
        self.CreateAccountWindow_ConfirmPasswordLabel = QtWidgets.QLabel(self.CreateAccountWindow_MainFrame)
        self.CreateAccountWindow_ConfirmPasswordLabel.setGeometry(QtCore.QRect(40, 500, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.CreateAccountWindow_ConfirmPasswordLabel.setFont(font)
        self.CreateAccountWindow_ConfirmPasswordLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    background: none;\n"
"    color: white;\n"
"}\n"
"")
        self.CreateAccountWindow_ConfirmPasswordLabel.setObjectName("CreateAccountWindow_ConfirmPasswordLabel")
        self.CreateAccountWindow_BtnsFrame = QtWidgets.QFrame(self.CreateAccountWindow_MainFrame)
        self.CreateAccountWindow_BtnsFrame.setGeometry(QtCore.QRect(30, 540, 201, 111))
        self.CreateAccountWindow_BtnsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CreateAccountWindow_BtnsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CreateAccountWindow_BtnsFrame.setObjectName("CreateAccountWindow_BtnsFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.CreateAccountWindow_BtnsFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CreateAccountWindow_CreateBtn = QtWidgets.QPushButton(self.CreateAccountWindow_BtnsFrame)
        self.CreateAccountWindow_CreateBtn.clicked.connect(createAccount)
        self.CreateAccountWindow_CreateBtn.setMinimumSize(QtCore.QSize(85, 40))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.CreateAccountWindow_CreateBtn.setFont(font)
        self.CreateAccountWindow_CreateBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CreateAccountWindow_CreateBtn.setStyleSheet("QPushButton {\n"
"    border-radius: 6px;\n"
"    background-color: rgb(255, 66, 69);\n"
"    color: white;\n"
"    padding-top: 3px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(255, 10, 22)\n"
"}")
        self.CreateAccountWindow_CreateBtn.setObjectName("CreateAccountWindow_CreateBtn")
        self.horizontalLayout.addWidget(self.CreateAccountWindow_CreateBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.CreateAccountWindow_ClearBtn = QtWidgets.QPushButton(self.CreateAccountWindow_BtnsFrame)
        self.CreateAccountWindow_ClearBtn.clicked.connect(clearInputs)
        self.CreateAccountWindow_ClearBtn.setMinimumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        self.CreateAccountWindow_ClearBtn.setFont(font)
        self.CreateAccountWindow_ClearBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CreateAccountWindow_ClearBtn.setStyleSheet("QPushButton {\n"
"    border-radius: 6px;\n"
"    background-color: rgb(255, 66, 69);\n"
"    color: white;\n"
"    padding-top: 3px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(255, 10, 22)\n"
"}")
        self.CreateAccountWindow_ClearBtn.setObjectName("CreateAccountWindow_ClearBtn")
        self.horizontalLayout.addWidget(self.CreateAccountWindow_ClearBtn)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(500, -10, 401, 711))
        self.frame.setStyleSheet("QFrame {\n"
"    background-image: url(:/newPrefix/imgs/jotaro_BG.jpg);\n"
"    background-position: center top;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 10, 401, 671))
        self.frame_2.setStyleSheet("QFrame {\n"
"    background: none;\n"
"    background-color: rgba(0, 0, 0, .4);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        CreateAccountWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CreateAccountWindow)
        QtCore.QMetaObject.connectSlotsByName(CreateAccountWindow)

    def retranslateUi(self, CreateAccountWindow):
        _translate = QtCore.QCoreApplication.translate
        CreateAccountWindow.setWindowTitle(_translate("CreateAccountWindow", "AnimexUI - Create an Account"))
        self.CreateAccountWindow_ExitBtn.setText(_translate("CreateAccountWindow", "✖"))
        self.CreateAccountWindow_BackBtn.setText(_translate("CreateAccountWindow", "🠜"))
        self.CreateAccountWindow_MainHeadingLabel.setText(_translate("CreateAccountWindow", "Create An Account."))
        self.CreateAccountWindow_MainTextLabel.setText(_translate("CreateAccountWindow", "Provide below, with the basic information that is needed to create your account."))
        self.CreateAccountWindow_UsernameLineEdit.setPlaceholderText(_translate("CreateAccountWindow", "ex: animelover1337"))
        self.CreateAccountWindow_EmailAddressLineEdit.setPlaceholderText(_translate("CreateAccountWindow", "ex: burner101@gmail.com"))
        self.CreateAccountWindow_PasswordLineEdit.setPlaceholderText(_translate("CreateAccountWindow", "ex: YarYarDaze123"))
        self.CreateAccountWindow_UsernameLabel.setText(_translate("CreateAccountWindow", "Username:"))
        self.CreateAccountWindow_EmailAddressLabel.setText(_translate("CreateAccountWindow", "Email Address:"))
        self.CreateAccountWindow_PasswordLabel.setText(_translate("CreateAccountWindow", "Password:"))
        self.CreateAccountWindow_ConfirmPasswordLineEdit.setPlaceholderText(_translate("CreateAccountWindow", "ex: YarYarDaze123"))
        self.CreateAccountWindow_ConfirmPasswordLabel.setText(_translate("CreateAccountWindow", "Con. Password:"))
        self.CreateAccountWindow_CreateBtn.setText(_translate("CreateAccountWindow", "CREATE"))
        self.CreateAccountWindow_ClearBtn.setText(_translate("CreateAccountWindow", "RESET"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateAccountWindow = QtWidgets.QMainWindow()
    ui = Ui_CreateAccountWindow()
    ui.setupUi(CreateAccountWindow)
    # CreateAccountWindow.show()

    print("You cannot run the app from this window.. Run StartWindow.py!")
    backupAllFiles()

    sys.exit()
