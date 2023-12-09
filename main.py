import sys
from PyQt5.QtWidgets import QApplication
from AppRun import AppRun
from Home import Home


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Home()
    ex.show()
    sys.exit(app.exec_())
