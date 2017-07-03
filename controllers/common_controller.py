from auri.autorig_lib import get_categories, get_scripts


class CommonController(object):
    def __init__(self, main_model):
        """

        Args:
            main_model (auri.models.main_model.MainModel):
        """
        self.main_model = main_model
        self.category_combobox = None
        self.script_combobox = None
        self.refresh()

    def new_rig(self):
        pass

    def open_rig(self):
        pass

    def save_rig(self):
        pass

    def save_rig_as(self):
        pass

    def refresh(self):
        self.refresh_categories()
        self.refresh_scripts()

    def refresh_categories(self):
        categories = get_categories()
        self.main_model.categories = categories
        if self.category_combobox is not None:
            self.category_combobox.setCurrentIndex(0)

    def refresh_scripts(self, category=None):
        scripts = get_scripts(category)
        self.main_model.scripts = scripts
        # if self.script_combobox is not None:
        #     self.script_combobox.setCurrentIndex(0)
