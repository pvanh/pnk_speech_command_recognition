import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtGui import QColor
import demo_ui
import Record as rec
import time
import regex
from regex import conn_ui

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = demo_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.record_button.clicked.connect(self.display_msg)
        self.show()

    def display_msg(self):
        # if rec.end:
        self.ui.text_box.setTextColor(QColor(200,200,200))
        self.ui.text_box.setText("Say something ....")
        self.ui.record_button.setText("Say")
        regex.reset_cmd()
        if rec.end:
            rec.record()
    @pyqtSlot(str, bool)
    def change_text_value(self, val:str, end:bool):
        if end:
            self.ui.text_box.setTextColor(QColor(255,0,0))
        else:
            self.ui.text_box.setTextColor(QColor(0,0,0))
        self.ui.text_box.setText(val)
    def make_connection(self, obj):
        obj.changedValue.connect(self.change_text_value)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.make_connection(conn_ui)
    w.show()
    sys.exit(app.exec_())
