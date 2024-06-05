import csv
import homepage_2
import register_new
import sys
import res_login

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtWidgets import QLineEdit, QMessageBox


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1920, 1080)
        Form.setWindowIcon(QIcon('img/icon.png'))

        self.bg = QtWidgets.QLabel(Form)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.bg.setStyleSheet("image: url(:/images/img/bg_login.png);")
        self.bg.setText("")
        self.bg.setObjectName("bg")

        self.nomort_telepon = QtWidgets.QLineEdit(Form)
        self.nomort_telepon.setGeometry(QtCore.QRect(1074, 411, 482, 71))
        font = QtGui.QFont()
        font.setFamily("Epilogue")
        font.setPointSize(12)
        self.nomort_telepon.setFont(font)
        self.nomort_telepon.setStyleSheet("background-color: #e1ecfe;\n"
                                          "padding: 0px 40px;\n"
                                          "border-radius: 35px;")
        self.nomort_telepon.setPlaceholderText("Nomor Telepon")
        self.nomort_telepon.setObjectName("nomort_telepon")

        # Set maximum length and numeric input only for nomort_telepon
        self.nomort_telepon.setMaxLength(15)  # Adjust the maximum length as needed
        reg_ex = QRegExp("[0-9]*")
        input_validator = QRegExpValidator(reg_ex, self.nomort_telepon)
        self.nomort_telepon.setValidator(input_validator)

        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(1074, 500, 482, 71))
        self.password.setFont(font)
        self.password.setStyleSheet("background-color: #e1ecfe;\n"
                                    "padding: 0px 40px;\n"
                                    "border-radius: 35px;")
        self.password.setPlaceholderText("Password")
        self.password.setObjectName("password")
        self.password.setEchoMode(QLineEdit.Password)

        self.login = QtWidgets.QPushButton(Form)
        self.login.setGeometry(QtCore.QRect(1074, 630, 482, 71))
        font.setPointSize(13)
        font.setBold(True)
        self.login.setFont(font)
        self.login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login.setStyleSheet("QPushButton#login{\n"
                                 "background-color: #e6fe52;\n"
                                 "padding: 10px 40px;\n"
                                 "border-radius: 35px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#login:hover{\n"
                                 "background-color: #eaff69;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#login:pressed{\n"
                                 "background-color: #c8dd44;\n"
                                 "}\n")
        self.login.setObjectName("login")
        self.login.setText("Login")

        self.daftar_dulu = QtWidgets.QPushButton(Form)
        self.daftar_dulu.setGeometry(QtCore.QRect(1219, 793, 161, 31))
        font.setPointSize(10)
        font.setItalic(True)
        self.daftar_dulu.setFont(font)
        self.daftar_dulu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.daftar_dulu.setStyleSheet("QPushButton#daftar_dulu{\n"
                                       "background-color: argb(255, 255, 255, 0 );\n"
                                       "color: rgb(42, 186, 161);\n"
                                       "border-radius: 15px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#daftar_dulu:hover{\n"
                                       "color: argb(45, 202, 173);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#daftar_dulu:pressed{\n"
                                       "color: argb(38, 171, 147);\n"
                                       "}\n")
        self.daftar_dulu.setObjectName("daftar_dulu")
        self.daftar_dulu.setText("Daftar Dulu Yuk")

        self.bg.raise_()
        self.nomort_telepon.raise_()
        self.password.raise_()
        self.login.raise_()
        self.daftar_dulu.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Connect login button to the check_login function
        self.login.clicked.connect(self.check_login)
        # Connect register button to the open_register function
        self.daftar_dulu.clicked.connect(self.open_register)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))

    def check_login(self):
        phone_number = self.nomort_telepon.text()
        password = self.password.text()

        if not phone_number or not password:
                QMessageBox.warning(None, "Input Error", "Nomor Telepon dan Password harus diisi!")
                return

    # Check credentials against the CSV file
        user_found = False
        username = None  # Initialize username variable
        try:
                with open('data/user_data.csv', mode='r') as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                                if row['nomor_telepon'] == phone_number and row['password'] == password:
                                        user_found = True
                                        username = row['username']  # Fetch the username
                                        break
        except FileNotFoundError:
                QMessageBox.critical(None, "File Error", "Database file not found!")
                return

        if user_found:
                QMessageBox.information(None, "Login Successful", "Login berhasil!")
                self.open_homepage(username)  # Pass the username to open_homepage
        else:
                QMessageBox.warning(None, "Login Failed", "Nomor Telepon atau Password salah!")

    def open_homepage(self, username):  # Modify to accept username parameter
        self.homepage_window = QtWidgets.QWidget()
        self.ui = homepage_2.Ui_Form(username)  # Pass the username to homepage_2.Ui_Form
        self.ui.setupUi(self.homepage_window)
        self.homepage_window.show()
        QtWidgets.QApplication.instance().activeWindow().close()

    def open_register(self):
        self.register_new_window = QtWidgets.QWidget()
        self.ui = register_new.Ui_Form()
        self.ui.setupUi(self.register_new_window)
        self.register_new_window.show()
        QtWidgets.QApplication.instance().activeWindow().close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
