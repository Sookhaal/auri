from auri.vendor.Qt import QtGui, QtCore, QtWidgets


class MainModel(object):
    def __init__(self):
        self.categories_model = QtCore.QStringListModel()
        self.subcategories_model = QtCore.QStringListModel()
        self.scripts_model = QtCore.QStringListModel()
        self.module_name = None
        self.selected_subcategory = None
        self.selected_category = None
        self.selected_script = None
        self.current_part = None
        self.current_project = None
        self.scripts_to_execute = []

    @property
    def categories(self):
        return self.categories_model

    @categories.setter
    def categories(self, value):
        self.categories_model.setStringList(value)

    @property
    def subcategories(self):
        return self.subcategories_model

    @subcategories.setter
    def subcategories(self, value):
        self.subcategories_model.setStringList(value)

    @property
    def scripts(self):
        return self.scripts_model

    @scripts.setter
    def scripts(self, value):
        self.scripts_model.setStringList(value)

    @property
    def add_btn_disabled(self):
        if self.selected_subcategory is None or self.selected_category is None or self.selected_script is None or self.module_name is None:
            return True
        if len(self.selected_subcategory) > 0 and len(self.selected_category) > 0 and len(self.selected_script) > 0 and len(self.module_name) > 0:
            return False
        return True
