"""
.. module:: thea_operators
   :platform: OS X, Windows, Linux
   :synopsis: Operators definitions

.. moduleauthor:: Grzegorz Rakoczy <grzegorz.rakoczy@solidiris.com>


"""

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy
import subprocess
import os
import sys
import copy
import time
import struct
from random import random
import platform
from math import *
from . import thea_globals
from TheaForBlender.thea_render_main import *
if os.name == "nt":
    try:
        import winreg
    except:
        thea_globals.log.info("Can't access windows registry")


class THEA_OT_quitBlender(bpy.types.Operator):
    bl_idname = "thea.quit_blender"
    bl_label = "quit Blender"

    def invoke(self, context, event):
        thea_globals.log.info("quit blender")
        try:
            if context.scene.get('thea_SDKPort'):
                port = context.scene.get('thea_SDKPort')
            else:
                port = 30000
        except:
            port = 30000

        data = sendSocketMsg('localhost', port, b'version')
        if data.find('v'):
            message = b'message "exit"'
            data = sendSocketMsg('localhost', port, message)

        try:
            if context.scene.get('thea_PreviewSDKPort'):
                port = context.scene.get('thea_PreviewSDKPort')
            else:
                port = 30001
        except:
            port = 30001

        data = sendSocketMsg('localhost', port, b'version')
        if data.find('v'):
            message = b'message "exit"'
            data = sendSocketMsg('localhost', port, message)

        bpy.ops.wm.quit_blender()
        return {'FINISHED'}


class RENDER_PT_thea_materialsPath(bpy.types.Operator):
    bl_idname = "thea.materials_path"
    bl_label = "Materials Path"

    filepath = bpy.props.StringProperty(name="file path", description="getting file path", maxlen= 1024, default= "")

    def execute(self, context):
        FilePath = self.filepath
        #set the string path fo the file here.
        #this is a variable created from the top to start it
        bpy.context.scene.thea_materialsPath = FilePath
        ##print("path: ",FilePath)#display the file name and current path

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}


class RENDER_PT_thea_makeLUT(bpy.types.Operator):
    bl_idname = "thea.make_lut"
    bl_label = "Generate LUT"

    def invoke(self, context, event):
        global dataPath

        scene = context.scene

        (exportPath, theaPath, theaDir, dataPath, currentBlendDir, currentBlendFile) = setPaths(scene)
        exporter=initExporter()

        import os

        # set paths here
        try:
            searchPath = scene.get('thea_materialsPath')
        except:
            searchPath = os.path.join(dataPath, "Materials")
        if not searchPath:
            searchPath = os.path.join(dataPath, "Materials")

        lutFileName = os.path.join(searchPath, "BlenderTransTable.txt")
        ##print("lutFileName: ", lutFileName)
        try:
            allowOverwrite = scene.get('thea_overwriteLUT')
        except:
            allowOverwrite = False


        allfiles = []
        subfiles = []

        if getattr(scene, 'thea_LUTScanSubdirectories'):
            for root, dirs, files in os.walk(searchPath):
                dirs[:] = [d for d in dirs if not d.startswith('.')]
                for f in files:
                    if f.endswith('.mat.thea') and not f.startswith('.'):
                        allfiles.append(os.path.join(root, f))
                        #if root != searchPath: # I'm in a subdirectory
                        subfiles.append(os.path.join(root, f))
        else:
             for f in os.listdir(searchPath):
                if f.endswith('.mat.thea') and not f.startswith('.'):
                    allfiles.append(os.path.join(searchPath, f))
                    #if root != searchPath: # I'm in a subdirectory
                    subfiles.append(os.path.join(searchPath, f))
        if len(subfiles) > 0:
            matList = []
            for matFile in sorted(subfiles):
                matList.append((os.path.basename(matFile).split(".mat.thea")[0], matFile))

            if os.path.exists(lutFileName) and not allowOverwrite:
                #print("\n!!\n!!!!!!!!!! File already exist !!!!!!!!\n!!")
                self.report({'ERROR'}, "!!!!!!!!!! File already exist !!!!!!!!\nPlease allow to overwrite the file")
                return {'FINISHED'}
            else:
                trFile = open(lutFileName, "w")
                #print("trFile: ", trFile)
                trFile.write("#Material translation table\n")
                trFile.write("#Blender_name;path/to/Thea/mat/file\n")
                for mat in matList:
                    trFile.write("%s;%s\n" % (mat[0][0:40], mat[1]))

        #print("LUT file generated! Press F8 to reaload LUT into GUI!")
        self.report({'INFO'}, "LUT file generated! Press F8 to reaload LUT into GUI!")
        scene['thea_lutMessage'] = "LUT file generated! Press F8 to reaload LUT into GUI!"

        return {'FINISHED'}


class RENDER_PT_thea_MoreLocations(bpy.types.Operator):
    bl_idname = "thea.morelocations"
    bl_label = "Display more locations"

    def invoke(self, context, event):
        scene = context.scene
        scene.thea_maxLines = int(scene.thea_maxLines)+200
        EnumProperty(   attr="thea_EnvLocationsMenu",
                items=getLocations(scene.thea_maxLines),
                name="Location",
                description="Location",
                default="3")
        return {'FINISHED'}


class RENDER_PT_thea_RenderFrame(bpy.types.Operator):
    bl_idname = "thea.render_frame"
    bl_label = "Render current frame"

    def invoke(self, context, event):
        scene = context.scene
        args = renderFrame(scene, scene.frame_current)
        p = subprocess.Popen(args)
        return {'FINISHED'}


class RENDER_PT_thea_RenderAnimation(bpy.types.Operator):
    bl_idname = "thea.render_animation"
    bl_label = "Render animation"

    def invoke(self, context, event):
        scene = context.scene
        renderAnimation(scene)
        return {'FINISHED'}


class RENDER_PT_thea_ExportFrame(bpy.types.Operator):
    bl_idname = "thea.export_frame"
    bl_label = "Export current frame"
    #   CHANGED > Added better description
    bl_description="Save current frame to scn.thea file"

    def invoke(self, context, event):
        scene = context.scene
        (exportPath, theaPath, theaDir, dataPath, currentBlendDir, currentBlendFile) = setPaths(scene)

        try:
            if bpy.context.active_object.mode != 'OBJECT':
                self.report({'ERROR'}, "Please change to object mode before rendering!")
                return {'FINISHED'}
        except:
            pass
        if len(currentBlendFile)<2:
            self.report({'ERROR'}, "Please save the scene before exporting!")
            return {'FINISHED'}
        if not os.path.isdir(exportPath):
            self.report({'ERROR'}, "Please set proper output path before exporting!")
            return {'FINISHED'}
#        from TheaForBlender.thea_render_main import checkTheaExtMat
#        if (checkTheaExtMat()==False):
#            self.report({'ERROR'}, "Please check linked materials")
##            thea_globals.log.debug("*** CheckMaterials = %s ***" % checkTheaExtMat())
#            return {'FINISHED'}
        from TheaForBlender.thea_render_main import checkTheaExtMat
        checkTheaExtMat()
        valuesExt = checkTheaExtMat()
        if (valuesExt[0]==False):
