from PySide2 import QtWidgets, QtCore, QtGui
from functools import partial

from auri.auri_lib import push_button, grpbox
from auri.views.script_selector_view import ScriptSelectorView


class MainView(QtWidgets.QWidget):
    def __init__(self, main_model, main_ctrl):
        """

        Args:
            main_ctrl (auri.controllers.main_controller.MainController):
            main_model (auri.models.main_model.MainModel):
        """
        self.model = main_model
        self.main_ctrl = main_ctrl
        super(MainView, self).__init__()
        self.main_layout = QtWidgets.QVBoxLayout()
        self.scrollable_layout = QtWidgets.QVBoxLayout()
        self.category_combobox = QtWidgets.QComboBox()
        self.script_selector_dialog = ScriptSelectorView(self.model.scripts, self.model)
        self.script_selector = push_button("Scripts", self.open_script_selector)
        self.add_btn = push_button("Add", partial(self.main_ctrl.add_selected_script, self))

        self.main_ctrl.setup(self.category_combobox, self.script_selector)
        self.setup_ui()

    def open_script_selector(self):
        result = self.script_selector_dialog.exec_()
        if result == 1:
            self.add_btn.setDisabled(self.model.add_btn_disabled)

    def setup_ui(self):
        self.setup_parts_ui()
        self.setup_properties_ui()
        self.setup_build_area()
        self.setLayout(self.main_layout)

    def setup_parts_ui(self):
        def create_category_combobox():
            self.category_combobox.setModel(self.model.categories)
            self.category_combobox.currentTextChanged.connect(self.main_ctrl.category_changed)
            self.category_combobox.currentTextChanged.connect(lambda: self.add_btn.setDisabled(self.model.add_btn_disabled))
            self.model.selected_category = self.category_combobox.currentText()
            return self.category_combobox

        def create_script_selector():
            return self.script_selector

        def create_name_textbox():
            name_textbox = QtWidgets.QLineEdit()

            # Replace spaces with underscores
            def name_fixup():
                name_textbox.setText(name_textbox.text().replace(" ", "_"))

            name_textbox.setPlaceholderText("Name")
            name_validator = QtGui.QRegExpValidator(QtCore.QRegExp("^[a-zA-Z][a-zA-Z\d#_ ]*"))
            name_textbox.setValidator(name_validator)
            name_textbox.textChanged.connect(name_fixup)
            name_textbox.textChanged.connect(self.main_ctrl.name_changed)
            name_textbox.textChanged.connect(lambda: self.add_btn.setDisabled(self.model.add_btn_disabled))
            return name_textbox

        def create_add_btn():
            self.add_btn.setDisabled(1)
            return self.add_btn

        parts_layout = QtWidgets.QHBoxLayout()
        parts_grp = grpbox("Parts", parts_layout)

        parts_layout.addWidget(create_category_combobox())
        parts_layout.addWidget(create_script_selector())
        parts_layout.addWidget(create_name_textbox())
        parts_layout.addWidget(create_add_btn())

        parts_grp.setLayout(parts_layout)
        self.main_layout.addWidget(parts_grp)

    def setup_properties_ui(self):
        def create_scroll_area():
            scroll_area = QtWidgets.QScrollArea()
            scroll_area.setWidgetResizable(1)
            scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
            scrollable_widget = QtWidgets.QWidget()
            scrollable_widget.setLayout(self.scrollable_layout)
            scroll_area.setWidget(scrollable_widget)
            return scroll_area

        properties_layout = QtWidgets.QVBoxLayout()
        properties_grp = grpbox("Properties", properties_layout)

        properties_layout.addWidget(create_scroll_area())

        self.main_layout.addWidget(properties_grp)

    def setup_build_area(self):
        def create_execute_all_btn():
            execute_all_btn = push_button("Execute All", self.main_ctrl.execute_all)
            return execute_all_btn

        def create_prebuild_all_btn():
            prebuild_all_btn = push_button("Prebuild All", self.main_ctrl.prebuild_all)
            return prebuild_all_btn

        build_layout = QtWidgets.QHBoxLayout()
        build_grp = grpbox("Build", build_layout)

        build_layout.addWidget(create_prebuild_all_btn())
        build_layout.addWidget(create_execute_all_btn())
        self.main_layout.addWidget(build_grp)
        pass
