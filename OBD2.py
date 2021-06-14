# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OBD2.ui',
# licensing of 'OBD2.ui' applies.
#
# Created: Sun Oct 13 14:09:25 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
import json
class OBD2_Ui_Form(QWidget):
    def __init__(self): 
        super().__init__() 
        self.setupUi()
    
    def setupUi(self):
        self.setObjectName("Form")
        self.resize(800, 420)
        with open('./data/obd2set.json', 'r') as f:
            dict = json.load(fp=f)
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(210,50, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(dict['rpm_ck'])            
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self)
        self.checkBox_2.setGeometry(QtCore.QRect(380, 50, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setChecked(dict['temp_ck'])     
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(130, 330, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 330, 121, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox_7 = QtWidgets.QCheckBox(self)
        self.checkBox_7.setGeometry(QtCore.QRect(40, 50, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setChecked(dict['speed_ck'])     
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self)
        self.checkBox_8.setGeometry(QtCore.QRect(500, 50, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setChecked(False)  
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self)
        self.checkBox_9.setGeometry(QtCore.QRect(650, 50, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setChecked(dict['IF_ck'])  
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self)
        self.checkBox_10.setGeometry(QtCore.QRect(40, 150, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.checkBox_10.setFont(font)
        self.checkBox_10.setChecked(dict['IMAP_ck'])  
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self)
        self.checkBox_11.setGeometry(QtCore.QRect(210, 150, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.checkBox_11.setFont(font)
        self.checkBox_11.setChecked(dict['TP_ck'])  
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self)
        self.checkBox_12.setGeometry(QtCore.QRect(370, 150, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.checkBox_12.setFont(font)
        self.checkBox_12.setChecked(dict['IAA_ck'])  
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(self)
        self.checkBox_13.setGeometry(QtCore.QRect(550, 150, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.checkBox_13.setFont(font)
        self.checkBox_13.setChecked(dict['EL_ck'])  
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(self)
        self.checkBox_14.setGeometry(QtCore.QRect(40, 250, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.checkBox_14.setFont(font)
        self.checkBox_14.setChecked(dict['RO_ck'])  
        self.checkBox_14.setObjectName("checkBox_14")
        self.pushButton.clicked.connect(self.pushButton_Click)
        self.pushButton_2.clicked.connect(self.pushButton2_Click)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


    def pushButton_Click(self):      
        self.close()
    def dict_to_json(self):
        dict={}
        dict['rpm_ck']=self.checkBox.isChecked()
        dict['temp_ck']=self.checkBox_2.isChecked()
        dict['speed_ck']=self.checkBox_7.isChecked()
        dict['IAT_ck']=self.checkBox_8.isChecked()
        dict['IF_ck']=self.checkBox_9.isChecked()
        dict['IMAP_ck']=self.checkBox_10.isChecked()
        dict['TP_ck']=self.checkBox_11.isChecked()
        dict['IAA_ck']=self.checkBox_12.isChecked()
        dict['EL_ck']=self.checkBox_13.isChecked()
        dict['RO_ck']=self.checkBox_14.isChecked()
        with open('./data/obd2set.json', 'w') as f:
            json.dump(dict, f)
    def pushButton2_Click(self):
        self.dict_to_json()
        self.close()
    
    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "OBD2", None, -1))
        self.checkBox.setText(QtWidgets.QApplication.translate("Form", "引擎轉速", None, -1))
        self.checkBox_2.setText(QtWidgets.QApplication.translate("Form", "水溫", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "取消", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Form", "套用並關閉", None, -1))
        self.checkBox_7.setText(QtWidgets.QApplication.translate("Form", "行車速度", None, -1))
        self.checkBox_8.setText(QtWidgets.QApplication.translate("Form", "進氣溫度", None, -1))
        self.checkBox_9.setText(QtWidgets.QApplication.translate("Form", "進氣流量", None, -1))
        self.checkBox_10.setText(QtWidgets.QApplication.translate("Form", "進氣歧管\n"
"絕對壓力", None, -1))
        self.checkBox_11.setText(QtWidgets.QApplication.translate("Form", "節氣門\n"
"絕對位置", None, -1))
        self.checkBox_12.setText(QtWidgets.QApplication.translate("Form", "點火提前角", None, -1))
        self.checkBox_13.setText(QtWidgets.QApplication.translate("Form", "引擎負荷", None, -1))
        self.checkBox_14.setText(QtWidgets.QApplication.translate("Form", "剩餘油量", None, -1))
if __name__ =="__main__":
    app=QtWidgets.QApplication(sys.argv)
    ex=OBD2_Ui_Form()
    ex.show()
    app.exec_()
