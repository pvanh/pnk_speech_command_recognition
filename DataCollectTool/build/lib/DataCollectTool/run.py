import sys
from PyQt5.QtWidgets import QDialog, QApplication
import DataCollectTool.RecToolUI as RecToolUI
import DataCollectTool.CommandRecord as rec
import _thread

FILE_PATH = ""
count = 1


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = RecToolUI.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.record_button.clicked.connect(self.start_record)
        self.ui.reset_button.clicked.connect(self.reset)
        self.show()

    def start_record(self):
        global count, FILE_PATH
        path = self.ui.path_edit.text()
        if path != rec.PATH:
            rec.PATH = path
            FILE_PATH = rec.PATH + "/Names.txt"
            with open(FILE_PATH, 'r') as f:
                for line in f:
                    count += 1

        namefile = open(FILE_PATH, "a")
        name = self.ui.name_lineEdit.text()
        if name != rec.NAME:
            rec.NAME = name
            namefile.write(str(count) + ". " + name + "\n")
            count += 1
            # self.reset()

        rec.TIMES_NEEDED = self.ui.times_needed_spinbox.value()
        if rec.end:
            rec.end = False
            self.ui.record_button.setText("Dừng")
            rec.record()
            self.ui.record_button.setText("Ghi âm")
        else:
            rec.end = True
            self.ui.record_button.setText("Ghi âm")

    def reset(self):
        rec.TIMES_RECORDED = 0
        rec.CUR_COMMAND = 0
        rec.CUR_DIRECTORY = 0
        print("Reset")
        # self.ui.cur_command_label.setText("")
        # self.ui.cur_remain_label.setText(0)

    def show_command(self):
        self.ui.cur_command_label.setText(rec.COMMAND[rec.CUR_COMMAND])
        self.ui.cur_remain_label.setText(str(15 - rec.TIMES_RECORDED))


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     w = MyForm()
#     w.show()
#     sys.exit(app.exec_())
