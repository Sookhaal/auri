from auri.autorig_lib import push_button, AuriScriptView, AuriScriptController, AuriScriptModel
from PySide2 import QtGui, QtWidgets


class View(AuriScriptView):
    def __init__(self, *args, **kwargs):
        super(View, self).__init__(*args, **kwargs)

    def set_model(self):
        self.model = Model()

    def set_controller(self):
        self.ctrl = Controller(self.model)

    def setup_ui(self):
        chk_a = QtWidgets.QCheckBox("Checkbox A")
        chk_a.stateChanged.connect(self.ctrl.on_chk_a_changed)

        txt_a = QtWidgets.QLineEdit()
        txt_a.textChanged.connect(self.ctrl.on_txt_a_changed)

        main_layout = QtWidgets.QHBoxLayout()
        main_layout.addWidget(chk_a)
        main_layout.addWidget(txt_a)

        self.setLayout(main_layout)


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
        print self.model.chk_a

    def on_txt_a_changed(self, txt):
        self.model.txt_a = txt


class Model(AuriScriptModel):
    def __init__(self):
        AuriScriptModel.__init__(self)
        self.chk_a = False
        self.txt_a = ""
