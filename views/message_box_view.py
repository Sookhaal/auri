from auri.vendor.Qt import QtWidgets, QtCore
from auri.auri_lib import push_button, get_application, get_houdini_style


class MessageBoxView(QtWidgets.QDialog):
    def __init__(self, window_title="Message", message="ENTER A MESSAGE"):
        super(MessageBoxView, self).__init__()
        self.setWindowTitle(window_title)
        self.setModal(1)
        self.setMinimumWidth(250)
        self.setMinimumHeight(150)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.message = QtWidgets.QLabel(message)
        self.ok_btn = push_button("Ok", self.ok_pressed)
        self.setup_ui()
        if get_application() is "standalone" or get_application() is "houdini":
            self.setStyleSheet(get_houdini_style())

    def setup_ui(self):
        self.main_layout.addWidget(self.message)
        self.main_layout.addWidget(self.ok_btn)
        self.setLayout(self.main_layout)

    def ok_pressed(self):
        QtWidgets.QDialog.accept(self)
