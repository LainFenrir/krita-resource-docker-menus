# Resource and Docker Menus

A simple plugin to add main menu entries for dockers and resources.

This plugin introduces 2 new menus, resources and dockers as a way to make them more visible and easier to access.

This plugin doesn't remove the the dockers and resources from the settings menu, nor its the intention of this plugin. So resources and dockers are accessible from both menus.

**Resources**  
Adds actions to open the resouce manager and the resource library that are also located in the settings menu.

**Dockers**  
Adds a menu with docker related actions of showing dockers and showing the docker titles, and also has a list of dockers not contained in a submenu.

## Installation

1- Copy the contents of the `plugin` folder into the `pykrita` folder in the krita resource folder (accessible through settings>manage resources>open resource folder).  
The folder resource-docker-menus need to be completely moved (moving just the files inside will not work).  
2- Open krita, go to settings>configure krita> python plugin manager. Locate the `Resource and Dockers Menus` and check it.  
3- Restart krita. They should appear on the main menu after `Help`.  

## Tips
There are some parts of commented code in the `rdMenus.py` in the `buildDockersMenu()` that can be uncommented to change the look.

to have a simple separator without text, change the code:

```py
    # dockersMenu.addSeparator()
    dockersMenu.addSection('Dockers')

    #change to
    dockersMenu.addSeparator()
    # dockersMenu.addSection('Dockers')
```

To have the original docker submenu, change the code:

```py
    #Grabs the actual dockers submenu 
    # dockers_submenu = Krita.instance().action('settings_dockers_menu')

#...some code here

 # adds the docker actions into the menu
        docker_actions = self.grabDockersActions()
        for action in docker_actions:
            dockersMenu.addAction(action)

        # this adds a dockers submenu to the dockers menu
        # dockersMenu.addAction(dockers_submenu)

# change to

    #Grabs the actual dockers submenu 
    dockers_submenu = Krita.instance().action('settings_dockers_menu')
    
    #...some code here

    # adds the docker actions into the menu
        # docker_actions = self.grabDockersActions()
        # for action in docker_actions:
        #     dockersMenu.addAction(action)

        # this adds a dockers submenu to the dockers menu
        dockersMenu.addAction(dockers_submenu)
```
