from PySide2 import QtWidgets

from auri.autorig_lib import get_application
from auri.viewmodels.main_toolbar_vm import MainToolbarViewModelStandalone, MainToolbarViewModelMaya


class MainToolBarView(QtWidgets.QToolBar):
    def __init__(self, vm):
        """

        Args:
            vm (auto_rig.viewmodels.bootstrap_vm.BootstrapViewModel):
        """
        super(MainToolBarView, self).__init__()
        if vm.host_application == "standalone":
            self.view_model = MainToolbarViewModelStandalone()
        elif vm.host_application == "maya":
            self.view_model = MainToolbarViewModelMaya()
        the_action = self.addAction("The Test", self.view_model.on_button_clicked)
        # assert isinstance(bootstrap_viewmodel, auto_rig.viewmodels.bootstrap_viewmodel.BootstrapViewModel)

    def the_action(self):
        print __name__.split(".")[-1]
