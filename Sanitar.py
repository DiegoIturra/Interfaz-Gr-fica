from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import psycopg2
import time
from datetime import date
from final import Ui_IngresarPaciente



class Ui_InfoPacienteS(object):

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_IngresarPaciente()
        self.ui.setupUi(self.window)
        #win.hide()
        self.window.show()
    
    def setupUi(self, InfoPaciente):
        InfoPaciente.setObjectName("InfoPaciente")
        InfoPaciente.resize(700, 500)
        self.centralwidget = QtWidgets.QWidget(InfoPaciente)
        self.centralwidget.setObjectName("centralwidget")
        self.infoPaciente = QtWidgets.QLabel(self.centralwidget)
        self.infoPaciente.setGeometry(QtCore.QRect(200, 20, 300, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.infoPaciente.setFont(font)
        self.infoPaciente.setObjectName("infoPaciente")
        self.rut = QtWidgets.QLabel(self.centralwidget)
        self.rut.setGeometry(QtCore.QRect(70, 70, 51, 31))
        self.rut.setObjectName("rut")
        self.nombrePaciente = QtWidgets.QLabel(self.centralwidget)
        self.nombrePaciente.setGeometry(QtCore.QRect(40, 120, 121, 31))
        self.nombrePaciente.setObjectName("nombrePaciente")
        self.fechaNacimiento = QtWidgets.QLabel(self.centralwidget)
        self.fechaNacimiento.setGeometry(QtCore.QRect(40, 170, 141, 31))
        self.fechaNacimiento.setObjectName("fechaNacimiento")
        self.edadPaciente = QtWidgets.QLabel(self.centralwidget)
        self.edadPaciente.setGeometry(QtCore.QRect(40, 220, 41, 31))
        self.edadPaciente.setObjectName("edadPaciente")
        self.prevSocial = QtWidgets.QLabel(self.centralwidget)
        self.prevSocial.setGeometry(QtCore.QRect(40, 270, 111, 31))
        self.prevSocial.setObjectName("prevSocial")
        self.tramo = QtWidgets.QLabel(self.centralwidget)
        self.tramo.setGeometry(QtCore.QRect(40, 320, 47, 31))
        self.tramo.setObjectName("tramo")
        self.outputNombre = QtWidgets.QLabel(self.centralwidget)
        self.outputNombre.setGeometry(QtCore.QRect(200, 120, 461, 31))
        self.outputNombre.setText("")
        self.outputNombre.setObjectName("outputNombre")
        self.outputFecNac = QtWidgets.QLabel(self.centralwidget)
        self.outputFecNac.setGeometry(QtCore.QRect(200, 170, 461, 31))
        self.outputFecNac.setText("")
        self.outputFecNac.setObjectName("outputFecNac")
        self.outputPrevSocial = QtWidgets.QLabel(self.centralwidget)
        self.outputPrevSocial.setGeometry(QtCore.QRect(200, 270, 461, 31))
        self.outputPrevSocial.setText("")
        self.outputPrevSocial.setObjectName("outputPrevSocial")
        self.outputEdad = QtWidgets.QLabel(self.centralwidget)
        self.outputEdad.setGeometry(QtCore.QRect(200, 220, 461, 31))
        self.outputEdad.setText("")
        self.outputEdad.setObjectName("outputEdad")
        self.outputTramo = QtWidgets.QLabel(self.centralwidget)
        self.outputTramo.setGeometry(QtCore.QRect(200, 320, 461, 31))
        self.outputTramo.setText("")
        self.outputTramo.setObjectName("outputTramo")
        self.inputRut = QtWidgets.QLineEdit(self.centralwidget)
        self.inputRut.setGeometry(QtCore.QRect(120, 70, 171, 31))
        self.inputRut.setObjectName("inputRut")
        self.botonOk = QtWidgets.QPushButton(self.centralwidget)
        self.botonOk.setGeometry(QtCore.QRect(320, 70, 71, 32))
        self.botonOk.setObjectName("botonOk")
        InfoPaciente.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(InfoPaciente)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 22))
        self.menubar.setObjectName("menubar")
        InfoPaciente.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(InfoPaciente)
        self.statusbar.setObjectName("statusbar")
        InfoPaciente.setStatusBar(self.statusbar)

        self.retranslateUi(InfoPaciente)
        QtCore.QMetaObject.connectSlotsByName(InfoPaciente)
        
        self.botonOk.clicked.connect(self.verInfo)

    def retranslateUi(self, InfoPaciente):
        _translate = QtCore.QCoreApplication.translate
        InfoPaciente.setWindowTitle(_translate("InfoPaciente", "Información del paciente"))
        self.infoPaciente.setText(_translate("InfoPaciente", "Información del paciente"))
        self.rut.setText(_translate("InfoPaciente", "Rut:"))
        self.nombrePaciente.setText(_translate("InfoPaciente", "Nombre:"))
        self.fechaNacimiento.setText(_translate("InfoPaciente", "Fecha de nacimiento:"))
        self.edadPaciente.setText(_translate("InfoPaciente", "Edad:"))
        self.prevSocial.setText(_translate("InfoPaciente", "Previsión social:"))
        self.tramo.setText(_translate("InfoPaciente", "Tramo:"))
        self.botonOk.setText(_translate("InfoPaciente", "Ok"))
        
        
    
    
    
    
    def showPopUp(self,tipoMensaje):
        popUp = QMessageBox()
        popUp.setWindowTitle("info")
        popUp.setStandardButtons(QMessageBox.Ok)
        popUp.setDefaultButton(QMessageBox.Ok)
        if tipoMensaje == "errorPaciente":
            popUp.setText("El rut, no ha sido ingresado como paciente")
            self.inputRut.setText("")
            popUp.setIcon(QMessageBox.Warning)
        elif tipoMensaje == "errorPersona":
            popUp.setText("El rut ingresado, no figura en la base de datos")
            self.inputRut.setText("")
            popUp.setIcon(QMessageBox.Information)
        elif tipoMensaje == "errorconexion":
            popUp.setText("Error de conexión a internet")
            popUp.setIcon(QMessageBox.Critical)
        x = popUp.exec_()
    
    
    def verInfo(self):
        rut = self.inputRut.text()
        print(rut)
            
        try:
            connection = psycopg2.connect(user="bdi2018f",password="bdi2018f",host="bdd.inf.udec.cl",database="bdi2018f",port=5432)
            cursor = connection.cursor()
            cursor.execute("SELECT p.prevision, p.tramo, p.edad, p.fecha_nac FROM ing.paciente AS p WHERE p.rut = %s",(rut,))
            lista1 = cursor.fetchall()
            cursor.execute("SELECT p.nombres, p.apellidos FROM ing.persona AS p WHERE p.rut = %s",(rut,))
            lista2 = cursor.fetchall()
                
            if(len(lista2) == 0):
                self.showPopUp("errorPersona")
                return
            elif(len(lista1) == 0):
                self.showPopUp("errorPaciente")
                return
                
            prevSo= str(lista1[0][0])
            tramo= str(lista1[0][1])
            edad= str(lista1[0][2])
            fecha= str(lista1[0][3])
                
            name = str(lista2[0][0]) +" "+str(lista2[0][1])
                
            if(tramo == "None" or len(tramo) == 0):
                tramo = "No aplica"
            
            #setear textos
            self.outputEdad.setText(edad)
            self.outputTramo.setText(tramo)
            self.outputPrevSocial.setText(prevSo)
            self.outputFecNac.setText(fecha)
            self.outputNombre.setText(name)
                
                    
                
            
        except Exception as e:
            self.showPopUp("errorconexion")
"""
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    infoFrame= Ui_InfoPacienteS()
    infoFrame.setupUi(win)
    win.show()
    sys.exit(app.exec_())
"""