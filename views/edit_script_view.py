from auri.vendor.Qt import QtWidgets, QtCore
from auri.auri_lib import push_button
from auri.views.message_box_view import MessageBoxView


class EditScriptView(QtWidgets.QDialog):
    def __init__(self, script_view, project_model):
        """

        Args:
            script_view (auri.views.script_module_view.ScriptModuleView):
            project_model (auri.models.project_model.ProjectModel):
        """
        self.script_view = script_view
        self.project_model = project_model
        super(EditScriptView, self).__init__()
        self.setWindowTitle("Edit Script")
        self.setModal(1)
        self.setMinimumWidth(250)
        self.setMinimumHeight(150)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.new_name = QtWidgets.QLineEdit()
        self.ok_btn = push_button("Ok", self.ok_pressed)
        self.cancel_btn = push_button("Cancel", self.cancel_pressed)
        self.message_box = None
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
        if self.new_name.text() not in self.project_model.unique_names or self.new_name.text() is self.script_view.module_name:
            self.script_view.change_module_name(self.new_name.text())
            QtWidgets.QDialog.accept(self)
        else:
            self.message_box = MessageBoxView("Naming Error", "<p style='font-size:12pt'>A module named <b>{0}</b> already exists.</p>".format(self.new_name.text()))
            self.message_box.show()
            QtWidgets.QDialog.reject(self)

    def cancel_pressed(self):
        QtWidgets.QDialog.reject(self)
