import sys
from os import path
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar, QAction, QStatusBar, QCheckBox
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon

currentDirectoryPath = path.dirname(path.abspath(__file__))
iconsPath = path.join(currentDirectoryPath, "Icon Set//icons")


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("My GUI App")

        label = QLabel("This is a PyQt5 window")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        buttonAction = QAction(QIcon(path.join(iconsPath, "bug.png")), "Your button", self)
        buttonAction.setStatusTip("This is your button")
        buttonAction.triggered.connect(self.onMyToolBarButtonClick)
        buttonAction.setCheckable(True)
        toolbar.addAction(buttonAction)

        toolbar.addSeparator()

        buttonAction2 = QAction(QIcon(path.join(iconsPath, "bug.png")), "Your button 2", self)
        buttonAction2.setStatusTip("This is your second button")
        buttonAction2.triggered.connect(self.onMyToolBarButtonClick)
        buttonAction2.setCheckable(True)
        toolbar.addAction(buttonAction2)

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

    @staticmethod
    def onMyToolBarButtonClick(s):
        print("click", s)


# Allow CLI arguments - use 'app = QApplication([])' if no CLI functionality wanted
app = QApplication(sys.argv)

window = MainWindow()
window.show()  # Windows are hidden by default, so need to show it

# PyQt5 event loop
app.exec_()
