from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox


def qfont(point_size, family='Epilogue', bold=False, italic=False, weight=50):
    q_font = QtGui.QFont()
    q_font.setFamily(family)
    q_font.setPointSize(point_size)
    q_font.setBold(bold)
    q_font.setItalic(italic)
    q_font.setWeight(weight)

    return q_font


def error_message(message):
    QMessageBox.critical(None, 'Error', message)
