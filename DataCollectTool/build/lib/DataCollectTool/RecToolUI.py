# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecToolUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(658, 452)
        self.title_label = QtWidgets.QLabel(Dialog)
        self.title_label.setGeometry(QtCore.QRect(140, 50, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.record_button = QtWidgets.QPushButton(Dialog)
        self.record_button.setGeometry(QtCore.QRect(200, 390, 131, 25))
        self.record_button.setObjectName("record_button")
        self.name_label = QtWidgets.QLabel(Dialog)
        self.name_label.setGeometry(QtCore.QRect(50, 140, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name_label.setFont(font)
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.reset_button = QtWidgets.QPushButton(Dialog)
        self.reset_button.setGeometry(QtCore.QRect(340, 390, 111, 25))
        self.reset_button.setObjectName("reset_button")
        self.name_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.name_lineEdit.setGeometry(QtCore.QRect(200, 140, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.name_lineEdit.setFont(font)
        self.name_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.times_needed_label = QtWidgets.QLabel(Dialog)
        self.times_needed_label.setGeometry(QtCore.QRect(60, 280, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.times_needed_label.setFont(font)
        self.times_needed_label.setObjectName("times_needed_label")
        self.times_needed_spinbox = QtWidgets.QSpinBox(Dialog)
        self.times_needed_spinbox.setGeometry(QtCore.QRect(460, 280, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.times_needed_spinbox.setFont(font)
        self.times_needed_spinbox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.times_needed_spinbox.setObjectName("times_needed_spinbox")
        self.path_label = QtWidgets.QLabel(Dialog)
        self.path_label.setGeometry(QtCore.QRect(60, 210, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.path_label.setFont(font)
        self.path_label.setObjectName("path_label")
        self.path_edit = QtWidgets.QLineEdit(Dialog)
        self.path_edit.setGeometry(QtCore.QRect(202, 210, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.path_edit.setFont(font)
        self.path_edit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.path_edit.setObjectName("path_edit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title_label.setText(_translate("Dialog", "Nhấn nút để bắt đầu ghi âm"))
        self.record_button.setText(_translate("Dialog", "Ghi âm"))
        self.name_label.setText(_translate("Dialog", "Tên:"))
        self.reset_button.setText(_translate("Dialog", "Đặt lại"))
        self.times_needed_label.setText(_translate("Dialog", "Số lần cần ghi âm:"))
        self.path_label.setText(_translate("Dialog", "Path:"))

