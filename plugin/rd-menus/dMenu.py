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
from PyQt5.QtWidgets import (QWidget)

# For autocomplete
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .PyKrita import *
else:
    from krita import *

class DockerMenu(object):
    def __init__(self):
        super()

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
        # generating actions messes up with the order, so need to sort the list again by the action name
        docker_actions.sort(key= lambda a: a.text())
        for action in docker_actions:
            dockersMenu.addAction(action)

        # this adds a dockers submenu to the dockers menu
        # dockersMenu.addAction(dockers_submenu)