#            self.report({'ERROR'}, "Please link Material: %s > Object: %s" % (valuesExt[1], valuesExt[2]))
            missing_Mat = ""
            for mat in valuesExt[3]:
                missing_Mat = missing_Mat+"\n"+mat
            self.report({'ERROR'}, "Please link Material:%s" % missing_Mat)
#            thea_globals.log.debug("*** CheckMaterials = %s ***" % valuesExt[1])
            return {'FINISHED'}


        exporter=initExporter()
        #print("exporter: ", exporter)
        #print("scene.render.filepath: ",exportPath)
        #os.chdir(scene.render.filepath)
        os.chdir(exportPath)
        scene.thea_startTheaAfterExport = True
        args = exportFrame(scene,scene.frame_current,exporter=exporter)
        #print("args: ", args)
        if not args:
            self.report({'ERROR'}, "Please set proper output path before exporting!")
            return {'FINISHED'}
#         if scene.get('thea_startTheaAfterExport'):
        p = subprocess.Popen(args)
        del exporter
        return {'FINISHED'}

class RENDER_PT_thea_SaveFrame(bpy.types.Operator):
    '''Save current frame to file'''
    bl_idname = "thea.save_frame"
    bl_label = "Save current frame to file"
#   CHANGED > Added better description
    bl_description = "Save current frame to XML-file"
#    and bpy.context.selected_objects != None
    filepath = bpy.props.StringProperty(name="file path", description="getting file path", maxlen= 1024, default= "")



    def execute(self, context):
        FilePath = self.filepath
#         #set the string path fo the file here.
#         #this is a variable created from the top to start it
#         bpy.context.scene.thea_mergeFilePath = FilePath
        #print("path: ",FilePath)#display the file name and current path
        scene = context.scene
        (exportPath, theaPath, theaDir, dataPath, currentBlendDir, currentBlendFile) = setPaths(scene)



        if bpy.context.active_object.mode != 'OBJECT':
            self.report({'ERROR'}, "Please change to object mode before exporting!")
            return {'FINISHED'}
        if len(currentBlendFile)<2:
            self.report({'ERROR'}, "Please save the scene before exporting!")
            return {'FINISHED'}
        if not os.path.isdir(exportPath):
            self.report({'ERROR'}, "Please set proper output path before exporting!")
            return {'FINISHED'}
        from TheaForBlender.thea_render_main import checkTheaExtMat
        checkTheaExtMat()
        valuesExt = checkTheaExtMat()
        if (valuesExt[0]==False):
#            self.report({'ERROR'}, "Please link Material: %s > Object: %s" % (valuesExt[1], valuesExt[2]))
            missing_Mat = ""
            for mat in valuesExt[3]:
                missing_Mat = missing_Mat+"\n"+mat
            self.report({'ERROR'}, "Please link Material:%s" % missing_Mat)
#            thea_globals.log.debug("*** CheckMaterials = %s ***" % valuesExt[1])
            return {'FINISHED'}


        exporter=initExporter()
        scene.thea_startTheaAfterExport = False
        #print("exporter: ", exporter)
#         #print("scene.render.filepath: ",exportPath)
        #os.chdir(scene.render.filepath)
#         os.chdir(exportPath)
        args = exportFrame(scene,scene.frame_current,exporter=exporter,xmlFile = self.filepath)
        if not args:
            self.report({'ERROR'}, "Please set proper output path before exporting!")
            return {'FINISHED'}
#         if scene.get('thea_startTheaAfterExport'):
#             p = subprocess.Popen(args)
        del exporter

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}

class RENDER_PT_thea_SaveFrame2(bpy.types.Operator):
    bl_idname = "thea.save_frame2"
    bl_label = "Save current frame to file"

    filepath = bpy.props.StringProperty(name="file path", description="getting file path", maxlen= 1024, default= "")

    def execute(self, context):
        FilePath = self.filepath
        #set the string path fo the file here.
        #this is a variable created from the top to start it
        #bpy.context.scene.thea_mergeFilePath = FilePath


        return {'FINISHED'}



    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)

        scene = context.scene
        (exportPath, theaPath, theaDir, dataPath, currentBlendDir, currentBlendFile) = setPaths(scene)



        if bpy.context.active_object.mode != 'OBJECT':
            self.report({'ERROR'}, "Please change to object mode before exporting!")
            return {'FINISHED'}
        if len(currentBlendFile)<2:
            self.report({'ERROR'}, "Please save the scene before exporting!")
            return {'FINISHED'}
        if not os.path.isdir(exportPath):
            self.report({'ERROR'}, "Please set proper output path before exporting!")
            return {'FINISHED'}


        #print("path: ",self.filepath)#display the file name and current path

        exporter=initExporter()
        #print("exporter: ", exporter)
        #print("scene.render.filepath: ",exportPath)
        #os.chdir(scene.render.filepath)
        os.chdir(exportPath)
        args = exportFrame(scene,scene.frame_current,exporter=exporter)
        if not args:
            self.report({'ERROR'}, "Please set proper output path before exporting!")
            return {'FINISHED'}
#         if scene.get('thea_startTheaAfterExport'):
#             p = subprocess.Popen(args)
        del exporter
        return {'FINISHED'}


class RENDER_PT_thea_ExportAnim(bpy.types.Operator):
    '''Export animation script'''
    bl_idname = "thea.export_anim"
    bl_label = "Export animation script"

    def invoke(self, context, event):
        scene = context.scene
        (exportPath, theaPath, theaDir, dataPath, currentBlendDir, currentBlendFile) = setPaths(scene)
        if len(currentBlendFile)<2:
            self.report({'ERROR'}, "Please save the scene before exporting!")
            return {'FINISHED'}
        if not os.path.isdir(exportPath):
            self.report({'ERROR'}, "Please set proper output path before exporting!")
            return {'FINISHED'}

        exporter=initExporter()
        #print("exporter: ", exporter)
        exportAnim(scene, exporter=exporter)
        del exporter
        return {'FINISHED'}


class RENDER_PT_thea_ExportStillCameras(bpy.types.Operator):
    '''Export visible cameras as animation script'''
    bl_idname = "thea.export_still_cameras"
    bl_label = "Export visible cameras as animation"

    def invoke(self, context, event):

        scene = context.scene
        (exportPath, theaPath, theaDir, dataPath, currentBlendDir, currentBlendFile) = setPaths(scene)
        if len(currentBlendFile)<2:
            self.report({'ERROR'}, "Please save the scene before exporting!")
            return {'FINISHED'}
        if not os.path.isdir(exportPath):
            self.report({'ERROR'}, "Please set proper output path before exporting!")
            return {'FINISHED'}
        exporter=initExporter()
        exportStillCameras(scene, exporter=exporter)
        return {'FINISHED'}


class RENDER_PT_thea_EnableAnimated(bpy.types.Operator):
    '''Set selected objects as animated meshes'''
    bl_idname = "thea.enable_animated"
    bl_label = "Set selected objects as animated meshes"

    def invoke(self, context, event):

        scene = context.scene
        for object in bpy.context.selected_objects:
            object['thAnimated'] = True
        return {'FINISHED'}



