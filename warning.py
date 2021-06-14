# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warning.ui',
# licensing of 'warning.ui' applies.
#
# Created: Thu Nov 28 14:34:25 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
import sys
import json
class Warning_Ui_Form(QWidget):
    def __init__(self): 
        super().__init__() 
        self.setupUi()
    
    def setupUi(self):
        self.setObjectName("Form")
        self.resize(800, 420)
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(340, 110, 241, 31))
        self.comboBox.setStyleSheet("font: 10pt \"Agency FB\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(220, 90, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(220, 190, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(130, 330, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 330, 121, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.spinBox = QtWidgets.QSpinBox(self)
        self.spinBox.setGeometry(QtCore.QRect(360, 200, 201, 51))
        self.spinBox.setSingleStep(10)
        self.spinBox.setMaximum(9999)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.pushButton.clicked.connect(self.pushButton_Click)
        self.pushButton_2.clicked.connect(self.pushButton_2_Click)
        self.comboBox.currentTextChanged.connect(self.combobox_change)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
    def combobox_change(self):
        with open('./data/warning_value.json', 'r',encoding='ISO-8859-1') as f:
            dict = json.load(fp=f)
        if self.comboBox.currentText()=='引擎轉速':
            self.spinBox.setValue(dict['rpm'])
        if self.comboBox.currentText()=='水溫':
            self.spinBox.setValue(dict['temp'])
        if self.comboBox.currentText()=='行車速度':
            self.spinBox.setValue(dict['speed'])
        if self.comboBox.currentText()=='進氣溫度':
            self.spinBox.setValue(dict['IAT'])
        if self.comboBox.currentText()=='進氣流量':
            self.spinBox.setValue(dict['IF'])
        if self.comboBox.currentText()=='進氣岐管絕對壓力':
            self.spinBox.setValue(dict['IMAP'])
        if self.comboBox.currentText()=='節氣門絕對位置':
            self.spinBox.setValue(dict['TP'])
        if self.comboBox.currentText()=='點火提前角':
            self.spinBox.setValue(dict['IAA'])
        if self.comboBox.currentText()=='引擎負荷':
            self.spinBox.setValue(dict['EL'])
        if self.comboBox.currentText()=='剩餘油量':
            self.spinBox.setValue(dict['RO'])

    def dict_to_json(self):
        with open('./data/warning_value.json', 'r',encoding='ISO-8859-1') as f:
            dict = json.load(fp=f)
        if self.comboBox.currentText()=='引擎轉速':
            dict['rpm']=self.spinBox.value()
        if self.comboBox.currentText()=='水溫':
            dict['temp']=self.spinBox.value()
        if self.comboBox.currentText()=='行車速度':
            dict['speed']=self.spinBox.value()
        if self.comboBox.currentText()=='進氣溫度':
            dict['IAT']=self.spinBox.value()
        if self.comboBox.currentText()=='進氣流量':
            dict['IF']=self.spinBox.value()
        if self.comboBox.currentText()=='進氣岐管絕對壓力':
            dict['IMAP']=self.spinBox.value()
        if self.comboBox.currentText()=='節氣門絕對位置':
            dict['TP']=self.spinBox.value()
        if self.comboBox.currentText()=='點火提前角':
            dict['IAA']=self.spinBox.value()
        if self.comboBox.currentText()=='引擎負荷':
            dict['EL']=self.spinBox.value()
        if self.comboBox.currentText()=='剩餘油量':
            dict['RO']=self.spinBox.value()

        dict['item']=self.comboBox.currentText()
        with open('./data/warning_value.json', 'w') as f:
            json.dump(dict, f,ensure_ascii=False)
    def pushButton_Click(self):
        self.close()
    def pushButton_2_Click(self):
        self.dict_to_json()
        self.close()
    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.comboBox.setItemText(0, QtWidgets.QApplication.translate("Form", "引擎轉速", None, -1))
        self.comboBox.setItemText(1, QtWidgets.QApplication.translate("Form", "水溫", None, -1))
        self.comboBox.setItemText(2, QtWidgets.QApplication.translate("Form", "行車速度", None, -1))
        self.comboBox.setItemText(3, QtWidgets.QApplication.translate("Form", "進氣溫度", None, -1))
        self.comboBox.setItemText(4, QtWidgets.QApplication.translate("Form", "進氣流量", None, -1))
        self.comboBox.setItemText(5, QtWidgets.QApplication.translate("Form", "進氣岐管絕對壓力", None, -1))
        self.comboBox.setItemText(6, QtWidgets.QApplication.translate("Form", "節氣門絕對位置", None, -1))
        self.comboBox.setItemText(7, QtWidgets.QApplication.translate("Form", "點火提前角", None, -1))
        self.comboBox.setItemText(8, QtWidgets.QApplication.translate("Form", "引擎負荷", None, -1))
        self.comboBox.setItemText(9, QtWidgets.QApplication.translate("Form", "剩餘油量", None, -1))
        with open('./data/warning_value.json', 'r',encoding='ISO-8859-1') as f: 
            dict = json.load(fp=f)
        self.comboBox.setCurrentIndex(self.comboBox.findText(str(dict['item'])))
        self.label.setText(QtWidgets.QApplication.translate("Form", "警示項目", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "警示範圍", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "取消", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Form", "套用並關閉", None, -1))
if __name__ =="__main__":
    app=QtWidgets.QApplication(sys.argv)
    ex=Warning_Ui_Form()
    ex.show()
    app.exec_()

