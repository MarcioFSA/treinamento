# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Reserva.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import datetime
import sqlite3

# from bd.conectar import conectarBD
from bd.conectar import connectarbd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QDateTime
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1070, 559)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(80, 30, 941, 581))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setGeometry(QtCore.QRect(90, 20, 761, 501))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 741, 381))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius: 50px;\n"
"border-top-left-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 120, 668, 47))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(8)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgb(0,0,0)")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setMinimumSize(QtCore.QSize(180, 0))
        self.comboBox.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(146,82,101,255);")
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(8)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgb(0,0,0)")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(240, 0))
        self.lineEdit.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(146,82,101,255);")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_4.addWidget(self.lineEdit)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(8)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgb(0,0,0)")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit.setMinimumSize(QtCore.QSize(110, 0))
        self.dateEdit.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(146,82,101,255);")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout_5.addWidget(self.dateEdit)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(8)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgb(0,0,0)")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit_2.setMinimumSize(QtCore.QSize(110, 0))
        self.dateEdit_2.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(146,82,101,255);")
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.verticalLayout_6.addWidget(self.dateEdit_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 741, 61))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"border-top-left-radius: 50px;\n"
"color:rgb(0,0,0)")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(526, 179, 182, 45))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(8)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:rgb(0,0,0)")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_7.addWidget(self.label_10)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_2.setMinimumSize(QtCore.QSize(180, 0))
        self.comboBox_2.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(146,82,101,255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_7.addWidget(self.comboBox_2)
        self.layoutWidget2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget2.setGeometry(QtCore.QRect(200, 180, 132, 45))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(8)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgb(0,0,0)")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.timeEdit = QtWidgets.QTimeEdit(self.layoutWidget2)
        self.timeEdit.setCalendarPopup(True)
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout.addWidget(self.timeEdit)
        self.layoutWidget3 = QtWidgets.QWidget(self.frame)
        self.layoutWidget3.setGeometry(QtCore.QRect(360, 180, 132, 45))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(8)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:rgb(0,0,0)")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.layoutWidget3)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.verticalLayout_2.addWidget(self.timeEdit_2)
        self.layoutWidget4 = QtWidgets.QWidget(self.frame)
        self.layoutWidget4.setGeometry(QtCore.QRect(40, 180, 112, 45))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(8)
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:rgb(0,0,0)")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_8.addWidget(self.label_13)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(110, 0))
        self.lineEdit_3.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(146,82,101,255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_8.addWidget(self.lineEdit_3)
        self.layoutWidget5 = QtWidgets.QWidget(self.frame)
        self.layoutWidget5.setGeometry(QtCore.QRect(390, 70, 327, 32))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_81 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_81.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_81.setAlignment(QtCore.Qt.AlignCenter)
        self.label_81.setObjectName("label_81")
        self.horizontalLayout.addWidget(self.label_81)
        self.txt_consultaNoti = QtWidgets.QLineEdit(self.layoutWidget5)
        self.txt_consultaNoti.setMinimumSize(QtCore.QSize(100, 0))
        self.txt_consultaNoti.setStyleSheet("\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px\n"
"")
        self.txt_consultaNoti.setText("")
        self.txt_consultaNoti.setObjectName("txt_consultaNoti")
        self.horizontalLayout.addWidget(self.txt_consultaNoti)
        self.btn_pesquisarNoti = QtWidgets.QPushButton(self.layoutWidget5)
        self.btn_pesquisarNoti.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.btn_pesquisarNoti.setFont(font)
        self.btn_pesquisarNoti.setStyleSheet("QPushButton#btn_pesquisarNoti{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_pesquisarNoti:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_pesquisarNoti:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_pesquisarNoti.setIconSize(QtCore.QSize(24, 24))
        self.btn_pesquisarNoti.setObjectName("btn_pesquisarNoti")
        self.horizontalLayout.addWidget(self.btn_pesquisarNoti)
        self.layoutWidget6 = QtWidgets.QWidget(self.frame)
        self.layoutWidget6.setGeometry(QtCore.QRect(40, 70, 208, 34))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_notifica = QtWidgets.QPushButton(self.layoutWidget6)
        self.btn_notifica.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.btn_notifica.setFont(font)
        self.btn_notifica.setStyleSheet("QPushButton#btn_notifica{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_notifica:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_notifica:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/relatorio-de-saude.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_notifica.setIcon(icon)
        self.btn_notifica.setIconSize(QtCore.QSize(24, 24))
        self.btn_notifica.setObjectName("btn_notifica")
        self.horizontalLayout_4.addWidget(self.btn_notifica)
        self.btn_editar = QtWidgets.QPushButton(self.layoutWidget6)
        self.btn_editar.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.btn_editar.setFont(font)
        self.btn_editar.setStyleSheet("QPushButton#btn_editar{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_editar:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_editar:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_editar.setIcon(icon)
        self.btn_editar.setIconSize(QtCore.QSize(24, 24))
        self.btn_editar.setObjectName("btn_editar")
        self.horizontalLayout_4.addWidget(self.btn_editar)
        self.layoutWidget7 = QtWidgets.QWidget(self.frame)
        self.layoutWidget7.setGeometry(QtCore.QRect(250, 300, 242, 34))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_agendar = QtWidgets.QPushButton(self.layoutWidget7)
        self.btn_agendar.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.btn_agendar.setFont(font)
        self.btn_agendar.setStyleSheet("QPushButton#btn_notifica{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_notifica:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_notifica:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_agendar.setIcon(icon)
        self.btn_agendar.setIconSize(QtCore.QSize(24, 24))
        self.btn_agendar.setObjectName("btn_agendar")
        self.horizontalLayout_5.addWidget(self.btn_agendar)
        self.btn_cancelar = QtWidgets.QPushButton(self.layoutWidget7)
        self.btn_cancelar.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.btn_cancelar.setFont(font)
        self.btn_cancelar.setStyleSheet("QPushButton#btn_notifica{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_notifica:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_notifica:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_cancelar.setIcon(icon)
        self.btn_cancelar.setIconSize(QtCore.QSize(24, 24))
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.horizontalLayout_5.addWidget(self.btn_cancelar)
        self.layoutWidget8 = QtWidgets.QWidget(self.frame)
        self.layoutWidget8.setGeometry(QtCore.QRect(11, 251, 713, 24))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget8)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget8)
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(8)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:rgb(0,0,0)")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget8)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(640, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(640, 16777215))
        self.lineEdit_2.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(146,82,101,255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.btn_reservas = QtWidgets.QPushButton(self.frame)
        self.btn_reservas.setGeometry(QtCore.QRect(311, 344, 131, 30))
        self.btn_reservas.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        self.btn_reservas.setFont(font)
        self.btn_reservas.setStyleSheet("QPushButton#btn_notifica{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_notifica:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_notifica:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.btn_reservas.setIcon(icon)
        self.btn_reservas.setIconSize(QtCore.QSize(24, 24))
        self.btn_reservas.setObjectName("btn_reservas")
        self.btn_sair = QtWidgets.QPushButton(self.frame)
        self.btn_sair.setGeometry(QtCore.QRect(650, 340, 51, 31))
        self.btn_sair.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.btn_sair.setFont(font)
        self.btn_sair.setStyleSheet("QPushButton#btn_sair{\n"
"    background-color:rgb(255,0,0);\n"
"    color:rgb(170, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton#btn_sair:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682,x2:1,y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#btn_sair:pressed{\n"
"    padding-left:5px;\n"
"    padding -top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.btn_sair.setIcon(icon)
        self.btn_sair.setIconSize(QtCore.QSize(24, 24))
        self.btn_sair.setObjectName("btn_sair")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 971, 491))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(self.page_2)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 941, 471))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(690, 100, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(200, 100, 49, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 100, 381, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(40, 150, 891, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(300, 20, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(23)
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color:rgb(0,0,0)")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 380, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "SETOR"))
        self.label_6.setText(_translate("MainWindow", "SOLICITANTE"))
        self.label_7.setText(_translate("MainWindow", "DATA SOLICITAÇÃO"))
        self.label_8.setText(_translate("MainWindow", "DATA AGENDA"))
        self.label_4.setText(_translate("MainWindow", "RESERVA SALA DE TREINAMENTO"))
        self.label_10.setText(_translate("MainWindow", "STATUS"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Agendado"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Aguardando chamado"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Aguardando confirmação"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Cancelado"))
        self.label_9.setText(_translate("MainWindow", "HORARIO INICIO"))
        self.label_11.setText(_translate("MainWindow", "HORARIO FIM"))
        self.label_13.setText(_translate("MainWindow", "CHAMADO GLPI"))
        self.label_81.setText(_translate("MainWindow", "Número da Reserva"))
        self.btn_pesquisarNoti.setText(_translate("MainWindow", "P E S Q U I S A R"))
        self.btn_notifica.setText(_translate("MainWindow", "NOVO"))
        self.btn_editar.setText(_translate("MainWindow", "EDITAR"))
        self.btn_agendar.setText(_translate("MainWindow", "A G E N D A R"))
        self.btn_cancelar.setText(_translate("MainWindow", "C A N C E L A R"))
        self.label_12.setText(_translate("MainWindow", "OBSERVACÃO"))
        self.btn_reservas.setText(_translate("MainWindow", "CONSULTAR RESERVAS"))
        self.btn_sair.setText(_translate("MainWindow", "S A I R"))
        self.pushButton.setText(_translate("MainWindow", "CONSULTAR"))
        self.label_2.setText(_translate("MainWindow", "Setor"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Reserva"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Setor"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Solicitante"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Data Solicitação"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Data Agenda"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Hora Inicio"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Hora Fim"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Status"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "OBS"))
        self.label_14.setText(_translate("MainWindow", "CONSULTAR RESERVAS"))
        self.pushButton_2.setText(_translate("MainWindow", "AGENDAR"))


        self.btn_reservas.clicked.connect(self.botaoreservas)
        self.pushButton_2.clicked.connect(self.botaovoltar)
        self.btn_sair.clicked.connect(MainWindow.close)
        self.btn_notifica.clicked.connect(self.InReserva)
        self.btn_agendar.clicked.connect(self.ConfReserva)
        self.btn_pesquisarNoti.clicked.connect(self.editarReserva)



    def botaoreservas(self):
            self.stackedWidget.setCurrentWidget(self.page_2)
    def botaovoltar(self):
            self.stackedWidget.setCurrentWidget(self.page)



    def InReserva(self):
            self.comboBox.setCurrentIndex(-1)
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.comboBox_2.setCurrentIndex(-1)
            self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
            self.dateEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())
            self.comboBox.setEnabled(True)
            self.lineEdit.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.comboBox_2.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.dateEdit.setEnabled(True)
            self.dateedit_2.setEnabled(True)
            self.timeEdit.setEnabled(True)
            self.timeedit_2.setEnabled(True)


    def ConfReserva(self):
            setor = self.comboBox.currentText()
            solicitante = self.lineEdit.text()
            data_solicitacao = self.dateEdit.text()
            data_agenda= self.dateEdit_2.text()
            chamado = self.lineEdit_3.text()
            hr_inicio = self.timeEdit.text()
            hr_fim = self.timeEdit_2.text()
            Estatus=self.comboBox_2.currentText()
            obs = self.lineEdit_2.text()            

            banco = sqlite3.connect('bd/Reserva_treinamento.db')
            cursor = banco.cursor()
            cursor.execute("INSERT INTO Reserva(setor,solicitante,data_solicitacao,data_agenda,chamado,hr_inicio,hr_fim,Estatus,obs) VALUES('"+setor+"','"+solicitante+"','"+data_solicitacao+"','"+data_agenda+"','"+chamado+"'\
                ,'"+hr_inicio+"','"+hr_fim+"','"+Estatus+"','"+obs+"')")

            banco.commit()
            banco.close()
            msg=QMessageBox()
            msg.setWindowTitle("AVISO")
            msg.setText("Dados Cadastrados com Sucesso")
            msg.exec()

            self.comboBox.setCurrentIndex(-1)
            self.lineEdit.setText("")
            self.lineEdit_3.setText("")
            self.comboBox_2.setCurrentIndex(-1)
            self.lineEdit_2.setText("")

            self.comboBox.setEnabled(False)
            self.lineEdit.setEnabled(False)
            self.lineEdit_3.setEnabled(False)
            self.comboBox_2.setEnabled(False)
            self.lineEdit_2.setEnabled(False)
            self.dateEdit.setEnabled(False)
            self.dateedit_2.setEnabled(False)
            self.timeEdit.setEnabled(False)
            self.timeedit_2.setEnabled(False)

    def editarReserva(self):
        solicitante = self.txt_consultaNoti.text()
        banco = sqlite3.connect('bd/Reserva_treinamento.db') 
        sql=( "SELECT * FROM reserva WHERE solicitante like '%"+str(solicitante)+"%'")
        resul = banco.execute(sql)
        if resul:
                
                for dt in resul: 
                        dt_solic_formatada = datetime.datetime.strptime(dt[3]), strftime('%d/%m/%Y')
                        self.comboBox.setCurrentText(str(dt[1]))
                        self.lineEdit.setText(str(dt[2]))
                        # self.dateEdit.date(dt_solic_formatada)
                        print(dt[3])
                        # (eval(dt[3]))

        # paciente = self.txt_nNotificao.text()
        #         conectar = sqlite3.connect('bd/notifica_bd.db')
        #         query = ("SELECT id_notificacao, nm_paciente FROM notificacao where id_notificacao LIKE '%"+str(paciente)+"%'")
        #         result = conectar.execute(query)
        #         if(result):
        #                 for dt in result:                       
        #                         self.txt_codPaciente.setText(str(dt[0]))
        #                         self.txt_nmPaciente.setText(str(dt[1]))
        



            




