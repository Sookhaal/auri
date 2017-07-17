import os
from PySide2 import QtWidgets, QtCore

from auri.auri_lib import get_categories, get_scripts
from auri.views.main_view import MainView


class CommonController(object):
    def __init__(self, main_model, project_model, bootstrap_view):
        """

        Args:
            main_model (auri.models.main_model.MainModel):
            project_model (auri.models.project_model.ProjectModel):
            bootstrap_view (auri.views.bootstrap_view.BootstrapView):
        """
        self.project_model = project_model
        self.main_model = main_model
        self.bootstrap_view = bootstrap_view
        self.main_view = None
        self.category_combobox = None
        self.script_selector = None
        self.refresh()

    def new_project(self):
        if self.main_view is None:
            self.main_view = self.bootstrap_view.main_view
        assert(isinstance(self.main_view, MainView))
        while self.main_view.scrollable_layout.count():
            child = self.main_view.scrollable_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        self.main_model.current_project = None
        self.project_model.scripts_to_execute = []

    def open_project(self):
        pass

    def save_project(self):
        if self.main_model.current_project is None:
            self.save_project_as()
        else:
            print "Save"

    def save_project_as(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setFilter(dialog.filter() | QtCore.QDir.Hidden)
        dialog.setDefaultSuffix("json")
        dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        dialog.setNameFilters(["JSON (*.json)"])
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.main_model.current_project = dialog.selectedFiles()[0]
            file(self.main_model.current_project, "w").close()
            self.bootstrap_view.setWindowTitle("Auri - {0}".format(os.path.basename(self.main_model.current_project)))
        else:
            # If the file does not exist, remove it from the title
            if self.main_model.current_project is not None:
                if not os.path.isfile(self.main_model.current_project):
                    self.main_model.current_project = None
                    self.bootstrap_view.setWindowTitle("Auri")

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
