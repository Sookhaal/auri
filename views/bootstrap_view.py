from auri.vendor.Qt import QtWidgets
from auri.controllers.common_controller import CommonController
from auri.controllers.main_controller import MainController
from auri.models.main_model import MainModel
from auri.models.project_model import ProjectModel
from auri.views.main_view import MainView
from auri.views.menubar_view import MenuBarView


class BootstrapView(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(BootstrapView, self).__init__(parent=parent)
        self.setWindowTitle("Auri - New Project")
        self.setMinimumWidth(400)
        self.setMinimumHeight(300)
        self.resize(500, 500)
        self.statusBar()

        self.main_model = MainModel()
        self.project_model = ProjectModel()
        self.common_ctrl = CommonController(self.main_model, self.project_model, self)
        self.main_ctrl = MainController(self.main_model, self.project_model, self.common_ctrl)
        self.main_view = MainView(self.main_model, self.main_ctrl)

        self.setMenuBar(MenuBarView(self.common_ctrl))

        self.setCentralWidget(self.main_view)
        self.common_ctrl.main_view = self.main_view

        self.show()
