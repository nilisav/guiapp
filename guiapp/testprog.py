import sys

from PyQt6.QtWidgets import QApplication

from app import MainWindow

class Application(QApplication):
    def __init__(self, *args, **kwargs):
        QApplication.__init__(self, *args, **kwargs)
        window = MainWindow(self)
        window.show()
        self.window = window

    def exec(self):
        print('Старт')
        result = QApplication.exec()
        print('Отключение')
        return result

def func():
    app = Application([])
    app.exec()