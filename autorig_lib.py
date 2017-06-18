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
