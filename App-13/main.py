import sys
from datetime import datetime
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, \
    QMainWindow, QTableWidget, QTableView
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Management System')

        fileMenu = self.menuBar().addMenu('&File')
        helpMenu = self.menuBar().addMenu('&Help')

        addStudent = QAction("Add Student", self)
        fileMenu.addAction(addStudent)

        aboutAction = QAction("About", self)
        helpMenu.addAction(aboutAction)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.setCentralWidget(self.table)

    def loadData(self):
        connection = sqlite3.connect('database.db')
        result = connection.execute("SELECT * FROM students")

        self.table

app = QApplication(sys.argv)
abc = MainWindow()
abc.loadData()
abc.show()
sys.exit(app.exec())