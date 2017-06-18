from PySide2 import QtWidgets, QtCore, QtGui

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

        self.setup_ui()

    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        self.scrollable_layout = QtWidgets.QVBoxLayout()

        self.setup_parts_ui()
        self.setup_properties_ui()

        self.main_layout.addStretch(1)

        self.setLayout(self.main_layout)

    def setup_parts_ui(self):
        def create_category_combobox():
            category_combobox = QtWidgets.QComboBox()
            category_combobox.addItem("AZE")
            category_combobox.addItem("RTY")
            return category_combobox

        def create_script_combobox():
            script_combobox = QtWidgets.QComboBox()
            script_combobox.addItem("SCR")
            script_combobox.addItem("IPT")
            return script_combobox

        def create_name_textbox():
            name_textbox = QtWidgets.QLineEdit()
            name_textbox.setPlaceholderText("Name")
            return name_textbox

        def create_add_btn():
            add_btn = push_button("ADD")
            return add_btn

        parts_layout = QtWidgets.QHBoxLayout()
        parts_grp = grpbox("Parts", parts_layout)

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
