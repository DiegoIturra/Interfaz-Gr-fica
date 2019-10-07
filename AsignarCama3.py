from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import psycopg2


class Ui_AsignarCama(object):
    def setupUi(self, MainWindow):
    	#pressed = False
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        self.pressed = False
        self.rut = ""
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(275, 0, 300, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.titulo.setFont(font) 
        self.titulo.setObjectName("titulo")
        self.nombrePaciente = QtWidgets.QLabel(self.centralwidget)
        self.nombrePaciente.setGeometry(QtCore.QRect(60, 80, 51, 31))
        self.nombrePaciente.setObjectName("nombrePaciente")
        self.edadPaciente = QtWidgets.QLabel(self.centralwidget)
        self.edadPaciente.setGeometry(QtCore.QRect(60, 230, 41, 31))
        self.edadPaciente.setObjectName("edadPaciente")
        self.tramo = QtWidgets.QLabel(self.centralwidget)
        self.tramo.setGeometry(QtCore.QRect(60, 330, 47, 31))
        self.tramo.setObjectName("tramo")
        self.fechaNacimiento = QtWidgets.QLabel(self.centralwidget)
        self.fechaNacimiento.setGeometry(QtCore.QRect(60, 180, 101, 31))
        self.fechaNacimiento.setObjectName("fechaNacimiento")
        self.prevSocial = QtWidgets.QLabel(self.centralwidget)
        self.prevSocial.setGeometry(QtCore.QRect(60, 280, 81, 31))
        self.prevSocial.setObjectName("prevSocial")
        self.rutPaciente = QtWidgets.QLabel(self.centralwidget)
        self.rutPaciente.setGeometry(QtCore.QRect(60, 130, 31, 31))
        self.rutPaciente.setObjectName("rutPaciente")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(365, 70, 301, 381))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.outputNombre = QtWidgets.QLabel(self.centralwidget)
        self.outputNombre.setGeometry(QtCore.QRect(116, 80, 241, 31))
        self.outputNombre.setText("")
        self.outputNombre.setObjectName("outputNombre")
        self.outputRut = QtWidgets.QLabel(self.centralwidget)
        self.outputRut.setGeometry(QtCore.QRect(116, 130, 231, 31))
        self.outputRut.setText("")
        self.outputRut.setObjectName("outputRut")
        self.outputFechaNac = QtWidgets.QLabel(self.centralwidget)
        self.outputFechaNac.setGeometry(QtCore.QRect(190, 182, 151, 31))
        self.outputFechaNac.setText("")
        self.outputFechaNac.setObjectName("outputFechaNac")
        self.outputEdad = QtWidgets.QLabel(self.centralwidget)
        self.outputEdad.setGeometry(QtCore.QRect(110, 232, 141, 31))
        self.outputEdad.setText("")
        self.outputEdad.setObjectName("outputEdad")
        self.outputPrevSocial = QtWidgets.QLabel(self.centralwidget)
        self.outputPrevSocial.setGeometry(QtCore.QRect(170, 282, 171, 31))
        self.outputPrevSocial.setText("")
        self.outputPrevSocial.setObjectName("outputPrevSocial")
        self.outputTramo = QtWidgets.QLabel(self.centralwidget)
        self.outputTramo.setGeometry(QtCore.QRect(130, 333, 111, 31))
        self.outputTramo.setText("")
        self.outputTramo.setObjectName("outputTramo")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 410, 81, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 30, 231, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 30, 75, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.setInfo)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.mostrarSalas(self.tableWidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Asignación de cama"))
        self.titulo.setText(_translate("MainWindow", "Asignar cama"))
        self.nombrePaciente.setText(_translate("MainWindow", "Nombre:"))
        self.edadPaciente.setText(_translate("MainWindow", "Edad:"))
        self.tramo.setText(_translate("MainWindow", "Tramo:"))
        self.fechaNacimiento.setText(_translate("MainWindow", "Fecha de nacimiento:"))
        self.prevSocial.setText(_translate("MainWindow", "Previsión social:"))
        self.rutPaciente.setText(_translate("MainWindow", "Rut:"))
        self.pushButton.setText(_translate("MainWindow", "Asignar"))
        self.pushButton_2.setText(_translate("MainWindow", "Buscar"))
        
    def mostrarSalas(self, tableWidget):
        try:
            connection = psycopg2.connect(user="bdi2018f",password="bdi2018f",host="bdd.inf.udec.cl",database="bdi2018f",port=5432)
            cursor = connection.cursor()
            cursor.execute("SELECT c.id_cama, c.disponibilidad, ic.piso, ic.sala, ic.numero " 
                + "FROM ing.cama AS c, ing.info_cama AS ic WHERE c.id_cama = ic.id_cama ORDER BY ic.piso ASC")
            #formato de salida: (id, disponibilidad, piso, sala, numero)
            salas = cursor.fetchall()
            tableWidget.setColumnCount(5)
            tableWidget.setRowCount(len(salas))
            tableWidget.setHorizontalHeaderLabels(["", "Disponibilidad","Número", "Sala", "Piso"])
            tableWidget.verticalHeader().setVisible(False)
            tableWidget.resizeColumnToContents(0)
            tableWidget.resizeColumnToContents(1)
            tableWidget.resizeColumnToContents(2)
            tableWidget.resizeColumnToContents(3)
            tableWidget.resizeColumnToContents(4)
            c = 0
            group = QButtonGroup()
            btn = []
            for i in range(len(salas)):
                btn.append(QtWidgets.QRadioButton(""))
                group.addButton(btn[i])
                group.setId(btn[i], i)
                if salas[i][1] == False:
                	btn[i].setEnabled(False)
                btn[i].clicked.connect(lambda: self.botonPresionado(group, salas))
            for i in range(len(salas)):
                tableWidget.setCellWidget(c,0, btn[i])
                if(salas[c][1] == True):
                    tableWidget.setItem(c, 1, QtWidgets.QTableWidgetItem("Disponible"))
                else:
                    tableWidget.setItem(c, 1, QtWidgets.QTableWidgetItem("No disponible"))
                tableWidget.setItem(c, 2, QtWidgets.QTableWidgetItem(str(salas[c][4])))
                tableWidget.setItem(c, 3, QtWidgets.QTableWidgetItem(str(salas[c][3])))
                tableWidget.setItem(c, 4, QtWidgets.QTableWidgetItem(str(salas[c][2])))
                c = c+ 1
            cursor.close()
            connection.close()
        except Exception as e:
            print(e)

    def botonPresionado(self, group, salas):
        self.fila = group.checkedId()
        self.item = [salas[self.fila][0], salas[self.fila][1], salas[self.fila][2], salas[self.fila][3], salas[self.fila][4]]
        if self.pressed == True:
            try:
                connection = psycopg2.connect(user="bdi2018f",password="bdi2018f",host="bdd.inf.udec.cl",database="bdi2018f",port=5432)
                cursor = connection.cursor()
                cursor.execute("SELECT c.id_cama, c.disponibilidad, ic.piso, ic.sala, ic.numero " 
                    + "FROM ing.cama AS c, ing.info_cama AS ic WHERE c.id_cama = ic.id_cama AND c.id_cama = %s", (self.item[0],))
                lista = cursor.fetchall()
                print(lista)
                if len(lista) == 1:
                	self.pushButton.clicked.connect(self.asignarCama)

                cursor.close()
                connection.close()
            except Exception as e:
                print(e)

    def asignarCama(self):
    	try:
    		connection = psycopg2.connect(user="bdi2018f",password="bdi2018f",host="bdd.inf.udec.cl",database="bdi2018f",port=5432)
    		cursor = connection.cursor()
    		#cursor.execute("INSERT INTO ing.cama_persona (rut,id_cama) VALUES (%s,%s)",(self.rut,self.item[0],))
    		cursor.execute("INSERT INTO ing.cama_paciente (rut, id_cama) VALUES (%s, %s)", (self.rut, self.item[0],))
    		cursor.execute("UPDATE ing.cama SET disponibilidad = False WHERE id_cama = %s", (self.item[0],))
    		cursor.close()
    		connection.commit()
    	except Exception as e:
    		print(e)

    def setInfo(self):
        self.rut = self.lineEdit.text()
        try:
            connection = psycopg2.connect(user="bdi2018f",password="bdi2018f",host="bdd.inf.udec.cl",database="bdi2018f",port=5432)
            cursor = connection.cursor()
            cursor.execute("SELECT p.prevision, p.tramo, p.edad, p.fecha_nac FROM ing.paciente AS p WHERE p.rut = %s",(self.rut,))
            lista1 = cursor.fetchall()
            cursor.execute("SELECT p.nombres, p.apellidos FROM ing.persona AS p WHERE p.rut = %s",(self.rut,))
            lista2 = cursor.fetchall()
            print(lista1)
            print(lista2)
            prevSo= str(lista1[0][0])
            tramo= str(lista1[0][1])
            edad= str(lista1[0][2])
            fecha= str(lista1[0][3])
            name = str(lista2[0][0]) +" "+str(lista2[0][1])
                
            if(tramo == "None" or len(tramo) == 0):
                tramo = "No aplica"
            self.outputNombre.setText(name)
            self.outputPrevSocial.setText(prevSo)
            self.outputTramo.setText(tramo)
            self.outputEdad.setText(edad)
            self.outputFechaNac.setText(fecha)
            self.outputRut.setText(self.rut)
            self.pressed = True
            cursor.close()
            connection.close()
        except Exception as e:
            print(e)

""""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AsignarCama()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
"""
