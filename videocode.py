# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'location.ui',
# licensing of 'location.ui' applies.
#
# Created: Mon Oct 14 02:37:26 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets
import sys
import os
import cv2
from PySide2.QtWidgets import *
import json
class Videocode_Ui_Form(QWidget):
    def __init__(self): 
        super().__init__() 
        self.setupUi() 
    def setupUi(self):
        self.setObjectName("Form")
        self.resize(800, 420)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(220, 160, 121, 31))
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
        self.comboBox.setGeometry(QtCore.QRect(360, 160, 221, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("(PIM1)MPEG-1 codec")
        self.comboBox.addItem("(MJPG)motion-jpeg codec")
        self.comboBox.addItem("(MP42)MPEG-4.2 codec")
        self.comboBox.addItem("(DIV3)MPEG-4.3 codec")
        self.comboBox.addItem("(DIVX)MPEG-4 codec")
        self.comboBox.addItem("(U263)H263 codec") 
        self.comboBox.addItem("(FLV1)FLV1 codec")
        with open('./data/videocode.json', 'r') as f:
            dict = json.load(fp=f)
        self.comboBox.setCurrentIndex(self.comboBox.findText(dict['videocode']))
        self.pushButton.clicked.connect(self.pushButton_Click)
        self.pushButton_2.clicked.connect(self.pushButton_2_Click)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
       
    def pushButton_Click(self):
        self.close()
    def dict_to_json(self):
        dict={}
        dict['videocode']=self.comboBox.currentText()
        with open('./data/videocode.json', 'w') as f:
            json.dump(dict, f)
    def pushButton_2_Click(self):
        reply = QMessageBox.information(self,'提示','下次重開後完成視訊編碼變更', QMessageBox.Ok )
        if reply == QMessageBox.Ok:
            self.dict_to_json()
            self.close()
        
    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Videocode", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "視訊編碼：", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "取消", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Form", "套用並關閉", None, -1))
if __name__ =="__main__":

    app = QtWidgets.QApplication(sys.argv)
    ex=Videocode_Ui_Form()
    ex.show()
    app.exec_()
