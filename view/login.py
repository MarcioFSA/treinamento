# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from view import Imagens
from view.reserva import Ui_MainWindow


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(484, 492)
        login.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        login.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(login)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 10, 421, 461))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 30, 181, 381))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"\n"
"border-top-left-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(200, 30, 191, 381))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(220, 70, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(23)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(0,0,0)")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(4, 280, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(8)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(0,0,0)")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(220, 190, 162, 64))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txt_usuario = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_usuario.setMinimumSize(QtCore.QSize(160, 0))
        self.txt_usuario.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_usuario.setFont(font)
        self.txt_usuario.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_usuario.setText("")
        self.txt_usuario.setObjectName("txt_usuario")
        self.verticalLayout_2.addWidget(self.txt_usuario)
        self.txt_senha = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_senha.setMinimumSize(QtCore.QSize(160, 0))
        self.txt_senha.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_senha.setFont(font)
        self.txt_senha.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px")
        self.txt_senha.setText("")
        self.txt_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_senha.setObjectName("txt_senha")
        self.verticalLayout_2.addWidget(self.txt_senha)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(0, 130, 211, 151))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(8)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("image: url(:/icones/treinamento.png);")
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(270, 260, 47, 88))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_login = QtWidgets.QPushButton(self.widget)
        self.btn_login.setMinimumSize(QtCore.QSize(45, 40))
        self.btn_login.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("QPushButton#btn_login{\n"
"        background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_login:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_login:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_login.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icones/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_login.setIcon(icon)
        self.btn_login.setIconSize(QtCore.QSize(32, 32))
        self.btn_login.setObjectName("btn_login")
        self.verticalLayout.addWidget(self.btn_login)
        self.btn_sairApp = QtWidgets.QPushButton(self.widget)
        self.btn_sairApp.setMinimumSize(QtCore.QSize(45, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_sairApp.setFont(font)
        self.btn_sairApp.setStyleSheet("QPushButton#btn_sairApp{\n"
"        background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_sairApp:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_sairApp:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_sairApp.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icones/saida.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_sairApp.setIcon(icon1)
        self.btn_sairApp.setIconSize(QtCore.QSize(32, 32))
        self.btn_sairApp.setObjectName("btn_sairApp")
        self.verticalLayout.addWidget(self.btn_sairApp)
        self.btn_login.setToolTip("ENTRAR NO SISTEMA")
        self.btn_sairApp.setToolTip("SAIR")
        # login.setCentralWidget(self.centralwidget)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)
        self.btn_login.clicked.connect(self.Login)
        self.btn_login.clicked.connect(login.close)
        self.btn_sairApp.clicked.connect(login.close)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "MainWindow"))
        self.label_3.setText(_translate("login", "L O G  I N"))
        self.label_4.setText(_translate("login", "RESERVA SALA DE TREINAMENTO"))
        self.txt_usuario.setPlaceholderText(_translate("login", "Usuário"))
        self.txt_senha.setPlaceholderText(_translate("login", "Senha"))

    def Login(self):

        nome_usuario = self.txt_usuario.text()
        senha = self.txt_senha.text()
        # cd_usuario = nome_usuario
        if not nome_usuario:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("AVISO")
            msg.setText("INFORME O NOME DO USUÁRIO")
            msg.exec()
            return False

        if not senha:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("AVISO")
            msg.setText("INFORME A SENHA DO USUÁRIO")
            msg.exec()
            return False



        else:
            if nome_usuario == "ti" and senha == "1234":
                self.janela = QtWidgets.QMainWindow()
                self.view = Ui_MainWindow()
                self.view.setupUi(self.janela)
                self.janela.show()

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("AVISO")
                msg.setText("USUÁRIO OU SENHA INVÁLIDOS")
                msg.exec()


