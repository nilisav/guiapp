import sys

from PyQt6.QtWidgets import QApplication

from app import MainWindow

class Application(QApplication):
    def __init__(self, *args, **kwargs):
        QApplication.__init__(self, *args, **kwargs)
        window = MainWindow()
        window.show()
        window.exit_this.connect(self.quit)
        self.window = window

    def exec(self):
        print('Старт')
        result = QApplication.exec()
        print('Отключение')
        return result

def func():
    app = Application([])
    app.exec()