class RENDER_PT_thea_DisableAnimated(bpy.types.Operator):
    '''Unset selected objects as animated meshes'''
    bl_idname = "thea.disable_animated"
    bl_label = "Unset selected objects as animated meshes"

    def invoke(self, context, event):

        scene = context.scene
        for object in bpy.context.selected_objects:
            object['thAnimated'] = False
        return {'FINISHED'}


class RENDER_PT_thea_CausticReceiver(bpy.types.Operator):
    '''Set selected object as caustic receiver'''
    bl_idname = "thea.caustic_receiver"
    bl_label = "Set selected object as caustic receiver"

    def invoke(self, context, event):

        scene = context.scene
        object = bpy.context.selected_objects[0]
#         if object.get('thCausticReceiver') == 0:
#             object['thCausticReceiver'] = 1
#         else:
#             object['thCausticReceiver'] = 0
        object.thCausticReceiver = not object.thCausticReceiver
        return {'FINISHED'}

class RENDER_PT_thea_CausticTransmitter(bpy.types.Operator):
    bl_idname = "thea.caustic_transmitter"
    bl_label = "Set selected object as caustic transmitter"

    def invoke(self, context, event):

        scene = context.scene
        object = bpy.context.selected_objects[0]
        if object.get('thCausticTransmitter') == 0:
            object['thCausticTransmitter'] = 1
        else:
            object['thCausticTransmitter'] = 0
        return {'FINISHED'}

class RENDER_PT_thea_Enabled(bpy.types.Operator):
    bl_idname = "thea.enabled"
    bl_label = "Enable selected object"

    def invoke(self, context, event):

        scene = context.scene
        object = bpy.context.selected_objects[0]
        if object.get('thEnabled') == 0:
            object['thEnabled'] = 1
        else:
            object['thEnabled'] = 0
        return {'FINISHED'}

class RENDER_PT_thea_Hide(bpy.types.Operator):
    bl_idname = "thea.visible"
    bl_label = "Set selected object visible in Thea"

    def invoke(self, context, event):

        scene = context.scene
        object = bpy.context.selected_objects[0]
        if object.get('thVisible') == 0:
            object['thVisible'] = 1
        else:
            object['thVisible'] = 0
        return {'FINISHED'}

class RENDER_PT_thea_ShadowCaster(bpy.types.Operator):
    bl_idname = "thea.shadow_caster"
    bl_label = "Set shadow casting for selected object"

    def invoke(self, context, event):

        scene = context.scene
        object = bpy.context.selected_objects[0]
        if object.get('thShadowCaster') == 0:
            object['thShadowCaster'] = 1
        else:
            object['thShadowCaster'] = 0
        return {'FINISHED'}

class RENDER_PT_thea_ShadowReceiver(bpy.types.Operator):
    bl_idname = "thea.shadow_receiver"
    bl_label = "Set shadow receiving for selected object"

    def invoke(self, context, event):

        scene = context.scene
        object = bpy.context.selected_objects[0]
        if object.get('thShadowReceiver') == 0:
            object['thShadowReceiver'] = 1
        else:
            object['thShadowReceiver'] = 0
        return {'FINISHED'}


class RENDER_PT_thea_EnableCausticReceiver(bpy.types.Operator):
    bl_idname = "thea.enable_caustic_receiver"
    bl_label = "Set selected objects as caustic receiver"

    def invoke(self, context, event):

        scene = context.scene
        for object in bpy.context.selected_objects:
            object.thCausticsReceiver = True
        return {'FINISHED'}


class RENDER_OT_thea_DisableCausticReceiver(bpy.types.Operator):
    bl_idname = "thea.disable_caustic_receiver"
    bl_label = "Unset selected objects as caustic receiver"

    def invoke(self, context, event):

        scene = context.scene
        for object in bpy.context.selected_objects:
            object.thCausticsReceiver = False
        return {'FINISHED'}


class RENDER_PT_thea_EnableTraceReflections(bpy.types.Operator):
    bl_idname = "thea.enable_trace_reflections"
    bl_label = "Enable trace reflections selected objects materials"

    def invoke(self, context, event):

        scene = context.scene
        for object in bpy.context.selected_objects:
            for obMat in object.material_slots:
                obMat.material.shadow_ray_bias = 0
        return {'FINISHED'}


class RENDER_PT_thea_DisableTraceReflections(bpy.types.Operator):
    bl_idname = "thea.disable_trace_reflections"
    bl_label = "Enable trace reflections selected objects materials"

    def invoke(self, context, event):

        scene = context.scene
        for object in bpy.context.selected_objects:
            for obMat in object.material_slots:
                obMat.material.shadow_ray_bias = 1
        return {'FINISHED'}


class RENDER_PT_thea_EnableAnimationExport(bpy.types.Operator):
    '''Enable animation export for selected objects'''
    bl_idname = "thea.enable_animation_export"
    bl_label = "Enable animation export for selected objects"

    def invoke(self, context, event):

        scene = context.scene
        for object in bpy.context.selected_objects:
            object.thExportAnimation = True
        return {'FINISHED'}


class RENDER_PT_thea_DisableCausticReceiver(bpy.types.Operator):
    '''Disable animation export for selected objects'''
    bl_idname = "thea.disable_animation_export"
    bl_label = "Disable animation export for selected objects"

    def invoke(self, context, event):

        scene = context.scene
        for object in bpy.context.selected_objects:
            object.thExportAnimation = False
        return {'FINISHED'}

class MATERIAL_PT_thea_TheaMaterialEditor(bpy.types.Operator):
    '''Edit material in Thea Material Editor'''
    bl_idname = "thea.thea_material_editor"
    bl_label = "Edit material in Thea"

    def invoke(self, context, event):
        scene = context.scene
        exporter=initExporter()
        res = editMaterial(scene,bpy.context.active_object.active_material, exporter=exporter)
        if not res:
            self.report({'ERROR'}, "Please set proper output path before editing material!")
            return {'FINISHED'}
        thea_globals.materialUpdated = True
        return {'FINISHED'}


class MATERIAL_PT_thea_deleteMaterialLink(bpy.types.Operator):
    '''Delete material link'''
    bl_idname = "thea.delete_material_link"
    bl_label = "Delete material link"

    def invoke(self, context, event):
        scene = context.scene
        try:
            del(bpy.context.active_object.active_material['thea_extMat'])
        except:
            pass
        return {'FINISHED'}



# class RENDER_PT_thea_saveIR(bpy.types.Operator):
class MATERIAL_PT_thea_copyMaterialLocally(bpy.types.Operator):
    '''Copy material file to the selected directory'''
    bl_idname = "thea.copy_material_locally"
    bl_label = "Copy material file locally"

    filepath = bpy.props.StringProperty(name="file path", description="getting file path", maxlen= 1024, default= "")

    def execute(self, context):
        matDir = os.path.dirname(self.filepath)
