from PySide2 import QtWidgets, QtCore, QtGui
from functools import partial

from auri.auri_lib import grpbox, get_auri_icon
from auri.views.script_module_view import ScriptModuleView




class MainController(object):
    def __init__(self, main_model, project_model, common_ctrl):
        """

        Args:
            common_ctrl (auri.controllers.common_controller.CommonController):
            main_model (auri.models.main_model.MainModel):
            project_model (auri.models.project_model.ProjectModel):
        """
        self.main_model = main_model
        self.project_model = project_model
        self.common_ctrl = common_ctrl

    def category_changed(self, new_category):
        if len(new_category) > 0:
            self.common_ctrl.refresh_scripts(new_category)
            self.main_model.selected_category = new_category
            self.main_model.selected_script = None

    def name_changed(self, new_name):
        self.main_model.module_name = new_name.replace(" ", "_")

    def setup(self, category_combobox, script_selector):
        self.common_ctrl.category_combobox = category_combobox
        self.common_ctrl.script_selector = script_selector

    def add_script(self, category, script, module_name, main_view, script_module_instance=None):
        if script_module_instance is not None:
            script_view = ScriptModuleView(category, script, module_name, self.main_model, script_module_instance.get_index() + 1)
            main_view.scrollable_layout.insertWidget(script_module_instance.get_index() + 1, script_view)
        else:
            script_view = ScriptModuleView(category, script, module_name, self.main_model)
            main_view.scrollable_layout.insertWidget(-1, script_view)
        script_view.duplicate_btn.pressed.connect(partial(self.add_script, category, script, module_name, main_view, script_view))
        script_view.delete_btn.pressed.connect(partial(self.remove_script, main_view, script_view))

    def add_selected_script(self, main_view):
        """

        Args:
            main_view (auri.views.main_view.MainView):
        """
        self.add_script(self.main_model.selected_category, self.main_model.selected_script, self.main_model.module_name, main_view)

    def remove_script(self, main_view, script_view):
        """

        Args:
            script_view (auri.views.script_module_view.ScriptModuleView):
        """
        main_view.scrollable_layout.removeWidget(script_view)
        script_view.deleteLater()

    def execute_all(self):
        for script in self.main_model.scripts_to_execute:
            script.execute()
