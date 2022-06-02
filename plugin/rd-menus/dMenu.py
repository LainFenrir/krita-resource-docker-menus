"""
rdMenus is a plugin for krita that adds resource and docker menus
    Copyright (C) 2022  LunarKreatures

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from PyQt5.QtWidgets import (QAction,QMenu)

# For autocomplete
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .PyKrita import *
else:
    from krita import *

# todo create favorites submenu
# todo create dialog interface to add the favorites
# todo persist information

class DockerMenu(object):
    def __init__(self):
        super()
        self.dockerActionsNames = []
        self.dockerActions = []

        # Had to put it hrere otherwise the QAction is not created
        self.show_dockerSubmenu = QAction("Use Dockers Submenu")
        self.show_dockerSubmenu.setCheckable(True)
        self.show_dockerSubmenu.setStatusTip("Toggles between dockers submenu or the section")
        self.show_dockerSubmenu.toggled.connect(self.toggleDockerSubMenu)



    # Grabs the toggleViewAction of all krita dockers and returns them in a list
    # This generates a checkable action the same way as `settings_dockers_menu` is
    def grabDockersActions(self):
        dockers = Krita.instance().dockers()
        actions = []
        for docker in dockers:
            actions.append(docker.toggleViewAction())

        # generating actions messes up with the order, so need to sort the list again by the action name
        actions.sort(key= lambda a: a.text())
        return actions

    # Generates the docker menu 
    def buildDockersMenu(self,main_menu):
        dockersMenu = main_menu.addMenu('Dockers')
        dockersMenu.setObjectName('Dockers')

        #Grabs the actual dockers submenu 
        dockers_submenu = Krita.instance().action('settings_dockers_menu')
        dockers_submenu.setVisible(False)
        

        optionsMenu = self.buildOptions(dockersMenu)
        
        # this adds a dockers submenu to the dockers menu
        dockersMenu.addAction(dockers_submenu)
        optionsMenu.addAction(self.show_dockerSubmenu)

        dockersMenu.addSection('Dockers')

        # adds the docker actions into the menu
        docker_actions = self.grabDockersActions()
        self.dockerActions = docker_actions

        for action in docker_actions:
            self.dockerActionsNames.append(action.text())    
        dockersMenu.addActions(docker_actions)

    def buildOptions(self, dockers_menu):
        # grabs the dockers related actions:
        # - to show dockers
        # - to toggle the title of the dockers
        show_dockers = Krita.instance().action('view_toggledockers')
        show_titles = Krita.instance().action('view_toggledockertitlebars')

        dOptionsMenu = dockers_menu.addMenu('Options')
        dOptionsMenu.setObjectName('Options')

        dOptionsMenu.addAction(show_dockers)
        dOptionsMenu.addAction(show_titles)
        return dOptionsMenu

    def toggleDockerSubMenu(self):
        main_menu = Krita.instance().activeWindow().qwindow().menuBar()
        dockers = main_menu.findChild(QMenu,'Dockers')
        submenu = None
        for d in dockers.actions():
            if d.objectName() == "settings_dockers_menu":
                submenu = d
                break
        
        # Since the actions in the dockers submenu are the same as the ones in the menu,
        # i cant make them invisble cause this will make them invisible in both places
        # the only option i found is to remove and add them back to the menu
        if self.show_dockerSubmenu.isChecked():
            submenu.setVisible(True)
            for d in dockers.actions():
                if d.text() in self.dockerActionsNames:
                    dockers.removeAction(d)


        else:
            submenu.setVisible(False)
            for d in dockers.actions():
                dockers.addActions(self.dockerActions)

