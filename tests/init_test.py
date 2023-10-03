
from pytestqt.qt_compat import qt_api
from guiapp.app import MainWindow
from guiapp.testprog import Application

def test_first(qtbot):
    app = Application([])
    window = MainWindow(app)
    qtbot.addWidget(window)

    window.input.setText('1 2 3')

    qtbot.mouseClick(window.button, qt_api.QtCore.Qt.MouseButton.LeftButton)

    assert window.label.text() == "1, 2, 3"

def test_second(qtbot):
    app = Application([])
    window = MainWindow(app)
    qtbot.addWidget(window)

    window.input.setText('1 6 3 8')

    qtbot.mouseClick(window.button, qt_api.QtCore.Qt.MouseButton.LeftButton)

    assert window.label.text() == "1, 3, 6, 8"

def test_third(qtbot):
    app = Application([])
    window = MainWindow(app)
    qtbot.addWidget(window)

    window.input.setText('')

    qtbot.mouseClick(window.button, qt_api.QtCore.Qt.MouseButton.LeftButton)

    assert window.label.text() == ""