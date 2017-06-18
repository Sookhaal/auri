from PySide2 import QtWidgets, QtCore, QtGui


class MenuBar(QtWidgets.QMenuBar):
    def __init__(self):
        super(MenuBar, self).__init__()
        file_menu = self.addMenu("&File")
        edit_menu = self.addMenu("&Edit")
        about_menu = self.addMenu("&About")
