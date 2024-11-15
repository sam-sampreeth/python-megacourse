import sys
from idlelib.help_about import AboutDialog

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, \
    QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QComboBox, QToolBar, QStatusBar, QMessageBox
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Management System')
        self.setMinimumSize(800, 600)

        fileMenu = self.menuBar().addMenu('&File')
        helpMenu = self.menuBar().addMenu('&Help')
        editMenu = self.menuBar().addMenu('&Edit')

        addStudent = QAction(QIcon("icons/add.png"), "Add Student", self)
        addStudent.triggered.connect(self.insert)
        fileMenu.addAction(addStudent)

        aboutAction = QAction("About", self)
        helpMenu.addAction(aboutAction)
        aboutAction.triggered.connect(self.about)

        searchAction = QAction(QIcon("icons/search.png"), "Search", self)
        editMenu.addAction(searchAction)
        searchAction.triggered.connect(self.search)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(addStudent)
        toolbar.addAction(searchAction)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        editButton = QPushButton("Edit record")
        editButton.clicked.connect(self.edit)

        deleteButton = QPushButton("Delete record")
        deleteButton.clicked.connect(self.delete)

        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusBar.removeWidget(child)

        self.statusBar.addWidget(editButton)
        self.statusBar.addWidget(deleteButton)

    def edit(self):
        dialog = EditDialog(self)
        dialog.exec()

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
        dialog = InsertDialog(self)
        dialog.exec()

    def search(self):
        dialog = SearchDialog(self)
        dialog.exec()

    def delete(self):
        dialog = DeleteDialog(self)
        dialog.exec()

    def about(self):
        dialog = QMessageBox(self)
        dialog.setWindowTitle('About')
        dialog.setText("This app was created by Sampreeth")
        dialog.setIcon(QMessageBox.Icon.Information)
        dialog.exec()


class InsertDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
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
        self.parent().loadData()
        self.accept()

class SearchDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
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
        items = self.parent().table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            self.parent().table.item(item.row(), 1).setSelected(True)
        cursor.close()
        connection.close()

class EditDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle('Edit Student')
        self.setFixedHeight(300)
        self.setFixedWidth(300)
        self.parent = parent

        layout = QVBoxLayout()

        # Get the selected student's current data
        index = self.parent.table.currentRow()
        self.student_id = self.parent.table.item(index, 0).text()  # Assuming ID is in the first column
        student_name = self.parent.table.item(index, 1).text()
        course_name = self.parent.table.item(index, 2).text()
        mobile = self.parent.table.item(index, 3).text()

        # Student Name field
        self.studentName = QLineEdit(student_name)
        self.studentName.setPlaceholderText("Enter Student Name")
        layout.addWidget(self.studentName)

        # Course field
        self.courseName = QComboBox()
        self.courseName.addItems(["Biology", "Math", "Astronomy", "Physics"])
        self.courseName.setCurrentText(course_name)
        layout.addWidget(self.courseName)

        # Mobile field
        self.mobile = QLineEdit(mobile)
        self.mobile.setPlaceholderText("Enter Mobile Number")
        layout.addWidget(self.mobile)

        # Update button
        btn = QPushButton("Update")
        btn.clicked.connect(self.update_student)
        layout.addWidget(btn)

        self.setLayout(layout)

    def update_student(self):
        name = self.studentName.text()
        course = self.courseName.currentText()
        mobile = self.mobile.text()

        # Update the record in the database
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET name = ?, course = ?, mobile = ? WHERE id = ?", (self.studentName.text(), self.courseName.itemText(self.courseName.currentIndex()), mobile, self.student_id))
        connection.commit()
        cursor.close()
        connection.close()

        # Refresh the table in the main window
        self.parent.loadData()
        self.accept()

class DeleteDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle('Delete Student Record')
        self.setFixedHeight(200)
        self.setFixedWidth(200)
        layout = QVBoxLayout()

        self.infoLabel = QLabel("Are you sure you want to delete this student?")
        layout.addWidget(self.infoLabel)

        deleteBtn = QPushButton("Delete")
        deleteBtn.clicked.connect(self.delete_student)
        layout.addWidget(deleteBtn)

        self.setLayout(layout)

    def delete_student(self):
        index = self.parent().table.currentRow()
        student_id = self.parent().table.item(index, 0).text()

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        connection.commit()
        cursor.close()
        connection.close()

        self.parent().loadData()
        self.accept()

class AbtDialog(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('About')
        self.setText("This app was created by Sampreeth")
        self.setIcon(QMessageBox.Icon.Information)


app = QApplication(sys.argv)
window = MainWindow()
window.loadData()
window.show()
sys.exit(app.exec())
