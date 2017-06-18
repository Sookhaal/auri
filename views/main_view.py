from PySide2 import QtWidgets, QtCore, QtGui
from functools import partial

from auri.autorig_lib import push_button, grpbox
from auri.viewmodels.main_vm import MainViewModelStandalone, MainViewModelMaya


class MainView(QtWidgets.QWidget):
    def __init__(self, vm):
        """

        Args:
            vm (auto_rig.viewmodels.bootstrap_vm.BootstrapViewModel):
        """
        super(MainView, self).__init__()

        if vm.host_application == "standalone":
            self.view_model = MainViewModelStandalone()
        if vm.host_application == "maya":
            self.view_model = MainViewModelMaya()

        self.main_layout = QtWidgets.QVBoxLayout()
        self.scrollable_layout = QtWidgets.QVBoxLayout()
        self.category_combobox = QtWidgets.QComboBox()
        self.category_combobox.setModel(self.view_model.categories_model)
        self.script_combobox = QtWidgets.QComboBox()
        self.script_combobox.setModel(self.view_model.scripts_model)

        self.setup_ui()
        self.view_model.set_old_selected_category(self.category_combobox.currentText())
        self.view_model.set_old_selected_script(self.script_combobox.currentText())
        self.view_model.refresh(self.category_combobox, self.script_combobox)

    def setup_ui(self):
        self.setup_parts_ui()
        self.setup_properties_ui()
        self.main_layout.addStretch(1)
        self.setLayout(self.main_layout)

    def setup_parts_ui(self):
        def create_refresh_btn():
            refresh_btn = push_button("Refresh", partial(self.view_model.refresh, self.category_combobox, self.script_combobox))
            return refresh_btn

        def create_category_combobox():
            self.category_combobox.currentTextChanged.connect(self.view_model.set_old_selected_category)
            return self.category_combobox

        def create_script_combobox():
            self.script_combobox.currentTextChanged.connect(self.view_model.set_old_selected_script)
            return self.script_combobox

        def create_name_textbox():
            name_textbox = QtWidgets.QLineEdit()
            name_textbox.setPlaceholderText("Name")
            return name_textbox

        def create_add_btn():
            add_btn = push_button("Add")
            return add_btn

        parts_layout = QtWidgets.QHBoxLayout()
        parts_grp = grpbox("Parts", parts_layout)

        parts_layout.addWidget(create_refresh_btn())
        parts_layout.addWidget(create_category_combobox())
        parts_layout.addWidget(create_script_combobox())
        parts_layout.addWidget(create_name_textbox())
        parts_layout.addWidget(create_add_btn())

        parts_grp.setLayout(parts_layout)
        self.main_layout.addWidget(parts_grp)

    def setup_properties_ui(self):
        def create_scroll_area():
            scroll_area = QtWidgets.QScrollArea()
            scroll_area.setWidgetResizable(1)
            scrollable_widget = QtWidgets.QWidget()
            scrollable_widget.setLayout(self.scrollable_layout)
            scroll_area.setWidget(scrollable_widget)
            return scroll_area

        properties_layout = QtWidgets.QVBoxLayout()
        properties_grp = grpbox("Properties", properties_layout)

        properties_layout.addWidget(create_scroll_area())

        self.main_layout.addWidget(properties_grp)
