import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# Allow CLI arguments - use 'app = QApplication([])' if no CLI functionality wanted
app = QApplication(sys.argv)

window = QMainWindow()
window.show()  # Windows are hidden by default, so need to show it

# PyQt5 event loop
app.exec_()
