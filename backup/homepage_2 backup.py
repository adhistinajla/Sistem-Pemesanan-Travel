import os, sys, csv, res_home, tiket
import login_new
import pandas as pd

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QDateEdit, QPushButton, QMessageBox, QDialog, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QObject, pyqtSignal


class SignalEmitter(QObject):
    # Define the search_signal
    search_signal = QtCore.pyqtSignal(str)


class Ui_Form(object):
    search_signal = QtCore.pyqtSignal(str)

    def __init__(self, username):
        super().__init__()  # Modify to accept username parameter  # Callback function to pass search results
        self.username = username
        self.signal_emitter = SignalEmitter()  # Store the received username

    def setupUi(self, Form):
        try:
            # Assuming the username is in the first column and the phone number is in the second column
            user_data = pd.read_csv('data/user_data.csv', header=None, index_col=0)
            if self.username in user_data.index:
                self.phone_number = user_data.loc[self.username].iloc[0]  # Assuming phone number is in the second column
            else:
                self.phone_number = ""  # Set phone number to empty string if username is not found
        except Exception as e:
            print(f"Error reading user_data.csv file: {e}")

        Form.setObjectName("Form")
        Form.resize(1920, 1080)
        self.bgatas = QtWidgets.QLabel(Form)
        self.bgatas.setEnabled(True)
        self.bgatas.setGeometry(QtCore.QRect(0, 0, 1920, 433))
        self.bgatas.setStyleSheet("image: url(:/images/img/atas.png);")
        self.bgatas.setText("")
        self.bgatas.setObjectName("bgatas")
        self.platform = QtWidgets.QLabel(Form)
        self.platform.setGeometry(QtCore.QRect(250, 227, 1420, 149))
        self.platform.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-color: rgb(213, 213, 213);\n"
                                    "border-radius:40px;\n"
                                    "border-style: solid;\n"
                                    "border-width: 1px;")
        self.platform.setText("")
        self.platform.setObjectName("platform")
        self.berangkat = QtWidgets.QComboBox(Form)
        self.berangkat.setGeometry(QtCore.QRect(364, 290, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Epilogue")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.berangkat.setFont(font)
        self.berangkat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.berangkat.setStyleSheet("/*style for the QComboBox*/\n"
                                     "#berangkat{\n"
                                     "    border-radius:20px;\n"
                                     "\n"
                                     "    background-color: rgba(255, 255, 255, 0);\n"
                                     "}\n"
                                     "\n"
                                     "#berangkat::drop-down{\n"
                                     "    border:0px;\n"
                                     "}\n"
                                     "\n"
                                     "#berangkat:down-arrow{\n"
                                     "    width: 15px;\n"
                                     "    height: 15px;\n"
                                     "    margin-right: 15px\n"
                                     "}")
        self.berangkat.setInputMethodHints(QtCore.Qt.ImhNone)
        self.berangkat.setDuplicatesEnabled(False)
        self.berangkat.setObjectName("berangkat")
        destinations = self.get_destinations('data/keberangkatan.csv')
        self.berangkat.addItems(destinations)
        self.berangkat.setCurrentText('Jogja')

        self.tujuan = QtWidgets.QComboBox(Form)
        self.tujuan.setGeometry(QtCore.QRect(744, 290, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Epilogue")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.tujuan.setFont(font)
        self.tujuan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tujuan.setStyleSheet("/*style for the QComboBox*/\n"
                                  "#tujuan{\n"
                                  "    border-radius:20px;\n"
                                  "\n"
                                  "    background-color: rgba(255, 255, 255, 0);\n"
                                  "}\n"
                                  "\n"
                                  "#tujuan::drop-down{\n"
                                  "    border:0px;\n"
                                  "}\n"
                                  "\n"
                                  "#tujuan:down-arrow{\n"
                                  "    width: 15px;\n"
                                  "    height: 15px;\n"
                                  "    margin-right: 15px\n"
                                  "}")
        self.tujuan.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tujuan.setDuplicatesEnabled(False)
        self.tujuan.setObjectName("tujuan")
        destinations = self.get_destinations('data/tujuan.csv')
        self.tujuan.addItems(destinations)
        self.tujuan.setCurrentText('Surakarta')

        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(1130, 298, 189, 31))
        self.dateEdit.setCalendarPopup(True)
        font = QtGui.QFont()
        font.setFamily("Epilogue")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("QDateEdit {\n"
                                    " border-radius: 2px; border: 0px solid #cccccc; \n"
                                    "background-color: rgba(255, 255, 255, 0);\n"
                                    "\n"
                                    "}\n"
                                    "\n"
                                    "QDateEdit::drop-down { border: none; width: 30px;\n"
                                    "background-color: rgba(255, 255, 255, 0);\n"
                                    "\n"
                                    " }\n"
                                    "\n"
                                    "QDateEdit::down-button {border: none; \n"
                                    "background-color: rgba(255, 255, 255, 0);\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "QDateEdit::up-button {border: none; \n"
                                    "background-color: rgba(255, 255, 255, 0);\n"
                                    "}")
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        qdate = QtCore.QDate.currentDate()
        qdate.setDate(2024, 1, 1)
        self.dateEdit.setDate(qdate)

        self.cari = QtWidgets.QPushButton(Form)
        self.cari.setGeometry(QtCore.QRect(1420, 246, 221, 111))
        font = QtGui.QFont()
        font.setFamily("Epilogue")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        
        self.cari.setFont(font)
        self.cari.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cari.setStyleSheet("QPushButton#cari{\n"
                                "background-color: #2abaa1;\n"
                                "color: rgb(255, 255, 255);\n"
                                "padding: 0px 20px;\n"
                                "border-radius: 32px;\n"
                                "}\n"
                                "\n"
                                "QPushButton#cari:pressed{\n"
                                "background-color: #219a85;\n"
                                "}\n"
                                "\n"
                                "")
        self.cari.setObjectName("cari")

        self.bgberangkat = QtWidgets.QLabel(Form)
        self.bgberangkat.setGeometry(QtCore.QRect(280, 232, 361, 140))
        self.bgberangkat.setStyleSheet(
            "image: url(:/images/img/berangkat dari.png);")
        self.bgberangkat.setText("")
        self.bgberangkat.setObjectName("bgberangkat")
        self.bgtujuan = QtWidgets.QLabel(Form)
        self.bgtujuan.setGeometry(QtCore.QRect(660, 232, 361, 140))
        self.bgtujuan.setStyleSheet(
            "image: url(:/images/img/untuk tujuan.png);")
        self.bgtujuan.setText("")
        self.bgtujuan.setObjectName("bgtujuan")
        self.bgtujuan_2 = QtWidgets.QLabel(Form)
        self.bgtujuan_2.setGeometry(QtCore.QRect(1040, 232, 361, 140))
        self.bgtujuan_2.setStyleSheet(
            "image: url(:/images/img/tanggal berangkat.png);")
        self.bgtujuan_2.setText("")
        self.bgtujuan_2.setObjectName("bgtujuan_2")
        self.ads1 = QtWidgets.QLabel(Form)
        self.ads1.setGeometry(QtCore.QRect(250, 490, 621, 351))
        self.ads1.setStyleSheet("image: url(:/images/img/ads1.png);")
        self.ads1.setText("")
        self.ads1.setObjectName("ads1")
        self.ads1_dummy_button = QtWidgets.QPushButton(Form)
        self.ads1_dummy_button.setGeometry(QtCore.QRect(251, 497, 621, 336))
        self.ads1_dummy_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ads1_dummy_button.setStyleSheet("QPushButton#ads1_dummy_button{\n"
                                             "background-color: rgba(0, 0, 0, 0);\n"
                                             "padding: 0px 20px;\n"
                                             "border-radius: 32px;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton#ads1_dummy_button:pressed{\n"
                                             "background-color: rgba(0, 0, 0, 30);\n"
                                             "}\n"
                                             "\n"
                                             "")
        self.ads1_dummy_button.setText("")
        self.ads1_dummy_button.setObjectName("ads1_dummy_button")
        self.ads1_dummy_button.clicked.connect(self.set_destination_bali)

        self.ads2 = QtWidgets.QLabel(Form)
        self.ads2.setGeometry(QtCore.QRect(900, 490, 771, 351))
        self.ads2.setStyleSheet("image: url(:/images/img/ads2.png);")
        self.ads2.setText("")
        self.ads2.setObjectName("ads2")
        self.ads2_dummy_button = QtWidgets.QPushButton(Form)
        self.ads2_dummy_button.setGeometry(QtCore.QRect(898, 497, 771, 336))
        self.ads2_dummy_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ads2_dummy_button.setStyleSheet("QPushButton#ads2_dummy_button{\n"
                                             "background-color: rgba(0, 0, 0, 0);\n"
                                             "padding: 0px 20px;\n"
                                             "border-radius: 32px;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton#ads2_dummy_button:pressed{\n"
                                             "background-color: rgba(0, 0, 0, 30);\n"
                                             "}\n"
                                             "\n"
                                             "")
        self.ads2_dummy_button.setText("")
        self.ads2_dummy_button.setObjectName("ads2_dummy_button")
        self.bgpolos = QtWidgets.QLabel(Form)
        self.bgpolos.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.bgpolos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bgpolos.setText("")
        self.bgpolos.setObjectName("bgpolos")
        self.tanggal = QtWidgets.QLabel(Form)
        self.tanggal.setGeometry(QtCore.QRect(240, 660, 1431, 681))
        self.tanggal.setStyleSheet("image: url(:/images/img/jadwal.png);")
        self.tanggal.setText("")
        self.tanggal.setObjectName("tanggal")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(1345, 64, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Epilogue SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight)
        self.label.setStyleSheet("QLabel{\n"
                                 "color: white;\n"
                                 "font: 63 12pt \"Epilogue SemiBold\";\n"
                                 "text-align:right;\n"
                                 "}")
        self.label.setObjectName("label")

        self.profil = QtWidgets.QPushButton(Form)
        self.profil.setGeometry(QtCore.QRect(1620, 55, 50, 50))
        self.profil.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.profil.setStyleSheet("border-image: url(:/images/img/pp_profil.png);")
        self.profil.setText("")
        self.profil.setObjectName("profil")
        self.profil.clicked.connect(self.show_profile_popup)

        self.bgpolos.raise_()
        self.bgatas.raise_()
        self.platform.raise_()
        self.ads1.raise_()
        self.ads1_dummy_button.raise_()
        self.ads2.raise_()
        self.ads2_dummy_button.raise_()
        self.tanggal.raise_()
        self.bgberangkat.raise_()
        self.bgtujuan.raise_()
        self.tujuan.raise_()
        self.bgtujuan_2.raise_()
        self.berangkat.raise_()
        self.cari.raise_()
        self.dateEdit.raise_()
        self.label.raise_()
        self.profil.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Connect the search button to the search function
        self.cari.clicked.connect(self.display_selection)
        self.destinations_df = pd.read_excel('data/data_destinasi.xlsx')
        self.user_data = pd.read_csv('data/user_data.csv', header=None)

        current_dir = os.path.dirname(os.path.realpath(__file__))
        self.csv_file_path = os.path.join(current_dir, 'data/user_data.csv')
        self.user_data = pd.read_csv(self.csv_file_path, header=None)
        self.display_username()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Homepage 2"))
        self.cari.setText(_translate("Form", "Cari"))
        self.label.setText(_translate("Form", "User"))

    def display_selection(self):
        departure = self.berangkat.currentText()
        destination = self.tujuan.currentText()
        date = self.dateEdit.date().toString("yyyy-MM-dd")

        if not departure or not destination or not date:
            QMessageBox.warning(None, "Peringatan", "Mohon pilih semua kolom.")
            return

        if departure == destination:
            QMessageBox.critical(None, "Kesalahan",
                                 "Mohon maaf, destinasi tujuan tidak bisa sama dengan destinasi keberangkatan Anda.")
            return

        # Filter the dataframe based on selection
        filtered_df = self.destinations_df[
            (self.destinations_df['Keberangkatan'] == departure) &
            (self.destinations_df['Tujuan'] == destination) &
            (self.destinations_df['Tanggal'] == date)
            ]

        if filtered_df.empty:
            QMessageBox.information(None, "Hasil Pencarian",
                                    "Tidak ada jadwal yang sesuai dengan "
                                    "pilihan Anda.")
        else:
            self.open_ticket_result(departure, destination, date)

    def get_destinations(self, filename):
        destinations = []
        try:
            with open(filename, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    destinations.append(row['nama_kota'])
        except Exception as e:
            print(f"Error reading CSV file: {e}")
        return destinations

    def display_username(self):
        # Modify to display the received username
        self.label.setText(self.username)

    def open_ticket_result(self, departure, destination, date):  # Modify to accept username parameter
        self.tiket_window = QtWidgets.QWidget()
        self.ui = tiket.Ui_Form(self.username, departure, destination, date)  # Pass the username to homepage_2.Ui_Form
        self.ui.setupUi(self.tiket_window)
        self.tiket_window.show()
        QtWidgets.QApplication.instance().activeWindow().close()

    def open_login(self):
        self.login_new_window = QtWidgets.QWidget()
        self.ui = login_new.Ui_Form()
        self.ui.setupUi(self.login_new_window)
        self.login_new_window.show()
        QtWidgets.QApplication.instance().activeWindow().close()

    def show_profile_popup(self):
        message = QMessageBox()
        message.setWindowTitle("Profile")
        message.setIcon(QMessageBox.Information)
        message.setText(f"Nama                   : {self.username}\nNomor Telepon    : {self.phone_number}")
        message.addButton(QMessageBox.Ok)
        logout_button = message.addButton("Logout", QMessageBox.RejectRole)
        
        message.exec_()
        
        if message.clickedButton() == logout_button:
            self.open_login()

    def set_destination_bali(self):
        self.tujuan.setCurrentText("Bali")
        QMessageBox.information(None, "Informasi", "Tujuan telah diset ke Bali.")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form_homepage = QtWidgets.QWidget()
    Form_homepage.setWindowIcon(QIcon('img/icon.png'))

    # Buat instance dari homepage
    ui_homepage = Ui_Form(object)
    ui_homepage.setupUi(Form_homepage)

    # ...

    Form_homepage.show()
    ui_homepage.display_username()

    sys.exit(app.exec_())  # Remove this line