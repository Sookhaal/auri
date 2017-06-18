import abc


# Base
class MainToolbarViewModelBase:
    def __init__(self):
        pass

    @abc.abstractmethod
    def on_button_clicked(self):
        pass


# Maya
class MainToolbarViewModelMaya(MainToolbarViewModelBase):
    def __init__(self):
        MainToolbarViewModelBase.__init__(self)

    def on_button_clicked(self):
        print("Maya")


# Standalone
class MainToolbarViewModelStandalone(MainToolbarViewModelBase):
    def __init__(self):
        MainToolbarViewModelBase.__init__(self)

    def on_button_clicked(self):
        print("Standalone")
