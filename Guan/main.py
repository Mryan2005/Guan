# import the Qt module
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QDesktopWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMenuBar

app = QApplication([])
desktop = QDesktopWidget()

# get screen size
screenSide = desktop.screenGeometry()
screenWidth = screenSide.width()
screenHeight = screenSide.height()


class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.background = None
        self.setWindowTitle('Slightest')
        self.setGeometry(100, 100, screenWidth - 200, screenHeight - 200)
        self.move(100, 100)
        self.setupUI()

    def setupUI(self):
        # set background image
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap('source/1.jpg').scaled(screenWidth - 200, screenHeight - 200))
        self.background.setGeometry(0, 0, screenWidth - 200, screenHeight - 200)
        # create a bar
        self.bar = QMenuBar(self)
        self.bar.setGeometry(0, 0, screenWidth - 200, 30)
        # create a button called file
        self.fileButtom = QPushButton('flie', self)
        self.fileButtom.setText('file')
        self.fileButtom.move(0, 0)
        # set button background transparent
        self.fileButtom.setStyleSheet('background-color: rgba(0, 0, 0, 0);')
        self.fileButtom.clicked.connect(self.file)
        # create a button called edit
        self.editButtom = QPushButton('edit', self)
        self.editButtom.setText('edit')
        self.editButtom.move(60, 0)
        # set button background transparent
        self.editButtom.setStyleSheet('background-color: rgba(0, 0, 0, 0);')
        self.editButtom.clicked.connect(self.edit)
        # create a button called view
        self.viewButtom = QPushButton('view', self)
        self.viewButtom.setText('view')
        self.viewButtom.move(120, 0)
        # set button background transparent
        self.viewButtom.setStyleSheet('background-color: rgba(0, 0, 0, 0);')
        self.viewButtom.clicked.connect(self.view)
        # create a button called help
        self.helpButtom = QPushButton('help', self)
        self.helpButtom.setText('help')
        self.helpButtom.move(180, 0)
        # set button background transparent
        self.helpButtom.setStyleSheet('background-color: rgba(0, 0, 0, 0);')
        self.helpButtom.clicked.connect(self.help)

    def file(self):
        print('file')

    def edit(self):
        print('edit')

    def view(self):
        print('view')

    def help(self):
        print('help')


if __name__ == '__main__':
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())
