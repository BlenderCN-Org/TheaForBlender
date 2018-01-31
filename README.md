# TheaForBlender

>Welcome to the TheaForBlender repository.

<b>[Thea Render](https://www.thearender.com)</b> is an exceptional quality external rendering solution that is now integrated on <b>[Blender](https://www.blender.org)</b> as tight as possible. Features such as interactive rendering, materials editing, instancing support make it possible to work inside <b>[Blender](https://www.blender.org)</b> creating astonishing results with a smooth workflow between <b>[Blender](https://www.blender.org)</b> and <b>[Thea Render](https://www.thearender.com)</b>.

!['Example Renders'](https://github.com/schroef/TheaForBlender/blob/master/wiki/images/header_theaforblender.jpg)

In addition, we have taken the decision to release the plugin under GPL (open source) that, we believe, fits the spirit of Blender development itself, meaning the plugin is free of charge (Thea Studio license is required).

>Code documentation can be found at: <b>[github page](https://grakoczy.github.io/TheaForBlender/)</b>


## What this project doesn't contain
- the RemoteDarkroom as this part is not released under GPL license.


## Project contains following python modules

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

| **OS** | **Blender** | **UVlayout** |
| ------------- | ------------- | ------------- |
| OSX | Blender 2.77 | All Versions |
| Windows | Blender 2.77 | All Versions |
| Linux | Not Tested | Not Tested |


### Installation Process

1. Download the <b>[latest release](http://thearender.com/forum/viewforum.php?f=69)</b> or clone the repository into a directory of your convenience.
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
| 0.5.4 | 13.07.2017 | • Fix<br>- Fixed Parallel preview in Blender, Thea doesn’t support shift X or Y, so it turnes off now.<br>- Fix for when 2 layers and coating was active, if the second layer had a weight map, this got transferred to the coating layer. <br>- Fixed mesh export when solidify mod is on, modifier get earlier applied. Did some test and difference didn’t look that much different (perhaps you should check it as well). <br>- Fixed a error when Material Preview for LUT materials was working (thea_render_main># 4176). <br>- Fixed IES lamp > Doesn’t have Attenuation. <br>- Fixed SPOT as its, was error in the code. <br>- Fixed when more than 1 sun is in scene, got exported as lamp. Now more suns can be exported. <br>- Fixed IBL Type > was added to all IBL maps, only needs to be applied to Image Based Lighting (Thea_exporter>#1851).<br><br>• Add<br>- Updated "Sync with Thea", all camera settings, lamp, sun settings get synced now as well.<br>- Updated layout Camera Panel, added items like; focal width and height, camera preview method (Spherical or Ortho), Added better check when items or on and which should be off.<br>- Updated Material Panel when IOR file is checked, all other items like; color, reflection, absorption, abbe get inactive now.<br>- Added Search button for IOR file, list is to long and goes beyond screen, now you can quickly search the dropdownmenu.<br>- Added Search button for LUT mat library, list is to long and goes beyond screen, now you can quickly search the dropdownmenu.<br>- Added option to choose export or frame folder for image save location. Thea4Blender always saves 2 images, 1 in export folder and 1 in frame folder. When doing a animation this takes a lot of unneeded time.<br>- Added more precise numbers for F-Number (aperture) and DOF distance. Needed to be more precise.<br>
| 0.5.3 | 22.06.2017 | • Add<br>- Update linked material warning with list of missing materials and name of object containing that material.<br>- Missing linked material warning added to export frame (XML file) from and export to studio.<br>- Missing linked material warning added to production render.<br>- Check list added in Material Tab, show list of remaining missing materials in scene.
| 0.5.2 | 13.06.2017 | • Fix<br>- Fix for crash while updating objects in IR mode.
| 0.5.1 | 06.06.2017 | • Fix<br>- Disabled IR start delay until it's working as expected.<br><br>• Add<br>- Strand option for linked materials.
| 0.5.0 | 26.05.2017 | • Fix<br>- Fixed Mask ID, wasn’t showing correct for multi path.<br><br>• Add<br>- Added new warning for missing or faulty linked materials (IR & production mode).<br>- Added new warning for Border render active (IR render).


### Official Blender Section Thea Render Forum

<b>[Thea Render Forum](http://thearender.com/forum/viewforum.php?f=59)</b>


<!--
- Fill in data
 -
 -
-->

