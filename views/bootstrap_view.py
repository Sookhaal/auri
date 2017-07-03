from PySide2 import QtWidgets
from auri.controllers.common_controller import CommonController
from auri.controllers.main_controller import MainController
from auri.models.main_model import MainModel
from auri.views.main_view import MainView
from auri.views.menubar_view import MenuBarView


class BootstrapView(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(BootstrapView, self).__init__(parent=parent)
        self.setWindowTitle("Auri")
        self.setMinimumWidth(500)
        self.setMinimumHeight(300)
        self.statusBar()

        self.main_model = MainModel()
        self.common_ctrl = CommonController(self.main_model)

        self.setMenuBar(MenuBarView(self.common_ctrl))

        self.main_ctrl = MainController(self.main_model, self.common_ctrl)
        self.setCentralWidget(MainView(self.main_model, self.main_ctrl))

        self.show()
