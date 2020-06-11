import sys
from PyQt5.QtWidgets import QApplication

# Allow CLI arguments - use 'app = QApplication([])' if no CLI functionality wanted
app = QApplication(sys.argv)

# PyQt5 event loop
app.exec_()
