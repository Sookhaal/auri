from PySide2 import QtGui, QtCore, QtWidgets


class MainModel(object):
    @property
    def categories(self):
        return self.categories_model

    @categories.setter
    def categories(self, value):
        self.categories_model.setStringList(value)

    @property
    def scripts(self):
        return self.scripts_model

    @scripts.setter
    def scripts(self, value):
        self.scripts_model.setStringList(value)

    def __init__(self):
        self.categories_model = QtGui.QStringListModel()
        self.scripts_model = QtGui.QStringListModel()
        self.module_name = "TEMP"
        self.selected_category = None
        self.selected_script = None
        self.current_part = None
        self.scripts_to_execute = []

    def add_btn_disabled(self):
        if len(self.selected_category) > 0 and len(self.selected_script) > 0:
            return False
        return True
