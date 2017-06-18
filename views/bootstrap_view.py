from PySide2 import QtWidgets, QtCore, QtGui

from auri.views.main_view import MainView
from auri.views.menubar_view import MenuBar
from auri.views.main_toolbar_view import MainToolBarView


class BootstrapView(QtWidgets.QMainWindow):
    def __init__(self, parent=None, view_model=None):
        """

        Args:
            view_model (auto_rig.viewmodels.bootstrap_vm.BootstrapViewModel):
        """
        super(BootstrapView, self).__init__(parent=parent)
        self.bootstrap_viewmodel = view_model
        self.setWindowTitle("Auri")
        self.setMinimumWidth(500)
        self.setMinimumHeight(300)

        self.setMenuBar(MenuBar())
        # self.addToolBar(MainToolBarView(self.bootstrap_viewmodel))
        self.setCentralWidget(MainView(self.bootstrap_viewmodel))

        self.show()
