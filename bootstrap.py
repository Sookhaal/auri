import auri.views.menubar_view
import auri.views.main_toolbar_view
import auri.views.bootstrap_view

reload(auri.views.menubar_view)
reload(auri.views.main_toolbar_view)
reload(auri.views.bootstrap_view)

from auri.viewmodels.bootstrap_vm import BootstrapViewModel
from auri.autorig_lib import get_application
from PySide2 import QtWidgets, QtCore, QtGui
from auri.views.bootstrap_view import BootstrapView
import sys


def bootstrap_standalone():
    app = QtWidgets.QApplication(sys.argv)
    win = BootstrapView(view_model=BootstrapViewModel("standalone", "auto_rig"))
    app.exec_()


def bootstrap_maya():
    from pymel import core as pmc
    win = BootstrapView(parent=pmc.toQtObject("MayaWindow"), view_model=BootstrapViewModel("maya", "auto_rig"))


def bootstrap():
    if get_application() == "standalone":
        bootstrap_standalone()
    elif get_application() == "maya":
        bootstrap_maya()


if __name__ == "__main__":
    bootstrap_standalone()
