# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fontset.ui',
# licensing of 'fontset.ui' applies.
#
# Created: Sun Sep 29 22:24:31 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import sys
import os
from PySide2.QtWidgets import *
import json
class Fontset_Ui_Form(QWidget):
    def __init__(self): 
     super().__init__() 
     self.setupUi()
    def setupUi(self):
        self.setObjectName("Form")
        self.resize(800, 420)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(240, 80, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(330, 90, 231, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("HERSHEY_SIMPLEX")
        self.comboBox.addItem("HERSHEY_DUPLEX")
        self.comboBox.addItem("HERSHEY_COMPLEX")
        self.comboBox.addItem("HERSHEY_TRIPLEX")
        with open('./data/fontset.json', 'r') as f:
            dict = json.load(fp=f)
        self.comboBox.setCurrentIndex(self.comboBox.findText(dict['font']))
        self.comboBox_2 = QtWidgets.QComboBox(self)
        self.comboBox_2.setGeometry(QtCore.QRect(330, 200, 231, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("large")
        self.comboBox_2.addItem("medium")
        self.comboBox_2.addItem("small")
        self.comboBox_2.setCurrentIndex(self.comboBox_2.findText(dict['size']))
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(240, 200, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(580, 330, 121, 51))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 330, 121, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.clicked.connect(self.pushButton_Click)
        self.pushButton_2.clicked.connect(self.pushButton_2_Click)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
    def dict_to_json(self):
        dict={}
        dict['font']=self.comboBox.currentText()
        dict['size']=self.comboBox_2.currentText()
        with open('./data/fontset.json', 'w') as f:
            json.dump(dict, f)  
    def pushButton_Click(self):
        self.dict_to_json()
        self.close()
    def pushButton_2_Click(self):
        self.close()
    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Fontset", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "字型：", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "大小：", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "套用並關閉", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Form", "取消", None, -1))
if __name__ =="__main__":
    app=QtWidgets.QApplication(sys.argv)
    ex=Fontset_Ui_Form()
    ex.show()
    app.exec_()
