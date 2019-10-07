from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import psycopg2
import time
from datetime import date
from iChequeo import Ui_check

class Ui_IngresarPaciente(object):
    #def __init__(self, rutMedico, nombre, rut, tramo, prevSocial, fecNac, edad):

    def openCheck(rut,name,fecha,edad,preS,tramo):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_chequeo(rut,name,fecha,edad,preS,tramo)
        self.ui.setupUi(self.window)
        #win.hide()
        self.window.show()
    
    def setupUi(self, IngresarPaciente):
        IngresarPaciente.setObjectName("IngresarPaciente")
        IngresarPaciente.resize(700, 500)
        self.centralwidget = QtWidgets.QWidget(IngresarPaciente)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(200, 20, 300, 34))
        self.titulo.setObjectName("titulo")
        self.Nombres = QtWidgets.QLabel(self.centralwidget)
        self.Nombres.setGeometry(QtCore.QRect(40, 70, 71, 31))
        self.Nombres.setObjectName("Nombres")
        self.inputNombres = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNombres.setGeometry(QtCore.QRect(175, 70, 351, 31))
        self.inputNombres.setObjectName("inputNombres")
        self.Apellidos = QtWidgets.QLabel(self.centralwidget)
        self.Apellidos.setGeometry(QtCore.QRect(40, 120, 71, 31))
        self.Apellidos.setObjectName("Apellidos")
        self.inputApellidos = QtWidgets.QLineEdit(self.centralwidget)
        self.inputApellidos.setGeometry(QtCore.QRect(175, 120, 351, 31))
        self.inputApellidos.setObjectName("inputApellidos")
        self.Rut = QtWidgets.QLabel(self.centralwidget)
        self.Rut.setGeometry(QtCore.QRect(40, 170, 51, 31))
        self.Rut.setObjectName("Rut")
        self.inputRut = QtWidgets.QLineEdit(self.centralwidget)
        self.inputRut.setGeometry(QtCore.QRect(175, 170, 171, 31))
        self.inputRut.setObjectName("inputRut")
        self.FechaNac = QtWidgets.QLabel(self.centralwidget)
        self.FechaNac.setGeometry(QtCore.QRect(40, 220, 131, 31))
        self.FechaNac.setObjectName("FechaNac")
        self.inputFechaNac = QtWidgets.QLineEdit(self.centralwidget)
        self.inputFechaNac.setGeometry(QtCore.QRect(175, 220, 171, 31))
        self.inputFechaNac.setObjectName("inputFechaNac")
        self.PrevSocial = QtWidgets.QLabel(self.centralwidget)
        self.PrevSocial.setGeometry(QtCore.QRect(40, 270, 121, 31))
        self.PrevSocial.setObjectName("PrevSocial")
        self.inputPrevSocial = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPrevSocial.setGeometry(QtCore.QRect(175, 270, 171, 31))
        self.inputPrevSocial.setObjectName("inputPrevSocial")
        self.Tramo = QtWidgets.QLabel(self.centralwidget)
        self.Tramo.setGeometry(QtCore.QRect(360, 270, 41, 31))
        self.Tramo.setObjectName("Tramo")
        self.inputTramo = QtWidgets.QLineEdit(self.centralwidget)
        self.inputTramo.setGeometry(QtCore.QRect(415, 270, 111, 31))
        self.inputTramo.setObjectName("inputTramo")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(215, 340, 241, 41))
        self.pushButton.setObjectName("pushButton")
        IngresarPaciente.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(IngresarPaciente)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 22))
        self.menubar.setObjectName("menubar")
        IngresarPaciente.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(IngresarPaciente)
        self.statusbar.setObjectName("statusbar")
        IngresarPaciente.setStatusBar(self.statusbar)
        
        self.pushButton.clicked.connect(self.ingresarInfo)

        self.retranslateUi(IngresarPaciente)
        QtCore.QMetaObject.connectSlotsByName(IngresarPaciente)

    def retranslateUi(self, IngresarPaciente):
        _translate = QtCore.QCoreApplication.translate
        IngresarPaciente.setWindowTitle(_translate("IngresarPaciente", "Ingresar paciente al sistema"))
        self.titulo.setText(_translate("IngresarPaciente", "Ingresar paciente al sistema"))
        self.Nombres.setText(_translate("IngresarPaciente", "Nombres:"))
        self.Apellidos.setText(_translate("IngresarPaciente", "Apellidos:"))
        self.Rut.setText(_translate("IngresarPaciente", "Rut:"))
        self.FechaNac.setText(_translate("IngresarPaciente", "Fecha de nacimiento:"))
        self.PrevSocial.setText(_translate("IngresarPaciente", "Previsión social:"))
        self.Tramo.setText(_translate("IngresarPaciente", "Tramo:"))
        self.pushButton.setText(_translate("IngresarPaciente", "Ingresar y pasar a chequeo"))
    
    def days_between(self,d1,d2):
        return abs(d2 - d1).days
    
    def showPopUp(self,tipoMensaje):
        popUp = QMessageBox()
        popUp.setWindowTitle("info")
        popUp.setStandardButtons(QMessageBox.Ok)
        popUp.setDefaultButton(QMessageBox.Ok)
        if tipoMensaje == "PacienteYaIngresado":
            popUp.setText("Paciente ya esta registrado")
            popUp.setIcon(QMessageBox.Warning)
        elif tipoMensaje == "ingresoCorrecto":
            popUp.setText("Paciente ingresado correctamente")
            popUp.setIcon(QMessageBox.Information)
        elif tipoMensaje == "errorconexion":
            popUp.setText("Error de conexión a internet")
            popUp.setIcon(QMessageBox.Critical)
        elif tipoMensaje == "errorDatos":
            popUp.setText("datos mal ingresados")
            self.inputFechaNac.setText("")
            popUp.setIcon(QMessageBox.Critical)
        x = popUp.exec_()
            

    def ingresarInfo(self):
        nombre = self.inputNombres.text()
        apellidos = self.inputApellidos.text()
        rut = self.inputRut.text()
        fecha = self.inputFechaNac.text()
        prevSocial = self.inputPrevSocial.text()
        tramo = self.inputTramo.text()
        a = "20"
        fechaActual = a+time.strftime("%y/%m/%d")
        splitting = fechaActual.split('/')
        print("hola")
        try:
            d1= date( int(splitting[0]) , int(splitting[1]) ,int(splitting[2]))
            splitting2 = fecha.split('-')
            d2= date( int(splitting2[0]) , int(splitting2[1]) ,int(splitting2[2]))
            edad= int(self.days_between(d1,d2)/365)
        except:
            self.showPopUp("errorDatos")
            return
        
        try:
            connection = psycopg2.connect(user="bdi2018f",password="bdi2018f",host="bdd.inf.udec.cl",database="bdi2018f",port=5432)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM ing.persona AS p WHERE p.rut = %s" ,(rut,))
            lista = cursor.fetchall()
            if len(lista) == 0:
                cursor.execute("INSERT INTO ing.persona (rut,nombres,apellidos) VALUES (%s,%s,%s)",(rut,nombre,apellidos,))
                print("Persona ingresada")
                connection.commit()
            else:
                print("Persona ya en base")
            cursor.execute("SELECT * FROM ing.paciente AS p WHERE p.rut = %s",(rut,))
            lista = cursor.fetchall()
            if len(lista) == 0:
                cursor.execute("INSERT INTO ing.paciente (rut,prevision,tramo,fecha_nac,edad) VALUES (%s,%s,%s,%s,%s)",(rut,prevSocial,tramo,fecha,edad,))
                connection.commit()
                self.showPopUp("ingresoCorrecto")
                print("Paciente ingresado")
                nombreCompleto = nombre+" "+apellidos
                self.openCheck(rut,nombreCompleto,fecha,edad,prevSocial,tramo)
                
            else:
                print("paciente ya en base")
                self.showPopUp("PacienteYaIngresado")
        except Exception as e:
            self.showPopUp("errorconexion")
"""
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    loginFrame = Ui_IngresarPaciente()
    loginFrame.setupUi(win)
    win.show()
    sys.exit(app.exec_())
"""





