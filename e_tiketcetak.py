import csv
import sys
import res_e_tiket
from PyQt5 import QtWidgets, QtGui, QtCore, QtPrintSupport
import pandas as pd
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QFileDialog
from PyQt5.QtGui import QRegExpValidator, QIcon, QPixmap
from PyQt5.QtCore import QRegExp
import qrcode
import os


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(794, 1123)

        self.bg = QtWidgets.QLabel(Form)
        self.bg.setGeometry(QtCore.QRect(0, 0, 794, 1123))
        self.bg.setStyleSheet("image: url(:/images/img/e-tiket_bg.png);")
        self.bg.setText("")
        self.bg.setObjectName("bg")

        self.id_pembayaran = QtWidgets.QLabel(Form)
        self.id_pembayaran.setGeometry(QtCore.QRect(70, 225, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Epilogue Medium")
        font.setPointSize(14)
        self.id_pembayaran.setFont(font)    
        self.id_pembayaran.setObjectName("id_pembayaran")
        self.nama_biodata = QtWidgets.QLabel(Form)
        self.nama_biodata.setGeometry(QtCore.QRect(580, 226, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Epilogue Medium")
        font.setPointSize(8)
        self.nama_biodata.setFont(font)
        self.nama_biodata.setObjectName("nama_biodata")
        self.telepon_biodata = QtWidgets.QLabel(Form)
        self.telepon_biodata.setGeometry(QtCore.QRect(580, 252, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Epilogue Medium")
        font.setPointSize(8)
        self.telepon_biodata.setFont(font)
        self.telepon_biodata.setObjectName("telepon_biodata")
        self.tanggal_pesanan = QtWidgets.QLabel(Form)
        self.tanggal_pesanan.setGeometry(QtCore.QRect(580, 279, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Epilogue Medium")
        font.setPointSize(8)
        self.tanggal_pesanan.setFont(font)
        self.tanggal_pesanan.setObjectName("tanggal_pesanan")
        self.travel = QtWidgets.QLabel(Form)
        self.travel.setGeometry(QtCore.QRect(93, 501, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Epilogue Medium")
        font.setPointSize(7)
        self.travel.setFont(font)
        self.travel.setObjectName("travel")
        self.jenis_travel = QtWidgets.QLabel(Form)
        self.jenis_travel.setGeometry(QtCore.QRect(219, 501, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Epilogue Medium")
        font.setPointSize(7)
        self.jenis_travel.setFont(font)
        self.jenis_travel.setObjectName("jenis_travel")
        self.tanggal_keberangkatan = QtWidgets.QLabel(Form)
        self.tanggal_keberangkatan.setGeometry(QtCore.QRect(340, 501, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Epilogue Medium")
        font.setPointSize(7)
        self.tanggal_keberangkatan.setFont(font)
        self.tanggal_keberangkatan.setObjectName("tanggal_keberangkatan")
        self.tanggal_tiba = QtWidgets.QLabel(Form)
        self.tanggal_tiba.setGeometry(QtCore.QRect(539, 501, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Epilogue Medium")
        font.setPointSize(7)
        self.tanggal_tiba.setFont(font)
        self.tanggal_tiba.setObjectName("tanggal_tiba")
        self.terminal_keberangkatan = QtWidgets.QLabel(Form)
        self.terminal_keberangkatan.setGeometry(QtCore.QRect(340, 520, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Epilogue Medium")
        font.setPointSize(7)
        self.terminal_keberangkatan.setFont(font)
        self.terminal_keberangkatan.setObjectName("terminal_keberangkatan")
        self.terminal_tiba = QtWidgets.QLabel(Form)
        self.terminal_tiba.setGeometry(QtCore.QRect(538, 520, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Epilogue Medium")
        font.setPointSize(7)
        self.terminal_tiba.setFont(font)
        self.terminal_tiba.setObjectName("terminal_tiba")
        self.kota_keberangkatan = QtWidgets.QLabel(Form)
        self.kota_keberangkatan.setGeometry(QtCore.QRect(339, 538, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Epilogue Medium")
        font.setPointSize(7)
        self.kota_keberangkatan.setFont(font)
        self.kota_keberangkatan.setObjectName("kota_keberangkatan")
        self.kota_tiba = QtWidgets.QLabel(Form)
        self.kota_tiba.setGeometry(QtCore.QRect(538, 538, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Epilogue Medium")
        font.setPointSize(7)
        self.kota_tiba.setFont(font)
        self.kota_tiba.setObjectName("kota_tiba")
        self.nama_penumpang = QtWidgets.QLabel(Form)
        self.nama_penumpang.setGeometry(QtCore.QRect(93, 743, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Epilogue Medium")
        font.setPointSize(7)
        self.nama_penumpang.setFont(font)
        self.nama_penumpang.setObjectName("nama_penumpang")
        self.nomer_kursi = QtWidgets.QLabel(Form)
        self.nomer_kursi.setGeometry(QtCore.QRect(304, 743, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Epilogue Medium")
        font.setPointSize(7)
        self.nomer_kursi.setFont(font)
        self.nomer_kursi.setObjectName("nomer_kursi")
        self.id_tiket = QtWidgets.QLabel(Form)
        self.id_tiket.setGeometry(QtCore.QRect(488, 744, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Epilogue Medium")
        font.setPointSize(7)
        self.id_tiket.setFont(font)
        self.id_tiket.setObjectName("id_tiket")
        self.export_pdf = QtWidgets.QPushButton(Form)
        self.export_pdf.setGeometry(QtCore.QRect(650, 1010, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Epilogue SemiBold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.export_pdf.setFont(font)
        self.export_pdf.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.export_pdf.setStyleSheet("QPushButton#export_pdf{\n"
"background-color: #2abaa1;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton#export_pdf:pressed{\n"
"background-color: #219a85;\n"
"}\n"
"\n"
"")
        self.export_pdf.setObjectName("export_pdf")
        self.export_pdf.clicked.connect(lambda: self.exportToPDF(Form))

        self.qrcode = QtWidgets.QLabel(Form)
        self.qrcode.setGeometry(QtCore.QRect(288, 253, 100, 100))
        self.qrcode.setText("")
        self.qrcode.setObjectName("qrcode")
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.populate_labels_from_excel()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.export_pdf.setText(_translate("Form", "Save"))


    def populate_labels_from_excel(self):  # Modified method signature
        # Baca file Excel
        try:
            df = pd.read_excel('data/data_booking.xlsx')
        except FileNotFoundError:
            print("File data_booking.xlsx tidak ditemukan.")
            return

        try:
            df_user = pd.read_csv('data/user_data.csv')
        except FileNotFoundError:
            print("File user_data.csv tidak ditemukan.")
            return

        last_row_booking = df.iloc[-1]
        username = last_row_booking['Username']
        nomor_telepon = df_user.loc[df_user['username'] == username, 'nomor_telepon'].values

        if nomor_telepon:
            self.telepon_biodata.setText(str(nomor_telepon[0]))
        else:
            print("Nomor telepon tidak ditemukan untuk username tersebut.")

        last_row = df.iloc[-1]


        self.id_pembayaran.setText(str(last_row['Id Pembayaran']))
        self.nama_biodata.setText(last_row['Username'])
        self.tanggal_pesanan.setText(str(last_row['Tanggal']))
        self.travel.setText(last_row['Nama Travel'])
        self.jenis_travel.setText(last_row['Jenis'])
        tanggal_keberangkatan = f"{last_row['Tanggal']} {last_row['Jam Keberangkatan']}"
        tanggal_tiba = f"{last_row['Tanggal']} {last_row['Jam Tujuan']}"
        self.tanggal_keberangkatan.setText(tanggal_keberangkatan)
        self.tanggal_tiba.setText(tanggal_tiba)
        self.terminal_keberangkatan.setText(last_row['Tm. Keberangkatan'])
        self.terminal_tiba.setText(last_row['Tm. Tujuan'])
        self.kota_keberangkatan.setText(last_row['Keberangkatan'])
        self.kota_tiba.setText(last_row['Tujuan'])
        self.nama_penumpang.setText(last_row['Username'])
        self.nomer_kursi.setText(str(last_row['Seat']))
        self.id_tiket.setText(str(last_row['Id Tiket']))
        self.generate_qr_code()


    def generate_qr_code(self):
        # Ubah teks self.id_pembayaran menjadi string jika belum dalam bentuk string
        data = str(self.id_pembayaran.text())

        # Buat objek QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # Tambahkan data QR code
        qr.add_data(data)
        qr.make(fit=True)

        # Buat gambar QR code
        img = qr.make_image(fill_color="black", back_color="white")

        # Simpan gambar QR code dalam file PNG
        img.save("img/qrcode.png")
        pixmap = QtGui.QPixmap("img/qrcode.png").scaled(100, 100)
        self.qrcode.setPixmap(pixmap)
        
    def exportToPDF(self, Form):
        # Munculkan dialog penyimpanan file
        file_path, filter_selected = QFileDialog.getSaveFileName(None, "Simpan e-Tiket", "", "PDF Files (*.pdf);;JPEG Files (*.jpg);;PNG Files (*.png)")

        if file_path:
            if filter_selected == "PDF Files (*.pdf)":
                printer = QPrinter(QPrinter.HighResolution)
                printer.setOutputFormat(QPrinter.PdfFormat)
                printer.setOutputFileName(file_path)

                # Menggunakan lebar jendela utama dari objek Ui_Form
                scale_factor = printer.pageRect().width() / float(Form.width())

                transform = QtGui.QTransform()
                transform.scale(scale_factor, scale_factor)

                painter = QtGui.QPainter(printer)
                painter.setTransform(transform)

                Form.render(painter)  # Menggunakan objek form dari Ui_Form

                painter.end()

                QMessageBox.information(None, "Export PDF", "e-Tiket berhasil dibuat dalam bentuk PDF.", QMessageBox.Ok)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    Form.setWindowIcon(QIcon('img/icon.png'))
    ui = Ui_Form()
    ui.setupUi(Form)
  # Call the method to populate labels from Excel
    Form.show()
    sys.exit(app.exec_())
    