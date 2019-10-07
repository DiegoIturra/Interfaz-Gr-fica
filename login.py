from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QMessageBox
import psycopg2
from Medic import Ui_InfoPaciente
from Sanitar import Ui_InfoPacienteS
from AsignarCama3 import Ui_AsignarCama

"""
clase que administra el login de usuario
"""


class LoginWindow(object):
        # establecer parametro inciales del frame login
        
        
    def openMedicWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_InfoPaciente(str(self.user))
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    
    def openSanitariosWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_InfoPacienteS()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def openAdminWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AsignarCama()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    
    def setParametersLoginWindow(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(583, 370)
        # deshabilitar botones min/max
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.userTextEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.userTextEdit.setGeometry(QtCore.QRect(160, 100, 331, 31))
        self.userTextEdit.setObjectName("userTextEdit")
        # self.userTextEdit.textChanged.connect(self.__enableLoginButton)
        self.passTextEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passTextEdit.setGeometry(QtCore.QRect(160, 170, 331, 31))
        self.passTextEdit.setObjectName("passTextEdit")
        self.passTextEdit.setEchoMode(QLineEdit.Password)
        self.userLabel = QtWidgets.QLabel(self.centralwidget)
        self.userLabel.setGeometry(QtCore.QRect(60, 100, 67, 22))
        self.userLabel.setObjectName("userLabel")
        self.passLabel = QtWidgets.QLabel(self.centralwidget)
        self.passLabel.setGeometry(QtCore.QRect(60, 170, 67, 22))
        self.passLabel.setObjectName("passLabel")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(250, 250, 103, 34))
        self.loginButton.setObjectName("loginButton")
        # self.loginButton.setEnabled(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 583, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # usar boton login(agregar login mas tarde)
        self.loginButton.clicked.connect(self.loginConnect)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    """
    obtener usuario y password para enviarlo a la base de datos
    """

    def loginConnect(self):
        # obtiene el nombre de usuario y password
        self.user = self.userTextEdit.text()
        passText = self.passTextEdit.text()
        nombres = None
        apellidos = None
        especialidad = None
        cargo = None
        try:
            connection = psycopg2.connect(
                user="bdi2018f", password="bdi2018f", host="bdd.inf.udec.cl", database="bdi2018f", port=5432)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM ing.usuario AS us, ing.administrativo as ad, ing.persona as p WHERE p.rut = ad.rut and  us.nombre = %s and us.contrasena = %s and ad.rut = us.nombre and p.rut = ad.rut", (self.user, passText,))
            userList = cursor.fetchall()

            if len(userList) == 1:
                # pasa a admin
                nombres = str(userList[0][4])
                apellidos = str(userList[0][5])
                print(userList)
                #mostrar ventana administrador
                self.openAdminWindow()
            else:
                cursor.execute(
                    "SELECT * FROM ing.usuario AS us, ing.sanitario as san, ing.persona as p WHERE p.rut = san.rut and us.nombre = %s and us.contrasena = %s and san.rut = us.nombre", (self.user, passText,))
                sanitarios = cursor.fetchall()
                if len(sanitarios) == 1:
                    especialidad = str(sanitarios[0][3])
                    nombres = str(sanitarios[0][5])
                    apellidos = str(sanitarios[0][6])
                    print(especialidad)
                    print(nombres)
                    print(apellidos)
                    if especialidad == "medico":
                        """
                        self.__showMedicWindow(
                            nombres, apellidos, especialidad)"""
                        self.openMedicWindow()
                    elif especialidad == "enfermero" or especialidad == "auxiliar de enfermeria" or especialidad == "paramedico":
                        self.openSanitariosWindow()
            cursor.close()
            connection.close()
        except Exception as e:
            print("fallo en la conexion")
            print(e)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inicio de sesión"))
        self.userLabel.setText(_translate("MainWindow", "Usuario"))
        self.passLabel.setText(_translate("MainWindow", "Contraseña"))
        self.loginButton.setText(_translate("MainWindow", "Iniciar sesión"))


# main correcto
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    loginFrame = LoginWindow()
    loginFrame.setParametersLoginWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
