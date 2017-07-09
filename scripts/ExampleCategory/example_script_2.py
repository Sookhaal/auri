from auri.autorig_lib import push_button, AuriScriptView, AuriScriptController
from PySide2 import QtGui, QtWidgets


class View(AuriScriptView):
    def __init__(self, *args, **kwargs):
        super(View, self).__init__(*args, **kwargs)

    def setup_ui(self):
        pass

    def set_controller(self):
        self.ctrl = Controller()


class Controller(AuriScriptController):
    def execute(self):
        print __name__

    def __init__(self):
        AuriScriptController.__init__(self)