#         scene = context.scene
#         (exportPath, theaPath, theaDir, dataPath, currentBlendDir, currentBlendFile) = setPaths(scene)
#
#         tempDir = os.path.join(exportPath,"~thexport")
#         if not os.path.isdir(tempDir):
#             os.mkdir(tempDir)
#         matDir = os.path.join(tempDir,"materials")
#         if not os.path.isdir(matDir):
#             os.mkdir(matDir)
        import shutil
        shutil.copy2(os.path.abspath(bpy.path.abspath(bpy.context.active_object.active_material['thea_extMat'])), matDir)
        bpy.context.active_object.active_material['thea_extMat'] = bpy.path.abspath(os.path.join(matDir, os.path.basename(bpy.context.active_object.active_material['thea_extMat'])))

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}
#
# class MATERIAL_PT_thea_copyMaterialLocally(bpy.types.Operator):
#     bl_idname = "thea.copy_material_locally"
#     bl_label = "Copy material file locally"
#
#     def invoke(self, context, event):
#         scene = context.scene
#         (exportPath, theaPath, theaDir, dataPath, currentBlendDir, currentBlendFile) = setPaths(scene)
#
#         tempDir = os.path.join(exportPath,"~thexport")
#         if not os.path.isdir(tempDir):
#             os.mkdir(tempDir)
#         matDir = os.path.join(tempDir,"materials")
#         if not os.path.isdir(matDir):
#             os.mkdir(matDir)
#         import shutil
#         shutil.copy2(os.path.abspath(bpy.path.abspath(bpy.context.active_object.active_material['thea_extMat'])), matDir)
#         bpy.context.active_object.active_material['thea_extMat'] = bpy.path.relpath(os.path.join(matDir, os.path.basename(bpy.context.active_object.active_material['thea_extMat'])))
#         return {'FINISHED'}


class Material_PT_thea_SetLibraryMaterial(bpy.types.Operator):
    '''Set library material'''
    bl_idname = "thea.set_library_material"
    bl_label = "Set library material"

    def invoke(self, context, event):
       lut = getLUTarray()
       mat = context.material
       #print("mat.get('thea_LUT')", mat.get('thea_LUT'))

       if mat.get('thea_LUT') > 0:
           mat.name = lut[mat.get('thea_LUT')]
           mat.use_cubic = True

       return {'FINISHED'}



class MATERIAL_PT_thea_BasicSyncTheaToBlender(bpy.types.Operator):
    '''Sync Basic component to blender material'''
    bl_idname = "thea.sync_basic_to_blender"
    bl_label = "Sync Basic component to blender material"

    def invoke(self, context, event):
        mat = context.material
        mat.raytrace_mirror.use = False
        mat.use_transparency = False
        mat.diffuse_intensity = 0.8
        try:
            mat.specular_color = mat.get('thea_BasicReflectanceCol')
        except:
            mat.specular_color = (0,0,0)
        mat.specular_intensity = 1.0
        mat.specular_shader = "COOKTORR"
        try:
            mat.specular_ior = mat.get('thea_BasicIOR')
        except:
            mat.specular_ior = 1.5
        try:
            mat.specular_hardness = 511 - (mat.get('thea_BasicStructureRoughness') * 5.11)
        except:
            mat.specular_ior = 1.5
        try:
            if mat.get('thea_BasicTrace'):
                mat.shadow_ray_bias = 0.0
            else:
                mat.shadow_ray_bias = 0.2
        except:
            mat.shadow_ray_bias = 0.0
        return {'FINISHED'}





class RENDER_PT_thea_SyncBlenderToThea(bpy.types.Operator):
    '''Enable basic component for materials without Thea material. To be used with internal render engine materials'''
    bl_idname = "thea.sync_blender_to_thea"
    bl_label = "Enable basic component for materials without Thea material"

    def invoke(self, context, event):
        scene = context.scene
        for object in bpy.data.objects:
            for matSlot in object.material_slots:
                mat = bpy.data.materials[matSlot.name]
                #print("mat: ", mat)
                if mat.get('thea_Basic')!=True and mat.get('thea_Glossy')!=True:
                    #force material preview generation
                    mat.diffuse_color = mat.diffuse_color
                    mat['thea_BasicReflectanceCol'] = mat.specular_color
                    mat['thea_BasicIOR'] = 1.5
                    if mat.specular_hardness == 50:
                        mat['thea_BasicStructureRoughness'] = 25.0
                    else:
                        mat['thea_BasicStructureRoughness'] = (((511.0 - mat.specular_hardness) / 511.0) * 100) / 2
                    if mat.shadow_ray_bias > 0:
                        mat['thea_BasicTrace'] = False
                    else:
                        mat['thea_BasicTrace'] = True
                    #enable all testures to be used with Basic component
                    for tex in mat.texture_slots:
                        try:
                            tex.texture['thea_Basic'] = True
                            if getattr(tex, 'use_map_color_diffuse') and os.path.exists(os.path.abspath(bpy.path.abspath(tex.texture.image.filepath))):
                                mat.thea_BasicDiffuseFilename=tex.texture.image.filepath
                        except:
                            pass

        return {'FINISHED'}



class MATERIAL_PT_thea_BasicSyncBlenderToThea(bpy.types.Operator):
    '''Sync Basic component with blender material'''
    bl_idname = "thea.sync_blender_to_basic"
    bl_label = "Sync Basic component with blender material"

    def invoke(self, context, event):
        mat = context.material
        #force material preview generation
        mat.diffuse_color = mat.diffuse_color
        mat['thea_BasicReflectanceCol'] = mat.specular_color
        mat['thea_BasicIOR'] = mat.specular_ior
        mat['thea_BasicStructureRoughness'] = ((511.0 - mat.specular_hardness) / 511.0) * 100
        if mat.shadow_ray_bias > 0:
            mat['thea_BasicTrace'] = False
        else:
            mat['thea_BasicTrace'] = True
        #enable all testures to be used with Basic component
        for tex in mat.texture_slots:
            try:
                tex.texture['thea_Basic'] = True
                if getattr(tex, 'use_map_color_diffuse') and os.path.exists(os.path.abspath(bpy.path.abspath(tex.texture.image.filepath))):
                    mat.thea_BasicDiffuseFilename=tex.texture.image.filepath
            except:
                pass

        return {'FINISHED'}


def getBSDFDiffuseNode(node):
#     #print("Diffuse node.name: %s, node.type: %s", (node.name, node.type))
    if node.type == 'BSDF_DIFFUSE':
        #print("found: ", node.name)
        return node
    for input in node.inputs:
#         #print("node: %s, input: %s", (node.name, input.name))
        if input.is_linked:
            node = getBSDFDiffuseNode(input.links[0].from_node)
            if node:
                return node
#             if fromNode.type == 'BSDF_DIFFUSE':
#                 #print("found: ", fromNode.name)
#                 return fromNode
#             else:
#                 getBSDFDiffuseNode(fromNode)

def getBSDFGlossyNode(node):
#     #print("Glossy node.name: %s, node.type: %s", (node.name, node.type))
    if node.type == 'BSDF_GLOSSY':
