import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, \
    QMainWindow, QTableWidget, QTableView, QTableWidgetItem, QDialog, QComboBox
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Management System')

        fileMenu = self.menuBar().addMenu('&File')
        helpMenu = self.menuBar().addMenu('&Help')
        editMenu = self.menuBar().addMenu('&Edit')

        addStudent = QAction("Add Student", self)
        addStudent.triggered.connect(self.insert)
        fileMenu.addAction(addStudent)

        aboutAction = QAction("About", self)
        helpMenu.addAction(aboutAction)

        searchAction = QAction("Search", self)
        editMenu.addAction(searchAction)
        searchAction.triggered.connect(self.search)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

    def loadData(self):
        connection = sqlite3.connect('database.db')
        result = connection.execute("SELECT * FROM students")
        self.table.setRowCount(0)
        for rowNumber, rowData in enumerate(result):
            self.table.insertRow(rowNumber)
            for colNumber, data in enumerate(rowData):
                self.table.setItem(rowNumber, colNumber, QTableWidgetItem(str(data)))
        connection.close()

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

    def search(self):
        dialog = SearchDialog()
        dialog.exec()

class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Insert Student')
        self.setFixedHeight(300)
        self.setFixedWidth(300)

        layout = QVBoxLayout()
        self.studentName = QLineEdit()
        self.studentName.setPlaceholderText("Enter Student Name")
        layout.addWidget(self.studentName)

        self.courseName = QComboBox()
        self.courseName.addItems(["Biology", "Math", "Astronomy", "Physics"])
        layout.addWidget(self.courseName)

        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Enter Mobile Number")
        layout.addWidget(self.mobile)

        btn = QPushButton("Insert")
        btn.clicked.connect(self.add_student)
        layout.addWidget(btn)

        self.setLayout(layout)

    def add_student(self):
        name = self.studentName.text()
        course = self.courseName.currentText()
        mobile = self.mobile.text()
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)", (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
        abc.loadData()

class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Search')
        self.setFixedHeight(300)
        self.setFixedWidth(300)
        layout = QVBoxLayout()
        self.studentName = QLineEdit()
        self.studentName.setPlaceholderText("Enter Student Name")
        layout.addWidget(self.studentName)

        butn = QPushButton("Search")
        butn.clicked.connect(self.search)
        layout.addWidget(butn)
        self.setLayout(layout)

    def search(self):
        name = self.studentName.text()
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        res = cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
        rows = list(res)
        print(rows)
        items = MainWindow.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            print(item)
            MainWindow.table.item(item.row(), 1).setSelected(True)
        cursor.close()
        connection.close()

app = QApplication(sys.argv)
abc = MainWindow()
abc.loadData()
abc.show()
sys.exit(app.exec())