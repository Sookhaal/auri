import json
import os
import glob
import re
from PySide2 import QtWidgets
import abc


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
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), "scripts")


def get_categories():
    categories = [cat for cat in os.listdir(get_scripts_directory()) if os.path.isdir(os.path.join(get_scripts_directory(), cat))]
    return categories


def get_scripts(category=None):
    if category is None:
        category = get_categories()[0]
    scripts = next(os.walk(os.path.join(get_scripts_directory(), category)))[2]
    excludes = r"__init__.py"
    scripts = [s for s in scripts if not re.match(excludes, s)]
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


def try_create_rig_file(rig_file_path):
    if not os.path.isfile(rig_file_path):
        file(rig_file_path, "w").close()


def load_rig_file(rig_file_path):
    if os.stat(rig_file_path).st_size > 0:
        with open(rig_file_path) as json_file:
            return json.load(json_file)
    return {}


class AuriScriptView(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(AuriScriptView, self).__init__(*args, **kwargs)
        self.viewmodel = None
        self.set_viewmodel()
        self.setup_ui()

    @abc.abstractmethod
    def set_viewmodel(self):
        pass

    @abc.abstractmethod
    def setup_ui(self):
        pass


class AuriScriptViewModel:
    def __init__(self):
        pass
