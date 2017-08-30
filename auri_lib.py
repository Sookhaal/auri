import abc
import os
import re
from auri import __version__
from auri.vendor.Qt import QtWidgets


def get_application():
    try:
        import maya.OpenMayaUI as mui
        import maya.cmds as cmds
        import pymel.core as pymel
        host_application = "maya"
    except (ImportError, TypeError):
        try:
            import hou
            host_application = "houdini"
        except ImportError:
            try:
                import nuke
                import nukescripts
                host_application = "nuke"
            except ImportError:
                try:
                    import MaxPlus
                    host_application = "3dsmax"
                except ImportError:
                    host_application = "standalone"
    return host_application


def get_auri_version():
    return __version__


def get_scripts_directory():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), "scripts")


def get_categories():
    categories = [cat for cat in os.listdir(get_scripts_directory()) if os.path.isdir(os.path.join(get_scripts_directory(), cat))]
    return categories


def get_subcategories(category=None):
    if category is None:
        category = get_categories()[0]
    category = os.path.join(get_scripts_directory(), category)
    subcategories = [subcat for subcat in os.listdir(category) if subcat != ".git" and os.path.isdir(os.path.join(category, subcat))]
    return subcategories


def get_scripts(category=None, subcategory=None):
    if category is None:
        category = get_categories()[0]
    if subcategory is None:
        subcategory = get_subcategories(category)[0]
    scripts = next(os.walk(os.path.join(get_scripts_directory(), category, subcategory)))[2]
    excludes = r"(__init__.py)|(.*.pyc)"
    includes = r".*.py$"
    scripts = [s for s in scripts if re.match(includes, s) and not re.match(excludes, s)]
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


def get_resources_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources")


def get_auri_icon(icon_name):
    return os.path.join(get_resources_path(), "icons", icon_name)


def is_checked(chkbox_state):
    """
    Connect to a checkbox stateChanged
    Args:
        chkbox_state (int):
    """
    switch = {0: False, 2: True}
    return switch.get(chkbox_state)


def get_houdini_style():
    with open(os.path.join(get_resources_path(), "themes", "houdini_base.qss"), "r") as houdini_style:
        style = houdini_style.read()
    return style


class AuriScriptView(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(AuriScriptView, self).__init__(*args, **kwargs)
        self.ctrl = None
        self.model = None
        self.set_model()
        self.set_controller()
        self.setup_ui()

    @abc.abstractmethod
    def set_model(self):
        pass

    @abc.abstractmethod
    def set_controller(self):
        pass

    @abc.abstractmethod
    def setup_ui(self):
        pass

    @abc.abstractmethod
    def refresh_view(self):
        pass


class AuriScriptController:
    def __init__(self):
        pass

    @abc.abstractmethod
    def execute(self):
        pass

    @abc.abstractmethod
    def prebuild(self):
        pass


class AuriScriptModel:
    def __init__(self):
        self.module_name = None
