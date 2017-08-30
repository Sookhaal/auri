from auri.auri_lib import get_application, get_houdini_style
from auri.views.bootstrap_view import BootstrapView
from auri.vendor.Qt import QtWidgets
import sys


def bootstrap_standalone():
    app = QtWidgets.QApplication(sys.argv)
    win = BootstrapView()
    win.setStyleSheet(get_houdini_style())
    app.exec_()


def bootstrap_maya():
    from pymel import core as pmc
    # No statusbar because there is already one in maya (bottom left by default)
    win = BootstrapView(parent=pmc.toQtObject("MayaWindow"), statusbar=False)


def bootstrap_houdini():
    import hou
    win = BootstrapView(parent=hou.ui.mainQtWindow())
    win.setStyleSheet(get_houdini_style())


def bootstrap_modo():
    import modo
    win = BootstrapView(parent=QtWidgets.QApplication.activeWindow())


def bootstrap_nuke():
    win = BootstrapView(parent=QtWidgets.QApplication.activeWindow())


def bootstrap():
    if get_application() == "standalone":
        bootstrap_standalone()
    elif get_application() == "maya":
        bootstrap_maya()
    elif get_application() == "houdini":
        bootstrap_houdini()
    elif get_application() == "modo":
        bootstrap_modo()
    elif get_application() == "nuke":
        bootstrap_nuke()


if __name__ == "__main__":
    bootstrap_standalone()
