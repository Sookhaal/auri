from auri.auri_lib import push_button, AuriScriptView, AuriScriptController, AuriScriptModel
from PySide2 import QtGui, QtWidgets


class View(AuriScriptView):
    def __init__(self, *args, **kwargs):
        super(View, self).__init__(*args, **kwargs)

    def set_model(self):
        self.model = Model()

    def set_controller(self):
        self.ctrl = Controller(self.model)

    def setup_ui(self):
        pass


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


class Model(AuriScriptModel):
    def __init__(self):
        AuriScriptModel.__init__(self)
