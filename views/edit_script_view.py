from auri.vendor.Qt import QtWidgets, QtCore
from auri.auri_lib import push_button


class EditScriptView(QtWidgets.QDialog):
    def __init__(self, script_view):
        """

        Args:
            script_view (auri.views.script_module_view.ScriptModuleView):
        """
        self.script_view = script_view
        super(EditScriptView, self).__init__()
        self.setWindowTitle("Edit Script")
        self.setModal(1)
        self.setMinimumWidth(250)
        self.setMinimumHeight(150)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.new_name = QtWidgets.QLineEdit()
        self.ok_btn = push_button("Ok", self.ok_pressed)
        self.cancel_btn = push_button("Cancel", self.cancel_pressed)
        self.setup_ui()

    def setup_ui(self):
        new_name_layout = QtWidgets.QHBoxLayout()
        new_name_label = QtWidgets.QLabel("New name:")
        self.new_name.setText(self.script_view.module_name)

        new_name_layout.addWidget(new_name_label)
        new_name_layout.addWidget(self.new_name)

        self.main_layout.addLayout(new_name_layout)
        self.main_layout.addStretch(1)
        self.main_layout.addWidget(self.ok_btn)
        self.main_layout.addWidget(self.cancel_btn)
        self.setLayout(self.main_layout)

    def ok_pressed(self):
        self.script_view.change_module_name(self.new_name.text())
        QtWidgets.QDialog.accept(self)

    def cancel_pressed(self):
        QtWidgets.QDialog.reject(self)
