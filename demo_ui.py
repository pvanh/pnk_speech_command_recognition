# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(639, 350)
        self.response_label = QtWidgets.QLabel(Dialog)
        self.response_label.setGeometry(QtCore.QRect(110, 30, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.response_label.setFont(font)
        self.response_label.setAlignment(QtCore.Qt.AlignCenter)
        self.response_label.setObjectName("response_label")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 150, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.record_button = QtWidgets.QPushButton(Dialog)
        self.record_button.setGeometry(QtCore.QRect(250, 290, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.record_button.setFont(font)
        self.record_button.setObjectName("record_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.response_label.setText(_translate("Dialog", "Nhấn nút để bắt đầu ghi âm"))
        self.label.setText(_translate("Dialog", " "))
        self.record_button.setText(_translate("Dialog", "Ghi âm"))

