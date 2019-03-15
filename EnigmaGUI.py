# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.11.3

from PyQt5 import QtCore, QtGui, QtWidgets

# Create Main UI Window
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("Enigma Sim")
        MainWindow.resize(640, 480)
        MainWindow.setFixedSize(640,480)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 291, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.staticwheelLBIgnore = QtWidgets.QLabel(self.groupBox)
        self.staticwheelLBIgnore.setGeometry(QtCore.QRect(80, 30, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(8)

        self.staticwheelLBIgnore.setFont(font)
        self.staticwheelLBIgnore.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.staticwheelLBIgnore.setObjectName("staticwheelLBIgnore")
        self.rotor2SrIgnore = QtWidgets.QLabel(self.groupBox)
        self.rotor2SrIgnore.setGeometry(QtCore.QRect(10, 80, 61, 21))
        self.rotor2SrIgnore.setFrameShape(QtWidgets.QFrame.Box)
        self.rotor2SrIgnore.setAlignment(QtCore.Qt.AlignCenter)
        self.rotor2SrIgnore.setObjectName("rotor2SrIgnore")
        self.rotor1selection = QtWidgets.QComboBox(self.groupBox)
        self.rotor1selection.setGeometry(QtCore.QRect(80, 50, 201, 22))
        font = QtGui.QFont()
        font.setPointSize(8)

        self.rotor1selection.setFont(font)
        self.rotor1selection.setObjectName("rotor1selection")
        self.rotor1selection.addItem("")
        self.rotor1selection.addItem("")
        self.rotor1selection.addItem("")
        self.rotor1selection.addItem("")
        self.rotor1selection.addItem("")
        self.rotor1selection.addItem("")
        self.rotor1selection.addItem("")
        self.rotor1selection.addItem("")

        self.rotor3SrIgnore = QtWidgets.QLabel(self.groupBox)
        self.rotor3SrIgnore.setGeometry(QtCore.QRect(10, 110, 61, 21))
        self.rotor3SrIgnore.setFrameShape(QtWidgets.QFrame.Box)
        self.rotor3SrIgnore.setAlignment(QtCore.Qt.AlignCenter)
        self.rotor3SrIgnore.setObjectName("rotor3SrIgnore")
        self.rotor2selection = QtWidgets.QComboBox(self.groupBox)
        self.rotor2selection.setGeometry(QtCore.QRect(80, 80, 201, 22))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.rotor2selection.setFont(font)
        self.rotor2selection.setObjectName("rotor2selection")
        self.rotor2selection.addItem("")
        self.rotor2selection.addItem("")
        self.rotor2selection.addItem("")
        self.rotor2selection.addItem("")
        self.rotor2selection.addItem("")
        self.rotor2selection.addItem("")
        self.rotor2selection.addItem("")
        self.rotor2selection.addItem("")

        self.rotor1SrIgnore = QtWidgets.QLabel(self.groupBox)
        self.rotor1SrIgnore.setGeometry(QtCore.QRect(10, 50, 61, 21))
        self.rotor1SrIgnore.setFrameShape(QtWidgets.QFrame.Box)
        self.rotor1SrIgnore.setAlignment(QtCore.Qt.AlignCenter)
        self.rotor1SrIgnore.setObjectName("rotor1SrIgnore")
        self.rotor3selection = QtWidgets.QComboBox(self.groupBox)
        self.rotor3selection.setGeometry(QtCore.QRect(80, 110, 201, 22))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.rotor3selection.setFont(font)
        self.rotor3selection.setObjectName("rotor3selection")
        self.rotor3selection.addItem("")
        self.rotor3selection.addItem("")
        self.rotor3selection.addItem("")
        self.rotor3selection.addItem("")
        self.rotor3selection.addItem("")
        self.rotor3selection.addItem("")
        self.rotor3selection.addItem("")
        self.rotor3selection.addItem("")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(360, 10, 261, 141))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.rotor1DropDown = QtWidgets.QComboBox(self.groupBox_2)
        self.rotor1DropDown.setGeometry(QtCore.QRect(190, 110, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rotor1DropDown.setFont(font)
        self.rotor1DropDown.setObjectName("rotor1DropDown")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
        self.rotor1DropDown.addItem("")
# Change the font for the display of 3 rotors
        displayfont = QtGui.QFont()
        displayfont.setBold(True)
        displayfont.setPointSize(25)

        self.rotor2display = QtWidgets.QLabel(self.groupBox_2)
        self.rotor2display.setFont(displayfont)
        self.rotor2display.setGeometry(QtCore.QRect(100, 50, 51, 51))
        self.rotor2display.setAutoFillBackground(True)
        self.rotor2display.setFrameShape(QtWidgets.QFrame.Box)
        self.rotor2display.setAlignment(QtCore.Qt.AlignCenter)
        self.rotor2display.setObjectName("rotor2display")
        self.rotor2display.setStyleSheet('background-color: white;')

        self.rotor3DropDown = QtWidgets.QComboBox(self.groupBox_2)
        self.rotor3DropDown.setGeometry(QtCore.QRect(10, 110, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rotor3DropDown.setFont(font)
        self.rotor3DropDown.setObjectName("rotor3DropDown")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")
        self.rotor3DropDown.addItem("")

        self.rotor1display = QtWidgets.QLabel(self.groupBox_2)
        self.rotor1display.setFont(displayfont)
        self.rotor1display.setGeometry(QtCore.QRect(190, 50, 51, 51))
        self.rotor1display.setAutoFillBackground(True)
        self.rotor1display.setFrameShape(QtWidgets.QFrame.Box)
        self.rotor1display.setAlignment(QtCore.Qt.AlignCenter)
        self.rotor1display.setObjectName("rotor1display")
        self.rotor1display.setStyleSheet('background-color: white;')

        self.rotor2DropDown = QtWidgets.QComboBox(self.groupBox_2)
        self.rotor2DropDown.setGeometry(QtCore.QRect(100, 110, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rotor2DropDown.setFont(font)
        self.rotor2DropDown.setObjectName("rotor2DropDown")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")
        self.rotor2DropDown.addItem("")

        self.rotor3display = QtWidgets.QLabel(self.groupBox_2)
        self.rotor3display.setFont(displayfont)
        self.rotor3display.setGeometry(QtCore.QRect(10, 50, 51, 51))
        self.rotor3display.setAutoFillBackground(True)
        self.rotor3display.setFrameShape(QtWidgets.QFrame.Box)
        self.rotor3display.setAlignment(QtCore.Qt.AlignCenter)
        self.rotor3display.setObjectName("rotor3display")
        self.rotor3display.setStyleSheet('background-color: white;')

        self.rotor1IsIgnore = QtWidgets.QLabel(self.groupBox_2)
        self.rotor1IsIgnore.setGeometry(QtCore.QRect(190, 30, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.rotor1IsIgnore.setFont(font)
        self.rotor1IsIgnore.setFrameShape(QtWidgets.QFrame.Box)
        self.rotor1IsIgnore.setAlignment(QtCore.Qt.AlignCenter)
        self.rotor1IsIgnore.setObjectName("rotor1IsIgnore")
        self.rotor2IsIgnore = QtWidgets.QLabel(self.groupBox_2)
        self.rotor2IsIgnore.setGeometry(QtCore.QRect(100, 30, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.rotor2IsIgnore.setFont(font)
        self.rotor2IsIgnore.setFrameShape(QtWidgets.QFrame.Box)
        self.rotor2IsIgnore.setAlignment(QtCore.Qt.AlignCenter)
        self.rotor2IsIgnore.setObjectName("rotor2IsIgnore")
        self.rotor3IsIgnore = QtWidgets.QLabel(self.groupBox_2)
        self.rotor3IsIgnore.setGeometry(QtCore.QRect(10, 30, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.rotor3IsIgnore.setFont(font)
        self.rotor3IsIgnore.setFrameShape(QtWidgets.QFrame.Box)
        self.rotor3IsIgnore.setAlignment(QtCore.Qt.AlignCenter)
        self.rotor3IsIgnore.setObjectName("rotor3IsIgnore")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 290, 601, 131))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")

        self.ResetBt = QtWidgets.QPushButton(self.groupBox_3)
        self.ResetBt.setGeometry(QtCore.QRect(10, 70, 61, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ResetBt.setFont(font)
        self.ResetBt.setObjectName("ResetBt")
# Text Input fields can only accept letters, setup validator for the text input field
        regex = QtCore.QRegExp("[a-z-A-Z_]+")
        validator = QtGui.QRegExpValidator(regex)

        self.messageInput = QtWidgets.QLineEdit(self.groupBox_3)
        self.messageInput.setGeometry(QtCore.QRect(80, 30, 501, 20))
        self.messageInput.setClearButtonEnabled(True)
        self.messageInput.setObjectName("messageInput")
        self.messageInput.setValidator(validator)

        self.InputlabelIgnore = QtWidgets.QLabel(self.groupBox_3)
        self.InputlabelIgnore.setGeometry(QtCore.QRect(10, 30, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.InputlabelIgnore.setFont(font)
        self.InputlabelIgnore.setFrameShape(QtWidgets.QFrame.Box)
        self.InputlabelIgnore.setAlignment(QtCore.Qt.AlignCenter)
        self.InputlabelIgnore.setObjectName("InputlabelIgnore")
        self.messageOutputTb = QtWidgets.QTextBrowser(self.groupBox_3)
        self.messageOutputTb.setGeometry(QtCore.QRect(80, 70, 501, 51))
        self.messageOutputTb.setObjectName("messageOutputTb")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 160, 601, 121))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")

        self.PBFirstLetter1 = QtWidgets.QLineEdit(self.groupBox_4)
        self.PBFirstLetter1.setGeometry(QtCore.QRect(10, 29, 31, 31))
        self.PBFirstLetter1.setMaxLength(1)
        self.PBFirstLetter1.setObjectName("PBFirstLetter1")
        self.PBFirstLetter1.setValidator(validator)


        self.PBSecondLetter1 = QtWidgets.QLineEdit(self.groupBox_4)
        self.PBSecondLetter1.setGeometry(QtCore.QRect(10, 79, 31, 31))
        self.PBSecondLetter1.setMaxLength(1)
        self.PBSecondLetter1.setClearButtonEnabled(False)
        self.PBSecondLetter1.setObjectName("PBSecondLetter1")
        self.PBSecondLetter1.setValidator(validator)

        self.line = QtWidgets.QFrame(self.groupBox_4)
        self.line.setGeometry(QtCore.QRect(10, 60, 31, 20))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.PBFirstLetter2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.PBFirstLetter2.setGeometry(QtCore.QRect(70, 29, 31, 31))
        self.PBFirstLetter2.setMaxLength(1)
        self.PBFirstLetter2.setObjectName("PBFirstLetter2")
        self.PBFirstLetter2.setValidator(validator)

        self.PBSecondLetter2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.PBSecondLetter2.setGeometry(QtCore.QRect(70, 79, 31, 31))
        self.PBSecondLetter2.setMaxLength(1)
        self.PBSecondLetter2.setObjectName("PBSecondLetter2")
        self.PBSecondLetter2.setValidator(validator)

        self.line_2 = QtWidgets.QFrame(self.groupBox_4)
        self.line_2.setGeometry(QtCore.QRect(70, 60, 31, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.PBFirstLetter3 = QtWidgets.QLineEdit(self.groupBox_4)
        self.PBFirstLetter3.setGeometry(QtCore.QRect(130, 29, 31, 31))
        self.PBFirstLetter3.setMaxLength(1)
        self.PBFirstLetter3.setObjectName("PBFirstLetter3")
        self.PBFirstLetter3.setValidator(validator)

        self.PBSecondLetter3 = QtWidgets.QLineEdit(self.groupBox_4)
        self.PBSecondLetter3.setGeometry(QtCore.QRect(130, 79, 31, 31))
        self.PBSecondLetter3.setMaxLength(1)
        self.PBSecondLetter3.setObjectName("PBSecondLetter3")
        self.PBSecondLetter3.setValidator(validator)

        self.line_3 = QtWidgets.QFrame(self.groupBox_4)
        self.line_3.setGeometry(QtCore.QRect(130, 60, 31, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.PBFirstLetter4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.PBFirstLetter4.setGeometry(QtCore.QRect(190, 30, 31, 31))
        self.PBFirstLetter4.setMaxLength(1)
        self.PBFirstLetter4.setObjectName("PBFirstLetter4")
        self.PBFirstLetter4.setValidator(validator)

        self.PBSecondLetter4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.PBSecondLetter4.setGeometry(QtCore.QRect(190, 80, 31, 31))
        self.PBSecondLetter4.setMaxLength(1)
        self.PBSecondLetter4.setObjectName("PBSecondLetter4")
        self.PBSecondLetter4.setValidator(validator)

        self.line_4 = QtWidgets.QFrame(self.groupBox_4)
        self.line_4.setGeometry(QtCore.QRect(190, 61, 31, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.PBFirstLetter5 = QtWidgets.QLineEdit(self.groupBox_4)
        self.PBFirstLetter5.setGeometry(QtCore.QRect(250, 29, 31, 31))
        self.PBFirstLetter5.setMaxLength(1)
        self.PBFirstLetter5.setObjectName("PBFirstLetter5")
        self.PBFirstLetter5.setValidator(validator)

        self.PBSecondLetter5 = QtWidgets.QLineEdit(self.groupBox_4)
        self.PBSecondLetter5.setGeometry(QtCore.QRect(250, 79, 31, 31))
        self.PBSecondLetter5.setMaxLength(1)
        self.PBSecondLetter5.setObjectName("PBSecondLetter5")
        self.PBSecondLetter5.setValidator(validator)

        self.line_5 = QtWidgets.QFrame(self.groupBox_4)
        self.line_5.setGeometry(QtCore.QRect(250, 60, 31, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        self.PBFirstLetter6 = QtWidgets.QLineEdit(self.groupBox_4)
        self.PBFirstLetter6.setGeometry(QtCore.QRect(310, 29, 31, 31))
        self.PBFirstLetter6.setMaxLength(1)
        self.PBFirstLetter6.setObjectName("PBFirstLetter6")
        self.PBFirstLetter6.setValidator(validator)

        self.PBSecondLetter6 = QtWidgets.QLineEdit(self.groupBox_4)
        self.PBSecondLetter6.setGeometry(QtCore.QRect(310, 79, 31, 31))
        self.PBSecondLetter6.setMaxLength(1)
        self.PBSecondLetter6.setObjectName("PBSecondLetter6")
        self.PBSecondLetter6.setValidator(validator)

        self.line_6 = QtWidgets.QFrame(self.groupBox_4)
        self.line_6.setGeometry(QtCore.QRect(310, 60, 31, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.groupBox_4)
        self.line_7.setGeometry(QtCore.QRect(490, 61, 31, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.groupBox_4)
        self.line_8.setGeometry(QtCore.QRect(550, 61, 31, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")

        self.PBFirstLetter7 = QtWidgets.QLineEdit(self.groupBox_4)
        self.PBFirstLetter7.setGeometry(QtCore.QRect(370, 30, 31, 31))
        self.PBFirstLetter7.setMaxLength(1)
        self.PBFirstLetter7.setObjectName("PBFirstLetter7")
        self.PBFirstLetter7.setValidator(validator)

        self.PBSecondLetter7 = QtWidgets.QLineEdit(self.groupBox_4)
        self.PBSecondLetter7.setGeometry(QtCore.QRect(370, 80, 31, 31))
        self.PBSecondLetter7.setMaxLength(1)
        self.PBSecondLetter7.setObjectName("PBSecondLetter7")
        self.PBSecondLetter7.setValidator(validator)

        self.PBFirstLetter8 = QtWidgets.QLineEdit(self.groupBox_4)
        self.PBFirstLetter8.setGeometry(QtCore.QRect(430, 31, 31, 31))
        self.PBFirstLetter8.setMaxLength(1)
        self.PBFirstLetter8.setObjectName("PBFirstLetter8")
        self.PBFirstLetter8.setValidator(validator)

        self.PBSecondLetter8 = QtWidgets.QLineEdit(self.groupBox_4)
        self.PBSecondLetter8.setGeometry(QtCore.QRect(430, 81, 31, 31))
        self.PBSecondLetter8.setMaxLength(1)
        self.PBSecondLetter8.setObjectName("PBSecondLetter8")
        self.PBSecondLetter8.setValidator(validator)

        self.PBFirstLetter9 = QtWidgets.QLineEdit(self.groupBox_4)
        self.PBFirstLetter9.setGeometry(QtCore.QRect(490, 30, 31, 31))
        self.PBFirstLetter9.setMaxLength(1)
        self.PBFirstLetter9.setObjectName("PBFirstLetter9")
        self.PBFirstLetter9.setValidator(validator)

        self.PBSecondLetter9 = QtWidgets.QLineEdit(self.groupBox_4)
        self.PBSecondLetter9.setGeometry(QtCore.QRect(490, 80, 31, 31))
        self.PBSecondLetter9.setMaxLength(1)
        self.PBSecondLetter9.setObjectName("PBSecondLetter9")
        self.PBSecondLetter9.setValidator(validator)

        self.PBFirstLetter10 = QtWidgets.QLineEdit(self.groupBox_4)
        self.PBFirstLetter10.setGeometry(QtCore.QRect(550, 30, 31, 31))
        self.PBFirstLetter10.setMaxLength(1)
        self.PBFirstLetter10.setObjectName("PBFirstLetter10")
        self.PBFirstLetter10.setValidator(validator)

        self.PBSecondLetter10 = QtWidgets.QLineEdit(self.groupBox_4)
        self.PBSecondLetter10.setGeometry(QtCore.QRect(550, 80, 31, 31))
        self.PBSecondLetter10.setMaxLength(1)
        self.PBSecondLetter10.setObjectName("PBSecondLetter10")
        self.PBSecondLetter10.setValidator(validator)



        self.line_9 = QtWidgets.QFrame(self.groupBox_4)
        self.line_9.setGeometry(QtCore.QRect(430, 62, 31, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")

        self.line_10 = QtWidgets.QFrame(self.groupBox_4)
        self.line_10.setGeometry(QtCore.QRect(370, 61, 31, 20))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.select_rotors() #Select rotor function
        self.messageInput.textEdited.connect(self.resultingMessage)
        self.ResetBt.clicked.connect(self.reset_to_initial)   #Reset to initial Setting
# Update rotor displays and output message
        self.rotor1DropDown.activated.connect(self.select_rotors)
        self.rotor2DropDown.activated.connect(self.select_rotors)
        self.rotor3DropDown.activated.connect(self.select_rotors)
        self.rotor1DropDown.activated.connect(self.resultingMessage)
        self.rotor2DropDown.activated.connect(self.resultingMessage)
        self.rotor3DropDown.activated.connect(self.resultingMessage)
        self.rotor1selection.activated.connect(self.resultingMessage)
        self.rotor2selection.activated.connect(self.resultingMessage)
        self.rotor3selection.activated.connect(self.resultingMessage)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Select Rotor"))
        self.staticwheelLBIgnore.setText(_translate("MainWindow", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.rotor2SrIgnore.setText(_translate("MainWindow", "Rotor 2"))
        self.rotor1selection.setItemText(0, _translate("MainWindow", "EKMFLGDQVZNTOWYHXUSPAIBRCJ"))
        self.rotor1selection.setItemText(1, _translate("MainWindow", "AJDKSIRUXBLHWTMCQGZNPYFVOE"))
        self.rotor1selection.setItemText(2, _translate("MainWindow", "BDFHJLCPRTXVZNYEIWGAKMUSQO"))
        self.rotor1selection.setItemText(3, _translate("MainWindow", "ESOVPZJAYQUIRHXLNFTGKDCMWB"))
        self.rotor1selection.setItemText(4, _translate("MainWindow", "VZBRGITYUPSDNHLXAWMJQOFECK"))
        self.rotor1selection.setItemText(5, _translate("MainWindow", "JPGVOUMFYQBENHZRDKASXLICTW"))
        self.rotor1selection.setItemText(6, _translate("MainWindow", "NZJHGRCXMYSWBOUFAIVLPEKQDT"))
        self.rotor1selection.setItemText(7, _translate("MainWindow", "FKQHTLXOCBJSPDZRAMEWNIUYGV"))

        self.rotor3SrIgnore.setText(_translate("MainWindow", "Rotor 3"))
        self.rotor2selection.setItemText(0, _translate("MainWindow", "EKMFLGDQVZNTOWYHXUSPAIBRCJ"))
        self.rotor2selection.setItemText(1, _translate("MainWindow", "AJDKSIRUXBLHWTMCQGZNPYFVOE"))
        self.rotor2selection.setItemText(2, _translate("MainWindow", "BDFHJLCPRTXVZNYEIWGAKMUSQO"))
        self.rotor2selection.setItemText(3, _translate("MainWindow", "ESOVPZJAYQUIRHXLNFTGKDCMWB"))
        self.rotor2selection.setItemText(4, _translate("MainWindow", "VZBRGITYUPSDNHLXAWMJQOFECK"))
        self.rotor2selection.setItemText(5, _translate("MainWindow", "JPGVOUMFYQBENHZRDKASXLICTW"))
        self.rotor2selection.setItemText(6, _translate("MainWindow", "NZJHGRCXMYSWBOUFAIVLPEKQDT"))
        self.rotor2selection.setItemText(7, _translate("MainWindow", "FKQHTLXOCBJSPDZRAMEWNIUYGV"))

        self.rotor1SrIgnore.setText(_translate("MainWindow", "Rotor 1"))
        self.rotor3selection.setItemText(0, _translate("MainWindow", "EKMFLGDQVZNTOWYHXUSPAIBRCJ"))
        self.rotor3selection.setItemText(1, _translate("MainWindow", "AJDKSIRUXBLHWTMCQGZNPYFVOE"))
        self.rotor3selection.setItemText(2, _translate("MainWindow", "BDFHJLCPRTXVZNYEIWGAKMUSQO"))
        self.rotor3selection.setItemText(3, _translate("MainWindow", "ESOVPZJAYQUIRHXLNFTGKDCMWB"))
        self.rotor3selection.setItemText(4, _translate("MainWindow", "VZBRGITYUPSDNHLXAWMJQOFECK"))
        self.rotor3selection.setItemText(5, _translate("MainWindow", "JPGVOUMFYQBENHZRDKASXLICTW"))
        self.rotor3selection.setItemText(6, _translate("MainWindow", "NZJHGRCXMYSWBOUFAIVLPEKQDT"))
        self.rotor3selection.setItemText(7, _translate("MainWindow", "FKQHTLXOCBJSPDZRAMEWNIUYGV"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Initial Setting"))
        self.rotor1DropDown.setItemText(0, _translate("MainWindow", "A"))
        self.rotor1DropDown.setItemText(1, _translate("MainWindow", "B"))
        self.rotor1DropDown.setItemText(2, _translate("MainWindow", "C"))
        self.rotor1DropDown.setItemText(3, _translate("MainWindow", "D"))
        self.rotor1DropDown.setItemText(4, _translate("MainWindow", "E"))
        self.rotor1DropDown.setItemText(5, _translate("MainWindow", "F"))
        self.rotor1DropDown.setItemText(6, _translate("MainWindow", "G"))
        self.rotor1DropDown.setItemText(7, _translate("MainWindow", "H"))
        self.rotor1DropDown.setItemText(8, _translate("MainWindow", "I"))
        self.rotor1DropDown.setItemText(9, _translate("MainWindow", "J"))
        self.rotor1DropDown.setItemText(10, _translate("MainWindow", "K"))
        self.rotor1DropDown.setItemText(11, _translate("MainWindow", "L"))
        self.rotor1DropDown.setItemText(12, _translate("MainWindow", "M"))
        self.rotor1DropDown.setItemText(13, _translate("MainWindow", "N"))
        self.rotor1DropDown.setItemText(14, _translate("MainWindow", "O"))
        self.rotor1DropDown.setItemText(15, _translate("MainWindow", "P"))
        self.rotor1DropDown.setItemText(16, _translate("MainWindow", "Q"))
        self.rotor1DropDown.setItemText(17, _translate("MainWindow", "R"))
        self.rotor1DropDown.setItemText(18, _translate("MainWindow", "S"))
        self.rotor1DropDown.setItemText(19, _translate("MainWindow", "T"))
        self.rotor1DropDown.setItemText(20, _translate("MainWindow", "U"))
        self.rotor1DropDown.setItemText(21, _translate("MainWindow", "V"))
        self.rotor1DropDown.setItemText(22, _translate("MainWindow", "W"))
        self.rotor1DropDown.setItemText(23, _translate("MainWindow", "X"))
        self.rotor1DropDown.setItemText(24, _translate("MainWindow", "Y"))
        self.rotor1DropDown.setItemText(25, _translate("MainWindow", "Z"))
        self.rotor2display.setText(_translate("MainWindow", ""))
        self.rotor3DropDown.setItemText(0, _translate("MainWindow", "A"))
        self.rotor3DropDown.setItemText(1, _translate("MainWindow", "B"))
        self.rotor3DropDown.setItemText(2, _translate("MainWindow", "C"))
        self.rotor3DropDown.setItemText(3, _translate("MainWindow", "D"))
        self.rotor3DropDown.setItemText(4, _translate("MainWindow", "E"))
        self.rotor3DropDown.setItemText(5, _translate("MainWindow", "F"))
        self.rotor3DropDown.setItemText(6, _translate("MainWindow", "G"))
        self.rotor3DropDown.setItemText(7, _translate("MainWindow", "H"))
        self.rotor3DropDown.setItemText(8, _translate("MainWindow", "I"))
        self.rotor3DropDown.setItemText(9, _translate("MainWindow", "J"))
        self.rotor3DropDown.setItemText(10, _translate("MainWindow", "K"))
        self.rotor3DropDown.setItemText(11, _translate("MainWindow", "L"))
        self.rotor3DropDown.setItemText(12, _translate("MainWindow", "M"))
        self.rotor3DropDown.setItemText(13, _translate("MainWindow", "N"))
        self.rotor3DropDown.setItemText(14, _translate("MainWindow", "O"))
        self.rotor3DropDown.setItemText(15, _translate("MainWindow", "P"))
        self.rotor3DropDown.setItemText(16, _translate("MainWindow", "Q"))
        self.rotor3DropDown.setItemText(17, _translate("MainWindow", "R"))
        self.rotor3DropDown.setItemText(18, _translate("MainWindow", "S"))
        self.rotor3DropDown.setItemText(19, _translate("MainWindow", "T"))
        self.rotor3DropDown.setItemText(20, _translate("MainWindow", "U"))
        self.rotor3DropDown.setItemText(21, _translate("MainWindow", "V"))
        self.rotor3DropDown.setItemText(22, _translate("MainWindow", "W"))
        self.rotor3DropDown.setItemText(23, _translate("MainWindow", "X"))
        self.rotor3DropDown.setItemText(24, _translate("MainWindow", "Y"))
        self.rotor3DropDown.setItemText(25, _translate("MainWindow", "Z"))
        self.rotor1display.setText(_translate("MainWindow", ""))
        self.rotor2DropDown.setItemText(0, _translate("MainWindow", "A"))
        self.rotor2DropDown.setItemText(1, _translate("MainWindow", "B"))
        self.rotor2DropDown.setItemText(2, _translate("MainWindow", "C"))
        self.rotor2DropDown.setItemText(3, _translate("MainWindow", "D"))
        self.rotor2DropDown.setItemText(4, _translate("MainWindow", "E"))
        self.rotor2DropDown.setItemText(5, _translate("MainWindow", "F"))
        self.rotor2DropDown.setItemText(6, _translate("MainWindow", "G"))
        self.rotor2DropDown.setItemText(7, _translate("MainWindow", "H"))
        self.rotor2DropDown.setItemText(8, _translate("MainWindow", "I"))
        self.rotor2DropDown.setItemText(9, _translate("MainWindow", "J"))
        self.rotor2DropDown.setItemText(10, _translate("MainWindow", "K"))
        self.rotor2DropDown.setItemText(11, _translate("MainWindow", "L"))
        self.rotor2DropDown.setItemText(12, _translate("MainWindow", "M"))
        self.rotor2DropDown.setItemText(13, _translate("MainWindow", "N"))
        self.rotor2DropDown.setItemText(14, _translate("MainWindow", "O"))
        self.rotor2DropDown.setItemText(15, _translate("MainWindow", "P"))
        self.rotor2DropDown.setItemText(16, _translate("MainWindow", "Q"))
        self.rotor2DropDown.setItemText(17, _translate("MainWindow", "R"))
        self.rotor2DropDown.setItemText(18, _translate("MainWindow", "S"))
        self.rotor2DropDown.setItemText(19, _translate("MainWindow", "T"))
        self.rotor2DropDown.setItemText(20, _translate("MainWindow", "U"))
        self.rotor2DropDown.setItemText(21, _translate("MainWindow", "V"))
        self.rotor2DropDown.setItemText(22, _translate("MainWindow", "W"))
        self.rotor2DropDown.setItemText(23, _translate("MainWindow", "X"))
        self.rotor2DropDown.setItemText(24, _translate("MainWindow", "Y"))
        self.rotor2DropDown.setItemText(25, _translate("MainWindow", "Z"))
        self.rotor3display.setText(_translate("MainWindow", ""))
        self.rotor1IsIgnore.setText(_translate("MainWindow", "Rotor 1"))
        self.rotor2IsIgnore.setText(_translate("MainWindow", "Rotor 2"))
        self.rotor3IsIgnore.setText(_translate("MainWindow", "Rotor 3"))
        self.ResetBt.setText(_translate("MainWindow", "Reset"))
        self.InputlabelIgnore.setText(_translate("MainWindow", "Input"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Plug Board"))


    def select_rotors(self):
        self.rotor1_select = [(self.rotor1selection.currentText()), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
        self.rotor2_select = [(self.rotor2selection.currentText()), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
        self.rotor3_select = [(self.rotor3selection.currentText()), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
        self.reflector = ['EJMZALYXVBWFCRQUONTSPIKHGD', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']

        self.rotor1_select = self.selectInitialSetting(self.rotor1_select, self.rotor1DropDown.currentText())
        self.rotor2_select = self.selectInitialSetting(self.rotor2_select, self.rotor2DropDown.currentText())
        self.rotor3_select = self.selectInitialSetting(self.rotor3_select, self.rotor3DropDown.currentText())

        self.rotor1display.setText(self.rotor1_select[1][0])
        self.rotor2display.setText(self.rotor2_select[1][0])
        self.rotor3display.setText(self.rotor3_select[1][0])
# Apply initial setting to the rotors
    def selectInitialSetting(self,rotor,letter):
        index = rotor[1].find(letter)
        rotor[0] = rotor[0][index:] + rotor[0][:index]
        rotor[1] = rotor[1][index:] + rotor[1][:index]
        return rotor
# Rotate rotor by 1 letter
    def rotateRotor(self, rotor):
        rotor[0] = rotor[0][1:] + rotor[0][0]
        rotor[1] = rotor[1][1:] + rotor[1][0]
        return rotor

    def index_input(self,index_in, rotor):
        return rotor[1].find(rotor[0][index_in])

    def index_output(self,index, rotor):
        letter = rotor[1][index]
        return rotor[0].find(letter)

# This section convert input letter through 3 rotors
    def rotors_section_message(self,rotor1, rotor2, rotor3, reflector, input):
        i, j = 0, 0
        static_wheel = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        message = input.upper()
        result = []
        for letter in message:
            index = static_wheel.find(letter)
            index = self.index_input(index, rotor1)
            index = self.index_input(index, rotor2)
            index = self.index_input(index, rotor3)
            index = self.index_input(index, reflector)
            index = self.index_output(index, rotor3)
            index = self.index_output(index, rotor2)
            index = self.index_output(index, rotor1)
            rotor1 = self.rotateRotor(rotor1)
            i += 1
            if i == 26:
                i = 0
                rotor2 = self.rotateRotor(rotor2)
                j += 1
            if j == 26:
                j = 0
                rotor3 = self.rotateRotor(rotor3)
            result.append(static_wheel[index])
        return ''.join(result)
# Take in inputs and switch places of the 2 letters, remove repeated letters pairs
    def plugBoard(self):
        self.topRow = [self.PBFirstLetter1.text().upper(), self.PBFirstLetter2.text().upper(),
                       self.PBFirstLetter3.text().upper(), self.PBFirstLetter4.text().upper(),
                       self.PBFirstLetter5.text().upper(), self.PBFirstLetter6.text().upper(),
                       self.PBFirstLetter7.text().upper(), self.PBFirstLetter8.text().upper(),
                       self.PBFirstLetter9.text().upper(), self.PBFirstLetter10.text().upper()]

        self.bottomRow = [self.PBSecondLetter1.text().upper(), self.PBSecondLetter2.text().upper(),
                          self.PBSecondLetter3.text().upper(), self.PBSecondLetter4.text().upper(),
                          self.PBSecondLetter5.text().upper(), self.PBSecondLetter6.text().upper(),
                          self.PBSecondLetter7.text().upper(), self.PBSecondLetter8.text().upper(),
                          self.PBSecondLetter9.text().upper(), self.PBSecondLetter10.text().upper()]

        for i in range(len(self.topRow)):
            if not self.topRow[i] or not self.bottomRow[i]:
                self.topRow[i] = ''
                self.bottomRow[i] = ''
        for i,ele in enumerate(self.topRow):
            if (self.topRow.count(ele) + self.bottomRow.count(ele)) > 1:
                self.topRow[i] =''
                self.bottomRow[i] =''
        for i,ele in enumerate(self.bottomRow):
            if self.topRow.count(ele) + self.bottomRow.count(ele) > 1:
                self.topRow[i] =''
                self.bottomRow[i] =''
        self.plugboardResetLetter()

    def plugboardResetLetter(self):
        self.PBFirstLetter1.setText(self.topRow[0])
        self.PBFirstLetter2.setText(self.topRow[1])
        self.PBFirstLetter3.setText(self.topRow[2])
        self.PBFirstLetter4.setText(self.topRow[3])
        self.PBFirstLetter5.setText(self.topRow[4])
        self.PBFirstLetter6.setText(self.topRow[5])
        self.PBFirstLetter7.setText(self.topRow[6])
        self.PBFirstLetter8.setText(self.topRow[7])
        self.PBFirstLetter9.setText(self.topRow[8])
        self.PBFirstLetter10.setText(self.topRow[9])
        self.PBSecondLetter1.setText(self.bottomRow[0])
        self.PBSecondLetter2.setText(self.bottomRow[1])
        self.PBSecondLetter3.setText(self.bottomRow[2])
        self.PBSecondLetter4.setText(self.bottomRow[3])
        self.PBSecondLetter5.setText(self.bottomRow[4])
        self.PBSecondLetter6.setText(self.bottomRow[5])
        self.PBSecondLetter7.setText(self.bottomRow[6])
        self.PBSecondLetter8.setText(self.bottomRow[7])
        self.PBSecondLetter9.setText(self.bottomRow[8])
        self.PBSecondLetter10.setText(self.bottomRow[9])


    def plugBoardConverter(self,input):
        for i,letter in enumerate(input):
            if input[i] in self.topRow:
                input[i] = self.bottomRow[self.topRow.index(input[i])]
            elif input[i] in self.bottomRow:
                input[i] = self.topRow[self.bottomRow.index(input[i])]
        return ''.join(input)

    def resultingMessage(self):
        self.plugBoard()
        self.select_rotors()
        self.input = self.plugBoardConverter(list(self.messageInput.text().upper()))
        output = self.rotors_section_message(self.rotor1_select,self.rotor2_select
                                    ,self.rotor3_select,self.reflector,self.input)
        output = self.plugBoardConverter(list(output))
        self.messageOutputTb.setText(output)
        self.rotor1display.setText(self.rotor1_select[1][0])
        self.rotor2display.setText(self.rotor2_select[1][0])
        self.rotor3display.setText(self.rotor3_select[1][0])

    def reset_to_initial(self):
        self.select_rotors()
        self.messageOutputTb.setText('')
        self.messageInput.setText('')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

