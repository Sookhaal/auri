from functools import partial
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

    def add_selected_script(self, main_view):
        """

        Args:
            main_view (auri.views.main_view.MainView):
        """
        self.common_ctrl.add_script(self.main_model.selected_category, self.main_model.selected_script, self.main_model.module_name, main_view)

    def execute_all(self):
        for script in self.main_model.scripts_to_execute:
            script.execute()
