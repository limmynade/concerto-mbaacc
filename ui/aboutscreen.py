from ui.concertoscreen import ConcertoScreen
from kivy.resources import resource_find
import config

class AboutScreen(ConcertoScreen):

    def __init__(self,CApp):
        super().__init__(CApp)
        with open(resource_find('res/about.txt'), mode="r", encoding="utf-8") as f:
            c = f.read()
            self.ids['about'].text = c
        self.ids['about'].bind(on_ref_press=self.open_link)
        self.ids['version'].text = "Version %s" % config.CURRENT_VERSION
