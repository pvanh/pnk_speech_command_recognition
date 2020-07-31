import sys
import DataCollectTool.run as run
from PyQt5.QtWidgets import QDialog, QApplication


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    app = QApplication(sys.argv)
    w = run.MyForm()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
