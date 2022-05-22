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

# For autocomplete
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .PyKrita import *
else:
    from krita import *

class ResourceMenu(object):
    def __init__(self):
        super()
    
    # Generates the resource menu 
    def buildResourceMenu(self,main_menu):
        # Grabbing already existing actions to be added to the menu
        manage_bundles = Krita.instance().action('manage_bundles')
        manage_resources = Krita.instance().action('manage_resources')

        resourceMenu = main_menu.addMenu('Resources')
        resourceMenu.addAction(manage_bundles)
        resourceMenu.addAction(manage_resources)