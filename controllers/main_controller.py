from PySide2 import QtWidgets, QtCore, QtGui
from auri.autorig_lib import grpbox, get_auri_icon


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
            self.model.selected_script = None

    def name_changed(self, new_name):
        self.model.module_name = new_name.replace(" ", "_")

    def setup(self, category_combobox, script_selector):
        self.common_ctrl.category_combobox = category_combobox
        self.common_ctrl.script_selector = script_selector

    def add_script(self, main_view):
        """

        Args:
            main_view (auri.views.main_view.MainView):
        """
        # Create the script module view & controller
        exec "import auri.scripts.{0}.{1} as the_script; the_view = the_script.View(); the_ctrl = the_view.ctrl".format(self.model.selected_category, self.model.selected_script)

        # Create the shell to hold the view
        script_layout = QtWidgets.QGridLayout()
        grp_title = "{0} - {1} - {2}".format(self.model.selected_category, self.model.selected_script, self.model.module_name)
        script_grp = grpbox(grp_title, script_layout)

        # Create the basic buttons
        btns_layout = QtWidgets.QHBoxLayout()
        btns_size = QtCore.QSize(24, 24)

        up_btn = QtWidgets.QToolButton()
        up_icon = QtGui.QIcon()
        up_icon.addPixmap(QtGui.QPixmap(get_auri_icon("Arrow_Up.png")))
        up_btn.setIcon(up_icon)
        up_btn.setIconSize(btns_size)
        up_btn.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)

        down_btn = QtWidgets.QToolButton()
        down_icon = QtGui.QIcon()
        down_icon.addPixmap(QtGui.QPixmap(get_auri_icon("Arrow_Down.png")))
        down_btn.setIcon(down_icon)
        down_btn.setIconSize(btns_size)
        down_btn.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)

        duplicate_btn = QtWidgets.QToolButton()
        duplicate_icon = QtGui.QIcon()
        duplicate_icon.addPixmap(QtGui.QPixmap(get_auri_icon("Duplicate.png")))
        duplicate_btn.setIcon(duplicate_icon)
        duplicate_btn.setIconSize(btns_size)
        duplicate_btn.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)

        delete_btn = QtWidgets.QToolButton()
        delete_icon = QtGui.QIcon()
        delete_icon.addPixmap(QtGui.QPixmap(get_auri_icon("Delete.png")))
        delete_btn.setIcon(delete_icon)
        delete_btn.setIconSize(btns_size)
        delete_btn.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        # Add the buttons
        btns_layout.addWidget(up_btn)
        btns_layout.addWidget(down_btn)
        btns_layout.addWidget(duplicate_btn)
        btns_layout.addWidget(delete_btn)
        script_layout.addLayout(btns_layout, 0, 0)
        # Add the view
        # noinspection PyUnresolvedReferences
        script_layout.addWidget(the_view, 1, 0)
        main_view.scrollable_layout.addWidget(script_grp)
        # noinspection PyUnresolvedReferences
        self.model.scripts_to_execute.append(the_ctrl)

    def execute_all(self):
        print "\n\nAuri will run:"
        for script in self.model.scripts_to_execute:
            script.execute()
