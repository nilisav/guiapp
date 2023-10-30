from PyQt6.QtCore import pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit, QWidget, QHBoxLayout, QVBoxLayout, QMainWindow

from sort import sortfunc

class MyLabel(QLabel):
    pass
class MyInput(QLineEdit):
    pass

class ExitButton(QPushButton):
    pass

class MainWindow(QMainWindow):
    exit_this = pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)

        self.setFixedSize(310, 120)
        self.setWindowTitle("Сортировка пузырьком")
        self.label = MyLabel()
        self.input = MyInput()

        self.button = QPushButton("Сортировка!")
        self.button.clicked.connect(self.sorted_array)
        exit_button = ExitButton("Выйти")


        Layout = QVBoxLayout()
        Layout.addWidget(self.input)
        Layout.addWidget(self.label)
        Layout.addWidget(self.button)
        Layout.addWidget(exit_button)
        exit_button.clicked.connect(self.activate_exit)

        container = QWidget()
        container.setLayout(Layout)

        self.setCentralWidget(container)

    @pyqtSlot()
    def activate_exit(self):
        self.exit_this.emit(1)

    def sorted_array(self):
        self.label.setText(sortfunc(self.input.text()))
        print(sortfunc(self.input.text()))

