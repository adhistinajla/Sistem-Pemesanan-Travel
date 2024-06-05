import pandas as pd
import sys
import homepage_2
import res_tiket

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QMainWindow, \
    QScrollArea, QVBoxLayout
from PyQt5.QtGui import QIcon

import seat
from common import error_message, qfont


class Ui_Form(object):
    def __init__(self, username, departure, destination, date):
        self.card_height = 281
        self.username = username
        self.departure = departure
        self.destination = destination
        self.date = date

        self.window = QMainWindow()
        self.scroll = QScrollArea()
        self.form = QWidget()
        self.widget = QWidget()
        self.vbox = QVBoxLayout()
        try:
            data = pd.read_excel('data/data_destinasi.xlsx')
            self.data = data[
                (data['Keberangkatan'] == departure) &
                (data['Tujuan'] == destination) &
                (data['Tanggal'] == date)
                ]
        except FileNotFoundError:
            # Tangani jika file tidak ditemukan
            error_message('File data_destinasi.xlsx tidak ditemukan.')

            return

        self.setupUi()

    def add_widget(self, widget):
        self.vbox.addWidget(widget)

    def setupUi(self, form=None):
        if form is not None:
            self.form = form
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate('Form', 'Form'))
        self.window.setWindowIcon(QIcon('img/icon.png'))
        self.window.setObjectName('Form')
        self.window.setFixedSize(1920, 1080)

        self.form.setWindowTitle(_translate('Form', 'Form'))
        self.form.setWindowIcon(QIcon('img/icon.png'))
        self.form.setObjectName('Form')
        self.form.setFixedSize(1920, 1080)

        bg_result = QtWidgets.QLabel(self.form)
        bg_result.setEnabled(True)
        bg_result.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        bg_image = self.get_bg_image_path()  # Mendapatkan path gambar background berdasarkan kota tujuan
        bg_result.setStyleSheet(f"image: url({bg_image});")
        bg_result.setObjectName('bg_result')

        self.create_search_bar()
        self.create_filter_bar()

        for i in range(len(self.data)):
            self.create_card_result(i)

        QtCore.QMetaObject.connectSlotsByName(self.form)

        self.widget.setLayout(self.vbox)

        # # Scroll Area Properties
        # self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.scroll.setWidgetResizable(True)
        # self.scroll.setWidget(self.form)
        #
        # self.window.setCentralWidget(self.scroll)

        self.form.show()
        # self.window.show()

    def get_bg_image_path(self):
        # Mendapatkan path gambar background berdasarkan kota tujuan
        if self.destination == 'Jakarta':
            return ":/images/img/bgtiket_jakarta.png"
        elif self.destination == 'Surakarta':
            return ":/images/img/bgtiket_surakarta.png"
        elif self.destination == 'Bali':
            return ":/images/img/bgtiket_bali.png"
        elif self.destination == 'Semarang':
            return ":/images/img/bgtiket_semarang.png"
        elif self.destination == 'Bandung':
            return ":/images/img/bgtiket_bandung.png"
        elif self.destination == 'Yogyakarta':
            return ":/images/img/bgtiket_yogyakarta.png"
        elif self.destination == 'Malang':
            return ":/images/img/bgtiket_malang.png"
        elif self.destination == 'Surabaya':
            return ":/images/img/bgtiket_surabaya.png"
        else:
            return ":/images/img/bgtiket.png"

    def create_search_bar(self):
        _translate = QtCore.QCoreApplication.translate

        font_kota = qfont(15, 'Epilogue SemiBold')
        kota_berangkat = QtWidgets.QLabel(self.form)
        kota_berangkat.setGeometry(QtCore.QRect(312 , 332, 151, 41))
        kota_berangkat.setFont(font_kota)
        kota_berangkat.setObjectName('kota_berangkat')
        kota_berangkat.setText(self.departure)

        kota_tujuan = QtWidgets.QLabel(self.form)
        kota_tujuan.setGeometry(QtCore.QRect(310, 354, 151, 41))
        kota_tujuan.setFont(font_kota)
        kota_tujuan.setObjectName('kota_tujuan')
        kota_tujuan.setText(self.destination)


        tanggal = QtWidgets.QDateEdit(self.form)
        tanggal.setGeometry(QtCore.QRect(310, 390, 189, 31))
        tanggal.setFont(qfont(15, 'Epilogue Medium', False, True))
        tanggal.setStyleSheet(
            "QDateEdit {\n"
            "border-radius: 2px; border: 0px solid "
            "#cccccc; \n"
            "color: rgb(84, 200, 179);\n"
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
        tanggal.setReadOnly(True)
        tanggal.setObjectName('tanggal')
        qdate = QtCore.QDate.currentDate()
        # tanggal.setDate(qdate.fromString(self.date, "dd/MM/yyyy"))
        tanggal.setDate(qdate.fromString(self.date, "yyyy-MM-dd"))

        cari = QtWidgets.QPushButton(self.form)
        cari.setGeometry(QtCore.QRect(1490, 61, 181, 62))
        cari.setFont(qfont(12, 'Epilogue', True, False, 75))
        cari.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        cari.setStyleSheet(
            "QPushButton#cari{\n"
            "background-color: #2abaa1;\n"
            "color: rgb(255, 255, 255);\n"
            "padding: 0px 20px;\n"
            "border-radius: 15px;\n"
            "}\n"
            "\n"
            "QPushButton#cari:pressed{\n"
            "background-color: #219a85;\n"
            "}\n"
            "\n"
            "")
        cari.setObjectName('cari')
        cari.setText(_translate('Form', 'Menu Utama'))
        cari.clicked.connect(self.open_homepage)

        try:
            kota_berangkat.setText(self.data['Keberangkatan'].iloc[0])
            kota_tujuan.setText(self.data['Tujuan'].iloc[0])
        except IndexError:
            # Tangani jika tidak ada data yang tersedia di file
            error_message('Tidak ada data yang tersedia di file '
                          'data_destinasi.xlsx.')

            return

    def open_homepage(self):  # Modify to accept username parameter
        self.homepage_window = QtWidgets.QWidget()
        self.ui = homepage_2.Ui_Form(self.username)  # Pass the username to homepage_2.Ui_Form
        self.ui.setupUi(self.homepage_window)
        self.homepage_window.show()
        self.form.close()

    def open_seat(self, jenis_kendaraan, destination_id):  
        # Mendapatkan jenis kendaraan dari data tiket
        if jenis_kendaraan == 'innova':
            # Menampilkan pesan popup
            
            # Setelah menampilkan pesan popup, tetap lanjutkan untuk membuka jendela kursi
            self.seat_window = QtWidgets.QWidget()
            self.ui = seat.Ui_Form(self.username, destination_id)
            self.ui.setupUi(self.seat_window)
            self.seat_window.show()
            QMessageBox.information(self.form, "Informasi", "Jenis kendaraan yang dipilih adalah Innova. Tidak perlu memilih kursi.")
            self.form.close()
        else:
            # Jika jenis kendaraan bukan Innova, buka jendela untuk memilih kursi langsung
            self.seat_window = QtWidgets.QWidget()
            self.ui = seat.Ui_Form(self.username, destination_id)
            self.ui.setupUi(self.seat_window)
            self.seat_window.show()
            self.form.close()

    def create_filter_bar(self):
        _translate = QtCore.QCoreApplication.translate

        font_pencarian = qfont(15, 'Epilogue Black', True, False, 75)
        hasil_pencarian = QtWidgets.QLabel(self.form)
        hasil_pencarian.setGeometry(QtCore.QRect(567, 221, 221, 41))
        hasil_pencarian.setFont(font_pencarian)
        hasil_pencarian.setObjectName('hasil_pencarian')
        hasil_pencarian.setText(_translate('Form', 'Hasil Pencarian'))

        filter_pencarian_text = QtWidgets.QLabel(self.form)
        filter_pencarian_text.setGeometry(QtCore.QRect(252, 221, 209, 35))
        filter_pencarian_text.setFont(font_pencarian)
        filter_pencarian_text.setObjectName('filter_pencarian_text')
        filter_pencarian_text.setText(
            _translate('Form', 'Destinasi'))


    def rect(self, dim, index):
        y = dim[1] + self.card_height * index + 10 * index

        return QtCore.QRect(dim[0], y, dim[2], dim[3])

    def create_card_result(self, index):
        count = index + 1
        card = 'card' + str(count)
        # Adjusted dimensions for two-column layout
        card_width, card_height = 541, 281
        margin = 20

        if index % 2 == 0:  # Even index (0, 2, 4, ...)
            x = 569
        else:  # Odd index (1, 3, 5, ...)
            x = 569 + card_width + margin

        y = 292 + (index // 2) * (card_height + margin)

        globals()[card] = QtWidgets.QLabel(self.form)
        globals()[card].setGeometry(QtCore.QRect(x, y, card_width, card_height))
        globals()[card].setFont(qfont(10))
        globals()[card].setStyleSheet("image: url(:/images/img/rec.png);")
        globals()[card].setObjectName(card)

        _translate = QtCore.QCoreApplication.translate

        logo = 'logo_trans' + str(count)
        globals()[logo] = QtWidgets.QLabel(self.form)
        globals()[logo].setGeometry(QtCore.QRect(x + 47, y + 35, 32, 42))
        globals()[logo].setStyleSheet(
            "image: url(:/images/img/logotrans.png);")
        globals()[logo].setObjectName(logo)

        nama_travel = 'nama_travel' + str(count)
        globals()[nama_travel] = QtWidgets.QLabel(self.form)
        globals()[nama_travel].setGeometry(QtCore.QRect(x + 95, y + 35, 111, 41))
        globals()[nama_travel].setFont(qfont(9))
        globals()[nama_travel].setObjectName(nama_travel)

        jenis_kendaraan = 'jenis_kendaraan' + str(count)
        globals()[jenis_kendaraan] = QtWidgets.QLabel(self.form)
        globals()[jenis_kendaraan].setGeometry(QtCore.QRect(x + 363, y + 39, 127, 31))
        globals()[jenis_kendaraan].setFont(
            qfont(12, 'Epilogue Medium', False, False, 50))
        globals()[jenis_kendaraan].setAlignment(QtCore.Qt.AlignRight)
        globals()[jenis_kendaraan].setObjectName(jenis_kendaraan)

        jam_berangkat = 'jam_berangkat' + str(count)
        font_jam = qfont(12, 'Epilogue Medium', False, True)
        globals()[jam_berangkat] = QtWidgets.QLabel(self.form)
        globals()[jam_berangkat].setGeometry(QtCore.QRect(x + 47, y + 100, 55, 21))
        globals()[jam_berangkat].setFont(font_jam)
        globals()[jam_berangkat].setStyleSheet("color: #2abaa1;")
        globals()[jam_berangkat].setObjectName(jam_berangkat)
        jam_tiba = 'jam_tiba' + str(count)
        globals()[jam_tiba] = QtWidgets.QLabel(self.form)
        globals()[jam_tiba].setGeometry(QtCore.QRect(x + 47, y + 120, 55, 21))
        globals()[jam_tiba].setFont(font_jam)
        globals()[jam_tiba].setStyleSheet("color: #2abaa1;")
        globals()[jam_tiba].setObjectName(jam_tiba)

        font_tempat = qfont(11, 'Epilogue SemiBold', True, False, 75)
        tempat_berangkat = 'tempat_berangkat' + str(count)
        globals()[tempat_berangkat] = QtWidgets.QLabel(self.form)
        globals()[tempat_berangkat].setGeometry(QtCore.QRect(x + 111, y + 91, 251, 41))
        globals()[tempat_berangkat].setFont(font_tempat)
        globals()[tempat_berangkat].setObjectName(tempat_berangkat)
        tempat_tujuan = 'tempat_tujuan' + str(count)
        globals()[tempat_tujuan] = QtWidgets.QLabel(self.form)
        globals()[tempat_tujuan].setGeometry(QtCore.QRect(x + 111, y + 110, 251, 41))
        globals()[tempat_tujuan].setFont(font_tempat)
        globals()[tempat_tujuan].setObjectName(tempat_tujuan)

        mata_uang = 'mata_uang' + str(count)
        font_harga = qfont(18, 'Epilogue Black', True, False, 75)
        globals()[mata_uang] = QtWidgets.QLabel(self.form)
        globals()[mata_uang].setGeometry(QtCore.QRect(x + 47, y + 199, 51, 41))
        globals()[mata_uang].setFont(font_harga)
        globals()[mata_uang].setStyleSheet("color: rgb(42, 186, 161);")
        globals()[mata_uang].setObjectName(mata_uang)
        globals()[mata_uang].setText(_translate('Form', 'Rp.'))

        mulai_dari = 'mulai_dari' + str(count)
        font_placeholder = qfont(12, 'Epilogue Light')
        globals()[mulai_dari] = QtWidgets.QLabel(self.form)
        globals()[mulai_dari].setGeometry(QtCore.QRect(x + 47, y + 175, 91, 31))
        globals()[mulai_dari].setFont(font_placeholder)
        globals()[mulai_dari].setObjectName(mulai_dari)
        globals()[mulai_dari].setText(_translate('Form', 'Mulai Dari'))
        per_tiket = 'per_tiket' + str(count)
        globals()[per_tiket] = QtWidgets.QLabel(self.form)
        globals()[per_tiket].setGeometry(QtCore.QRect(x + 225, y + 207, 91, 31))
        globals()[per_tiket].setFont(font_placeholder)
        globals()[per_tiket].setObjectName(per_tiket)
        globals()[per_tiket].setText(_translate('Form', '/ Tiket'))

        harga_tiket = 'harga_tiket' + str(count)
        globals()[harga_tiket] = QtWidgets.QLabel(self.form)
        globals()[harga_tiket].setGeometry(QtCore.QRect(x + 96, y + 199, 131, 41))
        globals()[harga_tiket].setFont(font_harga)
        globals()[harga_tiket].setStyleSheet("color: rgb(42, 186, 161);")
        globals()[harga_tiket].setObjectName(harga_tiket)

        book = 'book' + str(count)
        font_book = QtGui.QFont()
        font_book.setKerning(True)
        globals()[book] = QtWidgets.QPushButton(self.form)
        globals()[book].setGeometry(QtCore.QRect(x + 401, y + 170, 101, 81))
        globals()[book].setFont(font_book)
        globals()[book].setStyleSheet("image: url(:/images/img/book.png); background: transparent;")
        globals()[book].setObjectName(book)
        globals()[book].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        globals()[book].raise_()
        globals()[book].clicked.connect(lambda: self.open_seat(self.data['Jenis'].iloc[index], self.data['id'].iloc[index]))

        try:
            globals()[nama_travel].setText(self.data['Nama Travel'].iloc[index])
            globals()[jenis_kendaraan].setText(self.data['Jenis'].iloc[index])
            globals()[jam_berangkat].setText(
                str(self.data['Jam Keberangkatan'].iloc[index])[:5])
            globals()[jam_tiba].setText(
                str(self.data['Jam Tujuan'].iloc[index])[:5])
            globals()[tempat_berangkat].setText(
                self.data['Tm. Keberangkatan'].iloc[index])
            globals()[tempat_tujuan].setText(
                self.data['Tm. Tujuan'].iloc[index])
            # Convert price to string and format it
            harga = self.data['Harga'].iloc[index]
            formatted_harga = f"{harga:,}".replace(",", ".")
            globals()[harga_tiket].setText(_translate('Form', formatted_harga))

        except IndexError:
            # Tangani jika tidak ada data yang tersedia di file
            error_message('Tidak ada data yang tersedia di file '
                          'data_destinasi.xlsx.')

            return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_Form('123', 'Yogyakarta', 'Surakarta', '2024-06-01')
    sys.exit(app.exec_())