#         #print("found: ", node.name)
        return node
    for input in node.inputs:
        if input.is_linked:
            node = getBSDFGlossyNode(input.links[0].from_node)
            if node:
                return node
#             if fromNode.type == 'BSDF_GLOSSY':
#                 #print("found: ", fromNode.name)
#                 return fromNode
#             else:
#                 getBSDFGlossyNode(fromNode)

def getBSDFGlassNode(node):
#     #print("Glass  node.name: %s, node.type: %s", (node.name, node.type))
    if node.type == 'BSDF_GLASS':
#         #print("found: ", node.name)
        return node
    for input in node.inputs:
        if input.is_linked:
            node = getBSDFGlassNode(input.links[0].from_node)
            if node:
                return node
#             if fromNode.type == 'BSDF_GLASS':
#                 #print("found: ", fromNode.name)
#                 return fromNode
#             else:
#                 getBSDFGlassNode(fromNode)

def getTextureNode(node):
#     #print("Texture  node.name: %s, node.type: %s", (node.name, node.type))
    if node.type == 'TEX_IMAGE':
#         #print("found1: ", node.name)
        return node
    for input in node.inputs:
#         #print("input: ", input)
        if input.is_linked:
            texNode = getTextureNode(input.links[0].from_node)
            if texNode:
                return texNode
#             if fromNode.type == 'TEX_IMAGE':
#                 #print("found2: ", fromNode.name)
#                 return fromNode
#             else:
#                 getTextureNode(fromNode)


class MATERIAL_PT_thea_SyncCyclesToThea(bpy.types.Operator):
    '''Convert cycles materials to Thea materials'''
    bl_idname = "thea.sync_cycles_to_thea"
    bl_label = "Sync material with cycles material"

    def enableTexture(self, mat, node, origin):
#         #print("mat, node, origin: ", mat, node, origin)
        imgName = getattr(mat, origin)
        texName = mat.name+"_"+origin
        exists = False
        try:
            if mat.texture_slots[texName]:
                exists = True
                slot = mat.texture_slots[texName]
                tex = slot.texture
        except:
            pass

        if exists:
            try:
                if imgName:
                    img = bpy.data.images.load(imgName)
                    tex.image = img
                else:
                    #print("removing texture: ", slot, tex)
                    mat.texture_slots[texName].texture = None
            except:
                pass
        else:
            img = bpy.data.images.load(imgName)
            tex = bpy.data.textures.new(name=texName, type='IMAGE')
            tex.image = img
            tex.name = texName
            slot = mat.texture_slots.add()
            slot.texture = tex
            slot.texture_coords='UV'
            if 'Diffuse' in tex.name:
                slot.use_map_color_diffuse=True
            if 'Reflectance' in tex.name:
                slot.use_map_color_spec=True
                slot.use_map_color_diffuse=False
            if 'Basic' in tex.name:
                slot.texture.thea_Basic=True
            if 'Glossy' in tex.name:
                slot.texture.thea_Glossy=True

    def invoke(self, context, event):
        for mat in bpy.data.materials:
#         for object in bpy.data.objects:
# #             object.select = True
# #             bpy.context.scene.objects.active = object
#             s = 0
#             for matSlot in object.material_slots:
#                 mat = bpy.data.materials[matSlot.name]
# #                 object.active_material_index = s
# #                 s += 1
            #print("material: ", mat.name)
#         mat = context.material
    #force material preview generation
            if mat.node_tree:
                for node in mat.node_tree.nodes:
                    if node.type == 'OUTPUT_MATERIAL':
                        outputNode = node
                        if outputNode.inputs['Surface'].is_linked:
                            diffuseNode = getBSDFDiffuseNode(outputNode.inputs['Surface'].links[0].from_node)
                            glossyNode = getBSDFGlossyNode(outputNode.inputs['Surface'].links[0].from_node)
                            glassNode = getBSDFGlassNode(outputNode.inputs['Surface'].links[0].from_node)
                            #print("diffuseNode: ", diffuseNode)
                            #print("glossyNode: ", glossyNode)
                            #print("glassNode: ", glassNode)
                            if diffuseNode:
                                mat.thea_Basic = True
                                #print("diffuseNode: ", diffuseNode.name)
                                texNode = getTextureNode(diffuseNode)
#                                 if diffuseNode.inputs['Color'].is_linked and diffuseNode.inputs['Color'].links[0].from_node.type == 'TEX_IMAGE':
                                if texNode:
                                    #print("texNode: ", texNode.name, texNode.type)
                                    #make texture
#                                     texNode = getDiffuseNode.inputs['Color'].links[0].from_node
                                    try:
                                        mat.thea_BasicDiffuseFilename = texNode.image.filepath
                                        self.enableTexture(mat, texNode, "thea_BasicDiffuseFilename")
                                    except:
                                        pass
                                else:
                                    diffuseColor = diffuseNode.inputs['Color'].default_value
                                    mat.diffuse_color = (diffuseColor[0], diffuseColor[1], diffuseColor[2])
                                if glossyNode:
                                    if glossyNode.inputs['Color'].is_linked and glossyNode.inputs['Color'].links[0].from_node.type == 'TEX_IMAGE':
                                        #make texture
                                        try:
                                            texNode = glossyNode.inputs['Color'].links[0].from_node
                                            mat.thea_BasicReflectanceFilename = texNode.image.filepath
                                        except:
                                            pass
                                    else:
                                        reflectanceColor = glossyNode.inputs['Color'].default_value
                                        mat.thea_BasicReflectanceCol = (reflectanceColor[0], reflectanceColor[1], reflectanceColor[2])
                                    mat.thea_BasicStructureRoughness = glossyNode.inputs['Roughness'].default_value*100
                                    mat.thea_BasicIOR = 1.5
                            else:
                                mat.thea_Basic = False

                            if glossyNode and not diffuseNode:
                                #print("glossyNode: ", glossyNode.name)
                                mat.thea_Glossy = True
                                if glossyNode.inputs['Color'].is_linked and glossyNode.inputs['Color'].links[0].from_node.type == 'TEX_IMAGE':
                                    #make texture
                                    texNode = glossyNode.inputs['Color'].links[0].from_node
                                    mat.thea_GlossyReflectanceFilename = texNode.image.filepath
                                else:
                                    reflectanceColor = glossyNode.inputs['Color'].default_value
                                    mat.thea_GlossyReflectanceCol = (reflectanceColor[0], reflectanceColor[1], reflectanceColor[2])
                                mat.thea_GlossyStructureRoughness = glossyNode.inputs['Roughness'].default_value*100
                                mat.thea_GlossyIOR = 1.5


                            if glassNode:
                                #print("glassNode: ", glassNode.name)
                                mat.thea_Glossy = True
                                if glassNode.inputs['Color'].is_linked and glassNode.inputs['Color'].links[0].from_node.type == 'TEX_IMAGE':
                                    #make texture
                                    texNode = glassNode.inputs['Color'].links[0].from_node
                                    mat.thea_GlossyTransmittanceFilename = texNode.image.filepath
                                else:
                                    transmittanceColor = glassNode.inputs['Color'].default_value
                                    mat.thea_GlossyTransmittanceCol = (transmittanceColor[0], transmittanceColor[1], transmittanceColor[2])
                                mat.thea_GlossyReflectanceCol = (1,1,1)
                                mat.thea_GlossyStructureRoughness = glassNode.inputs['Roughness'].default_value*100
                                mat.thea_GlossyIOR = glassNode.inputs['IOR'].default_value
