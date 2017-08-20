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
    win = BootstrapView(parent=pmc.toQtObject("MayaWindow"), statusBar=False)


def bootstrap_houdini():
    import hou
    win = BootstrapView(parent=hou.ui.mainQtWindow())
    win.setStyleSheet(get_houdini_style())


def bootstrap():
    if get_application() == "standalone":
        bootstrap_standalone()
    elif get_application() == "maya":
        bootstrap_maya()
    elif get_application() == "houdini":
        bootstrap_houdini()


if __name__ == "__main__":
    bootstrap_standalone()
