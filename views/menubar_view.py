from PySide2 import QtWidgets, QtCore, QtGui


class MenuBarView(QtWidgets.QMenuBar):
    def __init__(self, common_ctrl):
        """

        Args:
            common_ctrl (auri.controllers.common_controller.CommonController):
        """
        self.common_ctrl = common_ctrl
        super(MenuBarView, self).__init__()

        file_menu = self.addMenu("&File")
        file_menu.addAction(self.new_rig_action())
        file_menu.addAction(self.open_rig_action())
        file_menu.addAction(self.save_rig_action())
        file_menu.addAction(self.save_rig_as_action())

        edit_menu = self.addMenu("&Edit")
        edit_menu.addAction(self.refresh_action())

        # about_menu = self.addMenu("&About")

    def new_rig_action(self):
        action = QtWidgets.QAction("&New Rig", self)
        action.triggered.connect(self.common_ctrl.new_rig)
        action.setShortcut("Ctrl+N")
        action.setStatusTip("Clear current rig")
        return action

    def open_rig_action(self):
        action = QtWidgets.QAction("&Open Rig", self)
        action.triggered.connect(self.common_ctrl.open_rig)
        action.setShortcut("Ctrl+O")
        action.setStatusTip("Open a rig")
        return action

    def save_rig_action(self):
        action = QtWidgets.QAction("&Save Rig", self)
        action.triggered.connect(self.common_ctrl.save_rig)
        action.setShortcut("Ctrl+S")
        action.setStatusTip("Save current rig")
        return action

    def save_rig_as_action(self):
        action = QtWidgets.QAction("Save Rig &As", self)
        action.triggered.connect(self.common_ctrl.save_rig_as)
        action.setShortcut("Ctrl+Shift+S")
        action.setStatusTip("Save current rig as")
        return action

    def refresh_action(self):
        action = QtWidgets.QAction("&Refresh", self)
        action.triggered.connect(self.common_ctrl.refresh)
        action.setShortcut("Ctrl+R")
        action.setStatusTip("Refresh category & script comboboxes")
        return action