#             object.select = False
#             bpy.context.scene.objects.active = None

#         mat.diffuse_color = mat.diffuse_color


        return {'FINISHED'}


class MATERIAL_PT_thea_Basic2SyncTheaToBlender(bpy.types.Operator):
    '''Sync second Basic component to blender material'''
    bl_idname = "thea.sync_basic2_to_blender"
    bl_label = "Sync second Basic component to blender material"

    def invoke(self, context, event):
        mat = context.material
        mat.raytrace_mirror.use = False
        mat.use_transparency = False
        mat.diffuse_intensity = 0.8
        mat.diffuse_color = mat.get('thea_Basic2DiffuseCol')
        try:
            mat.specular_color = mat.get('thea_Basic2ReflectanceCol')
        except:
            mat.specular_color = (0,0,0)
        mat.specular_intensity = 1.0
        mat.specular_shader = "COOKTORR"
        try:
            mat.specular_ior = mat.get('thea_Basic2IOR')
        except:
            mat.specular_ior = 1.5
        try:
            mat.specular_hardness = 511 - (mat.get('thea_Basic2StructureRoughness') * 5.11)
        except:
            mat.specular_ior = 1.5
        try:
            if mat.get('thea_Basic2Trace'):
                mat.shadow_ray_bias = 0.0
            else:
                mat.shadow_ray_bias = 0.2
        except:
            mat.shadow_ray_bias = 0.0
        return {'FINISHED'}

class MATERIAL_PT_thea_Basic2SyncBlenderToThea(bpy.types.Operator):
    '''Sync second Basic component with blender material'''
    bl_idname = "thea.sync_blender_to_basic2"
    bl_label = "Sync second Basic component with blender material"

    def invoke(self, context, event):
        mat = context.material
        #force material preview generation
        mat.diffuse_color = mat.diffuse_color
        mat['thea_Basic2DiffuseCol'] = mat.diffuse_color
        mat['thea_Basic2ReflectanceCol'] = mat.specular_color
        mat['thea_Basic2IOR'] = mat.specular_ior
        mat['thea_Basic2StructureRoughness'] = ((511.0 - mat.specular_hardness) / 511.0) * 100
        if mat.shadow_ray_bias > 0:
            mat['thea_Basic2Trace'] = False
        else:
            mat['thea_Basic2Trace'] = True
        return {'FINISHED'}

class MATERIAL_PT_thea_GlossySyncTheaToBlender(bpy.types.Operator):
    '''Sync Glossy component to blender material'''
    bl_idname = "thea.sync_glossy_to_blender"
    bl_label = "Sync Glossy component to blender material"

    def invoke(self, context, event):
        mat = context.material
        mat.specular_color = (0,0,0)
        mat.specular_intensity = 0.0
        mat.specular_shader = "COOKTORR"
        try:
            mat.raytrace_mirror.use = mat.get('thea_GlossyTraceReflections')
        except:
            mat.raytrace_mirror.use = True
        try:
            mat.use_transparency = mat.get('thea_GlossyTraceRefractions')
        except:
            mat.use_transparency = True
        mat.transparency_method = 'RAYTRACE'
        mat.raytrace_mirror.fresnel = 1.0
        mat.raytrace_mirror.reflect_factor = 1.0
        try:
            mat.diffuse_color = mat.get('thea_GlossyTransmittanceCol')
            mat.diffuse_intensity = 0.0
        except:
            mat.diffuse_color = (0,0,0)
        try:
            mat.raytrace_transparency.ior = mat.get('thea_GlossyIOR')
            raytrace_transparency.filter = 1.0
        except:
            mat.raytrace_transparency.ior = 1.5
            mat.raytrace_transparency.filter = 1.0
        try:
            if mat.get('thea_GlossyStructureRoughTrEn'):
                mat.raytrace_transparency.gloss_factor = 1-(mat.get('thea_GlossyStructureRoughnessTr')/100)
            else:
                mat.raytrace_transparency.gloss_factor = 1.0
        except:
            mat.raytrace_transparency.gloss_factor = 1.0
        try:
            mat.mirror_color = mat.get('thea_GlossyReflectanceCol')
        except:
            mat.mirror_color = (0,0,0)
        try:
            mat.raytrace_mirror.fresnel = mat.get('thea_GlossyIOR')
        except:
            mat.raytrace_mirror.fresnel = 1.5
        try:
            mat.raytrace_mirror.gloss_factor = 1-(mat.get('thea_GlossyStructureRoughness')/100)
        except:
            mat.raytrace_transparency.gloss_factor = 0.9

        try:
            if mat.get('thea_GlossyTraceReflections'):
                mat.shadow_ray_bias = 0.0
            else:
                mat.shadow_ray_bias = 0.2
        except:
            mat.shadow_ray_bias = 0.0
        return {'FINISHED'}

class MATERIAL_PT_thea_GlossySyncBlenderToThea(bpy.types.Operator):
    '''Sync Glossy component with blender material'''
    bl_idname = "thea.sync_blender_to_glossy"
    bl_label = "Sync Glossy component with blender material"

    def invoke(self, context, event):
        mat = context.material
        #force material preview generation
        mat.diffuse_color = mat.diffuse_color
        mat['thea_GlossyTransmittanceCol'] = mat.diffuse_color
        mat['thea_GlossyReflectanceCol'] = mat.mirror_color
        mat['thea_GlossyIOR'] = mat.raytrace_mirror.fresnel
        mat['thea_GlossyStructureRoughness'] = (1- mat.raytrace_mirror.gloss_factor) * 100
        mat['thea_GlossyStructureRoughnessTr'] = (1- mat.raytrace_transparency.gloss_factor) * 100
        if mat['thea_GlossyStructureRoughnessTr'] > 0:
            mat['thea_GlossyStructureRoughTrEn'] = True
        if mat.raytrace_mirror.use:
            mat['thea_GlossyTraceReflections'] = True
        else:
            mat['thea_GlossyTraceReflections'] = False
        if mat.use_transparency:
            mat['thea_GlossyTraceRefractions'] = True
        else:
            mat['thea_GlossyTraceRefractions'] = False
        return {'FINISHED'}

