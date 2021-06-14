# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Mon Sep 23 09:27:46 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!
import sys
import os
import cv2 
import threading
from PySide2 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import time
import datetime
import obd
from os.path import join, getsize
import pytz
import json

class Ui_Form(QWidget):
    
    def closeEvent(self, event):
        print('closing..')
        cv2.destroyAllWindows()
        event.accept()         
    def __init__(self): 
     super().__init__() 
     self.setupUi()
     self.pushButton.clicked.connect(self.pushButton_Click) 
    def setupUi(self):
        self.setObjectName("Form")
        self.resize(800, 420)
        self.label=QLabel("label",self)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 420))
        self.label.setScaledContents(True)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(650, 350, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()
    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "VRSWO", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "TextLabel", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "設定", None, -1))
    def SetPic(self,img):
        self.label.setPixmap(QPixmap.fromImage(img))
    def pushButton_Click(self):
        os.system('python setting.py')


thstop=False   

class OBDII:
    def __init__(self):
        self.rpm_value=0
        self.speed_value=0
        self.temp_value=0
        self.TP_value=0
        self.RO_value=0
        self.MAF_value=0
        self.IMAP_value=0
        self.IAA_value=0
        self.EL_value=0
        self.IT_value=0
        self.connect()
    def connect(self):
        print("connecting..")
        ports=obd.scan_serial()
        print(ports)
        connection = obd.Async(portstr=ports[1],  fast=False, check_voltage=False)
        connection.watch(obd.commands.RPM, callback=self.new_rpm, force=True)
        connection.watch(obd.commands.SPEED, callback=self.new_speed, force=True) 
        connection.watch(obd.commands.COOLANT_TEMP, callback=self.new_temp, force=True)
        connection.watch(obd.commands.INTAKE_TEMP, callback=self.new_IT, force=True)
        connection.watch(obd.commands.MAF, callback=self.new_MAF, force=True)
        connection.watch(obd.commands.INTAKE_PRESSURE, callback=self.new_IMAP, force=True)
        connection.watch(obd.commands.THROTTLE_POS, callback=self.new_TP, force=True)
        connection.watch(obd.commands.TIMING_ADVANCE, callback=self.new_IAA, force=True)
        connection.watch(obd.commands.ENGINE_LOAD, callback=self.new_EL, force=True)
        connection.watch(obd.commands.FUEL_LEVEL, callback=self.new_RO, force=True)   
        connection.start()
    def new_rpm(self,r):
        if not r.is_null():
            self.rpm_value = int(r.value.magnitude)
        else:   
            self.rpm_value = 0
        sys.stdout.flush()
        time.sleep(0.3)     
    def new_speed(self,r):
        if not r.is_null():
            self.speed_value = int(r.value.magnitude)
        else:
            self.speed_value = 0
        sys.stdout.flush()
        time.sleep(0.3)      
    def new_temp(self,r):
        if not r.is_null():
            self.temp_value = int(r.value.magnitude)
        else:
            self.temp_value= 0
        sys.stdout.flush()
        time.sleep(0.3)       
    def new_IT(self,r):
        if not r.is_null():
            self.IT_value = int(r.value.magnitude)
        else:
            self.IT_value= 0
        sys.stdout.flush()
        time.sleep(0.3)    
    def new_MAF(self,r):
        if not r.is_null():
            self.MAF_value = int(r.value.magnitude)
        else:
            self.MAF_value= 0
        sys.stdout.flush()
        time.sleep(0.3)    
    def new_IMAP(self,r):
        if not r.is_null():
            self.IMAP_value = int(r.value.magnitude)
        else:
            self.IMAP_value= 0
        sys.stdout.flush()
        time.sleep(0.3)       
    def new_TP(self,r):
        if not r.is_null():
            self.TP_value = int(r.value.magnitude)
        else:
            self.TP_value= 0
        sys.stdout.flush()
        time.sleep(0.3)    
    def new_IAA(self,r):
        if not r.is_null():
            self.IAA_value = int(r.value.magnitude)
        else:
            self.IAA_value= 0
        sys.stdout.flush()
        time.sleep(0.3)     
    def new_EL(self,r):
        if not r.is_null():
            self.EL_value = int(r.value.magnitude)
        else:
            self.EL_value= 0
        sys.stdout.flush()
        time.sleep(0.3)      
    def new_RO(self,r):
        if not r.is_null():
            self.RO_value = int(r.value.magnitude)
        else:
            self.RO_value= 0
        sys.stdout.flush()
        time.sleep(0.3)
        
    



