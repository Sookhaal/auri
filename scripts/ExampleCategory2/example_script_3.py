from auri.autorig_lib import push_button, AuriScriptView, AuriScriptViewModel
from PySide2 import QtGui, QtWidgets


class View(AuriScriptView):
    def __init__(self, *args, **kwargs):
        super(View, self).__init__(*args, **kwargs)

    def setup_ui(self):
        chk_a = QtWidgets.QCheckBox("Checkbox A")
        txt_a = QtWidgets.QLineEdit()

        main_layout = QtWidgets.QHBoxLayout()
        main_layout.addWidget(chk_a)
        main_layout.addWidget(txt_a)

        self.setLayout(main_layout)

    def set_viewmodel(self):
        self.viewmodel = ViewModel()


class ViewModel(AuriScriptViewModel):
    def execute(self):
        print __name__

    def __init__(self):
        AuriScriptViewModel.__init__(self)
