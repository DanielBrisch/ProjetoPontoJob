import sys
from PyQt5.QtWidgets import QApplication
from MainApp import MainApp


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec_())
