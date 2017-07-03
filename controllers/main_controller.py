from PySide2 import QtWidgets, QtCore

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QStyle

from auri.autorig_lib import grpbox, push_button


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
        """

        Args:
            main_view (auri.views.main_view.MainView):
        """
        exec "import auri.scripts.{0}.{1} as the_script; the_view = the_script.View(); the_vm = the_view.viewmodel".format(self.model.selected_category, self.model.selected_script)
        script_layout = QtWidgets.QGridLayout()
        grp_title = "{0}:{1}:{2}".format(self.model.selected_category, self.model.selected_script, self.model.module_name)
        script_grp = grpbox(grp_title, script_layout)
        btns_layout = QtWidgets.QVBoxLayout()

        btns_size = QtCore.QSize(24, 24)
        delete_btn = QtWidgets.QToolButton()
        delete_btn.setIcon(main_view.style().standardIcon(QStyle.SP_TrashIcon))
        delete_btn.setIconSize(btns_size)

        up_btn = QtWidgets.QToolButton()
        up_btn.setIcon(main_view.style().standardIcon(QStyle.SP_ArrowUp))
        up_btn.setIconSize(btns_size)

        down_btn = QtWidgets.QToolButton()
        down_btn.setIcon(main_view.style().standardIcon(QStyle.SP_ArrowDown))
        down_btn.setIconSize(btns_size)

        btns_layout.addWidget(delete_btn)
        btns_layout.addWidget(up_btn)
        btns_layout.addWidget(down_btn)

        script_layout.addLayout(btns_layout, 0, 0)
        script_layout.addWidget(the_view, 0, 1)
        main_view.scrollable_layout.addWidget(script_grp)
        self.model.scripts_to_execute.append(the_vm)

    def execute_all(self):
        for script in self.model.scripts_to_execute:
            script.execute()
