# TheaForBlender

>forked from <b>[grakoczy/TheaForBlender](https://github.com/grakoczy/TheaForBlender)</b>

<b>[Thea Render](https://www.thearender.com)</b> is an exceptional quality external rendering solution that is now integrated on <b>[Blender](https://www.blender.org)</b> as tight as possible. Features such as interactive rendering, materials editing, instancing support make it possible to work inside Blender creating astonishing results with a smooth workflow between Blender and Thea Render.

!['Example Renders'](https://raw.githubusercontent.com/wiki/schroef/TheaForBlender/images/header_thea4blender.jpg)

In addition, we have taken the decision to release the plugin under GPL (open source) that, we believe, fits the spirit of Blender development itself, meaning the plugin is free of charge (Thea Studio license is required).

>Code documentation can be found at: <b>[github page](https://grakoczy.github.io/TheaForBlender/)</b>


### What this project doesn't contain
- the RemoteDarkroom as this part is not released under GPL license.


### Project contains following python modules

- thea_exporter: XML class definitions responsible for writting scene into xml format
- thea_globals: Global variables, logger and functions to read/write the config file
- thea_gui: GUI definition
- thea_IR: Functions and classes handling Interactive Rendering
- thea_operators: Operators definitions
- thea_properties: Scene properties definitions along with helper functions called on property update
- thea_render_main: Functions to prepare environment, export frames and implements TheaRender class
- material preview scenes in scn.thea format with checker texture
- locations.txt file with geographic locations
- License dir with the licenses
- docs dir with auto generated documentation


### System Requirements

| **OS** | **Blender** | **Thea Render** |
| ------------- | ------------- | ------------- |
| OSX | Blender 2.77 | 1.5.09.1462 |
| Windows | Blender 2.77 | 1.5.09.1462 |
| Linux | Not Tested | Not Tested |


### Installation Process

1. Download the latest <b>[offical release](http://thearender.com/forum/viewtopic.php?f=69&t=19184)</b> or use my latest <b>[fork release](https://github.com/schroef/TheaForBlender/releases/)</b>
2. If you downloaded the zip file.
3. Open Blender.
4. Go to File -> User Preferences -> Addons.
5. At the bottom of the window, choose *Install From File*.
6. Select the file `TheaForBlender_VERSION.zip` from your download location..
7. Activate the checkbox for the plugin that you will now find in the list.
8. You set setup items for IR render here as well as adding shortcuts, if your OSX user or HDP screen user, you can choose to use Retina Screen, this is for pixel doubling.

> Official plugin is available here: <b>[Thea Render Forum](http://www.thearender.com/forum/viewtopic.php?f=69&t=19184)</b>


### Changelog

| **Version** | **Date** | **Change log** |
| ------------- | ------------- | ------------- |
| 0.6.0 | 10.08.2017 | • Add<br>- Made new panel menu align better. i think i will run over all panels and make them more compact.<br>  The new panel design have items grouped better together. Makes more it view much easier.<br>

>View complete <b>[change log](https://github.com/schroef/TheaForBlender/wiki/Change-Log)</b>.<br>


### Official Blender Section Thea Render Forum

<b>[Thea Render Forum](http://thearender.com/forum/viewforum.php?f=59)</b>


<!--
- Fill in data
 -
 -
-->

