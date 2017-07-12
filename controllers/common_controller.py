from PySide2 import QtWidgets, QtCore

from auri.auri_lib import get_categories, get_scripts


class CommonController(object):
    def __init__(self, main_model):
        """

        Args:
            main_model (auri.models.main_model.MainModel):
        """
        self.main_model = main_model
        self.category_combobox = None
        self.script_selector = None
        self.refresh()

    def new_project(self):
        pass

    def open_project(self):
        pass

    def save_project(self):
        pass

    def save_project_as(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setFilter(dialog.filter() | QtCore.QDir.Hidden)
        dialog.setDefaultSuffix("json")
        dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        dialog.setNameFilters(["JSON (*.json)"])
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            file(dialog.selectedFiles()[0], "w").close()
        else:
            print("Cancelled")

    def refresh(self):
        self.refresh_categories()
        self.refresh_scripts()

    def refresh_categories(self):
        categories = get_categories()
        self.main_model.categories = categories
        if self.category_combobox is not None:
            self.category_combobox.setCurrentIndex(0)

    def refresh_scripts(self, category=None):
        scripts = get_scripts(category)
        self.main_model.scripts = scripts
        # if self.script_combobox is not None:
        #     self.script_combobox.setCurrentIndex(0)
