import os
import glob
from PySide2 import QtWidgets


def get_application():
    host_application = ""
    try:
        import maya.OpenMayaUI as mui
        import maya.cmds as cmds
        host_application = "maya"
    except ImportError:
        try:
            import hou
            host_application = "houdini"
        except ImportError:
            try:
                import nuke
                import nukescripts
                host_application = "nuke"
            except ImportError:
                host_application = "standalone"
    return host_application


def get_scripts_directory():
    return os.path.abspath("./scripts/")


def get_categories():
    categories = [cat for cat in os.listdir(get_scripts_directory()) if os.path.isdir(os.path.join(get_scripts_directory(), cat))]
    return categories


def get_scripts(category=None):
    if category is None:
        return ""
    # scripts = glob.glob(os.path.join(get_scripts_directory(), category, "*.py"))
    scripts = next(os.walk(os.path.join(get_scripts_directory(), category)))[2]
    return scripts


def push_button(text, signal=None):
    assert isinstance(text, str)
    btn = QtWidgets.QPushButton(text)
    if signal is not None:
        btn.clicked.connect(signal)
    return btn


def grpbox(title, lyt=None):
    if lyt is None:
        lyt = QtWidgets.QVBoxLayout()
    g = QtWidgets.QGroupBox(title=title)
    g.setLayout(lyt)
    return g
