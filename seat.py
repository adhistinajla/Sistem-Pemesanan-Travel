import pandas as pd
import sys
import uuid

import homepage_2, tiket, pembayaran
import res_seat

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow, QScrollArea, QVBoxLayout, QMessageBox
from PyQt5.QtCore import QTimer
from datetime import datetime


from common import qfont, error_message


class Ui_Form(object):
    def __init__(self ,username , destinasi_id):
        self.card_height = 281
        row = [34, 129, 222, 315, 410]
        col = [40, 147, 251, 356]
        self.seat_width = 90
        self.seat_height = 80
        self.username = username
        self.selected_seat = None

        self.seat_dict = {
            0: (col[3], row[0]),
            1: (col[0], row[0]),
            2: (col[1], row[1]),
            3: (col[2], row[1]),
            4: (col[3], row[1]),
            5: (col[0], row[2]),
            6: (col[2], row[2]),
            7: (col[3], row[2]),
            8: (col[0], row[3]),
            9: (col[2], row[3]),
            10: (col[3], row[3]),
            11: (col[0], row[4]),
            12: (col[1], row[4]),
            13: (col[2], row[4]),
            14: (col[3], row[4]),
        }

        self.window = QMainWindow()
        self.scroll = QScrollArea()
        self.form = QWidget()
        self.widget = QWidget()
        self.vbox = QVBoxLayout()
        try:
            data = pd.read_excel('data/data_destinasi.xlsx')
            self.data = data.loc[data['id'] == destinasi_id].iloc[0]
        except FileNotFoundError:
            error_message('File data_destinasi.xlsx tidak ditemukan.')

            return

        self.setupUi()


    def get_data(self, col):
        return self.data[col]

    def setupUi(self, form=None):
        if form is not None:
            self.form = form
        self.form.setObjectName("Form")
        self.form.setFixedSize(1920, 1080)
        self.bg = QtWidgets.QLabel(self.form)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.bg.setStyleSheet("image: url(:/images/img/bg_seat.png);")
        self.bg.setText("")
        self.bg.setObjectName("bg")

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
        excel_date = self.get_data('Tanggal')
        formatted_date = excel_date.strftime('%Y-%m-%d')
        self.tanggal.setDate(QtCore.QDate.fromString(formatted_date, "yyyy-MM-dd"))
        self.tanggal.setObjectName("tanggal")

        self.groupBox = QtWidgets.QGroupBox(self.form)
        self.groupBox.setGeometry(QtCore.QRect(1142, 371, 511, 541))
        self.groupBox.setStyleSheet("border:none")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.logo_trans = QtWidgets.QLabel(self.groupBox)
        self.logo_trans.setGeometry(QtCore.QRect(34, 49, 32, 41))
        self.logo_trans.setStyleSheet("image: url(:/images/img/logotrans.png);")
        self.logo_trans.setText("")
        self.logo_trans.setObjectName("logo_trans")

        self.nama_trans = QtWidgets.QLabel(self.groupBox)
        self.nama_trans.setGeometry(QtCore.QRect(75, 49, 111, 41))
        self.nama_trans.setFont(qfont(9))
        self.nama_trans.setText(self.get_data('Nama Travel'))
        self.nama_trans.setObjectName("nama_trans")
        self.nama_trans.setStyleSheet("color: rgb(0, 0, 0);")

        self.jenis_kendaraan = QtWidgets.QLabel(self.groupBox)
        self.jenis_kendaraan.setGeometry(QtCore.QRect(351, 50, 127, 31))
        self.jenis_kendaraan.setFont(qfont(12, 'Epilogue Medium'))
        self.jenis_kendaraan.setText(self.get_data('Jenis'))
        self.jenis_kendaraan.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.jenis_kendaraan.setObjectName("jenis_kendaraan")
        self.jenis_kendaraan.setStyleSheet("color: rgb(0, 0, 0);")

        font_jam = qfont(12, 'Epilogue Medium', False, True)
        self.jam_berangkat = QtWidgets.QLabel(self.groupBox)
        self.jam_berangkat.setGeometry(QtCore.QRect(34, 114, 55, 21))
        self.jam_berangkat.setFont(font_jam)
        self.jam_berangkat.setStyleSheet("color: #2abaa1;")
        self.jam_berangkat.setText(self.get_data('Jam Keberangkatan').strftime('%H:%M'))
        self.jam_berangkat.setObjectName("jam_berangkat")

        self.jam_tujuan = QtWidgets.QLabel(self.groupBox)
        self.jam_tujuan.setGeometry(QtCore.QRect(34, 134, 55, 21))
        self.jam_tujuan.setFont(font_jam)
        self.jam_tujuan.setStyleSheet("color: #2abaa1;")
        self.jam_tujuan.setText (self.get_data('Jam Tujuan').strftime('%H:%M'))
        self.jam_tujuan.setObjectName("jam_tujuan")

        font_tempat = qfont(11, 'Epilogue SemiBold', True, False, 75)
        self.tempat_berangkat = QtWidgets.QLabel(self.groupBox)
        self.tempat_berangkat.setGeometry(QtCore.QRect(94, 104, 251, 41))
        self.tempat_berangkat.setFont(font_tempat)
        self.tempat_berangkat.setText(self.get_data('Tm. Keberangkatan'))
        self.tempat_berangkat.setObjectName("tempat_berangkat")
        self.tempat_berangkat.setStyleSheet("color: rgb(0, 0, 0);")

        self.tempat_tujuan = QtWidgets.QLabel(self.groupBox)
        self.tempat_tujuan.setGeometry(QtCore.QRect(94, 124, 211, 41))
        self.tempat_tujuan.setFont(font_tempat)
        self.tempat_tujuan.setText(self.get_data('Tm. Tujuan'))
        self.tempat_tujuan.setObjectName("tempat_tujuan")
        self.tempat_tujuan.setStyleSheet("color: rgb(0, 0, 0);")

        self.mulai_dari = QtWidgets.QLabel(self.groupBox)
        self.mulai_dari.setGeometry(QtCore.QRect(34, 190, 91, 31))
        self.mulai_dari.setFont(qfont(12, 'Epilogue Light'))
        self.mulai_dari.setText("Mulai Dari")
        self.mulai_dari.setObjectName("mulai_dari")
        self.mulai_dari.setStyleSheet("color: rgb(0, 0, 0);")

        font_harga = qfont(18, 'Epilogue Black', True, False, 75)
        self.Rp = QtWidgets.QLabel(self.groupBox)
        self.Rp.setGeometry(QtCore.QRect(34, 210, 51, 51))
        self.Rp.setFont(font_harga)
        self.Rp.setStyleSheet("color: rgb(42, 186, 161);")
        self.Rp.setText("Rp.")
        self.Rp.setObjectName("Rp")

        self.harga_tiket = QtWidgets.QLabel(self.groupBox)
        self.harga_tiket.setGeometry(QtCore.QRect(84, 215, 131, 41))
        harga = self.data['Harga']
        formatted_harga = f"{harga:,}".replace(",", ".")
        self.harga_tiket.setFont(font_harga)
        self.harga_tiket.setStyleSheet("color: rgb(42, 186, 161);")
        self.harga_tiket.setText(formatted_harga)
        self.harga_tiket.setObjectName("harga_tiket")

        self.pertiket = QtWidgets.QLabel(self.groupBox)
        self.pertiket.setGeometry(QtCore.QRect(212, 220, 91, 31))
        self.pertiket.setFont(qfont(12, 'Epilogue Light'))
        self.pertiket.setObjectName("pertiket")
        self.pertiket.setStyleSheet("color: rgb(0, 0, 0);")
        self.pertiket.setText('/ Tiket')

        self.seat_pesan = QtWidgets.QLabel(self.groupBox)
        self.seat_pesan.setGeometry(QtCore.QRect(345, 220, 91, 31))
        self.seat_pesan.setFont(qfont(12, 'Epilogue ExtraLight', False, True))
        self.seat_pesan.setText("Seat")
        self.seat_pesan.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.seat_pesan.setObjectName("seat_pesan")
        self.seat_pesan.setStyleSheet("color: rgb(0, 0, 0);")

        self.seat_number = QtWidgets.QLabel(self.groupBox)
        self.seat_number.setGeometry(QtCore.QRect(430, 213, 51, 41))
        self.seat_number.setFont(font_harga)
        self.seat_number.setStyleSheet("color: rgb(42, 186, 161);")
        self.seat_number.setText('-')
        self.seat_number.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.seat_number.setObjectName("seat_number")

        self.bayar = QtWidgets.QPushButton(self.groupBox)
        self.bayar.setGeometry(QtCore.QRect(223, 421, 261, 67))
        self.bayar.setFont(qfont(12, 'Epilogue Medium', False, True))
        self.bayar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bayar.setEnabled(False)
        self.bayar.setStyleSheet("QPushButton#bayar{\n"
                                 "background-color:#e6fe52;\n"
                                 "color: rgb(28, 25, 46);\n"
                                 "padding: 0px 20px;\n"
                                 "border-radius: 15px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#bayar:hover{\n"
                                 "background-color: #eefc9b;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#bayar:pressed{\n"
                                 "background-color: rgb(214, 235, 75);\n"
                                 "}")
        self.bayar.setText("Bayar")
        self.bayar.clicked.connect(self.save_to_excel)
        if self.get_data('Jenis') == "Innova":
                self.bayar.setEnabled(True)
        self.bayar.setObjectName("bayar")

        self.ubah_tiket = QtWidgets.QPushButton(self.groupBox)
        self.ubah_tiket.setGeometry(QtCore.QRect(29, 421, 181, 67))
        self.ubah_tiket.setFont(qfont(12, 'Epilogue ExtraLight', False, True))
        self.ubah_tiket.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ubah_tiket.setStyleSheet("QPushButton#ubah_tiket{\n"
                                      "background-color: rgb(236, 236, 236);\n"
                                      "color: rgb(28, 25, 46);\n"
                                      "padding: 0px 20px;\n"
                                      "border-radius: 15px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton#ubah_tiket:hover{\n"
                                      "background-color: rgb(239, 239, 239);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton#ubah_tiket:pressed{\n"
                                      "background-color: rgb(234, 234, 234);\n"
                                      "}")
        self.ubah_tiket.setText("Ubah Tiket")
        self.ubah_tiket.setObjectName("ubah_tiket")
        self.ubah_tiket.clicked.connect(self.open_ticket_result)

        self.ubah_cari = QtWidgets.QPushButton(self.form)
        self.ubah_cari.setGeometry(QtCore.QRect(1490, 61, 181, 62))
        self.ubah_cari.setFont(qfont(12, 'Epilogue', True, False, 75))
        self.ubah_cari.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ubah_cari.setStyleSheet("QPushButton#ubah_cari{\n"
                                     "background-color: #2abaa1;\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "padding: 0px 20px;\n"
                                     "border-radius: 15px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton#ubah_cari:pressed{\n"
                                     "background-color: #219a85;\n"
                                     "}\n"
                                     "\n"
                                     "")
        self.ubah_cari.setObjectName("ubah_cari")
        self.ubah_cari.setText('Menu Utama')
        self.ubah_cari.clicked.connect(self.open_homepage)

        self.groupBox_2 = QtWidgets.QGroupBox(self.form)
        self.groupBox_2.setGeometry(QtCore.QRect(335, 340, 481, 531))
        self.groupBox_2.setStyleSheet("border:none")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")

        for i in range(15):
            self.create_seat(i)

        self.form.show()


    def seat_selected(self, seat):
        self.selected_seat = seat


    def create_seat(self, index):
        font_seat = qfont(15, 'Epilogue', False, True)
        font_driver = qfont(10, 'Epilogue', False, True)

        seat = 'seat' + str(index)

        globals()[seat] = QtWidgets.QPushButton(self.groupBox_2)
        globals()[seat].setGeometry(QtCore.QRect(
            self.seat_dict[index][0], self.seat_dict[index][1], self.seat_width, self.seat_height))

        globals()[seat].setObjectName(seat)


        if self.get_data('Jenis') == "Innova":
            try:
                booked_seats = pd.read_excel('data/data_booking.xlsx', usecols=['Id Tiket', 'Seat'])
            except FileNotFoundError:
                booked_seats = pd.DataFrame(columns=['Id Tiket', 'Seat'])

            if index == 0:
                globals()[seat] = QtWidgets.QPushButton(self.groupBox_2)
                globals()[seat].setText('Driver')
                globals()[seat].setFont(font_driver)
                globals()[seat].setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
                globals()[seat].setStyleSheet("background-color: rgb(213, 63, 112);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius:35px;")
            else:
                globals()[seat] = QtWidgets.QPushButton(self.groupBox_2)
                globals()[seat].setText(str(index))
                globals()[seat].setFont(font_seat)
                globals()[seat].setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
                globals()[seat].setStyleSheet("QPushButton#%s{\nbackground-color: rgb(236, 236, 236);\nborder-radius:35px;\n"
                                                "\n}\n\n" % (seat))
                globals()[seat].setCheckable(False)
                globals()[seat].clicked.connect(lambda state, x=index: self.toggle_seat(x))
        else:
            try:
                booked_seats = pd.read_excel('data/data_booking.xlsx', usecols=['Id Tiket', 'Seat'])
            except FileNotFoundError:
                booked_seats = pd.DataFrame(columns=['Id Tiket', 'Seat'])

            if index == 0:
                globals()[seat] = QtWidgets.QPushButton(self.groupBox_2)
                globals()[seat].setText('Driver')
                globals()[seat].setFont(font_driver)
                globals()[seat].setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
                globals()[seat].setStyleSheet("background-color: rgb(213, 63, 112);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "border-radius:35px;")
            else:
                seat_number_text = str(index).zfill(2)
                if not booked_seats.empty and \
                        ((booked_seats['Seat'] == seat_number_text) & (booked_seats['Id Tiket'] == self.get_data('id'))).any():
                    globals()[seat] = QtWidgets.QPushButton(self.groupBox_2)
                    globals()[seat].setText(str(index))
                    globals()[seat].setFont(font_seat)
                    globals()[seat].setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
                    globals()[seat].setStyleSheet("QPushButton#%s{\nbackground-color: #d53f70;\nborder-radius:35px;\ncolor: rgb(255, 255, 255);\n"
                                                "\n}\n\n" % (seat))
                    globals()[seat].setEnabled(False)
                else:
                    globals()[seat] = QtWidgets.QPushButton(self.groupBox_2)
                    globals()[seat].setText(str(index))
                    globals()[seat].setFont(font_seat)
                    globals()[seat].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    globals()[seat].setStyleSheet("QPushButton#%s{\nbackground-color: rgb(236, 236, 236);\nborder-radius:35px;"
                                                "\n}\n\nQPushButton#%s:pressed, QPushButton#%s:checked{\nbackground-color: "
                                                "rgb(42, 186, 161);\ncolor: rgb(255, 255, 255);\n}" % (seat, seat, seat))
                    globals()[seat].setCheckable(True)
                    globals()[seat].clicked.connect(lambda state, x=index: self.toggle_seat(x))

        globals()[seat].setGeometry(QtCore.QRect(
            self.seat_dict[index][0], self.seat_dict[index][1], self.seat_width, self.seat_height))
        globals()[seat].setObjectName(seat)


    def toggle_seat(self, index):
        seat = 'seat' + str(index)
        checked = globals()[seat].isChecked()

        if checked:
            if self.selected_seat: 
                globals()[self.selected_seat].setChecked(False)

            self.selected_seat = seat

            self.bayar.setEnabled(True)
            seat_number_text = str(index).zfill(2)
            self.seat_number_text = seat_number_text
            self.seat_number.setText(seat_number_text)

        else:
            if self.selected_seat == seat:
                self.selected_seat = None

            self.seat_number.setText('-')

            if self.get_data('Jenis') == "Innova":
                self.bayar.setEnabled(True)
                QMessageBox.information(self.form, "Notice", "Kendaraan yang anda pilih adalah Innova. Tidak perlu memilih kursi.")

    def generate_random_code(self):
        random_uuid = uuid.uuid4()
        hex_string = random_uuid.hex
        random_code = int(hex_string[:5], 16)
        random_code = random_code % 100000
        random_code = str(random_code).zfill(5)
        return random_code
        


    def save_to_excel(self):
        payment_id = self.generate_random_code()

        tanggal = self.get_data('Tanggal').strftime('%Y-%m-%d')
        jam_keberangkatan = self.get_data('Jam Keberangkatan').strftime('%H:%M')
        jam_tujuan = self.get_data('Jam Tujuan').strftime('%H:%M')

        data_booking = {
            'Username': [self.username],
            'Id Tiket': [self.get_data('id')],
            'Id Pembayaran': [payment_id],  # Use the generated UUID
            'Tanggal': [tanggal],
            'Keberangkatan': [self.get_data('Keberangkatan')],
            'Tujuan': [self.get_data('Tujuan')],
            'Tm. Keberangkatan': [self.get_data('Tm. Keberangkatan')],
            'Tm. Tujuan': [self.get_data('Tm. Tujuan')],
            'Jam Keberangkatan': [jam_keberangkatan],  # Ubah ke format jam:menit
            'Jam Tujuan': [jam_tujuan],  # Ubah ke format jam:menit
            'Harga': [self.get_data('Harga')],
            'Jenis': [self.get_data('Jenis')],
            'Nama Travel': [self.get_data('Nama Travel')],
            'Status Pembayaran': ['Belum Bayar'],
            'Seat': [self.seat_number_text] if self.selected_seat else ['-']  # Atur '-' jika tidak ada kursi yang dipilih
              # Default status pembayaran
        }
        df = pd.DataFrame(data_booking)
        try:
            # Membaca file Excel
            book = pd.read_excel('data/data_booking.xlsx')
            # Menggabungkan data baru dengan data yang sudah ada
            book = pd.concat([book, df], ignore_index=True)
            # Menyimpan kembali ke file Excel
            book.to_excel('data/data_booking.xlsx', index=False)
        except FileNotFoundError:
            # Jika file tidak ditemukan, buat file baru
            df.to_excel('data/data_booking.xlsx', index=False)

        self.show_payment_popup(payment_id)
        


    def show_payment_popup(self, payment_id):
        msg = QMessageBox()
        msg.setWindowTitle("Kode Pembayaran")
        msg.setText("Kode Pembayaran Anda:")
        msg.setInformativeText(payment_id)
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        self.open_pembayaran(payment_id)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.form.setWindowTitle(_translate("Form", "Form"))

    def open_homepage(self):  # Modify to accept username parameter
        self.homepage_window = QtWidgets.QWidget()
        self.ui = homepage_2.Ui_Form(self.username)  # Pass the username to homepage_2.Ui_Form
        self.ui.setupUi(self.homepage_window)
        self.homepage_window.show()
        self.form.close()

    def open_ticket_result(self):  # Modify to accept username parameter
        self.tiket_window = QtWidgets.QWidget()
        self.ui = tiket.Ui_Form(
        self.username, self.get_data('Keberangkatan'), self.get_data('Tujuan'), str(self.get_data('Tanggal')))
        self.ui.setupUi(self.tiket_window)
        self.tiket_window.show()
        self.form.close()

    def open_pembayaran(self, id_pembayaran):
          # Modify to accept username parameter
        self.pembayaran_window = QtWidgets.QWidget()
        self.ui = pembayaran.Ui_Form(self.username, id_pembayaran)  # Pass the username to homepage_2.Ui_Form
        self.ui.setupUi(self.pembayaran_window)
        self.ui.setup_connections()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.setup_tombol()
        self.ui.setup_va()

        self.pembayaran_window.show()
        QtWidgets.QApplication.instance().activeWindow().close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form('123', 16)
    sys.exit(app.exec_())