class RENDER_PT_thea_syncWithThea(bpy.types.Operator):
    '''Sync selected object transform wih saved Thea scene'''
    bl_idname = "thea.sync_with_thea"
    bl_label = "Sync with Thea"

    def invoke(self, context, event):
        scene = context.scene

        (exportPath, theaPath, theaDir, dataPath, currentBlendDir, currentBlendFile) = setPaths(scene)
        xmlFilename = currentBlendFile.replace('.blend', '.xml')
        fileName = os.path.join(exportPath, os.path.basename(xmlFilename))
        f = open(fileName)
        i = 0
        foundOb = False
        camFocalLenght = 0
        it = iter(f)
        for line in it:
            i+=1
            if line.find('<Object Identifier="./Models/') >= 0:
                name = line.split(" ")[3].split('"')[1]
                ob = scene.objects.get(name)
                if ob in bpy.context.selected_objects:
                    foundOb = True
            if line.find('<Object Identifier="./Lights/') >= 0:
                name = line.split(" ")[3].split('"')[1]
                ob = scene.objects.get(name)
                if ob in bpy.context.selected_objects:
                    foundOb = True
            if line.find('<Object Identifier="./Cameras/') >= 0:
                name = line.split(" ")[4].split('"')[1]
                ob = scene.objects.get(name)
                if ob in bpy.context.selected_objects:
                    foundOb = True
                    line = next(it)
                    if line.find('<Parameter Name="Focal Length (mm)"') >= 0:
                        camFocalLenght = float(line.split(" ")[5].split('"')[1])
            if foundOb and (line.find('<Parameter Name="Frame"') >= 0):
                frame_str = line.split('"')[5]
                frame_arr = frame_str.split(" ")
                if ob.type in ('LAMP', 'CAMERA'):
                    ob.matrix_world = (float(frame_arr[0]), float(frame_arr[4]), float(frame_arr[8]), 0), (float(frame_arr[1])*-1, float(frame_arr[5])*-1, float(frame_arr[9])*-1, 0), (float(frame_arr[2])*-1, float(frame_arr[6])*-1, float(frame_arr[10])*-1, 0), (float(frame_arr[3]), float(frame_arr[7]), float(frame_arr[11]), 1)
                    if (ob.type == 'CAMERA') and (camFocalLenght >0):
                        ob.data.lens = camFocalLenght
                    print (name, " synced")
                    foundOb = False
                else:
                    ob.matrix_world = (float(frame_arr[0]), float(frame_arr[4]), float(frame_arr[8]), 0), (float(frame_arr[1]), float(frame_arr[5]), float(frame_arr[9]), 0), (float(frame_arr[2]), float(frame_arr[6]), float(frame_arr[10]), 0), (float(frame_arr[3]), float(frame_arr[7]), float(frame_arr[11]), 1)
                    print (name, " synced")
                    foundOb = False

        f.close()

        return {'FINISHED'}



class RENDER_PT_thea_mergeFile(bpy.types.Operator):
    '''Select Thea scnene to merge'''
    bl_idname = "thea.merge_file"
    bl_label = "Merge Thea Scene"

    filepath = bpy.props.StringProperty(name="file path", description="getting file path", maxlen= 1024, default= "")



    def execute(self, context):
        FilePath = self.filepath
        #set the string path fo the file here.
        #this is a variable created from the top to start it
        bpy.context.scene.thea_mergeFilePath = FilePath
        #print("path: ",FilePath)#display the file name and current path

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}

class RENDER_PT_thea_IBLFile(bpy.types.Operator):
    bl_idname = "thea.ibl_file"
    bl_label = "IBL filename"

    filepath = bpy.props.StringProperty(name="file path", description="getting file path", maxlen= 1024, default= "")



    def execute(self, context):
        FilePath = self.filepath
        bpy.context.scene.thea_IBLFilePath = FilePath
        #print("path: ",FilePath)#display the file name and current path

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}

class RENDER_PT_thea_BackgroundMappingFile(bpy.types.Operator):
    bl_idname = "thea.backgroundmapping_file"
    bl_label = "Background Mapping filename"

    filepath = bpy.props.StringProperty(name="file path", description="getting file path", maxlen= 1024, default= "")



    def execute(self, context):
        FilePath = self.filepath
        #set the string path fo the file here.
        #this is a variable created from the top to start it
        bpy.context.scene.thea_BackgroundMappingFilePath = FilePath
        #print("path: ",FilePath)#display the file name and current path

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}

class RENDER_PT_thea_ReflectionMappingFile(bpy.types.Operator):
    bl_idname = "thea.reflectionmapping_file"
    bl_label = "Reflection Mapping filename"

    filepath = bpy.props.StringProperty(name="file path", description="getting file path", maxlen= 1024, default= "")



    def execute(self, context):
        FilePath = self.filepath
        #set the string path fo the file here.
        #this is a variable created from the top to start it
        bpy.context.scene.thea_ReflectionMappingFilePath = FilePath
        #print("path: ",FilePath)#display the file name and current path

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}

class RENDER_PT_thea_RefractionMappingFile(bpy.types.Operator):
    bl_idname = "thea.refractionmapping_file"
    bl_label = "Refraction Mapping filename"

    filepath = bpy.props.StringProperty(name="file path", description="getting file path", maxlen= 1024, default= "")



    def execute(self, context):
        FilePath = self.filepath
        #set the string path fo the file here.
        #this is a variable created from the top to start it
        bpy.context.scene.thea_RefractionMappingFilePath = FilePath
        #print("path: ",FilePath)#display the file name and current path

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}

class RENDER_PT_thea_updateLoc(bpy.types.Operator):
    bl_idname = "thea.update_loc"
    bl_label = "Update location"



    def invoke(self, context, event):
       scene = context.scene
       loc = getLocation(scene.thea_EnvLocationsMenu, getLocations()[1], scene)
       if loc[0] != "":
           scene.thea_EnvLat = loc[0]
           scene.thea_EnvLong = loc[1]
           scene.thea_EnvTZ = str(loc[2])
       return {'FINISHED'}

class RENDER_PT_thea_RefreshRender(bpy.types.Operator):
    bl_idname = "thea.refresh_render"
    bl_label = "Refresh render result"

    def invoke(self, context, event):
        thea_globals.displayUpdated = True
        #print("refresh")
        return {'FINISHED'}

# class RENDER_PT_thea_StartInteractiveRender(bpy.types.Operator):
#     bl_idname = "thea.start_irender"
#     bl_label = "Refresh render result"
#
#     def invoke(self, context, event):
#         bpy.ops.thea.start_ir()
#         #print("refresh")
#         return {'FINISHED'}

class MATERIAL_PT_thea_checkTheaExtMat(bpy.types.Operator):
    '''check if Thea linked materials are live
        :return: False if missing link
        :rtype: bool
    '''
    bl_idname = "thea.check_thea_mat"
    bl_label = "check external linked materials for links"

    def invoke(self, context, event):
        missing_Materials = []
        matNameExt = ""
        matMesh = ""
        matExtLink = True
        for mat in bpy.data.materials:
            if getattr(mat, "thea_extMat"):
                extMat = os.path.exists(os.path.abspath(bpy.path.abspath(mat.get('thea_extMat'))))
                if extMat == False:
    #                matMesh = bpy.context.active_object.name
                    matExtLink = False
                    matNameExt = mat.name
                    MNAME = matNameExt
                    obs = []
                    for o in bpy.data.objects:
                        if isinstance(o.data, bpy.types.Mesh) and MNAME in o.data.materials:
    #                        obs.append(o.name)
                            matMesh = o.name
