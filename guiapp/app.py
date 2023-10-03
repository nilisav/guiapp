from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit, QWidget, QHBoxLayout, QVBoxLayout, QMainWindow

from sort import sortfunc

class MyLabel(QLabel):
    pass
class MyInput(QLineEdit):
    pass

class ExitButton(QPushButton):
    myclicked = pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        QPushButton.__init__(self, *args, **kwargs)
        self.clicked.connect(self._activate_myclick)

    def _activate_myclick(self):
        self.myclicked.emit(1)

class MainWindow(QMainWindow):
    def __init__(self, app, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)

        self.app = app

        self.setFixedSize(310, 120)
        self.setWindowTitle("Сортировка пузырьком")
        self.label = MyLabel()
        self.input = MyInput()

        self.button = QPushButton("Сортировка!")
        self.button.clicked.connect(self.sorted_array)
        exit_button = ExitButton("Выйти")
        exit_button.myclicked.connect(self.app.quit)


        Layout = QVBoxLayout()
        Layout.addWidget(self.input)
        Layout.addWidget(self.label)
        Layout.addWidget(self.button)
        Layout.addWidget(exit_button)

        container = QWidget()
        container.setLayout(Layout)

        self.setCentralWidget(container)

    def sorted_array(self):
        self.label.setText(sortfunc(self.input.text()))
        print(sortfunc(self.input.text()))

