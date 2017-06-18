import abc


# Base
class MainViewModelBase:
    def __init__(self):
        pass

    @abc.abstractmethod
    def on_button_clicked(self):
        pass


# Maya
class MainViewModelMaya(MainViewModelBase):
    def __init__(self):
        MainViewModelBase.__init__(self)

    def on_button_clicked(self):
        print("Maya")


# Standalone
class MainViewModelStandalone(MainViewModelBase):
    def __init__(self):
        MainViewModelBase.__init__(self)

    def on_button_clicked(self):
        print("Standalone")
