import csv
import homepage_2
import login_new
import sys
import res_register

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtWidgets import QLineEdit, QMessageBox


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1080)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label.setStyleSheet("image: url(:/images/img/register_bg.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.password = QtWidgets.QLineEdit(Form)
        
        self.password.setGeometry(QtCore.QRect(1074, 570, 482, 71))
        font = QtGui.QFont()
        font.setFamily("Epilogue")
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setStyleSheet("background-color: #e1ecfe;\n"
                                        "padding: 0px 40px;\n"
                                        "border-radius: 35px;")
        self.password.setInputMask("")
        self.password.setText("")
        self.password.setObjectName("password")

        self.login_aja = QtWidgets.QPushButton(Form)
        self.login_aja.clicked.connect(self.open_login)
        self.login_aja.setGeometry(QtCore.QRect(1213, 793, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Epilogue")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.login_aja.setFont(font)
        self.login_aja.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_aja.setStyleSheet("QPushButton#daftar_dulu{\n"
                                        "background-color: argb(255, 255, 255, 0 );\n"
                                        "color: rgb(42, 186, 161);\n"
                                        "border-radius: 15px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton#daftar_dulu:hover{\n"
                                        "color: rgb(36, 162, 139);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton#daftar_dulu:pressed{\n"
                                        "color: rgb(36, 162, 139);\n"
                                        "}\n"
                                        "\n"
                                        "")
        self.login_aja.setObjectName("daftar_dulu")

        self.nomor_telepon = QtWidgets.QLineEdit(Form)
        self.nomor_telepon.setGeometry(QtCore.QRect(1074, 391, 482, 71))
        font = QtGui.QFont()
        font.setFamily("Epilogue")
        font.setPointSize(12)
        self.nomor_telepon.setFont(font)
        self.nomor_telepon.setStyleSheet("background-color: #e1ecfe;\n"
                                                "padding: 0px 40px;\n"
                                                "border-radius: 35px;")
        self.nomor_telepon.setInputMask("")
        self.nomor_telepon.setText("")
        self.nomor_telepon.setObjectName("nomort_telepon")
        self.nomor_telepon.setMaxLength(15)  # Adjust the maximum length as needed
        reg_ex = QRegExp("[0-9]*")
        input_validator = QRegExpValidator(reg_ex, self.nomor_telepon)
        self.nomor_telepon.setValidator(input_validator)

        self.register = QtWidgets.QPushButton(Form)
        self.register.clicked.connect(self.check_register)
        self.register.setEnabled(True)
        self.register.setGeometry(QtCore.QRect(1074, 687, 482, 71))
        font = QtGui.QFont()
        font.setFamily("Epilogue")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.register.setFont(font)
        self.register.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.register.setAutoFillBackground(False)
        self.register.setStyleSheet("QPushButton#register{\n"
                                "background-color: #e6fe52;\n"
                                "padding: 10px 40px;\n"
                                "border-radius: 35px;\n"
                                "}\n"
                                "\n"
                                "QPushButton#register:hover{\n"
                                "background-color: #eaff69;\n"
                                "}\n"
                                "\n"
                                "QPushButton#register:pressed{\n"
                                "background-color: #c8dd44;\n"
                                "}\n"
                                "\n"
                                "")
        self.register.setObjectName("register")

        self.nama = QtWidgets.QLineEdit(Form)
        self.nama.setGeometry(QtCore.QRect(1074, 482, 482, 71))
        font = QtGui.QFont()
        font.setFamily("Epilogue")
        font.setPointSize(12)
        self.nama.setFont(font)
        self.nama.setStyleSheet("background-color: #e1ecfe;\n"
                                "padding: 0px 40px;\n"
                                "border-radius: 35px;")
        self.nama.setInputMask("")
        self.nama.setText("")
        self.nama.setObjectName("nomort_telepon")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.password.setPlaceholderText(_translate("Form", "Password"))
        self.login_aja.setText(_translate("Form", "Login Aja"))
        self.nomor_telepon.setPlaceholderText(_translate("Form", "Nomor Telepon"))
        self.register.setText(_translate("Form", "Register"))
        self.nama.setPlaceholderText(_translate("Form", "Nama"))

    def check_register(self):
        if not self.nama.text() or not self.nomor_telepon.text() or not self.password.text():
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Semua Isian tidak boleh kosong!")
                msg.setWindowTitle("Error Cok")
                msg.exec_()
        else:
        # Continue with your logic here if both fields are not empty
                username = self.nama.text()
                phone_number = self.nomor_telepon.text()
                password = self.password.text()

                with open('data/user_data.csv', 'r') as file:
                        reader = csv.reader(file)
                        for row in reader:
                                if username == row[0]:
                                        msg = QMessageBox()
                                        msg.setIcon(QMessageBox.Warning)
                                        msg.setText("Username sudah ada!\nSilakan masukkan Username yang berbeda.")
                                        msg.setWindowTitle("Peringatan")
                                        msg.exec_()
                                        return
                                elif phone_number == row[1]:
                                        msg = QMessageBox()
                                        msg.setIcon(QMessageBox.Warning)
                                        msg.setText("Nomor Telepon sudah ada!\nSilakan masukkan Nomor Telepon yang berbeda.")
                                        msg.setWindowTitle("Peringatan")
                                        msg.exec_()
                                        return

        # If user data does not exist, save it
                with open('data/user_data.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([username, phone_number, password])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Data telah tersimpan!\nSilakan kembali ke menu login untuk masuk")
                msg.setWindowTitle("Informasi")
                msg.exec_()

                self.open_login()

    def open_login(self):
        self.login_new_window = QtWidgets.QWidget()
        self.ui = login_new.Ui_Form()
        self.ui.setupUi(self.login_new_window)
        self.login_new_window.show()
        QtWidgets.QApplication.instance().activeWindow().close()

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        Form.setWindowIcon(QIcon('img/icon.png'))
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())
