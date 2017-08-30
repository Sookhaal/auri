from auri.vendor.Qt import QtWidgets, QtCore
from auri.auri_lib import push_button, get_application, get_houdini_style, get_auri_version


class AboutView(QtWidgets.QDialog):
    def __init__(self):
        super(AboutView, self).__init__()
        self.setWindowTitle("About Auri")
        self.setModal(1)
        self.setFixedSize(400, 300)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.about_text = QtWidgets.QLabel()
        self.ok_btn = push_button("Ok", self.ok_pressed)
        # self.cancel_btn = push_button("Cancel", self.cancel_pressed)
        self.setup_ui()
        if get_application() is "standalone" or get_application() is "houdini":
            self.setStyleSheet(get_houdini_style())

    def setup_ui(self):
        self.about_text.setText(
            "<h1 align='center'>Auri</h1>"
            "<h5 align='center'>{0}</h5>"
            "<p style='font-size:12pt' align='justify'>Auri is a modular python script launcher.<br>The main idea is to build a library of scripts (we call them <b>modules</b>) and have a shell (<b>Auri</b>) executing the stacked scripts in a top to bottom order.</p>"
            "<p align='center' style='font-size:12pt'><a href='https://github.com/Sookhaal/auri' style='text-decoration:none; color:inherit;'>Github</a></p>".format(get_auri_version())
        )
        self.about_text.setOpenExternalLinks(True)
        self.about_text.setWordWrap(True)
        self.main_layout.addWidget(self.about_text)
        self.main_layout.addWidget(self.ok_btn)
        self.setLayout(self.main_layout)

    def ok_pressed(self):
        QtWidgets.QDialog.accept(self)

    def cancel_pressed(self):
        QtWidgets.QDialog.reject(self)

    def exec_(self, *args, **kwargs):
        return super(AboutView, self).exec_()
