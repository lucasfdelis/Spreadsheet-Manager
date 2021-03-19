# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import time

class Ui_Login(object):
    def openAtendente(self):
        try:
            from atendentes import Ui_atendentes 
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_atendentes()
            self.ui.setupUi(self.window)
            self.window.show()
            #Login.hide()
        except Exception as e:
            print(e) 
    def openWindow(self):
        try:
            from main import Ui_MainWindow      
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow(self.priv_bd)
            self.ui.setupUi(self.window)
            self.window.show()
            #Login.hide()
        except Exception as e:
            print(e)
    def checkpassword(self):
        try:
            banco = sqlite3.connect('bdCadastro.db')
            cursor = banco.cursor()
            cursor.execute("SELECT senha FROM cadastro WHERE login ='{}'".format(self.lineEdit.text()))
            senha_bd = cursor.fetchall()
            cursor.execute("SELECT priv FROM cadastro WHERE login ='{}'".format(self.lineEdit.text()))
            priv_bd = cursor.fetchall()
            self.priv_bd = priv_bd[0][0]
            banco.close()                
            if (self.lineEdit_2.text() == senha_bd[0][0]):
                if(self.priv_bd == 'atendente'):
                    self.openAtendente()
                else:
                    self.openWindow()
            else:
                self.msg = QMessageBox()
                self.msg.setWindowTitle('Erro')
                self.msg.setIcon(QMessageBox.Information)
                self.msg.setText("Dados incorretos. Verifique se a senha foi digitada corretamente ou se o login fornecido existe.")
                self.msg.exec_() 
        except Exception as e:
           self.msg = QMessageBox()
           self.msg.setWindowTitle('Erro')
           self.msg.setIcon(QMessageBox.Critical)
           self.msg.setText("Dados incorretos, verifique se a senha foi digitada corretamente ou se o login fornecido existe.")
           self.msg.setInformativeText("Detalhes do erro abaixo:")
           self.msg.setDetailedText(str(e))
           self.msg.exec_()
           

    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.setFixedSize(440, 572)
        Login.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"font-size: 24px\n"
"}\n"
"\n"
"QMainWindow{\n"
"background:url(img/background.jpeg);\n"
"}\n"
"QFrame\n"
"{\n"
"background: rgba(0,0,0,0.8);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"color: #333;\n"
"background: white;\n"
"border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color: 333;\n"
"background: gray;\n"
"border-radius: 10px\n"
"}\n"
"\n"
"\n"
"QToolButton\n"
"{\n"
"background: white;\n"
"border-radius: 10px\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"color: white;\n"
"background: transparent;\n"
"}\n"
"\n"
"#label_4\n"
"{\n"
"color: pink;\n"
"font-family: arial;\n"
"font-size: 16px\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"background: transparent;\n"
"border: none;\n"
"color: #717072;\n"
"border-bottom: 1px solid #717072;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 70, 381, 411))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(160, 60, 81, 51))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 330, 321, 51))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.checkpassword)
        
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(40, 150, 291, 41))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 250, 291, 41))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 191, 31))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 220, 211, 31))
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(220, 300, 131, 20))
        self.label_4.setObjectName("label_4")
        self.label_4.hide()
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(170, 20, 111, 111))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/multi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(100, 100))
        self.toolButton.setObjectName("toolButton")
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label.setText(_translate("Login", "LOGIN"))
        self.pushButton.setText(_translate("Login", "Entrar"))
        self.lineEdit.setPlaceholderText(_translate("Login", "Usuário"))
        self.lineEdit_2.setPlaceholderText(_translate("Login", "Senha"))
        self.label_2.setText(_translate("Login", "Usuário"))
        self.label_3.setText(_translate("Login", "Senha"))
        self.label_4.setText(_translate("Login", "Dados incorretos."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
