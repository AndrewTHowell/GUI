import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My First GUI App")

        label = QLabel("This is a PyQt5 window")

        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)


# Allow CLI arguments - use 'app = QApplication([])' if no CLI functionality wanted
app = QApplication(sys.argv)

window = MainWindow()
window.show()  # Windows are hidden by default, so need to show it

# PyQt5 event loop
app.exec_()
