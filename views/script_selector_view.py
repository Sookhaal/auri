import os
from PySide2 import QtWidgets, QtCore
from auri.autorig_lib import push_button


class ScriptSelectorView(QtWidgets.QDialog):
    def __init__(self, scripts, main_model):
        """

        Args:
            main_model (auri.models.main_model.MainModel):
        """
        self.model = main_model
        self.scripts = scripts
        super(ScriptSelectorView, self).__init__()
        self.setWindowTitle("Script Selection")
        self.setModal(1)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.script_list = QtWidgets.QListView()
        self.ok_btn = push_button("Ok", self.ok_pressed)
        self.cancel_btn = push_button("Cancel", self.cancel_pressed)
        self.setup_ui()

    def setup_ui(self):
        self.script_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.script_list.setModel(self.scripts)

        self.main_layout.addWidget(self.script_list)
        self.main_layout.addWidget(self.ok_btn)
        self.main_layout.addWidget(self.cancel_btn)
        self.setLayout(self.main_layout)

    def ok_pressed(self):
        index = self.script_list.currentIndex()
        self.model.selected_script = os.path.splitext(index.data())[0]
        QtWidgets.QDialog.accept(self)

    def cancel_pressed(self):
        self.model.selected_script = None
        QtWidgets.QDialog.reject(self)

    def exec_(self, *args, **kwargs):
        # Select first item if old selection index is not valid
        if not self.script_list.currentIndex().isValid():
            self.script_list.setCurrentIndex(self.scripts.index(0, 0))
        return super(ScriptSelectorView, self).exec_()
