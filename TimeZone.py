# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'location.ui',
# licensing of 'location.ui' applies.
#
# Created: Sun Sep 29 21:55:03 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import sys
import os
from PySide2.QtWidgets import *
import json
class TimeZone_Ui_Form(QWidget):
    def __init__(self): 
        super().__init__() 
        self.setupUi() 
    def setupUi(self):
        self.setObjectName("Form")
        self.resize(800, 420)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(250, 160, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(130, 330, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 330, 121, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(330, 160, 221, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("亞洲-台港澳地區(UTC+8:00)")
        self.comboBox.addItem("亞洲-日本韓國(UTC+9:00)")
        self.comboBox.addItem("亞洲-越南(UTC+7:00)")
        self.comboBox.addItem("歐洲-英國(UTC+0:00)")
        self.comboBox.addItem("歐洲-法國(UTC+1:00)")
        self.comboBox.addItem("美洲-美國(UTC-8:00)")
        self.comboBox.addItem("美洲-墨西哥(UTC-6:00)")
        self.comboBox.addItem("美洲-丹麥(UTC-3:00)")
        self.comboBox.addItem("大洋洲-澳洲(UTC+10:00)")
        self.comboBox.addItem("大洋洲-紐西蘭(UTC+12:00)")
        self.comboBox.addItem("非洲-埃及(UTC+2:00)")
        with open('./data/timezone.json', 'r') as f:
            dict = json.load(fp=f)
        self.comboBox.setCurrentIndex(self.comboBox.findText(dict['timezone']))
        self.pushButton.clicked.connect(self.pushButton_Click)
        self.pushButton_2.clicked.connect(self.pushButton_2_Click)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
    def pushButton_Click(self):
        self.close()
    def dict_to_json(self):
        dict={}
        dict['timezone']=self.comboBox.currentText()
        with open('./data/timezone.json', 'w') as f:
            json.dump(dict, f,ensure_ascii=False) 
    def pushButton_2_Click(self):
        self.dict_to_json()
        self.close()
    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "TimeZone", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "時區", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "取消", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Form", "套用並關閉", None, -1))
if __name__ =="__main__":
    app=QtWidgets.QApplication(sys.argv)
    ex=TimeZone_Ui_Form()
    ex.show()
    app.exec_()
