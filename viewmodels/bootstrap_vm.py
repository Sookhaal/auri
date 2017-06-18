class BootstrapViewModel:
    def __init__(self, host_application, main_module):
        """

        Args:
            main_module (str): The name of the main module (ex: auto_rig)
            host_application (str): Change viewmodel implementation depending on the hosting application (standalone, maya, nuke or houdini)
        """
        self.host_application = host_application
        self.main_module = main_module
