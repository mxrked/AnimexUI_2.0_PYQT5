
from PyQt5 import QtCore, QtGui, QtWidgets
from assets.medias.qrcs import CLUSTER_1, logo
from assets.files._backUpFiles import backupAllFiles

import sys, os
import CreateAccountWindow

class Ui_StartWindow(object):
    def setupUi(self, StartWindow):

        ''' FUNCTIONS '''
        def closeApp():
            sys.exit()

        def closeInfoPopup(popup):

            # Hiding the darken frame
            self.StartWindow_DarkenFrame.setMinimumHeight(0)
            self.StartWindow_DarkenFrame.setMaximumHeight(0)

            # Closing the info dialog
            popup.close()

        def infoPopup():

            # Display darken background
            self.StartWindow_DarkenFrame.setMinimumHeight(810)
            self.StartWindow_DarkenFrame.setMaximumHeight(810)


            # Creating the dialog/popup
            infoPopup = QtWidgets.QDialog()
            infoPopup.setStyleSheet("""
            
                QDialog {
                
	                background-color: rgb(25, 25, 25);
	                border-radius: 5px;
                
                }
            
            """)

            # Settings
            infoPopup.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Hides the title bar
            infoPopup.setFixedSize(300, 150)

            # Widgets
            infoPopupLayout = QtWidgets.QVBoxLayout()
            infoPopupCloser = QtWidgets.QPushButton("✖", infoPopup)
            infoPopupCloser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

            infoPopupCloser.mousePressEvent = lambda event: closeInfoPopup(infoPopup)
            infoPopupCloser.setMinimumSize(30, 30)
            infoPopupCloser.setMaximumSize(30, 30)

            infoPopupCloser.setStyleSheet("""
            
                QPushButton {
                    background-color: rgb(255, 66, 69);
                    color: white;
                    border: none;
                    font-size: 14px;
                }
                
                QPushButton::hover {
                    background-color: rgb(255, 10, 22)
                }
            
            """)

            infoPopupText = QtWidgets.QLabel("By Parker Phelps - (w/ PYQT5)", infoPopup)
            infoPopupText.setStyleSheet("""
            
                QLabel {
                    padding-bottom: 25px;
                    color: white;
                    font-size: 15px;
                }
            
            """)

            infoPopupLayout.addWidget(infoPopupCloser, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
            infoPopupLayout.addWidget(infoPopupText, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)



            infoPopup.setLayout(infoPopupLayout)

            infoPopup.exec_()

        def enterCreateAccountWindow():

            # Showing new window
            self.ui = CreateAccountWindow.Ui_CreateAccountWindow()
            self.window = QtWidgets.QMainWindow()
            self.ui.setupUi(self.window)
            self.window.show()

            # Hiding current window
            StartWindow.hide()

            print("Routing to CreateAccountWindow!")

        StartWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Hides the title bar
        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(1000, 800)
        StartWindow.setMinimumSize(QtCore.QSize(1000, 800))
        StartWindow.setMaximumSize(QtCore.QSize(1000, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/imgs/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StartWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(StartWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.StartWindow_TopFrame = QtWidgets.QFrame(self.centralwidget)
        self.StartWindow_TopFrame.setGeometry(QtCore.QRect(0, 0, 1001, 221))
        self.StartWindow_TopFrame.setStyleSheet("QFrame {\n"
"    background-color: rgb(25, 25, 25);\n"
"    border-image: none;\n"
"}")
        self.StartWindow_TopFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.StartWindow_TopFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.StartWindow_TopFrame.setObjectName("StartWindow_TopFrame")
        self.StartWindow_TopFrameHeading = QtWidgets.QLabel(self.StartWindow_TopFrame)
        self.StartWindow_TopFrameHeading.setGeometry(QtCore.QRect(8, -10, 991, 171))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.StartWindow_TopFrameHeading.setFont(font)
        self.StartWindow_TopFrameHeading.setStyleSheet("QLabel {\n"
"    padding-top: 5px;\n"
"    color: white;\n"
"}")
        self.StartWindow_TopFrameHeading.setAlignment(QtCore.Qt.AlignCenter)
        self.StartWindow_TopFrameHeading.setObjectName("StartWindow_TopFrameHeading")
        self.StartWindow_TopFrameText = QtWidgets.QLabel(self.StartWindow_TopFrame)
        self.StartWindow_TopFrameText.setGeometry(QtCore.QRect(6, 110, 991, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.StartWindow_TopFrameText.setFont(font)
        self.StartWindow_TopFrameText.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    border-image: none;\n"
"}")
        self.StartWindow_TopFrameText.setAlignment(QtCore.Qt.AlignCenter)
        self.StartWindow_TopFrameText.setObjectName("StartWindow_TopFrameText")
        self.StartWindow_ExitBtn = QtWidgets.QPushButton(self.StartWindow_TopFrame)
        self.StartWindow_ExitBtn.clicked.connect(closeApp)
        self.StartWindow_ExitBtn.setGeometry(QtCore.QRect(960, 10, 31, 31))
        self.StartWindow_ExitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartWindow_ExitBtn.setStyleSheet("QPushButton {\n"
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
        self.StartWindow_ExitBtn.setObjectName("StartWindow_ExitBtn")
        self.StartWindow_BottomFrame = QtWidgets.QFrame(self.centralwidget)
        self.StartWindow_BottomFrame.setGeometry(QtCore.QRect(0, 570, 1001, 231))
        self.StartWindow_BottomFrame.setStyleSheet("QFrame {\n"
"    background-color: rgb(25, 25, 25);\n"
"    border-image: none;\n"
"}")
        self.StartWindow_BottomFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.StartWindow_BottomFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.StartWindow_BottomFrame.setObjectName("StartWindow_BottomFrame")
        self.StartWindow_InfoToggler = QtWidgets.QLabel(self.StartWindow_BottomFrame)
        self.StartWindow_InfoToggler.mousePressEvent = lambda event: infoPopup()
        self.StartWindow_InfoToggler.setGeometry(QtCore.QRect(470, 180, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.StartWindow_InfoToggler.setFont(font)
        self.StartWindow_InfoToggler.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartWindow_InfoToggler.setStyleSheet("QLabel {\n"
"    color: rgba(207, 207, 207, .65);\n"
"    padding-top: 3px;\n"
"}\n"
"\n"
"QLabel::hover {\n"
"    color: white;\n"
"}")
        self.StartWindow_InfoToggler.setAlignment(QtCore.Qt.AlignCenter)
        self.StartWindow_InfoToggler.setObjectName("StartWindow_InfoToggler")
        self.StartWindow_BottomFrameInner = QtWidgets.QFrame(self.StartWindow_BottomFrame)
        self.StartWindow_BottomFrameInner.setGeometry(QtCore.QRect(320, 20, 391, 91))
        self.StartWindow_BottomFrameInner.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.StartWindow_BottomFrameInner.setFrameShadow(QtWidgets.QFrame.Raised)
        self.StartWindow_BottomFrameInner.setObjectName("StartWindow_BottomFrameInner")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.StartWindow_BottomFrameInner)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.StartWindow_BottomFrame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(270, 40, 461, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.StartWindow_BottomFrameInnerHL = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.StartWindow_BottomFrameInnerHL.setContentsMargins(0, 0, 0, 0)
        self.StartWindow_BottomFrameInnerHL.setObjectName("StartWindow_BottomFrameInnerHL")
        self.StartWindow_CreateBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.StartWindow_CreateBtn.clicked.connect(enterCreateAccountWindow)
        self.StartWindow_CreateBtn.setMinimumSize(QtCore.QSize(190, 40))
        self.StartWindow_CreateBtn.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        self.StartWindow_CreateBtn.setFont(font)
        self.StartWindow_CreateBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartWindow_CreateBtn.setStyleSheet("QPushButton {\n"
"    border-radius: 6px;\n"
"    background-color: rgb(255, 66, 69);\n"
"    color: white;\n"
"    padding-top: 3px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(255, 10, 22)\n"
"}")
        self.StartWindow_CreateBtn.setObjectName("StartWindow_CreateBtn")
        self.StartWindow_BottomFrameInnerHL.addWidget(self.StartWindow_CreateBtn)
        self.StartWindow_LoginBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.StartWindow_LoginBtn.setMinimumSize(QtCore.QSize(230, 40))
        self.StartWindow_LoginBtn.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        self.StartWindow_LoginBtn.setFont(font)
        self.StartWindow_LoginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartWindow_LoginBtn.setStyleSheet("QPushButton {\n"
"    border-radius: 6px;\n"
"    background-color: rgb(255, 66, 69);\n"
"    color: white;\n"
"    padding-top: 3px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(255, 10, 22)\n"
"}")
        self.StartWindow_LoginBtn.setObjectName("StartWindow_LoginBtn")
        self.StartWindow_BottomFrameInnerHL.addWidget(self.StartWindow_LoginBtn)
        self.StartWindow_MiddleFrame = QtWidgets.QFrame(self.centralwidget)
        self.StartWindow_MiddleFrame.setGeometry(QtCore.QRect(0, 190, 1001, 381))
        self.StartWindow_MiddleFrame.setStyleSheet("border-image: url(:/newPrefix/imgs/CLUSTER_1.png);")
        self.StartWindow_MiddleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.StartWindow_MiddleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.StartWindow_MiddleFrame.setObjectName("StartWindow_MiddleFrame")
        self.StartWindow_MiddleFrameBg = QtWidgets.QFrame(self.StartWindow_MiddleFrame)
        self.StartWindow_MiddleFrameBg.setGeometry(QtCore.QRect(0, 0, 1001, 381))
        self.StartWindow_MiddleFrameBg.setStyleSheet("border-image: none;\n"
"background-color: rgba(0, 0, 0, .40);")
        self.StartWindow_MiddleFrameBg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.StartWindow_MiddleFrameBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.StartWindow_MiddleFrameBg.setObjectName("StartWindow_MiddleFrameBg")
        self.StartWindow_DarkenFrame = QtWidgets.QFrame(self.centralwidget)
        self.StartWindow_DarkenFrame.setGeometry(QtCore.QRect(0, 0, 1001, 0))
        self.StartWindow_DarkenFrame.setMaximumSize(QtCore.QSize(16777215, 0))
        self.StartWindow_DarkenFrame.setStyleSheet("QFrame {\n"
"\n"
"    \n"
"    background-color: rgba(0, 0, 0, .60);\n"
"\n"
"}")
        self.StartWindow_DarkenFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.StartWindow_DarkenFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.StartWindow_DarkenFrame.setObjectName("StartWindow_DarkenFrame")
        StartWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartWindow)
        QtCore.QMetaObject.connectSlotsByName(StartWindow)

    def retranslateUi(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "AnimexUI - Welcome"))
        self.StartWindow_TopFrameHeading.setText(_translate("StartWindow", "ANIMEX.UI"))
        self.StartWindow_TopFrameText.setText(_translate("StartWindow", "Anime/Manga Desktop App"))
        self.StartWindow_ExitBtn.setText(_translate("StartWindow", "✖"))
        self.StartWindow_InfoToggler.setText(_translate("StartWindow", "🛈"))
        self.StartWindow_CreateBtn.setText(_translate("StartWindow", "CREATE AN ACCOUNT"))
        self.StartWindow_LoginBtn.setText(_translate("StartWindow", "LOGIN TO YOUR ACCOUNT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartWindow = QtWidgets.QMainWindow()
    ui = Ui_StartWindow()
    ui.setupUi(StartWindow)
    StartWindow.show()

    # Backs up the files after exiting program
    # backupAllFiles()


    sys.exit(app.exec_())
