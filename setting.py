# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui',
# licensing of 'setting.ui' applies.
#
# Created: Sun Oct 13 15:07:06 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!
import sys
import os
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets
import shutil


class Setting_Ui_Form(QWidget): 
    def __init__(self): 
        super().__init__() 
        self.setupUi() 
    def setupUi(self):
        self.setObjectName("Form")
        self.resize(800, 420)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(140, 50, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 170, 121, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 50, 121, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 290, 121, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(390, 170, 121, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self)
        self.pushButton_6.setGeometry(QtCore.QRect(640, 50, 121, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self)
        self.pushButton_7.setGeometry(QtCore.QRect(390, 290, 121, 51))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton.clicked.connect(self.pushButton_Click)
        self.pushButton_2.clicked.connect(self.pushButton_2_Click)
        self.pushButton_3.clicked.connect(self.pushButton_3_Click)
        self.pushButton_4.clicked.connect(self.pushButton_4_Click)
        self.pushButton_5.clicked.connect(self.pushButton_5_Click)
        self.pushButton_6.clicked.connect(self.pushButton_6_Click)
        self.pushButton_7.clicked.connect(self.pushButton_7_Click)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
    def pushButton_Click(self):
        os.system('python OBD2.py')
    def pushButton_2_Click(self):
        os.system('python fontset.py')
    def pushButton_3_Click(self):
        reply=QMessageBox.warning(self,"記憶卡格式化","此功能將把記憶卡內容全部清除，\n請確認是否執行?",QMessageBox.Yes,QMessageBox.No)
        if reply == QMessageBox.Yes:
            shutil.rmtree('video')
            os.mkdir('video')
    def pushButton_4_Click(self):
        os.system('python TimeZone.py')
    def pushButton_5_Click(self):
        os.system('python videocode.py')
    def pushButton_6_Click(self):
        self.close()
    def pushButton_7_Click(self):
        os.system('python warning.py')
    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "setting", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "OBD2顯示選項", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Form", "調整字體大小", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("Form", "記憶卡格式化", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("Form", "調整時區", None, -1))
        self.pushButton_5.setText(QtWidgets.QApplication.translate("Form", "視訊編碼選項", None, -1))
        self.pushButton_6.setText(QtWidgets.QApplication.translate("Form", "返回", None, -1))
        self.pushButton_7.setText(QtWidgets.QApplication.translate("Form", "警示選項設置", None, -1))
    
        
if __name__ =="__main__":
    app=QtWidgets.QApplication(sys.argv)
    ex=Setting_Ui_Form()
    ex.show()
    app.exec_()

