from PySide2 import QtWidgets

from auri.autorig_lib import grpbox


class MainController(object):
    def __init__(self, main_model, common_ctrl):
        """

        Args:
            common_ctrl (auri.controllers.common_controller.CommonController):
            main_model (auri.models.main_model.MainModel):
        """
        self.model = main_model
        self.common_ctrl = common_ctrl

    def category_changed(self, new_category):
        if len(new_category) > 0:
            self.common_ctrl.refresh_scripts(new_category)
            self.model.selected_category = new_category

    def setup(self, category_combobox, script_combobox):
        self.common_ctrl.category_combobox = category_combobox
        self.common_ctrl.script_combobox = script_combobox

    def add_script(self, main_view):
        # print "import auri.scripts.{0}.{1} as the_script; the_view = the_script.View()".format(self.model.selected_category, self.model.selected_script)
        """

        Args:
            main_view (auri.views.main_view.MainView):
        """
        exec "import auri.scripts.{0}.{1} as the_script; the_view = the_script.View()".format(self.model.selected_category, self.model.selected_script)
        script_layout = QtWidgets.QVBoxLayout()
        grp_title = "{0}:{1}:{2}".format(self.model.selected_category, self.model.selected_script, self.model.module_name)
        script_grp = grpbox(grp_title, script_layout)
        script_layout.addWidget(the_view)
        main_view.scrollable_layout.addWidget(script_grp)