class CAM:
    def __init__(self):
        self.font=cv2.FONT_HERSHEY_SIMPLEX
        self.tz=pytz.timezone('Asia/Taipei')
        self.size=0.3
        self.fourcc=cv2.VideoWriter_fourcc(*'XVID')
        self.showcam()
    def set_size_font(self):
        with open('./data/fontset.json', 'r') as f:
            dict = json.load(fp=f)
            f.close()
        if dict['size']=='large':
            self.size=0.8
        if dict['size']=='medium':
            self.size=0.6
        if dict['size']=='small':
            self.size=0.3
        if dict['font']=='HERSHEY_SIMPLEX':
             self.font=cv2.FONT_HERSHEY_SIMPLEX
        if dict['font']=='HERSHEY_DUPLEX':
             self.font=cv2.FONT_HERSHEY_DUPLEX
        if dict['font']=='HERSHEY_COMPLEX':
             self.font=cv2.FONT_HERSHEY_COMPLEX
        if dict['font']=='HERSHEY_TRIPLEX':
             self.font=cv2.FONT_HERSHEY_TRIPLEX
    def set_video_code(self):
        with open('./data/videocode.json', 'r') as f:
            dict = json.load(fp=f)
            f.close()
        if dict['videocode']=='(PIM1)MPEG-1 codec':
            fourcc = cv2.VideoWriter_fourcc(*'PIM1')
        if dict['videocode']=='(MJPG)motion-jpeg codec':
            fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        if dict['videocode']=='(MP42)MPEG-4.2 codec':
            fourcc = cv2.VideoWriter_fourcc(*'MP42')
        if dict['videocode']=='(DIV3)MPEG-4.3 codec':
            fourcc = cv2.VideoWriter_fourcc(*'DIV3')
        if dict['videocode']=='(DIVX)MPEG-4 codec':
            fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        if dict['videocode']=='(U263)H263 codec':
            fourcc = cv2.VideoWriter_fourcc(*'U263')
        if dict['videocode']=='(FLV1)FLV1 codec':
            fourcc = cv2.VideoWriter_fourcc(*'FLV1')
    def set_checked(self):
        with open('./data/obd2set.json', 'r') as f:
            dict = json.load(fp=f)
        self.ctn=0
        self.ctn_2=0
        self.item=[0]*10
        self.unitem=[0]*10
        if dict['rpm_ck']==True:
            self.item[self.ctn]='Rpm:'
            self.ctn=self.ctn+1
        else:
            self.unitem[self.ctn_2]='Rpm:'
            self.ctn_2=self.ctn_2+1
        if dict['temp_ck']==True:
            self.item[self.ctn]='Temp:'
            self.ctn=self.ctn+1
        else:
            self.unitem[self.ctn_2]='temp:'
            self.ctn_2=self.ctn_2+1
        if dict['speed_ck']==True:
            self.item[self.ctn]='Speed:'
            self.ctn=self.ctn+1
        else:
            self.unitem[self.ctn_2]='Speed:'
            self.ctn_2=self.ctn_2+1
        if dict['IAT_ck']==True:
            self.item[self.ctn]='IAT:'
            self.ctn=self.ctn+1
        else:
            self.unitem[self.ctn_2]='IAT:'
            self.ctn_2=self.ctn_2+1
        if dict['IF_ck']==True:
            self.item[self.ctn]='IF:'
            self.ctn=self.ctn+1
        else:
            self.unitem[self.ctn_2]='IF:'
            self.ctn_2=self.ctn_2+1
        if dict['IMAP_ck']==True:
            self.item[self.ctn]='IMAP:'
            self.ctn=self.ctn+1
        else:
            self.unitem[self.ctn_2]='IMAP:'
            self.ctn_2=self.ctn_2+1
        if dict['TP_ck']==True:
            self.item[self.ctn]='TP:'
            self.ctn=self.ctn+1
        else:
            self.unitem[self.ctn_2]='TP:'
            self.ctn_2=self.ctn_2+1
        if dict['IAA_ck']==True:
            self.item[self.ctn]='IAA:'
            self.ctn=self.ctn+1
        else:
            self.unitem[self.ctn_2]='IAA:'
            self.ctn_2=self.ctn_2+1
        if dict['EL_ck']==True:
            self.item[self.ctn]='EL:'
            self.ctn=self.ctn+1
        else:
            self.unitem[self.ctn_2]='EL:'
            self.ctn_2=self.ctn_2+1
        if dict['RO_ck']==True:
            self.item[self.ctn]='RO:'
            self.ctn=self.ctn+1
        else:
            self.unitem[self.ctn_2]='RO:'
            self.ctn_2=self.ctn_2+1      
    
    def showcam(self):
        def rotate(image,angle,center=None,scale=1):
            (h,w)= image.shape[:2]
            if center is None:
                center =(w/2,h/2)
            m=cv2.getRotationMatrix2D(center,angle,scale)
            rotated=cv2.warpAffine(image,m,(w,h))
            return rotated
        def filerename():
            filename = 'output_{0}.avi'.format(datetime.datetime.now().strftime("%Y-%m-%d"))
            if os.path.isfile('./video/'+filename):
                fn2 = filename[0:-4]+'_{0}.avi'
                count = 1
                while os.path.isfile('./video/' +fn2.format(count)):
                    count += 1
                filename=fn2.format(count)
            return filename  
        cap=cv2.VideoCapture(0) 
        
        cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)#320*240
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
        cap.set(cv2.CAP_PROP_FPS,20)#字體根據解析度
         
        filename=filerename()
        self.set_video_code()
        self.set_checked()
        self.set_size_font()
        with open('./data/warning_value.json', 'r',encoding='ISO-8859-1') as f:
            dict = json.load(fp=f)
         
        video=cv2.VideoWriter('./video/'+filename, self.fourcc ,20,(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

        link=OBDII()
        while cap.isOpened():

            if thstop:
                return
            ret,frame=cap.read()
            if ret==False:
                continue
            frame=cv2.flip(frame,-1)
            frame=rotate(frame,-90)
            
            localtime_1 = datetime.datetime.now(self.tz).strftime("%Y/%m/%d")
            localtime_2 = datetime.datetime.now(self.tz).strftime("%H:%M:%S")

           
            cv2.putText(frame, localtime_1, (250,20), self.font, self.size, (255, 255, 255), 1)
            cv2.putText(frame, localtime_2, (250,50), self.font, self.size, (255, 255, 255), 1)
            x=20
            value=0

            for i in range(self.ctn):
                color=(255,255,255)
                
                if self.item[i]=="Rpm:":
                    value=link.rpm_value
                    if value>=int(dict['rpm']):
                        color=(0,0,255)
                if self.item[i]=="Temp:":
                    value=link.temp_value
                    if value>int(dict['temp']):
                        color=(0,0,255)
                if self.item[i]=="Speed:":
                    value=link.speed_value
                    if value>int(dict['speed']):
                        color=(0,0,255)            
                if self.item[i]=="IAT:":
                    value=link.IT_value
                    if value>int(dict['IAT']):
                        color=(0,0,255)
                if self.item[i]=="IF:":
                    value=link.MAF_value
                    if value>int(dict['IF']):
                        color=(0,0,255)
                if self.item[i]=="IMAP:":
                    value=link.IMAP_value
                    if value>int(dict['IMAP']):
                        color=(0,0,255)
                if self.item[i]=="TP:":
                    value=link.TP_value
                    if value>int(dict['TP']):
                        color=(0,0,255)
                if self.item[i]=="IAA:":
                    value=link.IAA_value
                    if value>int(dict['IAA']):
                        color=(0,0,255)
                if self.item[i]=="EL:":
                    value=link.EL_value
                    if value>int(dict['EL']):
                        color=(0,0,255)
                if self.item[i]=="RO:":
                    value=link.RO_value
                    if value < int(dict['RO']):
                        color=(0,0,255)        
                
                cv2.putText(frame,self.item[i]+str(value),(20,x),self.font,self.size,color,1)
                x=x+30
            for i in range(self.ctn_2):
                if self.unitem[i]=="Rpm:":
                    value=link.rpm_value
                    if value>=int(dict['rpm']):
                        cv2.putText(frame,self.unitem[i]+str(value),(20,x),self.font,self.size,(0,0,255),1)
                        x=x+30
                if self.unitem[i]=="Temp:":
                    value=link.temp_value
                    if value>int(dict['temp']):
                        cv2.putText(frame,self.unitem[i]+str(value),(20,x),self.font,self.size,(0,0,255),1)
                        x=x+30
                if self.unitem[i]=="Speed:":
                    value=link.speed_value
                    if value>int(dict['speed']):
                        cv2.putText(frame,self.unitem[i]+str(value),(20,x),self.font,self.size,(0,0,255),1)
                        x=x+30           
                if self.unitem[i]=="IAT:":
                    value=link.IT_value
                    if value>int(dict['IAT']):
                        cv2.putText(frame,self.unitem[i]+str(value),(20,x),self.font,self.size,(0,0,255),1)
                        x=x+30
                if self.unitem[i]=="IF:":
                    value=link.MAF_value
                    if value>int(dict['IF']):
                        cv2.putText(frame,self.unitem[i]+str(value),(20,x),self.font,self.size,(0,0,255),1)
                        x=x+30
                if self.unitem[i]=="IMAP:":
                    value=link.IMAP_value
                    if value>int(dict['IMAP']):
                        cv2.putText(frame,self.unitem[i]+str(value),(20,x),self.font,self.size,(0,0,255),1)
                        x=x+30
                if self.unitem[i]=="TP:":
                    value=link.TP_value
                    if value>int(dict['TP']):
                        cv2.putText(frame,self.unitem[i]+str(value),(20,x),self.font,self.size,(0,0,255),1)
                        x=x+30
                if self.unitem[i]=="IAA:":
                    value=link.IAA_value
                    if value>int(dict['IAA']):
                        cv2.putText(frame,self.unitem[i]+str(value),(20,x),self.font,self.size,(0,0,255),1)
                        x=x+30
                if self.unitem[i]=="EL:":
                    value=link.EL_value
                    if value>int(dict['EL']):
                        cv2.putText(frame,self.unitem[i]+str(value),(20,x),self.font,self.size,(0,0,255),1)
                        x=x+30
                if self.unitem[i]=="RO:":
                    value=link.RO_value
                    if value < int(dict['RO']):
                        cv2.putText(frame,self.unitem[i]+str(value),(20,x),self.font,self.size,(0,0,255),1)
                        x=x+30


                

            frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
            a=QImage(frame.data,frame.shape[1],frame.shape[0],QImage.Format_RGB888)    
       
            mb=int(os.path.getsize('./video/'+filename))/1024/1024
            if mb>100:
                filename=filerename()
                video=cv2.VideoWriter('./video/'+filename, self.fourcc ,20,(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
        
            video.write(cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))
    
            ex.SetPic(a)
           
     

            

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex=Ui_Form()
    th=threading.Thread(target=CAM)
    th.start()
    ex.show()
    app.exec_()
    thstop=True
