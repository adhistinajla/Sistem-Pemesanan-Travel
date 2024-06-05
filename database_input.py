import sys
import os
import pandas as pd
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QComboBox, QDateEdit, QPushButton, QTableWidget,
                             QTableWidgetItem, QMessageBox, QFormLayout, QSpinBox)
from PyQt5.QtCore import QDate
from openpyxl import load_workbook
from datetime import datetime

class DestinationSelector(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pemilihan Destinasi Wisata")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.search_layout = QVBoxLayout()
        self.add_search_fields()
        layout.addLayout(self.search_layout)

        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.results_layout = QVBoxLayout()
        layout.addLayout(self.results_layout)

        self.load_data_button = QPushButton("Load Data")
        self.load_data_button.clicked.connect(self.load_data)
        layout.addWidget(self.load_data_button)

        self.add_data_fields(layout)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.load_data()

    def add_search_fields(self):
        search_fields_layout = QHBoxLayout()

        self.departure_label = QLabel("Keberangkatan:")
        self.departure_combobox = QComboBox()
        search_fields_layout.addWidget(self.departure_label)
        search_fields_layout.addWidget(self.departure_combobox)

        self.destination_label = QLabel("Tujuan:")
        self.destination_combobox = QComboBox()
        search_fields_layout.addWidget(self.destination_label)
        search_fields_layout.addWidget(self.destination_combobox)

        self.date_label = QLabel("Tanggal:")
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        search_fields_layout.addWidget(self.date_label)
        search_fields_layout.addWidget(self.date_edit)

        self.search_layout.addLayout(search_fields_layout)

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_data)
        self.search_layout.addWidget(self.search_button)

    def load_data(self):
        df = pd.read_excel("data/data_destinasi.xlsx", converters={'Tanggal': pd.to_datetime})
        self.update_filters(df)
        self.table.setRowCount(df.shape[0])
        self.table.setColumnCount(df.shape[1])
        self.table.setHorizontalHeaderLabels(df.columns)

        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                self.table.setItem(i, j, QTableWidgetItem(str(df.iloc[i, j])))

    def search_data(self):
        departure = self.departure_combobox.currentText()
        destination = self.destination_combobox.currentText()
        date = self.date_edit.date().toString("yyyy-MM-dd")

        df = pd.read_excel("data/data_destinasi.xlsx", converters={'Tanggal': pd.to_datetime})

        if not departure and not destination and not date:
            self.load_data()
            return

        if departure:
            df = df[df['Keberangkatan'] == departure]
            if df.empty:
                QMessageBox.information(self, "Pencarian", f"Tidak ada data dengan keberangkatan {departure}.")
                return
        if destination:
            df = df[df['Tujuan'] == destination]
            if df.empty:
                QMessageBox.information(self, "Pencarian", f"Tidak ada data dengan tujuan {destination}.")
                return
        if date:
            df = df[df['Tanggal'].dt.strftime('%Y-%m-%d') == date]
            if df.empty:
                QMessageBox.information(self, "Pencarian", f"Tidak ada data pada tanggal {date}.")
                return

        if not df.empty:
            result_text = "Hasil Pencarian:\n\n"
            for index, row in df.iterrows():
                result_text += (
                    f"Keberangkatan dari {row['Keberangkatan']} menuju {row['Tujuan']} pada tanggal {row['Tanggal'].strftime('%d-%m-%Y')}:\n"
                    f"Tm. Keberangkatan: {row['Tm. Keberangkatan']}\n"
                    f"Tm. Tujuan: {row['Tm. Tujuan']}\n"
                    f"Jam Keberangkatan: {row['Jam Keberangkatan']}\n"
                    f"Jam Tujuan: {row['Jam Tujuan']}\n"
                    f"Harga: {row['Harga']}\n"
                    f"Jenis: {row['Jenis']}\n"
                    f"Nama Travel: {row['Nama Travel']}\n\n"
                )

            QMessageBox.information(self, "Pencarian", result_text)

        self.table.setRowCount(df.shape[0])
        self.table.setColumnCount(df.shape[1])
        self.table.setHorizontalHeaderLabels(df.columns)

        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                self.table.setItem(i, j, QTableWidgetItem(str(df.iloc[i, j])))

    def update_filters(self, df=None):
        if df is None:
            df = pd.read_excel("data/data_destinasi.xlsx", converters={'Tanggal': pd.to_datetime})

        self.departure_combobox.clear()
        self.departure_combobox.addItems(df['Keberangkatan'].unique().tolist())

        self.destination_combobox.clear()
        self.destination_combobox.addItems(df['Tujuan'].unique().tolist())

        self.date_edit.setDate(QDate.currentDate())

    def add_data_fields(self, layout):
        add_data_layout = QFormLayout()

        self.new_data_inputs = {}

        cities = ["Malang", "Bali", "Surakarta", "Jakarta", "Surabaya", "Semarang", "Jogja", "Bandung"]
        fields = ['id', 'Tanggal', 'Keberangkatan', 'Tujuan', 'Tm. Keberangkatan', 'Tm. Tujuan', 'Jam Keberangkatan',
                  'Jam Tujuan', 'Harga', 'Jenis', 'Nama Travel']

        for field in fields:
            if field == 'id':
                id_spinbox = QSpinBox()
                id_spinbox.setMinimum(1)  # Set minimum ID value
                id_spinbox.setMaximum(99999)  # Set maximum ID value
                self.new_data_inputs[field] = id_spinbox
                add_data_layout.addRow(QLabel(f'{field}:'), id_spinbox)
            elif field == 'Tanggal':
                date_edit = QDateEdit()
                date_edit.setCalendarPopup(True)
                self.new_data_inputs[field] = date_edit
                add_data_layout.addRow(QLabel(f'{field}:'), date_edit)
            elif field in ['Keberangkatan', 'Tujuan']:
                combo_box = QComboBox()
                combo_box.addItems(cities)
                self.new_data_inputs[field] = combo_box
                add_data_layout.addRow(QLabel(f'{field}:'), combo_box)
            elif field == 'Jenis':
                combo_box = QComboBox()
                combo_box.addItems(['Hiace', 'Innova'])
                self.new_data_inputs[field] = combo_box
                add_data_layout.addRow(QLabel(f'{field}:'), combo_box)
            else:
                input_line = QLineEdit()
                self.new_data_inputs[field] = input_line
                add_data_layout.addRow(QLabel(f'{field}:'), input_line)

        self.submit_button = QPushButton('Tambah Data')
        self.submit_button.clicked.connect(self.add_data)
        add_data_layout.addRow(self.submit_button)

        layout.addLayout(add_data_layout)
        self.update_new_id()

    def update_new_id(self):
        df = pd.read_excel("data/data_destinasi.xlsx", converters={'Tanggal': pd.to_datetime})
        if not df.empty:
            max_id = df['id'].max()
            new_id = max_id + 1
        else:
            new_id = 1
        self.new_data_inputs['id'].setValue(new_id)

    def add_data(self):
        data = {field: self.new_data_inputs[field].currentText() if isinstance(self.new_data_inputs[field], QComboBox)
                else self.new_data_inputs[field].date().toString("yyyy-MM-dd") if isinstance(self.new_data_inputs[field], QDateEdit)
                else self.new_data_inputs[field].text() for field in self.new_data_inputs}

        if any(value == '' for value in data.values()):
            QMessageBox.warning(self, 'Peringatan', 'Semua field harus diisi!')
            return

        if data['Keberangkatan'] == data['Tujuan']:
            QMessageBox.warning(self, 'Peringatan', 'Kota keberangkatan dan kota tujuan sama, tidak bisa ditambah!')
            return

        file_path = 'data/data_destinasi.xlsx'

        if os.path.exists(file_path):
            wb = load_workbook(file_path)
            sheet = wb.active
        else:
            QMessageBox.critical(self, 'Error', 'File data_destinasi.xlsx tidak ditemukan!')
            return

        new_row = list(data.values())
        sheet.append(new_row)
        wb.save(file_path)

        QMessageBox.information(self, 'Berhasil', 'Data berhasil ditambahkan!')

        for input_line in self.new_data_inputs.values():
            if isinstance(input_line, QLineEdit) and not input_line.isReadOnly():
                input_line.clear()
            elif isinstance(input_line, QComboBox):
                input_line.setCurrentIndex(0)
            elif isinstance(input_line, QDateEdit):
                input_line.setDate(QDate.currentDate())
        self.update_filters()
        self.update_new_id()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = DestinationSelector()
    main_window.show()
    sys.exit(app.exec_())
