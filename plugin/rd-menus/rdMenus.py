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
from PyQt5.QtWidgets import (QAction)
from .dMenu import DockerMenu
from .rMenu import ResourceMenu
# For autocomplete
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .PyKrita import *
else:
    from krita import *

##TODO:
# Add a settings submenu for dockers
# move show title and show dockers to the settings submenu
# add option to move scripter from scripts to tool menu
# add option to show all dockers as just a list or submenu
# add a favorite dockers section 
# create dialog window to add dockers and arrange them in this list
# save system for options and favorite docker list


class RDMenus(Extension):
    def __init__(self, parent):
        super().__init__(parent)

        #Instances the menu classes
        self.dmenu = DockerMenu()
        self.rmenu = ResourceMenu()

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

    # Calls the menus creation also adding a separator from the original krita menu
    def buildMenus(self):
        main_menu = Krita.instance().activeWindow().qwindow().menuBar()
        
        # Adds a separator from the main menu
        separator = QAction('|',main_menu)
        separator.setEnabled(False)
        main_menu.addAction(separator)

        # Calls the bulding functions for the menus
        self.rmenu.buildResourceMenu(main_menu)
        self.dmenu.buildDockersMenu(main_menu)