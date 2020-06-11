import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("My First GUI App")

        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit
        ]

        for widget in widgets:
            layout.addWidget(widget())

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


# Allow CLI arguments - use 'app = QApplication([])' if no CLI functionality wanted
app = QApplication(sys.argv)

window = MainWindow()
window.show()  # Windows are hidden by default, so need to show it

# PyQt5 event loop
app.exec_()
