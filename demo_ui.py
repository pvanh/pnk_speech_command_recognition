# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.response_label = QtWidgets.QLabel(Dialog)
        self.response_label.setGeometry(QtCore.QRect(90, 30, 231, 51))
        self.response_label.setObjectName("response_label")
        self.text_box = QtWidgets.QTextEdit(Dialog)
        self.text_box.setGeometry(QtCore.QRect(50, 100, 300, 100))
        self.text_box.setReadOnly(True)
        self.text_box.setObjectName("label")
        self.record_button = QtWidgets.QPushButton(Dialog)
        self.record_button.setGeometry(QtCore.QRect(140, 230, 131, 25))
        self.record_button.setObjectName("record_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.response_label.setText(_translate("Dialog", "Press the button to say command"))
        self.text_box.setTextColor(QColor(200,200,200))
        self.text_box.setText("Say something ....")
        self.record_button.setText(_translate("Dialog", "Start"))

