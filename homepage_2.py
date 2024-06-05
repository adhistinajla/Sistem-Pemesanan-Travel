import os, sys, csv, res_home, tiket
import login_new
import pandas as pd, random

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QDateEdit, QPushButton, QMessageBox, QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QObject, pyqtSignal, Qt


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
        Form.setFixedSize(1920, 1080)

        self.bgpolos = QtWidgets.QLabel(Form)
        self.bgpolos.setGeometry(QtCore.QRect(0, 139, 1920, 941))
        self.bgpolos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bgpolos.setText("")
        self.bgpolos.setObjectName("bgpolos")

        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignRight)
        self.label.setGeometry(QtCore.QRect(1345, 65, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Epilogue SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label.setFont(font)
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

        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(0, 129, 1920, 1100))
        self.scrollArea.setStyleSheet("QScrollArea{\n"
        "background:transparent;\n"
        "border:none;}\n"
        "\n"
        "            }\n"
        "            QScrollBar:vertical {\n"
        "                background:transparent;\n"
        "                width: 15px;\n"
        "                margin: 0px 0px 0px 0px;\n"
        "            }\n"
        "            QScrollBar::handle:vertical {\n"
        ";\n"
        ";\n"
        "    background-color: rgb(213, 224, 240);\n"
        "                min-height: 20px;\n"
        "                border-radius: 7px;\n"
        "            }\n"
        "            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
        "                border: none;\n"
        "                background:transparent;\n"
        "            }\n"
        "            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
        "                background:transparent;\n"
        "            }\n"
        "            QScrollBar:horizontal {\n"
        "                border: none;\n"
        "                background:transparent;\n"
        "                height: 15px;\n"
        "                margin: 0px 0px 0px 0px;\n"
        "            }\n"
        "            QScrollBar::handle:horizontal {\n"
        "                background-color: rgb(213, 224, 240);\n"
        "                min-height: 20px;\n"
        "                border-radius: 7px;\n"
        "            }\n"
        "            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
        "                border: none;\n"
        "                background: none;\n"
        "            }\n"
        "            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
        "                background: none;")
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -1958, 1936, 3050))
        self.scrollAreaWidgetContents.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(0, 2000))
        self.frame.setStyleSheet("background: none")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")

        self.ads1_dummy_button = QtWidgets.QPushButton(self.frame)
        self.ads1_dummy_button.setGeometry(QtCore.QRect(240, 306, 621, 336))
        self.ads1_dummy_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.ads1_dummy_button.clicked.connect(self.set_destination_jogja)

        self.ads1 = QtWidgets.QLabel(self.frame)
        self.ads1.setGeometry(QtCore.QRect(240, 305, 621, 341))
        self.ads1.setStyleSheet("image: url(:/images/img/ads1.png);")
        self.ads1.setText("")
        self.ads1.setObjectName("ads1")
        

        self.ads2 = QtWidgets.QLabel(self.frame)
        self.ads2.setGeometry(QtCore.QRect(880, 306, 777, 341))
        self.ads2.setStyleSheet("image: url(:/images/img/ads2.png);")
        self.ads2.setText("")
        self.ads2.setObjectName("ads2")
        self.ads2_dummy_button = QtWidgets.QPushButton(self.frame)
        self.ads2_dummy_button.setGeometry(QtCore.QRect(880, 306, 776, 338))
        self.ads2_dummy_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.ads2_dummy_button.clicked.connect(self.ads2_dummy_button_clicked)

        self.jadwal_judul = QtWidgets.QLabel(self.frame)
        self.jadwal_judul.setGeometry(QtCore.QRect(720, 20, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Epilogue")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.jadwal_judul.setFont(font)
        self.jadwal_judul.setStyleSheet("border-image: url(:/images/img/text_atas.png);")
        self.jadwal_judul.setText("")
        self.jadwal_judul.setAlignment(QtCore.Qt.AlignCenter)
        self.jadwal_judul.setObjectName("jadwal_judul")

        self.jadwal_border = QtWidgets.QLabel(self.frame)
        self.jadwal_border.setGeometry(QtCore.QRect(239, 750, 1419, 671))
        self.jadwal_border.setStyleSheet("background-color: rgb(225, 236, 254);\n"
            "border-radius:30px;")
        self.jadwal_border.setText("")
        self.jadwal_border.setObjectName("jadwal_border")

        self.jadwal = QtWidgets.QLabel(self.frame)
        self.jadwal.setGeometry(QtCore.QRect(280, 790, 1339, 591))
        self.jadwal.setStyleSheet("background-color: rgb(255, 255, 255);\n"
            "border-radius:30px;")
        self.jadwal.setText("")
        self.jadwal.setObjectName("jadwal")

        self.tujuan = QtWidgets.QComboBox(self.frame)
        self.tujuan.setGeometry(QtCore.QRect(733, 136, 191, 41))
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
            "}\n"
            "\n"
            "\n"
            "QComboBox QAbstractItemView{\n"
            "border:none;\n"
            "background-color: rgb(255, 255, 255);}")
        self.tujuan.setObjectName("tujuan")
        destinations = self.get_destinations('data/tujuan.csv')
        self.tujuan.addItems(destinations)
        self.tujuan.setCurrentText('Semarang')

        self.cari = QtWidgets.QPushButton(self.frame)
        self.cari.setGeometry(QtCore.QRect(1416, 90, 218, 114))
        font = QtGui.QFont()
        font.setFamily("Poppins")
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

        self.platform = QtWidgets.QLabel(self.frame)
        self.platform.setGeometry(QtCore.QRect(240, 72, 1420, 149))
        self.platform.setStyleSheet("background-color: rgb(255, 255, 255);\n"
            "border-color: rgb(213, 213, 213);\n"
            "border-radius:40px;\n"
            "border : none;")
        self.platform.setText("")
        self.platform.setObjectName("platform")

        self.bgtujuan = QtWidgets.QLabel(self.frame)
        self.bgtujuan.setGeometry(QtCore.QRect(650, 76, 361, 140))
        self.bgtujuan.setStyleSheet("image: url(:/images/img/untuk tujuan.png);")
        self.bgtujuan.setText("")
        self.bgtujuan.setObjectName("bgtujuan")

        self.bgberangkat = QtWidgets.QLabel(self.frame)
        self.bgberangkat.setGeometry(QtCore.QRect(262, 76, 361, 140))
        self.bgberangkat.setStyleSheet("image: url(:/images/img/berangkat dari.png);")
        self.bgberangkat.setText("")
        self.bgberangkat.setObjectName("bgberangkat")
        

        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(1118, 138, 171, 41))
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
            "}\n"
            "\n"
            "QCalendarWidget {\n"
            "        background: transparent;\n"
            "    }\n"
            "    QCalendarWidget > #dateEdit {\n"
            "        /* background for calendar dates */\n"
            "        background: rgba(204, 204, 204, 127);\n"
            "        /* \n"
            "            default background for headers, can be overridden by using\n"
            "            QCalendarWidget.setHeaderTextFormat()\n"
            "        */\n"
            "        alternate-background-color: rgba(127, 127, 127, 127);}")
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        qdate = QtCore.QDate.currentDate()
        qdate.setDate(2024, 6, 1)
        self.dateEdit.setDate(qdate)

        self.bgtujuan_2 = QtWidgets.QLabel(self.frame)
        self.bgtujuan_2.setGeometry(QtCore.QRect(1030, 76, 361, 140))
        self.bgtujuan_2.setStyleSheet("image: url(:/images/img/tanggal berangkat.png);")
        self.bgtujuan_2.setText("")
        self.bgtujuan_2.setObjectName("bgtujuan_2")

        self.berangkat = QtWidgets.QComboBox(self.frame)
        self.berangkat.setGeometry(QtCore.QRect(345, 136, 191, 41))
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
            "}\n"
            "\n"
            "QComboBox QAbstractItemView{\n"
            "border:none;\n"
            "background-color: rgb(255, 255, 255);}\n"
            "")
        self.berangkat.setInputMethodHints(QtCore.Qt.ImhNone)
        self.berangkat.setDuplicatesEnabled(False)
        self.berangkat.setObjectName("berangkat")
        destinations = self.get_destinations('data/keberangkatan.csv')
        self.berangkat.addItems(destinations)
        self.berangkat.setCurrentText('Surakarta')

        self.text_jadwal_minggu_ini = QtWidgets.QLabel(self.frame)
        self.text_jadwal_minggu_ini.setGeometry(QtCore.QRect(239, 670, 431, 61))
        font = QtGui.QFont()
        font.setFamily("Epilogue ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.text_jadwal_minggu_ini.setFont(font)
        self.text_jadwal_minggu_ini.setObjectName("text_jadwal_minggu_ini")

        self.bg_scroll = QtWidgets.QLabel(self.frame)
        self.bg_scroll.setEnabled(True)
        self.bg_scroll.setGeometry(QtCore.QRect(0, -150, 1920, 436))
        self.bg_scroll.setStyleSheet("image: url(:/images/img/atas.png);")
        self.bg_scroll.setText("")
        self.bg_scroll.setObjectName("bg_scroll")
        
        self.ads3_perjalanan = QtWidgets.QLabel(self.frame)
        self.ads3_perjalanan.setGeometry(QtCore.QRect(240, 1540, 1421, 601))
        self.ads3_perjalanan.setStyleSheet("image: url(:/images/img/ads3.png);")
        self.ads3_perjalanan.setText("")
        self.ads3_perjalanan.setObjectName("ads3_perjalanan")

        self.judul_perjalanan_anda = QtWidgets.QLabel(self.frame)
        self.judul_perjalanan_anda.setGeometry(QtCore.QRect(240, 1460, 431, 61))
        font = QtGui.QFont()
        font.setFamily("Epilogue ExtraBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.judul_perjalanan_anda.setFont(font)
        self.judul_perjalanan_anda.setObjectName("judul_perjalanan_anda")

        self.ads4_review = QtWidgets.QLabel(self.frame)
        self.ads4_review.setGeometry(QtCore.QRect(240, 2190, 1421, 361))
        self.ads4_review.setStyleSheet("image: url(:/images/img/review_home.png);")
        self.ads4_review.setText("")
        self.ads4_review.setObjectName("ads4_review")

        self.ads5_about = QtWidgets.QLabel(self.frame)
        self.ads5_about.setGeometry(QtCore.QRect(240, 2610, 1421, 261))
        self.ads5_about.setStyleSheet("image: url(:/images/img/about_home.png);")
        self.ads5_about.setText("")
        self.ads5_about.setObjectName("ads5_about")

        self.jadwal_pandas = QtWidgets.QTableWidget(self.frame)
        self.jadwal_pandas.setGeometry(QtCore.QRect(320, 820, 1271, 531))
        self.jadwal_pandas.setStyleSheet("border:none")
        self.jadwal_pandas.setObjectName("jadwal_pandas")
        self.jadwal_pandas.setStyleSheet("QTableWidget{\n"
        "border:none;}\n"
        "\n"
        "            }\n"
        "            QScrollBar:vertical {\n"
        "                background:transparent;\n"
        "                width: 8px;\n"
        "                margin: 0px 0px 0px 0px;\n"
        "            }\n"
        "            QScrollBar::handle:vertical {\n"
        ";\n"
        ";\n"
        "    background-color: rgb(213, 224, 240);\n"
        "                min-height: 20px;\n"
        "                border-radius: 3px;\n"
        "            }\n"
        "            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
        "                border: none;\n"
        "                background:transparent;\n"
        "            }\n"
        "            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
        "                background:transparent;\n"
        "            }\n"
        "            QScrollBar:horizontal {\n"
        "                border: none;\n"
        "                background:transparent;\n"
        "                height: 8px;\n"
        "                margin: 0px 0px 0px 0px;\n"
        "            }\n"
        "            QScrollBar::handle:horizontal {\n"
        "                background-color: rgb(213, 224, 240);\n"
        "                min-height: 20px;\n"
        "                border-radius: 3px;\n"
        "            }\n"
        "            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
        "                border: none;\n"
        "                background: none;\n"
        "            }\n"
        "            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
        "                background: none;")

        self.jadwal_pandas.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        df = pd.read_excel("data/data_destinasi.xlsx", converters={'Tanggal': pd.to_datetime})

        if 'id' in df.columns:
            df = df.drop(columns=['id'])

        today = pd.Timestamp.now()
        one_week_later = today + pd.Timedelta(weeks=1)
        df = df[(df['Tanggal'] >= today) & (df['Tanggal'] <= one_week_later)]

        self.jadwal_pandas.setRowCount(df.shape[0])
        self.jadwal_pandas.setColumnCount(df.shape[1])
        self.jadwal_pandas.setHorizontalHeaderLabels(df.columns)

        harga_column_index = df.columns.get_loc('Harga')

        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                value = df.iloc[i, j]
                if isinstance(value, pd.Timestamp):  # Format kolom Tanggal
                    value = value.strftime('%Y-%m-%d')  # Ubah format tanggal
                elif j == harga_column_index:  # Ganti dengan indeks kolom harga
                    value = "{:,.2f}".format(value).replace(',', '.')  # Format harga dengan pemisah "."
                elif df.columns[j] == 'Jam Keberangkatan':  # Ubah format jam menjadi jam, menit
                    value = value.strftime('%H:%M')
                elif df.columns[j] == 'Jam Tujuan':  # Ubah format jam menjadi jam, menit
                    value = value.strftime('%H:%M')  # Ubah format jam
                self.jadwal_pandas.setItem(i, j, QTableWidgetItem(str(value)))


        self.copyright_kotak = QtWidgets.QLabel(self.frame)
        self.copyright_kotak.setGeometry(QtCore.QRect(-10, 2809, 1921, 101))
        self.copyright_kotak.setStyleSheet("background-color: rgb(242, 247, 254);")
        self.copyright_kotak.setText("")
        self.copyright_kotak.setObjectName("copyright_kotak")




        self.bg_scroll.raise_()
        self.ads1.raise_()
        self.ads2.raise_()
        self.ads1_dummy_button.raise_()
        self.ads2_dummy_button.raise_()
        self.jadwal_judul.raise_()
        self.jadwal_border.raise_()
        self.jadwal.raise_()
        self.platform.raise_()
        self.bgtujuan_2.raise_()
        self.cari.raise_()
        self.bgtujuan.raise_()
        self.bgberangkat.raise_()
        self.dateEdit.raise_()
        self.berangkat.raise_()
        self.tujuan.raise_()
        self.text_jadwal_minggu_ini.raise_()
        self.jadwal_pandas.raise_()
        self.copyright_kotak.raise_()
        self.ads3_perjalanan.raise_()
        self.judul_perjalanan_anda.raise_()
        self.ads4_review.raise_()
        self.ads5_about.raise_()
        self.verticalLayout.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.bg_nutupi_scroll = QtWidgets.QLabel(Form)
        self.bg_nutupi_scroll.setEnabled(True)
        self.bg_nutupi_scroll.setGeometry(QtCore.QRect(0, 0, 1920, 142))
        self.bg_nutupi_scroll.setStyleSheet("image: url(:/images/img/atas_scroll.png);")
        self.bg_nutupi_scroll.setText("")
        self.bg_nutupi_scroll.setObjectName("bg_nutupi_scroll")
        self.bgpolos.raise_()
        self.scrollArea.raise_()
        self.bg_nutupi_scroll.raise_()
        self.label.raise_()
        self.profil.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

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
        self.text_jadwal_minggu_ini.setText(_translate("Form", "Jadwal Minggu Ini"))
        self.judul_perjalanan_anda.setText(_translate("Form", "Perjalanan Anda"))

    def set_column_width_by_name(self):
        self.set_column_width('Harga', 120)
        self.set_column_width('Tujuan', 150)
        self.set_column_width('Jam Tujuan', 150)
        self.set_column_width('Jenis', 100)

    def set_column_width(self, column_name, width):
        column_index = self.get_column_index(column_name)
        if column_index is not None:
            self.jadwal_pandas.setColumnWidth(column_index, width)

    def get_column_index(self, column_name):
        for col in range(self.jadwal_pandas.columnCount()):
            if self.jadwal_pandas.horizontalHeaderItem(col).text() == column_name:
                return col
        return None

    def get_column_index(self, column_name):
        for col in range(self.jadwal_pandas.columnCount()):
            if self.jadwal_pandas.horizontalHeaderItem(col).text() == column_name:
                return col
        return None


    def ads2_dummy_button_clicked(self):
        try:
            df = pd.read_excel("data/diskon.xlsx")
            kode_diskon_list = df['Kode Diskon'].tolist()
            diskon_list = df['Diskon'].tolist()

            if kode_diskon_list and diskon_list:
                index = random.randint(0, len(kode_diskon_list) - 1)
                kode_diskon = kode_diskon_list[index]
                diskon = diskon_list[index] * 100  # Konversi diskon ke persen
                diskon_str = f"{diskon:g}%"  # Format diskon tanpa trailing zeros

                message = QMessageBox()
                message.setWindowTitle("Kode Diskon")
                message.setIcon(QMessageBox.Information)
                message.setText(f"Kode Diskon Anda  : {kode_diskon}\nDiskon                      : {diskon_str}")
                message.setStandardButtons(QMessageBox.Ok)
                message.setDefaultButton(QMessageBox.Ok)
                copy_button = message.addButton("Copy Kode", QMessageBox.ActionRole)

                result = message.exec_()

                if result == QMessageBox.Ok:
                    pass
                elif message.clickedButton() == copy_button:
                    clipboard = QApplication.clipboard()
                    clipboard.setText(kode_diskon)
            else:
                QMessageBox.warning(None, "Peringatan", "Tidak ada kode diskon yang tersedia.")
        except Exception as e:
            QMessageBox.critical(None, "Kesalahan", f"Terjadi kesalahan: {e}")


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

    def show_profile_popup(self):
        message = QMessageBox()
        message.setWindowTitle("Profile")
        message.setIcon(QMessageBox.Information)
        message.setText(f"Nama                    : {self.username}\nNomor Telepon    : {self.phone_number}")
        message.addButton(QMessageBox.Ok)
        logout_button = message.addButton("Logout", QMessageBox.RejectRole)
        
        result = message.exec_()
        
        if message.clickedButton() == logout_button:
            # User clicked Logout
            self.open_login()
        elif result == QMessageBox.Ok:
            # User clicked OK, do nothing
            pass
        elif result == QMessageBox.Rejected:
            # User closed the dialog without clicking Logout
            pass

    def open_login(self):
        self.login_new_window = QtWidgets.QWidget()
        self.ui = login_new.Ui_Form()
        self.ui.setupUi(self.login_new_window)
        self.login_new_window.show()
        QtWidgets.QApplication.instance().activeWindow().close()


    def set_destination_jogja(self):
        self.tujuan.setCurrentText("Yogyakarta")
        QMessageBox.information(None, "Informasi", "Tujuan telah diset ke Yogyakarta.")



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