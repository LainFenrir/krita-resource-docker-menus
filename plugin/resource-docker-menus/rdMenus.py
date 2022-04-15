from PyQt5.QtWidgets import (QWidget, QAction)
from krita import *

class RDMenus(Extension):
    def __init__(self, parent):
        super().__init__(parent)

    # Krita.instance() exists, so do any setup work
    def setup(self):
        # Setting up a notifier to only run the code when the window is ready
        # Its necessary to wait the window to be created otherwise qwindow() is null
        appNotifier  = Krita.instance().notifier()
        appNotifier.windowCreated.connect(self.buildMenus)
        pass
    
    # called after setup(self)
    def createActions(self, window):
        pass


    def buildResourceMenu(self,main_menu):
        # Grabbing already existing actions to be added to the menu
        manage_bundles = Krita.instance().action('manage_bundles')
        manage_resources = Krita.instance().action('manage_resources')

        resourceMenu = main_menu.addMenu('Resources')
        resourceMenu.addAction(manage_bundles)
        resourceMenu.addAction(manage_resources)

    def buildDockersMenu(self,main_menu):
        dockers = Krita.instance().action('settings_dockers_menu')
        show_dockers = Krita.instance().action('view_toggledockers')
        show_titles = Krita.instance().action('view_toggledockertitlebars')

        dockersMenu = main_menu.addMenu('Dockers')
        dockersMenu.addAction(show_dockers)
        dockersMenu.addAction(show_titles)
        dockersMenu.addSeparator()
        dockersMenu.addAction(dockers)



    def buildMenus(self):
        main_menu = Krita.instance().activeWindow().qwindow().menuBar()
        main_menu.addSeparator()
        self.buildResourceMenu(main_menu)
        self.buildDockersMenu(main_menu)
        pass



   