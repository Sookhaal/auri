from auri.auri_lib import push_button, AuriScriptView, AuriScriptController, AuriScriptModel
from PySide2 import QtGui, QtWidgets


class View(AuriScriptView):
    def __init__(self, *args, **kwargs):
        self.chk_a = QtWidgets.QCheckBox("Checkbox A")
        self.txt_a = QtWidgets.QLineEdit()
        super(View, self).__init__(*args, **kwargs)

    def set_model(self):
        self.model = Model()

    def set_controller(self):
        self.ctrl = Controller(self.model)

    def setup_ui(self):
        self.chk_a.stateChanged.connect(self.ctrl.on_chk_a_changed)

        self.txt_a.textChanged.connect(self.ctrl.on_txt_a_changed)

        main_layout = QtWidgets.QHBoxLayout()
        main_layout.addWidget(self.chk_a)
        main_layout.addWidget(self.txt_a)

        self.setLayout(main_layout)

    def refresh_view(self):
        self.chk_a.setChecked(self.model.chk_a)
        self.txt_a.setText(self.model.txt_a)


class Controller(AuriScriptController):
    def __init__(self, model):
        """

        Args:
            model (Model):
        """
        self.model = model
        AuriScriptController.__init__(self)

    def execute(self):
        print __name__

    def on_chk_a_changed(self, state):
        switch = {0: False, 2: True}
        self.model.chk_a = switch.get(state)

    def on_txt_a_changed(self, txt):
        self.model.txt_a = txt


class Model(AuriScriptModel):
    def __init__(self):
        AuriScriptModel.__init__(self)
        self.chk_a = False
        self.txt_a = ""
