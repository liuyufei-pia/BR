import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(400,200)
        self.status = self.statusBar()
        self.status.showMessage("这儿是状态栏", 5000)
        self.setWindowTitle("这儿是标题栏")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("weapon.png"))
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())