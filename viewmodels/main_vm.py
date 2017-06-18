import abc
import os
from PySide2 import QtGui, QtWidgets
from auri.autorig_lib import get_categories, get_scripts


# Base
class MainViewModelBase:
    def __init__(self):
        self.script_combobox = None
        self.old_selected_category = ""
        self.old_selected_script = ""
        self.categories = ()
        self.scripts = ()

        self.categories_model = QtGui.QStringListModel(self.categories)
        self.scripts_model = QtGui.QStringListModel(self.scripts)

        self.refresh()

    def refresh(self, category_combobox=None, script_combobox=None):
        """

        Args:
            script_combobox (QtWidgets.QCombobox):
            category_combobox (QtWidgets.QCombobox):
        """
        if script_combobox is not None:
            self.script_combobox = script_combobox
        cat_backup = self.old_selected_category
        script_backup = self.old_selected_script
        self.refresh_categories(category_combobox)
        self.refresh_scripts(script_combobox)
        if category_combobox is not None:
            category_combobox.setCurrentText(cat_backup)
        if script_combobox is not None:
            script_combobox.setCurrentText(script_backup)

    def refresh_categories(self, category_combobox=None):
        self.categories = get_categories()
        self.categories_model.setStringList(self.categories)
        if category_combobox is not None:
            category_combobox.setCurrentIndex(0)

    def refresh_scripts(self, script_combobox=None):
        self.scripts = get_scripts(self.old_selected_category)
        self.scripts_model.setStringList(self.scripts)
        if script_combobox is not None:
            script_combobox.setCurrentIndex(0)

    def set_old_selected_category(self, category):
        if len(category) > 0:
            self.old_selected_category = category
            self.refresh_scripts(self.script_combobox)

    def set_old_selected_script(self, script):
        if len(script) > 0:
            self.old_selected_script = script


# Maya
class MainViewModelMaya(MainViewModelBase):
    def __init__(self):
        MainViewModelBase.__init__(self)


# Standalone
class MainViewModelStandalone(MainViewModelBase):
    def __init__(self):
        MainViewModelBase.__init__(self)
