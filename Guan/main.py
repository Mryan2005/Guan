# import the Qt module
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import threading
import cv2
import numpy as np
import glob


# Create a new Qt window
class Window(QWidget):
      def __init__(self):
            super().__init__()
            self.setWindowTitle("Guan")
            self.setGeometry(100, 100, 800, 600)
            self.initUI()

      def initUI(self):
            # read the images
            self.images = glob.glob("./images/*.jpg")
            self.images += glob.glob("./images/*.png")
if __name__ == "__main__":
    app = QApplication([])
    win = Window()
    win.show()
    app.exit(app.exec_())