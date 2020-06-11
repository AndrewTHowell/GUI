import sys
from PyQt5.QtWidgets import QApplication, QWidget

# Allow CLI arguments - use 'app = QApplication([])' if no CLI functionality wanted
app = QApplication(sys.argv)

window = QWidget()
window.show()  # Windows are hidden by default, so need to show it

# PyQt5 event loop
app.exec_()
