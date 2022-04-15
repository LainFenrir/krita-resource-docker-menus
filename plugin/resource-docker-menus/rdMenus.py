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

    # Generates the resource menu 
    def buildResourceMenu(self,main_menu):
        # Grabbing already existing actions to be added to the menu
        manage_bundles = Krita.instance().action('manage_bundles')
        manage_resources = Krita.instance().action('manage_resources')

        resourceMenu = main_menu.addMenu('Resources')
        resourceMenu.addAction(manage_bundles)
        resourceMenu.addAction(manage_resources)

    # Grabs the toggleViewAction of all krita dockers and returns them in a list
    # This generates a checkable action the same way as `settings_dockers_menu` is
    def grabDockersActions(self):
        dockers = Krita.instance().dockers()
        actions = []
        for docker in dockers:
            actions.append(docker.toggleViewAction())
        return actions

    # Generates the docker menu 
    def buildDockersMenu(self,main_menu):
        #Grabs the actual dockers submenu 
        # dockers_submenu = Krita.instance().action('settings_dockers_menu')

        # grabs the dockers related actions:
        # - to show dockers
        # - to toggle the title of the dockers
        show_dockers = Krita.instance().action('view_toggledockers')
        show_titles = Krita.instance().action('view_toggledockertitlebars')

        dockersMenu = main_menu.addMenu('Dockers')
        dockersMenu.addAction(show_dockers)
        dockersMenu.addAction(show_titles)
        # dockersMenu.addSeparator()
        dockersMenu.addSection('Dockers')

        # adds the docker actions into the menu
        docker_actions = self.grabDockersActions()
        for action in docker_actions:
            dockersMenu.addAction(action)

        # this adds a dockers submenu to the dockers menu
        # dockersMenu.addAction(dockers_submenu)


    # Calls the menus creation also adding a separator from the original krita menu
    def buildMenus(self):
        main_menu = Krita.instance().activeWindow().qwindow().menuBar()
        
        # Adds a separator from the main menu
        separator = QAction('|',main_menu)
        separator.setEnabled(False)
        main_menu.addAction(separator)

        # Calls the bulding functions for the menus
        self.buildResourceMenu(main_menu)
        self.buildDockersMenu(main_menu)
   