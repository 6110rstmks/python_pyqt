from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys

def clicked():
    print("clicked")

def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,300,300) 
    win.setWindowTitle("My first window!") 
    
    label = QLabel(win)
    label.setText("my first label")
    label.move(50, 50)  

    b1 = QtWidgets.QPushButton(win)
    b1.setText("button")
    b1.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())

main()  # make sure to call the function
