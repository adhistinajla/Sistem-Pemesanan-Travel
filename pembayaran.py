import pandas as pd
import sys, random, string

import homepage_2, seat, tiket, e_tiketcetak
import res_pembayaran

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow, QScrollArea, QVBoxLayout, QMessageBox
from PyQt5.QtCore import QDate, QDateTime
from datetime import datetime, timedelta
 
from common import qfont, error_message


class Ui_Form(object):
    def __init__(self ,username, id_pembayaran):

        self.window = QMainWindow()
        self.scroll = QScrollArea()
        self.form = QWidget()
        self.widget = QWidget()
        self.vbox = QVBoxLayout()
        self.username = username

        try:
            data = pd.read_excel('data/data_booking.xlsx', dtype={'Id Pembayaran': str})
            self.data = data.loc[data['Id Pembayaran'] == id_pembayaran].iloc[0]
        except FileNotFoundError:
            # Tangani jika file tidak ditemukan 
            error_message('File data_booking.xlsx tidak ditemukan.')

            return

        self.setupUi(self.form)
        self.setup_connections()
        self.stackedWidget.setCurrentIndex(0)
        self.setup_tombol()
        self.setup_va()

    def setup_tombol(self):
        # Inisialisasi tombol dan atur tampilan awal
        self.tombol_qris.setChecked(True)
        self.tombol_qris.setStyleSheet("border-image: url(:/images/img/qris_select.png);")
        self.tombol_va.setChecked(False)
        self.tombol_va.setStyleSheet("border-image: url(:/images/img/va_unselected.png);")

    def setup_va(self):
        # Generate dan atur nomor VA
        va_number = self.generate_va_number()
        self.va.setText(va_number)


    def setupUi(self, Form=None):
        if Form is not None:
            self.form = Form
        Form.setObjectName("Form")  # Changed from self.form to Form
        Form.setFixedSize(1920, 1080)
        self.background = QtWidgets.QLabel(Form)
        self.background.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.background.setStyleSheet("image: url(:/images/img/bg_pembayaran.png);")
        self.background.setText("")
        self.background.setObjectName("background")

        self.tombol_qris = QtWidgets.QPushButton(Form)
        self.tombol_qris.setGeometry(QtCore.QRect(350, 359, 151, 81))
        self.tombol_qris.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tombol_qris.setStyleSheet("QPushButton#tombol_qris{\n"
                "border-image: url(:/images/img/qris_unselected.png);\n"
                "}\n"
                "\n"
                "QPushButton#tombol_qris:pressed{\n"
                "border-image: url(:/images/img/qris_select.png);\n"
                "}\n"
                "\n"
                "QPushButton#tombol_qris:checked{\n"
                "border-image: url(:/images/img/qris_select.png);\n"
                "}\n"
                "")
        self.tombol_qris.setText("")
        self.tombol_qris.setObjectName("tombol_qris")

        self.tombol_va = QtWidgets.QPushButton(Form)
        self.tombol_va.setGeometry(QtCore.QRect(510, 359, 221, 81))
        self.tombol_va.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tombol_va.setStyleSheet("QPushButton#tombol_va{\n"
                "border-image: url(:/images/img/va_unselected.png);\n"
                "}\n"
                "\n"
                "QPushButton#tombol_va:pressed{\n"
                "border-image: url(:/images/img/va_select.png);\n"
                "}\n"
                "\n"
                "QPushButton#tombol_va:checked{\n"
                "border-image: url(:/images/img/va_select.png);\n"
                "}")
        self.tombol_va.setText("")
        self.tombol_va.setObjectName("tombol_va")

        self.tanggal_bataswaktu = QtWidgets.QDateEdit(Form)
        self.tanggal_bataswaktu.setGeometry(QtCore.QRect(755, 388, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Epilogue Medium")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(False)
        self.tanggal_bataswaktu.setFont(font)
        self.tanggal_bataswaktu.setAccessibleName("")
        self.tanggal_bataswaktu.setStyleSheet("QDateEdit {\n"
                "border: 0px solid #cccccc; \n"
                "    color: rgb(28, 25, 46);\n"
                "background-color: rgba(255, 255, 255, 0);\n"
                "\n"
                "}\n"
                "\n"
                "QDateEdit::drop-down { border: none; \n"
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
        self.tanggal_bataswaktu.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.tanggal_bataswaktu.setFrame(False)
        self.tanggal_bataswaktu.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tanggal_bataswaktu.setReadOnly(False)
        self.tanggal_bataswaktu.setKeyboardTracking(False)
        self.tanggal_bataswaktu.setDisplayFormat("dd/MM/yyyy HH:mm")
        self.tanggal_bataswaktu.setCalendarPopup(False)
        self.tanggal_bataswaktu.setObjectName("tanggal_bataswaktu")
        now = datetime.now()
        next_day = now + timedelta(days=1)
        self.tanggal_bataswaktu.setDateTime(QDateTime(next_day.year, next_day.month, next_day.day, next_day.hour, next_day.minute))


        self.tiket = QtWidgets.QGroupBox(Form)
        self.tiket.setGeometry(QtCore.QRect(1142, 371, 511, 541))
        self.tiket.setStyleSheet("border:none")
        self.tiket.setTitle("")
        self.tiket.setObjectName("tiket")

        self.jenis_kendaraan = QtWidgets.QLabel(self.tiket)
        self.jenis_kendaraan.setGeometry(QtCore.QRect(351, 50, 127, 31))
        font = QtGui.QFont()
        font.setFamily("Epilogue Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.jenis_kendaraan.setFont(font)
        self.jenis_kendaraan.setText(self.get_data('Jenis'))
        self.jenis_kendaraan.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.jenis_kendaraan.setObjectName("jenis_kendaraan")

        self.jam_berangkat = QtWidgets.QLabel(self.tiket)
        self.jam_berangkat.setGeometry(QtCore.QRect(34, 114, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Epilogue Medium")
        font.setPointSize(12)
        font.setItalic(True)
        self.jam_berangkat.setFont(font)
        self.jam_berangkat.setStyleSheet("color: #2abaa1;")
        self.jam_berangkat.setText(str(self.get_data('Jam Keberangkatan')))
        self.jam_berangkat.setObjectName("jam_berangkat")

        self.pertiket = QtWidgets.QLabel(self.tiket)
        self.pertiket.setGeometry(QtCore.QRect(212, 222, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Epilogue Light")
        font.setPointSize(12)
        self.pertiket.setFont(font)
        self.pertiket.setObjectName("pertiket")

        font_harga = qfont(18, 'Epilogue Black', True, False, 75)
        self.harga_tiket = QtWidgets.QLabel(self.tiket)
        self.harga_tiket.setGeometry(QtCore.QRect(84, 215, 131, 41))
        harga = self.data['Harga']
        formatted_harga = f"{harga:,}".replace(",", ".")
        self.harga_tiket.setFont(font_harga)
        self.harga_tiket.setStyleSheet("color: rgb(42, 186, 161);")
        self.harga_tiket.setText(formatted_harga)
        self.harga_tiket.setObjectName("harga_tiket")

        self.mulai_dari = QtWidgets.QLabel(self.tiket)
        self.mulai_dari.setGeometry(QtCore.QRect(34, 190, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Epilogue Light")
        font.setPointSize(10)
        self.mulai_dari.setFont(font)
        self.mulai_dari.setText("Harus Dibayar")
        self.mulai_dari.setObjectName("mulai_dari")

        self.jam_tujuan = QtWidgets.QLabel(self.tiket)
        self.jam_tujuan.setGeometry(QtCore.QRect(34, 134, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Epilogue Medium")
        font.setPointSize(12)
        font.setItalic(True)
        self.jam_tujuan.setFont(font)
        self.jam_tujuan.setStyleSheet("color: #2abaa1;")
        self.jam_tujuan.setText(str(self.get_data('Jam Tujuan')))
        self.jam_tujuan.setObjectName("jam_tujuan")

        self.nama_trans = QtWidgets.QLabel(self.tiket)
        self.nama_trans.setGeometry(QtCore.QRect(75, 49, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Epilogue")
        font.setPointSize(9)
        self.nama_trans.setFont(font)
        self.nama_trans.setText("Adiwilaga")
        self.nama_trans.setObjectName("nama_trans")
        self.nama_trans.setText(self.get_data('Nama Travel'))

        font_tempat = qfont(11, 'Epilogue SemiBold', True, False, 75)
        self.tempat_berangkat = QtWidgets.QLabel(self.tiket)
        self.tempat_berangkat.setGeometry(QtCore.QRect(94, 104, 251, 41))
        self.tempat_berangkat.setFont(font_tempat)
        self.tempat_berangkat.setText(self.get_data('Tm. Keberangkatan'))
        self.tempat_berangkat.setObjectName("tempat_berangkat")
        self.tempat_berangkat.setStyleSheet("color: rgb(0, 0, 0);")

        self.Rp = QtWidgets.QLabel(self.tiket)
        self.Rp.setGeometry(QtCore.QRect(34, 210, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Epilogue Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Rp.setFont(font)
        self.Rp.setStyleSheet("color: rgb(42, 186, 161);")
        self.Rp.setText("Rp.")
        self.Rp.setObjectName("Rp")

        self.logo_trans = QtWidgets.QLabel(self.tiket)
        self.logo_trans.setGeometry(QtCore.QRect(34, 49, 32, 41))
        self.logo_trans.setStyleSheet("image: url(:/images/img/logotrans.png);")
        self.logo_trans.setText("")
        self.logo_trans.setObjectName("logo_trans")

        self.tempat_tujuan = QtWidgets.QLabel(self.tiket)
        self.tempat_tujuan.setGeometry(QtCore.QRect(94, 124, 211, 41))
        self.tempat_tujuan.setFont(font_tempat)
        self.tempat_tujuan.setText(self.get_data('Tm. Tujuan'))
        self.tempat_tujuan.setObjectName("tempat_tujuan")
        self.tempat_tujuan.setStyleSheet("color: rgb(0, 0, 0);")

        self.seat_pesan = QtWidgets.QLabel(self.tiket)
        self.seat_pesan.setGeometry(QtCore.QRect(345, 220, 91, 31))
        self.seat_pesan.setFont(qfont(12, 'Epilogue ExtraLight', False, True))
        self.seat_pesan.setText("Seat")
        self.seat_pesan.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.seat_pesan.setObjectName("seat_pesan")
        self.seat_pesan.setStyleSheet("color: rgb(0, 0, 0);")

        self.seat = QtWidgets.QLabel(self.tiket)
        self.seat.setGeometry(QtCore.QRect(430, 213, 51, 41))
        self.seat.setFont(font_harga)
        self.seat.setStyleSheet("color: rgb(42, 186, 161);")
        self.seat.setText('-')
        self.seat.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        seat_data = self.get_data('Seat')
        if seat_data == '-':
            self.seat.setText("-")
        else:
            self.seat.setText(str(seat_data).zfill(2))
        self.seat.setObjectName("seat_number")

        self.cetak_bukti = QtWidgets.QPushButton(self.tiket)
        self.cetak_bukti.setGeometry(QtCore.QRect(30, 420, 175, 67))
        font = QtGui.QFont()
        font.setFamily("Epilogue Medium")
        font.setPointSize(11)
        font.setItalic(True)
        font.setKerning(False)
        self.cetak_bukti.setFont(font)
        self.cetak_bukti.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.cetak_bukti.setStyleSheet("QPushButton#cetak_bukti{\n"
                "background-color: rgb(240, 246, 255);\n"
                "color:rgb(177, 182, 188);\n"
                "padding: 0px 20px;\n"
                "border-radius: 15px;\n"
                "}\n")
        self.cetak_bukti.setText("Cetak e-Tiket")
        self.cetak_bukti.setObjectName("cetak_bukti")

        self.konfirmasi = QtWidgets.QPushButton(self.tiket)
        self.konfirmasi.setGeometry(QtCore.QRect(220, 420, 265, 67))
        font = QtGui.QFont()
        font.setFamily("Epilogue")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.konfirmasi.setFont(font)
        self.konfirmasi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.konfirmasi.setStyleSheet("QPushButton#konfirmasi{\n"
                "background-color: #2abaa1;\n"
                "    color: rgb(255, 255, 255);\n"
                "padding: 0px 20px;\n"
                "border-radius: 15px;\n"
                "}\n"
                "\n"
                "QPushButton#konfirmasi:pressed{\n"
                "background-color: #e6fe52;\n"
                "color: rgb(27, 25, 45);\n"
                "}\n"
                "\n"
                "QPushButton#konfirmasi:clicked{\n"
                "background-color: #ececec;\n"
                "color: rgb(27, 24, 44);\n"
                "}\n"
                "\n"
                "background-color: #2abaa1;")
        self.konfirmasi.setObjectName("konfirmasi")

        self.berangkat_atas = QtWidgets.QLabel(self.form)
        self.berangkat_atas.setGeometry(QtCore.QRect(1170, 310, 131, 41))
        self.berangkat_atas.setFont(qfont(12, 'Epilogue SemiBold'))
        self.berangkat_atas.setStyleSheet("color: rgb(255, 255, 255);")
        self.berangkat_atas.setObjectName("berangkat_atas")
        self.berangkat_atas.setText(self.get_data('Keberangkatan'))

        self.tujuan_atas = QtWidgets.QLabel(self.form)
        self.tujuan_atas.setGeometry(QtCore.QRect(1170, 330, 131, 41))
        self.tujuan_atas.setFont(qfont(12, 'Epilogue SemiBold'))
        self.tujuan_atas.setStyleSheet("color: rgb(255, 255, 255);")
        self.tujuan_atas.setObjectName("tujuan_atas")
        self.tujuan_atas.setText(self.get_data('Tujuan'))

        self.tanggal = QtWidgets.QDateEdit(self.form)
        self.tanggal.setGeometry(QtCore.QRect(1460, 318, 189, 31))
        self.tanggal.setFont(qfont(12, 'Epilogue Medium', False, True))
        self.tanggal.setAccessibleName("")
        self.tanggal.setStyleSheet("QDateEdit {\n"
                                   "border: 0px solid #cccccc; \n"
                                   "    color: rgb(255, 255, 255);\n"
                                   "background-color: rgba(255, 255, 255, 0);\n"
                                   "\n"
                                   "}\n"
                                   "\n"
                                   "QDateEdit::drop-down { border: none; \n"
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
        self.tanggal.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.tanggal.setFrame(False)
        self.tanggal.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tanggal.setReadOnly(False)
        self.tanggal.setKeyboardTracking(False)
        self.tanggal.setCalendarPopup(False)
        self.tanggal.setObjectName("tanggal")
        excel_date = self.get_data('Tanggal')
        self.tanggal.setDate(QtCore.QDate.fromString(excel_date, "yyyy-MM-dd"))

        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(320, 463, 671, 261))
        self.stackedWidget.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.stackedWidget.setObjectName("stackedWidget")

        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")

        self.cara_bayar_qris = QtWidgets.QLabel(self.page)
        self.cara_bayar_qris.setGeometry(QtCore.QRect(0, 25, 680, 222))
        self.cara_bayar_qris.setStyleSheet("image: url(:/images/img/cara_bayar_qris.png);")
        self.cara_bayar_qris.setText("")
        self.cara_bayar_qris.setObjectName("cara_bayar_qris")
        self.stackedWidget.addWidget(self.page)

        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.cara_bayar_va = QtWidgets.QLabel(self.page_2)
        self.cara_bayar_va.setGeometry(QtCore.QRect(30, 21, 471, 231))
        self.cara_bayar_va.setStyleSheet("image: url(:/images/img/cara_bayar_va.png);")
        self.cara_bayar_va.setText("")
        self.cara_bayar_va.setObjectName("cara_bayar_va")

        self.va = QtWidgets.QLabel(self.page_2)
        self.va.setGeometry(QtCore.QRect(70, 57, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Epilogue Medium")
        font.setPointSize(10)
        self.va.setFont(font)
        self.va.setObjectName("va")
        self.stackedWidget.addWidget(self.page_2)

        self.menu_utama = QtWidgets.QPushButton(Form)
        self.menu_utama.setGeometry(QtCore.QRect(1490, 61, 181, 62))
        font = QtGui.QFont()
        font.setFamily("Epilogue")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.menu_utama.setFont(font)
        self.menu_utama.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu_utama.setStyleSheet("QPushButton#menu_utama{\n"
                "background-color: #2abaa1;\n"
                "color: rgb(255, 255, 255);\n"
                "padding: 0px 20px;\n"
                "border-radius: 15px;\n"
                "}\n"
                "\n"
                "QPushButton#menu_utama:pressed{\n"
                "background-color: #219a85;\n"
                "}\n"
                "\n"
                "")
        self.menu_utama.setObjectName("menu_utama")
        self.menu_utama.clicked.connect(self.open_homepage)
        
        self.masukkan_kode_diskon = QtWidgets.QLineEdit(Form)
        self.masukkan_kode_diskon.setGeometry(QtCore.QRect(510, 760, 271, 67))
        font = QtGui.QFont()
        font.setFamily("Epilogue Medium")
        font.setPointSize(11)
        self.masukkan_kode_diskon.setFont(font)
        self.masukkan_kode_diskon.setStyleSheet("background-color: rgb(240, 246, 255);\n"
                "color: rgb(28, 25, 46);\n"
                "padding: 0px 20px;\n"
                "border-radius: 15px;")
        self.masukkan_kode_diskon.setInputMask("")
        self.masukkan_kode_diskon.setReadOnly(False)
        self.masukkan_kode_diskon.setObjectName("masukkan_kode_diskon")

        self.claim_diskon = QtWidgets.QPushButton(Form)
        self.claim_diskon.setGeometry(QtCore.QRect(344, 760, 151, 67))
        self.claim_diskon.clicked.connect(self.check_discount)
        font = QtGui.QFont()
        font.setFamily("Epilogue")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.claim_diskon.setFont(font)
        self.claim_diskon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.claim_diskon.setStyleSheet("QPushButton#claim_diskon{\n"
                "background-color: #2abaa1;\n"
                "color: rgb(255, 255, 255);\n"
                "padding: 0px 20px;\n"
                "border-radius: 15px;\n"
                "}\n"
                "\n"
                "QPushButton#claim_diskon:pressed{\n"
                "background-color: #219a85;\n"
                "}\n"
                "\n"
                "background-color: #2abaa1;")
        self.claim_diskon.setObjectName("claim_diskon")

        self.diskon_angka_va = QtWidgets.QLabel(Form)
        self.diskon_angka_va.setGeometry(QtCore.QRect(923, 780, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Epilogue")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.diskon_angka_va.setFont(font)
        self.diskon_angka_va.setStyleSheet("color: rgb(42, 186, 161);")
        self.diskon_angka_va.setObjectName("diskon_angka_va")

        self.diskon_label_va = QtWidgets.QLabel(Form)
        self.diskon_label_va.setGeometry(QtCore.QRect(925, 770, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Epilogue")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.diskon_label_va.setFont(font)
        self.diskon_label_va.setObjectName("diskon_label_va")

        #self.ubah_kursi = QtWidgets.QPushButton(Form)
        #self.ubah_kursi.setGeometry(QtCore.QRect(1296, 61, 181, 62))
        #font = QtGui.QFont()
        #font.setFamily("Epilogue")
        #font.setPointSize(12)
        #font.setBold(True)
        #font.setWeight(75)
        #self.ubah_kursi.setFont(font)
        #self.ubah_kursi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        #self.ubah_kursi.setStyleSheet("QPushButton#ubah_kursi{\n"
                #"background-color: rgb(240, 246, 255);\n"
                #"color:rgb(177, 182, 188);\n"
                #"padding: 0px 20px;\n"
                #"border-radius: 15px;\n"
               # "}\n"
                #"\n"
                #"\n"
                #"QPushButton#ubah_kursi:pressed{\n"
                #"background-color: rgb(231, 237, 245);\n"
                #"}")
        #self.ubah_kursi.setObjectName("ubah_kursi")
        #self.ubah_kursi.clicked.connect(lambda: self.open_seat(self.data['Id Tiket']))

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.form.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.menu_utama.setText(_translate("Form", "Menu Utama"))
        self.masukkan_kode_diskon.setPlaceholderText(_translate("Form", "Masukkan Kode Diskon"))
        self.claim_diskon.setText(_translate("Form", "Klaim"))
        self.diskon_angka_va.setText(_translate("Form", "00%"))
        self.diskon_label_va.setText(_translate("Form", "Disc."))
        #self.ubah_kursi.setText(_translate("Form", "Ubah Kursi"))
        self.konfirmasi.setText(_translate("Form", "Konfirmasi"))


    def generate_va_number(self):
        # Generate nomor acak dengan panjang 9 digit
        va_number = ''.join(random.choices(string.digits, k=15))
        return va_number

    def setup_connections(self):
        self.tombol_qris.clicked.connect(self.toggle_qris)
        self.tombol_va.clicked.connect(self.toggle_va)
        self.tombol_qris.clicked.connect(lambda: self.change_stacked_widget(0))
        self.tombol_va.clicked.connect(lambda: self.change_stacked_widget(1))
        self.konfirmasi.clicked.connect(self.confirm_payment)

    def toggle_qris(self):
        self.tombol_qris.setChecked(True)
        self.tombol_va.setChecked(False)
        self.tombol_qris.setStyleSheet("border-image: url(:/images/img/qris_select.png);")
        self.tombol_va.setStyleSheet("border-image: url(:/images/img/va_unselected.png);")

    def toggle_va(self):
        self.tombol_va.setChecked(True)
        self.tombol_qris.setChecked(False)
        self.tombol_va.setStyleSheet("border-image: url(:/images/img/va_select.png);")
        self.tombol_qris.setStyleSheet("border-image: url(:/images/img/qris_unselected.png);")
        
    def change_stacked_widget(self, index):
        self.stackedWidget.setCurrentIndex(index)    

    def get_data(self, col):
        return self.data[col]

    def check_discount(self):
        entered_code = self.masukkan_kode_diskon.text().strip()

        try:

                df_diskon = pd.read_excel('data/diskon.xlsx')
            
                matched_discount = df_diskon.loc[df_diskon['Kode Diskon'] == entered_code, 'Diskon'].iloc[0]
                matched_discount_percent = matched_discount * 100

                # Hitung harga yang didiskon
                harga_tiket = self.data['Harga']
                diskon_amount = harga_tiket * matched_discount
                harga_diskon = harga_tiket - diskon_amount

                # Tampilkan diskon dan harga tiket setelah diskon
                self.diskon_angka_va.setText(f"{matched_discount_percent:.0f}%")
                self.harga_tiket.setText(f"{harga_diskon:,.0f}".replace(",", "."))

                QMessageBox.information(self.form, "Sukses", f"Kode diskon {entered_code} berhasil diterapkan sebesar {matched_discount_percent:.0f}%.")

        except FileNotFoundError:
                error_message('File diskon.xlsx tidak ditemukan.')

        except IndexError:
        # Tampilkan pesan gagal
                QMessageBox.warning(self.form, "Kesalahan", "Kode diskon tidak valid.")


    def confirm_payment(self):
        try:
                data = pd.read_excel('data/data_booking.xlsx')
                data.loc[data['Id Pembayaran'] == self.data['Id Pembayaran'], 'Status Pembayaran'] = 'Sudah Terbayar'
                data.to_excel('data/data_booking.xlsx', index=False)
                
                reply = QMessageBox.question(self.form, 'Konfirmasi Pembayaran', 
                                                "Apakah Anda yakin pembayaran telah terkonfirmasi?",
                                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                        self.konfirmasi.setEnabled(False)
                        self.konfirmasi.setText("Sudah Terbayar")
                        self.cetak_bukti.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                        self.konfirmasi.setStyleSheet("QPushButton#konfirmasi{\n"
                                                        "background-color: #e6fe52;\n"
                                                        "color: rgb(27, 25, 45);;\n"
                                                        "border-radius: 15px;\n"
                                                        "}")
                        self.cetak_bukti.setEnabled(True)  # Aktifkan tombol cetak bukti
                        self.cetak_bukti.setStyleSheet("QPushButton#cetak_bukti{\n"
                                                        "background-color: #2abaa1;\n"
                                                        "color: rgb(255, 255, 255);\n"
                                                        "padding: 0px 20px;\n"
                                                        "border-radius: 15px;\n"
                                                        "}\n"
                                                        "\n"
                                                        "QPushButton#cetak_bukti:pressed{\n"
                                                        "background-color: rgb(42, 185, 160);\n"
                                                        "color: rgb(255, 255, 255);\n"
                                                        "}\n"
                                                        "\n"
                                                        "QPushButton#cetak_bukti:clicked{\n"
                                                        "background-color: rgb(42, 185, 160);\n"
                                                        "color: rgb(255, 255, 255);\n"
                                                        "}\n")
                        self.cetak_bukti.clicked.connect(self.open_e_tiket)
                        QMessageBox.information(self.form, "Sukses", "Pembayaran berhasil dikonfirmasi.")
                else:
                        pass
        except FileNotFoundError:
                error_message('File data_booking.xlsx tidak ditemukan.')

    def open_homepage(self, username):  # Modify to accept username parameter
        self.homepage_window = QtWidgets.QWidget()
        self.ui = homepage_2.Ui_Form(self.username)  # Pass the username to homepage_2.Ui_Form
        self.ui.setupUi(self.homepage_window)
        self.homepage_window.show()
        QtWidgets.QApplication.instance().activeWindow().close()

    def open_seat(self, destination_id):  # Modify to accept username parameter
        self.seat_window = QtWidgets.QWidget()
        self.ui = seat.Ui_Form(self.username, destination_id)  # Pass the username to homepage_2.Ui_Form
        self.ui.setupUi(self.seat_window)
        self.seat_window.show()
        self.form.close()

    def open_e_tiket(self):
        self.e_tiketcetak_window = QtWidgets.QWidget()
        self.ui = e_tiketcetak.Ui_Form()
        self.ui.setupUi(self.e_tiketcetak_window)
        self.e_tiketcetak_window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form('123', '14977')
    sys.exit(app.exec_())
