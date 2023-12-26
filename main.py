import sys
from datetime import datetime

from PyQt5.QtWidgets import QApplication
from Home import Home


if __name__ == '__main__':
    current_time = datetime.datetime.now().time()
    if current_time.hour == 7 and current_time.minute == 45:
        main()
    else:
        time.sleep(60)
    app = QApplication(sys.argv)
    ex = Home()
    ex.show()
    sys.exit(app.exec_())
