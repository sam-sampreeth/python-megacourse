import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QComboBox


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Speed Calculator')
        grid = QGridLayout()

        dist_label = QLabel('Distance:')
        self.dist_box = QLineEdit()

        time_label = QLabel('Time(Hrs):')
        self.time_box = QLineEdit()

        self.units = QComboBox()
        self.units.addItem('KM')
        self.units.addItem('Miles')

        calculate_btn = QPushButton("Calculate")
        calculate_btn.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        grid.addWidget(dist_label, 0, 0)
        grid.addWidget(self.dist_box, 0, 1)
        grid.addWidget(self.units, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_box, 1, 1)
        grid.addWidget(calculate_btn, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)
        self.setLayout(grid)

    def calculate_speed(self):
        dist = float(self.dist_box.text())
        time = float(self.time_box.text())

        speed = dist / time

        if self.units.currentText() == 'KM':
            speed = round(speed, 2)
            unit = 'km/h'
        if self.units.currentText() == 'Miles':
            speed = round(speed * 0.621371, 2)
            unit = 'm/h'
        self.output_label.setText(f"Average Speed: {speed} {unit}")

app = QApplication(sys.argv)
calculator = SpeedCalculator()
calculator.show()
sys.exit(app.exec())