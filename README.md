# TheaForBlender

>Welcome to the TheaForBlender repository.

<b>[Thea Render](https://www.thearender.com)</b> is an exceptional quality external rendering solution that is now integrated on <b>[Blender](https://www.blender.org)</b> as tight as possible. Features such as interactive rendering, materials editing, instancing support make it possible to work inside <b>[Blender](https://www.blender.org)</b> creating astonishing results with a smooth workflow between <b>[Blender](https://www.blender.org)</b> and <b>[Thea Render](https://www.thearender.com)</b>.

!['Example Renders'](https://github.com/schroef/TheaForBlender/blob/master/wiki/images/header_theaforblender.jpg)

In addition, we have taken the decision to release the plugin under GPL (open source) that, we believe, fits the spirit of Blender development itself, meaning the plugin is free of charge (Thea Studio license is required).

Code documentation can be found at: <b>[github page](https://grakoczy.github.io/TheaForBlender/)</b>


## Project contains following python modules:

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


## Official Blender Section Thea Render Forum

<b>[Thea Render Forum](http://thearender.com/forum/viewforum.php?f=59)</b>

## What it doesn't contain:
- the RemoteDarkroom as this part is not released under GPL license.


## System Requirements

| **OS** | **Blender** | **UVlayout** |
| ------------- | ------------- | ------------- |
| OSX | Blender 2.77 | All Versions |
| Windows | Blender 2.77 | All Versions |
| Linux | Not Tested | Not Tested |


## Installation Process

1. Download the <b>[latest release](http://thearender.com/forum/viewforum.php?f=69)</b> or clone the repository into a directory of your convenience.
2. If you downloaded the zip file.
3. Open Blender.
4. Go to File -> User Preferences -> Addons.
5. At the bottom of the window, choose *Install From File*.
6. Select the file `TheaForBlender_VERSION.zip` from your download location..
7. Activate the checkbox for the plugin that you will now find in the list.
8. You set setup items for IR render here as well as adding shortcuts, if your OSX user or HDP screen user, you can choose to use Retina Screen, this is for pixel doubling.

> Official plugin is available here: <b>[Thea Render Forum](http://www.thearender.com/forum/viewtopic.php?f=69&t=19184)</b>


## Changelog

| **Version** | **Date** | **Change log** |
| ------------- | ------------- | ------------- |
| 0.5.2 | 07.12.2017 | • Fix<br>- Fix for crash while updating objects in IR mode.
| 0.5.1 | 06.06.2017 | • Fix<br>- Disabled IR start delay until it's working as expected.<br>• Add<br>- Strand option for linked materials.
| 0.5.0 | 26.05.2017 | • Fix<br>- Fixed Mask ID, wasn’t showing correct for multi path.<br>• New<br>- Added new warning for missing or faulty linked materials (IR & production mode).<br>- Added new warning for Border render active (IR render).


<!--
- Fill in data
 -
 -
-->