#                    missing_Materials.append("%s > Mesh obj: %s" % (matNameExt, matMesh))
#                    missing_Materials += matNameExt + "> Mesh obj:"+ matMesh+"\n"
                    missing_Materials = matNameExt + "\n"
    #                return [matExtLink, matNameExt, matMesh]
                else:
                    pass
#            missing_Materials = sorted(list(set(missing_Materials)))
    #    thea_globals.log.debug("*** Missing Material list: %s" % missing_Materials)
#        return [matExtLink, matNameExt, matMesh, missing_Materials]
        self.report({'ERROR'}, missing_Materials)
        return {'FINISHED'}

class MATERIAL_PT_thea_listLinkedMaterials(bpy.types.Operator):
    '''List materials using the same Thea material file'''
    bl_idname = "thea.list_linked_materials"
    bl_label = "List materials using the same Thea material file"

    def invoke(self, context, event):
        mat = bpy.context.scene.objects.active.active_material
        materials = "Materials using the same Thea material file: \n"
        if len(getattr(mat, "thea_extMat"))>5:
            for m in bpy.data.materials:
                if getattr(mat, "thea_extMat") == getattr(m, "thea_extMat"):
                    materials+=m.name+"\n"

        #print("materials: ", materials)
        self.report({'ERROR'}, materials)
        return {'FINISHED'}


class RENDER_PT_thea_saveIR(bpy.types.Operator):
    '''Save IR result'''
    bl_idname = "thea.save_ir"
    bl_label = "Save IR result"
    filepath = bpy.props.StringProperty(name="file path", description="getting file path", maxlen= 1024, default= "")

    def execute(self, context):
        FilePath = self.filepath
#        CHANGED > Added string below, was missing and took from old part
        scn = context.scene
#       CHANGED > Strips .blend from file name when saving
        FilePath = FilePath[:-6]
        if FilePath[-4:] not in (".jpg", ".png", ".bmp", ".hdr", ".ext", ".tif"):
            fileFormat = ".png"
            color_mode = scn.render.image_settings.color_mode
            if context.scene.render.image_settings.file_format == "JPEG":
                fileFormat = ".jpg"
            if context.scene.render.image_settings.file_format == "PNG":
                fileFormat = ".png"
            if context.scene.render.image_settings.file_format == "BMP":
                fileFormat = ".bmp"
            if context.scene.render.image_settings.file_format == "HDR":
                fileFormat = ".hdr"
            if context.scene.render.image_settings.file_format == "OPEN_EXR":
                fileFormat = ".exr"
            if context.scene.render.image_settings.file_format == "TIFF":
                fileFormat = ".tif"
        else:
            fileFormat = ""

        if context.scene.thea_ir_running == True:
            try:
                if context.scene.get('thea_SDKPort'):
                    port = context.scene.get('thea_SDKPort')
                else:
                    port = 30000
                #if context.scene.get('thea_RefreshDelay'):
                #    self.DELAY = context.scene.get('thea_RefreshDelay')
            except:
                port = 30000

            data = sendSocketMsg('localhost', port, b'version')
            if data.find('v'):

#                 outputImage = os.path.join(exportPath, os.path.basename(FilePath) + fileFormat)
                outputImage = os.path.join(os.path.dirname(FilePath), os.path.basename(FilePath) + fileFormat)
                #print("outputImage: ", outputImage)
                message = 'message "./UI/Viewport/SaveImage %s"' % outputImage
                #print("message: ", message)
                data = sendSocketMsg('localhost', port, message.encode())
                #print("data: ", data, data.find('Ok'))
                if data.find('Ok')>0:
                    self.report({'INFO'}, "File %s saved" % outputImage)
                else:
                    self.report({'ERROR'}, "Error while saving file!")
            else:
                self.report({'ERROR'}, "Error while saving file!")

        #print("path: ",FilePath)#display the file name and current path
        thea_globals.log.debug("FilePath: %s" % FilePath)

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}


#     def invoke(self, context, event):
#
#         (exportPath, theaPath, theaDir, dataPath, currentBlendDir, currentBlendFile) = setPaths(context.scene)
#         scn = context.scene
#
#         fileFormat = ".png"
#         color_mode = scn.render.image_settings.color_mode
#
#
#         if scn.render.image_settings.file_format == "JPEG":
#             fileFormat = ".jpg"
#         if scn.render.image_settings.file_format == "PNG":
#             fileFormat = ".png"
#         if scn.render.image_settings.file_format == "BMP":
#             fileFormat = ".bmp"
#         if scn.render.image_settings.file_format == "HDR":
#             fileFormat = ".hdr"
#         if scn.render.image_settings.file_format == "OPEN_EXR":
#             fileFormat = ".exr"
#         if scn.render.image_settings.file_format == "TIFF":
#             fileFormat = ".tif"
#
#         if context.scene.thea_ir_running == True:
#             try:
#                 if context.scene.get('thea_SDKPort'):
#                     port = context.scene.get('thea_SDKPort')
#                 else:
#                     port = 30000
#                 #if context.scene.get('thea_RefreshDelay'):
#                 #    self.DELAY = context.scene.get('thea_RefreshDelay')
#             except:
#                 port = 30000
#
#             data = sendSocketMsg('localhost', port, b'version')
#             if data.find('v'):
#                 imageFilename = currentBlendFile.replace('.blend', '_ir_result')
#                 outputImage = os.path.join(exportPath, os.path.basename(imageFilename) + fileFormat)
#                 #print("outputImage: ", outputImage)
#                 message = 'message "./UI/Viewport/SaveImage %s"' % outputImage
#                 #print("message: ", message)
#                 data = sendSocketMsg('localhost', port, message.encode())
#                 #print("data: ", data, data.find('Ok'))
#                 if data.find('Ok')>0:
#                     self.report({'INFO'}, "File %s saved" % outputImage)
#                 else:
#                     self.report({'ERROR'}, "Error while saving file!")
#             else:
#                 self.report({'ERROR'}, "Error while saving file!")
#
#         return {'FINISHED'}

class RENDER_PT_thea_installTheaStudio(bpy.types.Operator):
    bl_idname = "thea.install_thea_studio"
    bl_label = "Install Thea Studio"

    def invoke(self, context, event):
        import webbrowser
        url = "http://thearender.com/studio"
        webbrowser.open(url)
        return {'FINISHED'}


class MATERIAL_PT_thea_refreshDiffuseColor(bpy.types.Operator):
    '''Refresh diffuse color from mat.thea file'''
    bl_idname = "thea.refresh_diffuse_color"
    bl_label = "Refresh diffuse color from mat.thea file"

    def invoke(self, context, event):
        updateActiveMaterialColor()
        return {'FINISHED'}


class LAMP_PT_thea_refreshLamp(bpy.types.Operator):
    bl_idname = "thea.refresh_lamp"
    bl_label = "Refresh lamp data"

    def invoke(self, context, event):
        thea_globals.lampUpdated = True
        return {'FINISHED'}

