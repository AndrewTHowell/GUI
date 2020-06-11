import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # SIGNAL: The connected function will be called whenever the window
        # title is changed. The new title will be passed to the function.
        self.windowTitleChanged.connect(self.onWindowTitleChange)

        # SIGNAL: The connected function will be called whenever the window
        # title is changed. The new title is discarded in the lambda and the
        # function is called without parameters.
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn())

        # SIGNAL: The connected function will be called whenever the window
        # title is changed. The new title is passed to the function
        # and replaces the default parameter
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))

        # SIGNAL: The connected function will be called whenever the window
        # title is changed. The new title is passed to the function
        # and replaces the default parameter. Extra data is passed from
        # within the lambda.
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, "Custom Parameter"))

        # This sets the window title which will trigger all the above signals
        # sending the new title to the attached functions or lambdas as the
        # first parameter.
        self.setWindowTitle("My Slotted App")

        label = QLabel("Main window label")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

    # SLOT: This accepts a string, e.g. the window title, and prints it
    @staticmethod
    def onWindowTitleChange(title):
        print(title)

    # SLOT: This has default parameters and can be called without a value
    @staticmethod
    def my_custom_fn(title="Default Title", param="Default Parameter"):
        print(title, param)

    def contextMenuEvent(self, event: QtGui.QContextMenuEvent) -> None:
        print("Context menu event")
        super().contextMenuEvent(event)

    # Event propagation up the UI hierarchy
    """
    Event object 'e'
    
    e.accept() - stops propagation further up the UI hierarchy
    e.ignore() - allows further propagation
    """


# Allow CLI arguments - use 'app = QApplication([])' if no CLI functionality wanted
app = QApplication(sys.argv)

window = MainWindow()
window.show()  # Windows are hidden by default, so need to show it

# PyQt5 event loop
app.exec_()
