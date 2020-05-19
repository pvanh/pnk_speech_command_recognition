import sys
from PyQt5.QtWidgets import QDialog, QApplication
import demo_ui
import Record as rec
import time


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = demo_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.record_button.clicked.connect(self.display_msg)
        self.show()

    def display_msg(self):
        if rec.end:
            rec.end = False
            self.ui.label.setText("Say something")
            self.ui.record_button.setText("Stop")
            rec.record()
        else:
            rec.end = True
            self.ui.label.setText("Stopped")
            self.ui.record_button.setText("Record")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
