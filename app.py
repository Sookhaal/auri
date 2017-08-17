from auri.auri_lib import get_application
from auri.views.bootstrap_view import BootstrapView
from auri.vendor.Qt import QtWidgets
import sys


def bootstrap_standalone():
    app = QtWidgets.QApplication(sys.argv)
    win = BootstrapView()
    app.exec_()


def bootstrap_maya():
    from pymel import core as pmc
    win = BootstrapView(parent=pmc.toQtObject("MayaWindow"))


def bootstrap():
    if get_application() == "standalone":
        bootstrap_standalone()
    elif get_application() == "maya":
        bootstrap_maya()


if __name__ == "__main__":
    bootstrap_standalone()
