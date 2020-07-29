# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CountingDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CountingDialog(object):
    def setupUi(self, CountingDialog):
        CountingDialog.setObjectName("CountingDialog")
        CountingDialog.resize(578, 391)
        self.command_label = QtWidgets.QLabel(CountingDialog)
        self.command_label.setGeometry(QtCore.QRect(60, 130, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.command_label.setFont(font)
        self.command_label.setObjectName("command_label")
        self.times_remain_label = QtWidgets.QLabel(CountingDialog)
        self.times_remain_label.setGeometry(QtCore.QRect(60, 190, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.times_remain_label.setFont(font)
        self.times_remain_label.setObjectName("times_remain_label")
        self.command_lbl = QtWidgets.QLabel(CountingDialog)
        self.command_lbl.setGeometry(QtCore.QRect(330, 130, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.command_lbl.setFont(font)
        self.command_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.command_lbl.setObjectName("command_lbl")
        self.times_remain_lbl = QtWidgets.QLabel(CountingDialog)
        self.times_remain_lbl.setGeometry(QtCore.QRect(390, 190, 64, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.times_remain_lbl.setFont(font)
        self.times_remain_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.times_remain_lbl.setObjectName("times_remain_lbl")
        self.status_label = QtWidgets.QLabel(CountingDialog)
        self.status_label.setGeometry(QtCore.QRect(60, 250, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.status_label.setFont(font)
        self.status_label.setObjectName("status_label")
        self.status_lbl = QtWidgets.QLabel(CountingDialog)
        self.status_lbl.setGeometry(QtCore.QRect(300, 250, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.status_lbl.setFont(font)
        self.status_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.status_lbl.setObjectName("status_lbl")
        self.name_label = QtWidgets.QLabel(CountingDialog)
        self.name_label.setGeometry(QtCore.QRect(60, 70, 64, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.name_lbl = QtWidgets.QLabel(CountingDialog)
        self.name_lbl.setGeometry(QtCore.QRect(190, 70, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.name_lbl.setFont(font)
        self.name_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.name_lbl.setObjectName("name_lbl")

        self.retranslateUi(CountingDialog)
        QtCore.QMetaObject.connectSlotsByName(CountingDialog)

    def retranslateUi(self, CountingDialog):
        _translate = QtCore.QCoreApplication.translate
        CountingDialog.setWindowTitle(_translate("CountingDialog", "Nhìn vào đây!"))
        self.command_label.setText(_translate("CountingDialog", "Lệnh:"))
        self.times_remain_label.setText(_translate("CountingDialog", "Số lần đã thu âm:"))
        self.command_lbl.setText(_translate("CountingDialog", "**"))
        self.times_remain_lbl.setText(_translate("CountingDialog", "0"))
        self.status_label.setText(_translate("CountingDialog", "Trạng thái:"))
        self.status_lbl.setText(_translate("CountingDialog", "**"))
        self.name_label.setText(_translate("CountingDialog", "Tên:"))
        self.name_lbl.setText(_translate("CountingDialog", "**"))

