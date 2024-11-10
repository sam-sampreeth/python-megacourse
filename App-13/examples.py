# Age Calculator
import sys
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton


class AgeCalculator(QWidget): # age_calc = QWidget()
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Age Calculator')
        grid = QGridLayout()

        # Create widgets
        name_label = QLabel("Name: ")
        self.name_box = QLineEdit()

        dob_label = QLabel("Enter DOB in MM/DD/YYYY: ")
        self.dob_box = QLineEdit()

        calculate_btn = QPushButton("Calculate")
        calculate_btn.clicked.connect(self.calculate_age)
        self.output_label = QLabel("Output: ")

        # Add widgets to grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_box, 0, 1)
        grid.addWidget(dob_label, 1, 0)
        grid.addWidget(self.dob_box, 1, 1)
        grid.addWidget(calculate_btn, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_age(self):
        curr_year = datetime.now().year
        dob_year = self.dob_box.text()
        yob = datetime.strptime(dob_year, "%m/%d/%Y").date().year
        age = curr_year - yob
        self.output_label.setText(f"Hi, {self.name_box.text()}! Your age is {age}")

app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())