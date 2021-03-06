# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'status.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

#from main import Ui_MainWindow
class Ui_Status(object):
    def __init__(self,tPF1,tPF2,tPF3,tPF4,tPF5,tPF6,folder1):
        self.folder1 = folder1
        self.tPF1 = tPF1
        self.tPF2 = tPF2
        self.tPF3 = tPF3
        self.tPF4 = tPF4
        self.tPF5 = tPF5
        self.tPF6 = tPF6
        #print(tPF1)
    def setupUi(self, Status):
        Status.setObjectName("Status")
        Status.setFixedSize(980, 471)
        Status.setStyleSheet(open("css/status.css").read())
        self.centralwidget = QtWidgets.QWidget(Status)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 961, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(390, 10, 191, 31))
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 70, 961, 331))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(490, 10, 461, 71))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(6, 3, 341, 20))
        self.label_2.setObjectName("label_2")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(10, 40, 441, 16))
        self.label_11.setObjectName("label_11")
        
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(430, 10, 21, 23))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        if(self.folder1 == '' or self.folder1 == 'Pasta principal n??o selecionada.'):
            self.pushButton.setStyleSheet("background: red")
        else:
            self.pushButton.setStyleSheet("background: green")
        
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(10, 90, 461, 71))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(10, 5, 441, 21))
        self.label_3.setObjectName("label_3")
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        self.label_12.setGeometry(QtCore.QRect(10, 40, 441, 16))
        self.label_12.setObjectName("label_12")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 10, 21, 23))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        if(self.tPF1 == '' or self.tPF1 == 'PF1 N??o selecionado.'):
            self.pushButton_2.setStyleSheet("background: red")
        else:
            self.pushButton_2.setStyleSheet("background: green")
        
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setGeometry(QtCore.QRect(490, 90, 461, 71))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        self.label_6.setGeometry(QtCore.QRect(10, 5, 441, 21))
        self.label_6.setObjectName("label_6")
        self.label_15 = QtWidgets.QLabel(self.frame_5)
        self.label_15.setGeometry(QtCore.QRect(10, 40, 441, 16))
        self.label_15.setObjectName("label_15")
        
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_5.setGeometry(QtCore.QRect(430, 10, 21, 23))
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        if(self.tPF2 == '' or self.tPF2 == 'PF2 N??o selecionado.'):
            self.pushButton_5.setStyleSheet("background: red")
        else:
            self.pushButton_5.setStyleSheet("background: green")
        
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(490, 170, 461, 71))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_7 = QtWidgets.QLabel(self.frame_6)
        self.label_7.setGeometry(QtCore.QRect(10, 5, 441, 21))
        self.label_7.setObjectName("label_7")
        self.label_16 = QtWidgets.QLabel(self.frame_6)
        self.label_16.setGeometry(QtCore.QRect(10, 40, 441, 16))
        self.label_16.setObjectName("label_16")
        
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_6.setGeometry(QtCore.QRect(430, 10, 21, 23))
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        if(self.tPF4 == '' or self.tPF4 == 'PF4 N??o selecionado.'):
            self.pushButton_6.setStyleSheet("background: red")
        else:
            self.pushButton_6.setStyleSheet("background: green")
        
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setGeometry(QtCore.QRect(10, 170, 461, 71))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_8 = QtWidgets.QLabel(self.frame_7)
        self.label_8.setGeometry(QtCore.QRect(10, 5, 441, 21))
        self.label_8.setObjectName("label_8")
        self.label_13 = QtWidgets.QLabel(self.frame_7)
        self.label_13.setGeometry(QtCore.QRect(10, 40, 441, 16))
        self.label_13.setObjectName("label_13")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 10, 21, 23))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        if(self.tPF3 == '' or self.tPF3 == 'PF3 N??o selecionado.'):
            self.pushButton_3.setStyleSheet("background: red")
        else:
            self.pushButton_3.setStyleSheet("background: green")
        
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setGeometry(QtCore.QRect(10, 250, 461, 71))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_9 = QtWidgets.QLabel(self.frame_8)
        self.label_9.setGeometry(QtCore.QRect(10, 5, 441, 21))
        self.label_9.setObjectName("label_9")
        self.label_14 = QtWidgets.QLabel(self.frame_8)
        self.label_14.setGeometry(QtCore.QRect(10, 40, 441, 16))
        self.label_14.setObjectName("label_14")
        
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 10, 21, 23))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        if(self.tPF5 == '' or self.tPF5 == 'PF5 N??o selecionado.'):
            self.pushButton_4.setStyleSheet("background: red")
        else:
            self.pushButton_4.setStyleSheet("background: green")
        
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setGeometry(QtCore.QRect(490, 250, 461, 71))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_10 = QtWidgets.QLabel(self.frame_9)
        self.label_10.setGeometry(QtCore.QRect(10, 5, 441, 21))
        self.label_10.setObjectName("label_10")
        self.label_17 = QtWidgets.QLabel(self.frame_9)
        self.label_17.setGeometry(QtCore.QRect(10, 40, 441, 16))
        self.label_17.setObjectName("label_17")
        
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_7.setGeometry(QtCore.QRect(430, 10, 21, 23))
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        if(self.tPF6 == '' or self.tPF6 == 'PF6 N??o selecionado.'):
            self.pushButton_7.setStyleSheet("background: red")
        else:
            self.pushButton_7.setStyleSheet("background: green")
        
        self.frame_10 = QtWidgets.QFrame(self.centralwidget)
        self.frame_10.setGeometry(QtCore.QRect(10, 410, 961, 51))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_18 = QtWidgets.QLabel(self.frame_10)
        self.label_18.setGeometry(QtCore.QRect(270, 15, 191, 21))
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        #self.pushButton_8 = QtWidgets.QPushButton(self.frame_10)
        #self.pushButton_8.setGeometry(QtCore.QRect(10, 10, 941, 31))
        #self.pushButton_8.setObjectName("pushButton_8")
        Status.setCentralWidget(self.centralwidget)

        self.retranslateUi(Status)
        QtCore.QMetaObject.connectSlotsByName(Status)

    def retranslateUi(self, Status):
        _translate = QtCore.QCoreApplication.translate
        Status.setWindowTitle(_translate("Status", "Status"))
        self.label.setText(_translate("Status", "Status de envio"))
        self.label_2.setText(_translate("Status", "Pasta principal"))
        self.label_11.setText(_translate("Status", self.folder1))
        self.label_3.setText(_translate("Status", "Televendas PF1"))
        self.label_12.setText(_translate("Status", self.tPF1))
        self.label_6.setText(_translate("Status", "Televendas PF2"))
        self.label_15.setText(_translate("Status", self.tPF2))
        self.label_7.setText(_translate("Status", "Televendas PF4"))
        self.label_16.setText(_translate("Status", self.tPF4))
        self.label_8.setText(_translate("Status", "Televendas PF3"))
        self.label_13.setText(_translate("Status", self.tPF3))
        self.label_9.setText(_translate("Status", "Televendas PF5"))
        self.label_14.setText(_translate("Status", self.tPF5))
        self.label_10.setText(_translate("Status", "Televendas PF6"))
        self.label_17.setText(_translate("Status", self.tPF6))
        #self.pushButton_8.setText(_translate("Status", "Voltar ao menu principal"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Status = QtWidgets.QMainWindow()
    ui = Ui_Status()
    ui.setupUi(Status)
    Status.show()
    sys.exit(app.exec_())
