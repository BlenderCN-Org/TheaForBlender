"""
.. module:: thea_gui
   :platform: OS X, Windows, Linux
   :synopsis: GUI definition

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
#  Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy
import os
from . import thea_globals
from . import thea_properties
from . import thea_render_main
from bpy.props import *
from bpy.types import Header, Menu, Panel

# Use some of the existing buttons.
from bl_ui import properties_render
from tempfile import gettempdir
properties_render.RENDER_PT_dimensions.COMPAT_ENGINES.add('THEA_RENDER')
properties_render.RENDER_PT_output.COMPAT_ENGINES.add('THEA_RENDER')
properties_render.RENDER_PT_post_processing.COMPAT_ENGINES.add('THEA_RENDER')
del properties_render

from bl_ui import properties_render_layer
properties_render_layer.RENDERLAYER_PT_layers.COMPAT_ENGINES.add('THEA_RENDER')
properties_render_layer.RENDERLAYER_PT_layer_options.COMPAT_ENGINES.add('THEA_RENDER')
del properties_render_layer

# Use only a subset of the world panels
from bl_ui import properties_world
#properties_world.WORLD_PT_preview.COMPAT_ENGINES.add('THEA_RENDER')
properties_world.WORLD_PT_context_world.COMPAT_ENGINES.add('THEA_RENDER')
properties_world.WORLD_PT_world.COMPAT_ENGINES.add('THEA_RENDER')
properties_world.WORLD_PT_ambient_occlusion.COMPAT_ENGINES.add('THEA_RENDER')
del properties_world

# from bl_ui import properties_data_lamp
# for member in dir(properties_data_lamp):
#     subclass = getattr(properties_data_lamp, member)
#     try:        subclass.COMPAT_ENGINES.add('THEA_RENDER')
#     except: pass
# del properties_data_lamp


from bl_ui import properties_material
for member in ('MATERIAL_PT_context_material', 'MATERIAL_PT_preview', 'MATERIAL_PT_custom_props', 'MaterialButtonsPanel', 'PropertyPanel', 'bpy', 'check_material', 'simple_material'):
    subclass = getattr(properties_material, member)
    try:        subclass.COMPAT_ENGINES.add('THEA_RENDER')
    except: pass
del properties_material
from bl_ui import properties_data_mesh
for member in dir(properties_data_mesh):
    subclass = getattr(properties_data_mesh, member)
    try:
        subclass.COMPAT_ENGINES.add('THEA_RENDER')
    except:
        pass
del properties_data_mesh
from bl_ui import properties_texture
properties_texture.TEXTURE_PT_colors.COMPAT_ENGINES.add('THEA_RENDER')
properties_texture.TEXTURE_PT_context_texture.COMPAT_ENGINES.add('THEA_RENDER')
properties_texture.TEXTURE_PT_preview.COMPAT_ENGINES.add('THEA_RENDER')
properties_texture.TEXTURE_PT_image.COMPAT_ENGINES.add('THEA_RENDER')
properties_texture.TEXTURE_PT_clouds.COMPAT_ENGINES.add('THEA_RENDER')
properties_texture.TEXTURE_PT_wood.COMPAT_ENGINES.add('THEA_RENDER')
properties_texture.TEXTURE_PT_marble.COMPAT_ENGINES.add('THEA_RENDER')
properties_texture.TEXTURE_PT_magic.COMPAT_ENGINES.add('THEA_RENDER')
properties_texture.TEXTURE_PT_stucci.COMPAT_ENGINES.add('THEA_RENDER')
properties_texture.TEXTURE_PT_clouds.COMPAT_ENGINES.add('THEA_RENDER')
properties_texture.TEXTURE_PT_blend.COMPAT_ENGINES.add('THEA_RENDER')
properties_texture.TEXTURE_PT_musgrave.COMPAT_ENGINES.add('THEA_RENDER')
properties_texture.TEXTURE_PT_voronoi.COMPAT_ENGINES.add('THEA_RENDER')
properties_texture.TEXTURE_PT_ocean.COMPAT_ENGINES.add('THEA_RENDER')
properties_texture.TEXTURE_PT_pointdensity.COMPAT_ENGINES.add('THEA_RENDER')
properties_texture.TEXTURE_PT_pointdensity_turbulence.COMPAT_ENGINES.add('THEA_RENDER')
properties_texture.TEXTURE_PT_distortednoise.COMPAT_ENGINES.add('THEA_RENDER')
#properties_texture.TEXTURE_PT_mapping.COMPAT_ENGINES.add('THEA_RENDER')


# for member in dir(properties_texture):
#     subclass = getattr(properties_texture, member)
#     print(subclass)
#     try:
#         subclass.COMPAT_ENGINES.add('THEA_RENDER')
#     except:
#         pass
# del properties_texture
from bl_ui import properties_data_camera
for member in dir(properties_data_camera):
    subclass = getattr(properties_data_camera, member)
    try:
        subclass.COMPAT_ENGINES.add('THEA_RENDER')
    except:
        pass
del properties_data_camera

from bl_ui import properties_particle
for member in dir(properties_particle):
    subclass = getattr(properties_particle, member)
    try:
        subclass.COMPAT_ENGINES.add('THEA_RENDER')
    except:
        pass
del properties_particle

from bl_ui import properties_physics_common
for member in dir(properties_physics_common):
    subclass = getattr(properties_physics_common, member)
    try:
        subclass.COMPAT_ENGINES.add('THEA_RENDER')
    except:
        pass
del properties_physics_common

from bl_ui import properties_physics_cloth
for member in dir(properties_physics_cloth):
    subclass = getattr(properties_physics_cloth, member)
    try:
        subclass.COMPAT_ENGINES.add('THEA_RENDER')
    except:
        pass
del properties_physics_cloth

from bl_ui import properties_physics_dynamicpaint
for member in dir(properties_physics_dynamicpaint):
    subclass = getattr(properties_physics_dynamicpaint, member)
    try:
        subclass.COMPAT_ENGINES.add('THEA_RENDER')
    except:
        pass
del properties_physics_dynamicpaint

from bl_ui import properties_physics_field
for member in dir(properties_physics_field):
    subclass = getattr(properties_physics_field, member)
    try:
        subclass.COMPAT_ENGINES.add('THEA_RENDER')
    except:
        pass
del properties_physics_field

from bl_ui import properties_physics_fluid
for member in dir(properties_physics_fluid):
    subclass = getattr(properties_physics_fluid, member)
    try:
        subclass.COMPAT_ENGINES.add('THEA_RENDER')
    except:
        pass
del properties_physics_fluid

from bl_ui import properties_physics_rigidbody
for member in dir(properties_physics_rigidbody):
    subclass = getattr(properties_physics_rigidbody, member)
    try:
        subclass.COMPAT_ENGINES.add('THEA_RENDER')
    except:
        pass
del properties_physics_rigidbody

from bl_ui import properties_physics_rigidbody_constraint
for member in dir(properties_physics_rigidbody_constraint):
    subclass = getattr(properties_physics_rigidbody_constraint, member)
    try:
        subclass.COMPAT_ENGINES.add('THEA_RENDER')
    except:
        pass
del properties_physics_rigidbody_constraint

from bl_ui import properties_physics_smoke
for member in dir(properties_physics_smoke):
    subclass = getattr(properties_physics_smoke, member)
    try:
        subclass.COMPAT_ENGINES.add('THEA_RENDER')
    except:
        pass
del properties_physics_smoke

from bl_ui import properties_physics_softbody
for member in dir(properties_physics_softbody):
    subclass = getattr(properties_physics_softbody, member)
    try:
        subclass.COMPAT_ENGINES.add('THEA_RENDER')
    except:
        pass
del properties_physics_softbody

from bl_ui import properties_scene
for member in dir(properties_scene):
    subclass = getattr(properties_scene, member)
    try:        subclass.COMPAT_ENGINES.add('THEA_RENDER')
    except: pass
del properties_scene


def particle_panel_poll(cls, context):
    psys = context.particle_system
    engine = context.scene.render.engine
    settings = 0

    if psys:
        settings = psys.settings
    elif isinstance(context.space_data.pin_id, bpy.types.ParticleSettings):
        settings = context.space_data.pin_id

    if not settings:
        return False

    return settings.is_fluid is False and (engine in cls.COMPAT_ENGINES)


class RenderButtonsPanel():
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    # COMPAT_ENGINES must be defined in each subclass, external engines can add themselves here

    @classmethod
    def poll(cls, context):
        rd = context.scene.render
        return (context.scene and rd.use_game_engine is False) and (rd.engine in cls.COMPAT_ENGINES)

class WorldButtonsPanel():
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "world"
    # COMPAT_ENGINES must be defined in each subclass, external engines can add themselves here

    @classmethod
    def poll(cls, context):
        return (context.world and context.scene.render.engine in cls.COMPAT_ENGINES)

class CameraButtonsPanel():
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return context.camera and (engine in cls.COMPAT_ENGINES)


class MaterialButtonsPanel():
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "material"
    # COMPAT_ENGINES must be defined in each subclass, external engines can add themselves here

    @classmethod
    def poll(cls, context):
        return context.material and (context.scene.render.engine in cls.COMPAT_ENGINES)

class ObjectButtonsPanel():
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    @classmethod
    def poll(cls, context):
        return context.active_object and (context.scene.render.engine in cls.COMPAT_ENGINES)

class TextureButtonsPanel():
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "texture"

    @classmethod
    def poll(cls, context):
        tex = context.texture
        return tex and (tex.type != 'NONE' or tex.use_nodes) and (context.scene.render.engine in cls.COMPAT_ENGINES)

class DisplayButtonsPanel():
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_context = "image"
    # COMPAT_ENGINES must be defined in each subclass, external engines can add themselves here

    @classmethod
    def poll(cls, context):
        sima = context.space_data
        return (sima.image and context.scene.render.engine in cls.COMPAT_ENGINES)

class View3DPanel():
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'

class ParticleButtonsPanel():
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "particle"

    @classmethod
    def poll(cls, context):
        return particle_panel_poll(cls, context)


class RENDER_PT_InstallThea(RenderButtonsPanel, bpy.types.Panel):
    bl_label = "Install Thea Studio"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (thea_globals.theaPath is False) and (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
       layout = self.layout
       scene = context.scene
       layout.operator("thea.install_thea_studio", "Install Thea Studio")


class MATERIAL_PT_LUT(MaterialButtonsPanel, bpy.types.Panel):
    bl_label = "Thea Library"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return getattr(context.scene, 'thea_useLUT') and (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
       layout = self.layout
       scene = context.scene
       mat  = context.material
       split = layout.split()
       row = layout.row()
       split = layout.split()
       row = layout.row()
       col = split.column()
       col.prop(mat,"thea_LUT")
       #col.operator("thea.set_library_material", text="Set library material")


class MATERIAL_PT_Color(MaterialButtonsPanel, bpy.types.Panel):
    bl_label = "Color"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (not thea_globals.showMatGui)and (engine in cls.COMPAT_ENGINES)
        #return (thea_globals.showMatGui)and (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mat  = context.material
        split = layout.split(percentage=0.8)
        row = layout.row()
        colL = split.column()
        colR = split.column()
        colL.prop(mat, "diffuse_color", text="")
        colR.operator("thea.refresh_diffuse_color", text="", icon="FILE_REFRESH")

class MATERIAL_PT_Header(MaterialButtonsPanel, bpy.types.Panel):
    bl_label = "Material Settings"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        thea_globals.showMatGui = False
        if hasattr(bpy.context, 'active_object'):
            try:
                extMat = os.path.exists(os.path.abspath(bpy.path.abspath(bpy.context.active_object.active_material.get('thea_extMat'))))
            except:
                extMat = False
            if getattr(bpy.context.active_object, 'active_material') is not None:
                thea_globals.showMatGui = True
            else:
                thea_globals.showMatGui = False
            if extMat:
                thea_globals.showMatGui = False
            if int(getattr(bpy.context.active_object.active_material, 'thea_LUT', 0)) > 0:
                thea_globals.showMatGui = False
        else:
            thea_globals.showMatGui = True2
        return (thea_globals.showMatGui) and (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
       layout = self.layout
       scene = context.scene
       mat  = context.material
#    CHANGED > Added new layout for general mat panel
       layout.label(text="Scene Preview")
       split = layout.split(percentage=0.4)
       colL = split.column()
       colR = split.column()
       colL.prop(mat, "thea_EnableUnbiasedPreview")
       colR.prop(mat, "thea_PreviewScenesMenu")
       split = layout.split()
       layout.label(text="General Options")
       split = layout.split()
       colL = split.column()
       colR = split.column()
       colL.prop(mat, "thea_ShadowCatcher")
#    CHANGED > added more material options
       colR.prop(mat, "thea_twoSided")
       colL.prop(mat, "thea_repaintable")
       colR.prop(mat, "thea_dirt")
       layout.prop(mat, "thea_description")
#        layout.operator("thea.sync_cycles_to_thea", text="Convert Cycles material")



class MATERIAL_PT_Coating(MaterialButtonsPanel, bpy.types.Panel):
    bl_label = "Coating Component"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (thea_globals.showMatGui) and (engine in cls.COMPAT_ENGINES)

    def draw_header(self, context):
       scene = context.scene
       mat  = context.material
       self.layout.prop(mat, "thea_Coating", text="")

    def draw(self, context):
       layout = self.layout
       scene = context.scene
       mat  = context.material
       split = layout.split()
       row = layout.row()

       if mat.get('thea_Coating'):
           split = layout.split()
           row = layout.row()
#           colL = split.column()
#           colR = split.column()
#           colL.operator("thea.sync_glossy_to_blender", text="T>B")
#           colR.operator("thea.sync_blender_to_glossy", text="B>T")
#CHANGED > Delete double split and row here
           if(mat.thea_CoatingWeightFilename==""):
                row.prop(mat, "thea_CoatingWeight")
           row.prop(mat, "thea_CoatingWeightFilename")
#CHANGED > Added split to set layer weight more to top
           split = layout.split()
           row = layout.row()
           if(mat.thea_CoatingReflectanceFilename==""):
                row.prop(mat, "thea_CoatingReflectanceCol")
           row.prop(mat, "thea_CoatingReflectanceFilename")
           row = layout.row()
           layout.prop(mat, "thea_CoatingIOR")
           layout.prop(mat, "thea_CoatingEC")
           split = layout.split()
           row = layout.row()
           row.prop(mat, "thea_CoatingThicknessEnable")
           if(getattr(mat, "thea_CoatingThicknessEnable", False)):
               row.prop(mat, "thea_CoatingThickness")
               row.prop(mat, "thea_CoatingThicknessFilename")
#             CHANGED > Added absorption color coatin thickness
           split = layout.split()
           row = layout.row()
           col = split.column()
           col.prop(mat, "thea_CoatingAbsorptionEnable")
           if(getattr(mat, "thea_CoatingAbsorptionEnable", False)):
               if(mat.thea_CoatingAbsorptionFilename==""):
                    row.prop(mat, "thea_CoatingThicknessAbsorptionCol")
               row.prop(mat, "thea_CoatingAbsorptionFilename")
           split = layout.split()
           row = layout.row()
           col = split.column()
           col.prop(mat, "thea_CoatingTraceReflections")
           split = layout.split()
           layout.label(text="Structure")
           row = layout.row()
           row.prop(mat, "thea_CoatingStructureRoughness")
           row.prop(mat, "thea_CoatingRoughnessFilename")
           row = layout.row()
           row.prop(mat, "thea_CoatingStructureAnisotropy")
           row.prop(mat, "thea_CoatingAnisotropyFilename")
           row = layout.row()
           row.prop(mat, "thea_CoatingStructureRotation")
           row.prop(mat, "thea_CoatingRotationFilename")
           row = layout.row()
           row.prop(mat, "thea_CoatingStructureBump")
           row.prop(mat, "thea_CoatingBumpFilename")
           row = layout.row()
           layout.prop(mat, "thea_CoatingStructureNormal")
           row = layout.row()
           row.prop(mat, "thea_CoatingMicroRoughness")
           if(getattr(mat, "thea_CoatingMicroRoughness", False)):
               row.prop(mat, "thea_CoatingMicroRoughnessWidth")
               row.prop(mat, "thea_CoatingMicroRoughnessHeight")

class MATERIAL_PT_Components(MaterialButtonsPanel, bpy.types.Panel):
    bl_label = "Layer Weight"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (thea_globals.showMatGui) and (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mat  = context.material

        matTuples = [(mat.thea_BasicOrder, "Basic", "thea_BasicOrder", "thea_BasicWeight"),
                     (mat.thea_Basic2Order, "Basic2", "thea_Basic2Order", "thea_Basic2Weight"),
                     (mat.thea_GlossyOrder, "Glossy", "thea_GlossyOrder", "thea_GlossyWeight"),
                     (mat.thea_Glossy2Order, "Glossy2", "thea_Glossy2Order", "thea_Glossy2Weight"),
                     (mat.thea_SSSOrder, "SSS", "thea_SSSOrder", "thea_SSSWeight"),
                     (mat.thea_ThinFilmOrder, "ThinFilm", "thea_ThinFilmOrder", "thea_ThinFilmWeight"),


                     ]
        sortedMats = sorted(matTuples, key=lambda mat: mat[0])
        for order, label, orderProp, weithProp  in sortedMats:
            if getattr(mat, 'thea_'+label, 0):
                row = layout.row()
                row.label(label)
                row.prop(mat, 'thea_'+label, text="")
                row.prop(mat, orderProp)
                row.prop(mat, weithProp, text="Weight")
                row.prop(mat, 'thea_'+label+"WeightFilename")

class MATERIAL_PT_Component(MaterialButtonsPanel, bpy.types.Panel):
    bl_label = "Material"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (thea_globals.showMatGui)and (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mat  = context.material
        tex = context.texture
        split = layout.split()
        row = layout.row()
        #col = split.column()
        #mat.thea_MaterialComponent.items=thea_properties.getMaterialComponents()
        row.prop(mat, "thea_MaterialComponent")

#------ Basic
        if mat.thea_MaterialComponent == "Basic":
            row.prop(mat, "thea_Basic", text="Enabled")
            row = layout.row()
            #row.operator("thea.sync_basic_to_blender", text="T>B")
            row.operator("thea.sync_blender_to_basic", text="B>T")
            row.label("     ")
            row.label("     ")
            #layout.prop(mat, "thea_BasicWeight")
            row = layout.row()
            if(mat.thea_BasicDiffuseFilename==""):
                row.prop(mat, "diffuse_color")
                #row.prop(mat, "thea_BasicDiffuseCol")
            row.prop(mat, "thea_BasicDiffuseFilename")

            row = layout.row()
            if(mat.thea_BasicReflectanceFilename==""):
                row.prop(mat, "thea_BasicReflectanceCol")
            row.prop(mat, "thea_BasicReflectanceFilename")

            row = layout.row()
            if(mat.thea_BasicTranslucentFilename==""):
                row.prop(mat, "thea_BasicTranslucentCol")
            row.prop(mat, "thea_BasicTranslucentFilename")

            row = layout.row()
            row.prop(mat, "thea_BasicAbsorptionCol")
            row.prop(mat, "thea_BasicAbsorption")
            row = layout.row()
            layout.prop(mat, "thea_BasicIOR")
            layout.prop(mat, "thea_BasicEC")
            layout.prop(mat, "thea_BasicTrace")
            split = layout.split()
            layout.label(text="Structure")
            row = layout.row()
            row.prop(mat, "thea_BasicStructureSigma")
            row.prop(mat, "thea_BasicSigmaFilename")
            row = layout.row()
            row.prop(mat, "thea_BasicStructureRoughness")
            row.prop(mat, "thea_BasicRoughnessFilename")
            row = layout.row()
            row.prop(mat, "thea_BasicStructureAnisotropy")
            row.prop(mat, "thea_BasicAnisotropyFilename")
            row = layout.row()
            row.prop(mat, "thea_BasicStructureRotation")
            row.prop(mat, "thea_BasicRotationFilename")
            row = layout.row()
            row.prop(mat, "thea_BasicStructureBump")
            row.prop(mat, "thea_BasicBumpFilename")
            row = layout.row()
            layout.prop(mat, "thea_BasicStructureNormal")
            row = layout.row()
            row.prop(mat, "thea_BasicMicroRoughness")
            if(getattr(mat, "thea_BasicMicroRoughness", False)):
               row.prop(mat, "thea_BasicMicroRoughnessWidth")
               row.prop(mat, "thea_BasicMicroRoughnessHeight")
#------ Basic2
        if mat.thea_MaterialComponent == "Basic2":
            row.prop(mat, "thea_Basic2", text="Enabled")
#             row = layout.row()
#             row.operator("thea.sync_basic_to_blender", text="T>B")
#             row.operator("thea.sync_blender_to_basic", text="B>T")
            #layout.prop(mat, "thea_BasicWeight")
            row = layout.row()
            if(mat.thea_Basic2DiffuseFilename==""):
                row.prop(mat, "thea_Basic2DiffuseCol")
            row.prop(mat, "thea_Basic2DiffuseFilename")

            row = layout.row()
            if(mat.thea_Basic2ReflectanceFilename==""):
                row.prop(mat, "thea_Basic2ReflectanceCol")
            row.prop(mat, "thea_Basic2ReflectanceFilename")

            row = layout.row()
            if(mat.thea_Basic2TranslucentFilename==""):
                row.prop(mat, "thea_Basic2TranslucentCol")
            row.prop(mat, "thea_Basic2TranslucentFilename")

            row = layout.row()
            row.prop(mat, "thea_Basic2AbsorptionCol")
            row.prop(mat, "thea_Basic2Absorption")
            row = layout.row()
            layout.prop(mat, "thea_Basic2IOR")
            layout.prop(mat, "thea_Basic2EC")
            layout.prop(mat, "thea_Basic2Trace")
            split = layout.split()
            layout.label(text="Structure")
            row = layout.row()
            row.prop(mat, "thea_Basic2StructureSigma")
            row.prop(mat, "thea_Basic2SigmaFilename")
            row = layout.row()
            row.prop(mat, "thea_Basic2StructureRoughness")
            row.prop(mat, "thea_Basic2RoughnessFilename")
            row = layout.row()
            row.prop(mat, "thea_Basic2StructureAnisotropy")
            row.prop(mat, "thea_Basic2AnisotropyFilename")
            row = layout.row()
            row.prop(mat, "thea_Basic2StructureRotation")
            row.prop(mat, "thea_Basic2RotationFilename")
            row = layout.row()
            row.prop(mat, "thea_Basic2StructureBump")
            row.prop(mat, "thea_Basic2BumpFilename")
            row = layout.row()
            layout.prop(mat, "thea_Basic2StructureNormal")
            row = layout.row()
            row.prop(mat, "thea_Basic2MicroRoughness")
            if(getattr(mat, "thea_Basic2MicroRoughness", False)):
               row.prop(mat, "thea_Basic2MicroRoughnessWidth")
               row.prop(mat, "thea_Basic2MicroRoughnessHeight")
#------ Glossy
        if mat.thea_MaterialComponent == "Glossy":
            row.prop(mat, "thea_Glossy", text="Enabled")
            row = layout.row()
            split = layout.split()
            row = layout.row()
            #colL.operator("thea.sync_glossy_to_blender", text="T>B")
            row.operator("thea.sync_blender_to_glossy", text="B>T")
            row.label("     ")
            row.label("     ")
            row = layout.row()
            if(mat.thea_GlossyReflectanceFilename==""):
                row.prop(mat, "thea_GlossyReflectanceCol")
            row.prop(mat, "thea_GlossyReflectanceFilename")

            #col.prop(mat, "thea_GlossyReflectanceCol")
            row = layout.row()
            if(mat.thea_GlossyTransmittanceFilename==""):
                row.prop(mat, "thea_GlossyTransmittanceCol")
            row.prop(mat, "thea_GlossyTransmittanceFilename")
            #col.prop(mat, "thea_GlossyTransmittanceCol")
            split = layout.split()
            row = layout.row()
            row.prop(mat, "thea_GlossyAbsorptionCol")
            row.prop(mat, "thea_GlossyAbsorption")
            split = layout.split()
            row = layout.row()
            col = split.column()
            col.prop(mat, "thea_GlossyIOR")
            col.prop(mat, "thea_GlossyEC")
            split = layout.split()
            row = layout.row()
            colL = split.column()
            colR = split.column()
            colL.prop(mat, "thea_GlossyAbbeNumberEnable")
            colR.prop(mat, "thea_GlossyAbbeNumber")
            row = layout.row()
            row.prop(mat, "thea_GlossyIORFileEnable")
            if getattr(mat, "thea_GlossyIORFileEnable"):
                row.prop(mat, "thea_GlossyIORMenu")
            split = layout.split()
            col = split.column()
            col.prop(mat, "thea_GlossyTraceReflections")
            col.prop(mat, "thea_GlossyTraceRefractions")
            split = layout.split()
            layout.label(text="Structure")
            row = layout.row()
            row.prop(mat, "thea_GlossyStructureRoughness")
            row.prop(mat, "thea_GlossyRoughnessFilename")
            row = layout.row()
            row.prop(mat, "thea_GlossyStructureRoughTrEn")
            if getattr(mat, "thea_GlossyStructureRoughTrEn"):
                row.prop(mat, "thea_GlossyStructureRoughnessTr")
            row = layout.row()
            row.prop(mat, "thea_GlossyStructureAnisotropy")
            row.prop(mat, "thea_GlossyAnisotropyFilename")
            row = layout.row()
            row.prop(mat, "thea_GlossyStructureRotation")
            row.prop(mat, "thea_GlossyRotationFilename")
            row = layout.row()
            row.prop(mat, "thea_GlossyStructureBump")
            row.prop(mat, "thea_GlossyBumpFilename")
            row = layout.row()
            layout.prop(mat, "thea_GlossyStructureNormal")
            row = layout.row()
            row.prop(mat, "thea_GlossyMicroRoughness")
            if(getattr(mat, "thea_GlossyMicroRoughness", False)):
               row.prop(mat, "thea_GlossyMicroRoughnessWidth")
               row.prop(mat, "thea_GlossyMicroRoughnessHeight")
#------ Glossy2
        if mat.thea_MaterialComponent == "Glossy2":
            row.prop(mat, "thea_Glossy2", text="Enabled")
            row = layout.row()
            split = layout.split()
            row = layout.row()
            if(mat.thea_Glossy2ReflectanceFilename==""):
                row.prop(mat, "thea_Glossy2ReflectanceCol")
            row.prop(mat, "thea_Glossy2ReflectanceFilename")

            #col.prop(mat, "thea_Glossy2ReflectanceCol")
            row = layout.row()
            if(mat.thea_Glossy2TransmittanceFilename==""):
                row.prop(mat, "thea_Glossy2TransmittanceCol")
            row.prop(mat, "thea_Glossy2TransmittanceFilename")
            #col.prop(mat, "thea_Glossy2TransmittanceCol")
            split = layout.split()
            row = layout.row()
            row.prop(mat, "thea_Glossy2AbsorptionCol")
            row.prop(mat, "thea_Glossy2Absorption")
            split = layout.split()
            row = layout.row()
            col = split.column()
            col.prop(mat, "thea_Glossy2IOR")
            col.prop(mat, "thea_Glossy2EC")
            split = layout.split()
            row = layout.row()
            colL = split.column()
            colR = split.column()
            colL.prop(mat, "thea_Glossy2AbbeNumberEnable")
            colR.prop(mat, "thea_Glossy2AbbeNumber")
            row = layout.row()
            row.prop(mat, "thea_Glossy2IORFileEnable")
            if getattr(mat, "thea_Glossy2IORFileEnable"):
                row.prop(mat, "thea_Glossy2IORMenu")
            split = layout.split()
            col = split.column()
            col.prop(mat, "thea_Glossy2TraceReflections")
            col.prop(mat, "thea_Glossy2TraceRefractions")
            split = layout.split()
            layout.label(text="Structure")
            row = layout.row()
            row.prop(mat, "thea_Glossy2StructureRoughness")
            row.prop(mat, "thea_Glossy2RoughnessFilename")
            row = layout.row()
            row.prop(mat, "thea_Glossy2StructureRoughTrEn")
            if getattr(mat, "thea_Glossy2StructureRoughTrEn"):
                row.prop(mat, "thea_Glossy2StructureRoughnessTr")
            row = layout.row()
            row.prop(mat, "thea_Glossy2StructureAnisotropy")
            row.prop(mat, "thea_Glossy2AnisotropyFilename")
            row = layout.row()
            row.prop(mat, "thea_Glossy2StructureRotation")
            row.prop(mat, "thea_Glossy2RotationFilename")
            row = layout.row()
            row.prop(mat, "thea_Glossy2StructureBump")
            row.prop(mat, "thea_Glossy2BumpFilename")
            row = layout.row()
            layout.prop(mat, "thea_Glossy2StructureNormal")
            row = layout.row()
            row.prop(mat, "thea_Glossy2MicroRoughness")
            if(getattr(mat, "thea_Glossy2MicroRoughness", False)):
               row.prop(mat, "thea_Glossy2MicroRoughnessWidth")
               row.prop(mat, "thea_Glossy2MicroRoughnessHeight")
#------ SSS
        if mat.thea_MaterialComponent == "SSS":
            row.prop(mat, "thea_SSS", text="Enabled")
            row = layout.row()
            split = layout.split()
            row = layout.row()
            if(mat.thea_SSSReflectanceFilename==""):
                row.prop(mat, "thea_SSSReflectanceCol")
            row.prop(mat, "thea_SSSReflectanceFilename")
            row = layout.row()
            row.prop(mat, "thea_SSSAbsorptionCol")
            row.prop(mat, "thea_SSSAbsorption")
            row = layout.row()
            row.prop(mat, "thea_SSSScatteringCol")
            row.prop(mat, "thea_SSSScattering")
            split = layout.split()
            row = layout.row()
            col = split.column()
            col.prop(mat, "thea_SSSAsymetry")
            col.prop(mat, "thea_SSSIOR")
            col.prop(mat, "thea_SSSTraceReflections")
            col.prop(mat, "thea_SSSTraceRefractions")
            split = layout.split()
            col = split.column()
            row.label(text="Structure")
            row = layout.row()
            col.prop(mat, "thea_SSSStructureRoughness")
            split = layout.split()
            row = layout.row()
            colL = split.column()
            colR = split.column()
            colL.prop(mat, "thea_SSSStructureRoughTrEn")
            colR.prop(mat, "thea_SSSStructureRoughnessTr")
            split = layout.split()
            layout.label(text="Structure")
            row = layout.row()
            row.prop(mat, "thea_SSSStructureRoughness")
            row.prop(mat, "thea_SSSRoughnessFilename")
            row = layout.row()
            row.prop(mat, "thea_SSSStructureAnisotropy")
            row.prop(mat, "thea_SSSAnisotropyFilename")
            row = layout.row()
            row.prop(mat, "thea_SSSStructureRotation")
            row.prop(mat, "thea_SSSRotationFilename")
            row = layout.row()
            row.prop(mat, "thea_SSSStructureBump")
            row.prop(mat, "thea_SSSBumpFilename")
            row = layout.row()
            layout.prop(mat, "thea_SSSStructureNormal")
        if mat.thea_MaterialComponent == "ThinFilm":
            row.prop(mat, "thea_ThinFilm", text="Enabled")
            row = layout.row()
            split = layout.split()
            row = layout.row()
            #col.prop(mat, "thea_ThinFilmWeight")
            if(mat.thea_ThinFilmTransmittanceFilename==""):
                row.prop(mat, "thea_ThinFilmTransmittanceCol")
            row.prop(mat, "thea_ThinFilmTransmittanceFilename")
#            col.prop(mat, "thea_ThinFilmTransmittanceCol")
            split = layout.split()
            row = layout.row()
            col = split.column()
            col.prop(mat, "thea_ThinFilmIOR")
#            CHANGED > Added inactive state to ThinFilm  THickness
            row = layout.row()
            split = layout.split()
            col.prop(mat, "thea_ThinFilmInterference")
            col = split.column()
            sub = col.row()
            sub.active = mat.thea_ThinFilmInterference == True
            sub.prop(mat, "thea_ThinFilmThickness")
            sub.prop(mat, "thea_ThinFilmThicknessFilename")
#            col.prop(mat, "thea_ThinFilmThickness")
            row = layout.row()
            split = layout.split()
            col = split.column()
            row.label(text="Structure")
#           CHANGED > Was given the name of glossy
            col.prop(mat, "thea_ThinFilmStructureBump")
            col.prop(mat, "thea_ThinFilmBumpFilename")
            col.prop(mat, "thea_ThinFilmStructureNormal")




class MATERIAL_PT_Clipping(MaterialButtonsPanel, bpy.types.Panel):
    bl_label = "Clipping"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (thea_globals.showMatGui) and (engine in cls.COMPAT_ENGINES)

    def draw_header(self, context):
       scene = context.scene
       mat  = context.material
       self.layout.prop(mat, "thea_Clipping", text="")

    def draw(self, context):
       layout = self.layout
       scene = context.scene
       mat  = context.material
       split = layout.split()
       row = layout.row()

       if mat.get('thea_Clipping'):
           row = layout.row()
           col = split.column()
           col.prop(mat, "thea_ClippingFilename")
           col.prop(mat, "thea_ClippingThreshold")
           col.prop(mat, "thea_ClippingSoft")

class MATERIAL_PT_Emittance(MaterialButtonsPanel, bpy.types.Panel):
    bl_label = "Emittance"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (thea_globals.showMatGui) and (engine in cls.COMPAT_ENGINES)

    def draw_header(self, context):
       scene = context.scene
       mat  = context.material
       self.layout.prop(mat, "thea_Emittance", text="")

    def draw(self, context):
       layout = self.layout
       scene = context.scene
       mat  = context.material
       split = layout.split()
       row = layout.row()

       if mat.get('thea_Emittance'):
           row = layout.row()
           if(mat.thea_EmittanceFilename==""):
                row.prop(mat, "thea_EmittanceCol")
           row.prop(mat, "thea_EmittanceFilename")
           row = layout.row()
           row.prop(mat, "thea_EmittancePower")
#      CHANGED > Added this to hide with other light units
           if getattr(context.material, "thea_EmittanceUnit") in ("Watts", "W/m2", "W/sr", "W/sr/m2"):
               row.prop(mat, "thea_EmittanceEfficacy")
#           row.prop(mat, "thea_EmittanceEfficacy")
           layout.prop(mat, "thea_EmittanceUnit")
           row = layout.row()
           row.prop(mat, "thea_EmittanceIES")
           if(getattr(mat, "thea_EmittanceIES")):
               row.prop(mat, "thea_EmittanceIESFilename")
               row = layout.row()
               layout.prop(mat, "thea_EmittanceIESMultiplier")
           row = layout.row()
           layout.prop(mat, "thea_EmittancePassiveEmitter")
           row = layout.row()
           row.prop(mat, "thea_EmittanceAmbientEmitter")
           if(getattr(mat, "thea_EmittanceAmbientEmitter")):
               row.prop(mat, "thea_EmittanceAmbientLevel")
           col = split.column()

class MATERIAL_PT_Medium(MaterialButtonsPanel, bpy.types.Panel):
    bl_label = "Medium"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (thea_globals.showMatGui) and (engine in cls.COMPAT_ENGINES)

    def draw_header(self, context):
       scene = context.scene
       mat  = context.material
       self.layout.prop(mat, "thea_Medium", text="")

    def draw(self, context):
       layout = self.layout
       scene = context.scene
       mat  = context.material
       split = layout.split()
       row = layout.row()

       if mat.get('thea_Medium'):
           row = layout.row()
           if(mat.thea_MediumAbsorptionFilename==""):
                row.prop(mat, "thea_MediumAbsorptionCol")
           row.prop(mat, "thea_MediumAbsorptionFilename")
           row = layout.row()
           if(mat.thea_MediumScatterFilename==""):
                row.prop(mat, "thea_MediumScatterCol")
           row.prop(mat, "thea_MediumScatterFilename")
           row = layout.row()
           if(mat.thea_MediumAbsorptionDensityFilename==""):
               row.prop(mat, "thea_MediumAbsorptionDensity")
           row.prop(mat, "thea_MediumAbsorptionDensityFilename")
           row = layout.row()
           if(mat.thea_MediumScatterDensityFilename==""):
               row.prop(mat, "thea_MediumScatterDensity")
           row.prop(mat, "thea_MediumScatterDensityFilename")
           row = layout.row()
           row.prop(mat, "thea_MediumCoefficient")
           if(mat.thea_MediumCoefficient):
               row.prop(mat, "thea_MediumMenu")
           row = layout.row()
           row.prop(mat, "thea_MediumPhaseFunction")


class MATERIAL_PT_Displacement(MaterialButtonsPanel, bpy.types.Panel):
    bl_label = "Displacement"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (thea_globals.showMatGui) and (engine in cls.COMPAT_ENGINES)

    def draw_header(self, context):
       scene = context.scene
       mat  = context.material
       self.layout.prop(mat, "thea_Displacement", text="")

    def draw(self, context):
       layout = self.layout
       scene = context.scene
       mat  = context.material
       split = layout.split()
       row = layout.row()

       if mat.get('thea_Displacement'):
           row = layout.row()
           col = split.column()
           col.prop(mat, "thea_DisplacementFilename")
           col.prop(mat, "thea_DispSub")
#            col.prop(mat, "thea_DispBump")
           col.prop(mat, "thea_DisplacementHeight")
           col.prop(mat, "thea_DisplacementCenter")
           col.prop(mat, "thea_DisplacementNormalSmooth")
           col.prop(mat, "thea_DisplacementTightBounds")


class MATERIAL_PT_Thea_Strand(MaterialButtonsPanel, bpy.types.Panel):
    bl_label = "Strand"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (thea_globals.showMatGui) and (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
       layout = self.layout
       scene = context.scene
       mat  = context.material
       tan = mat.strand
       split = layout.split()
       row = layout.row()
       col = split.column()
       col.prop(mat, "thea_StrandRoot")
       col.prop(mat, "thea_StrandTip")
       col.prop(mat, "thea_FastHairExport")
       col.prop(mat, "thea_ColoredHair")

class MATERIAL_PT_theaEditMaterial(MaterialButtonsPanel, bpy.types.Panel):
    bl_label = "External Thea Material"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        if hasattr(bpy.context, 'active_object'):
            try:
                extMat = os.path.exists(os.path.abspath(bpy.path.abspath(bpy.context.active_object.active_material.get('thea_extMat'))))
            except:
                extMat = False
        return ((thea_globals.showMatGui) or extMat) and (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
       layout = self.layout
       scene = context.scene
       mat  = context.material
       split = layout.split()
       row = layout.row()
       colL = split.column()
       colR = split.column()
       colL.operator("thea.thea_material_editor", text="Edit in Thea")
       colR.operator("thea.delete_material_link", text="Delete link")
       split = layout.split()
       row = layout.row()
       col = split.column()
#        if (mat.get('thea_extMat')):
       col.prop(mat, "thea_extMat")
       if len(getattr(mat, "thea_extMat"))>5:
           if not thea_render_main.isMaterialLinkLocal(getattr(mat, "thea_extMat")):
                if os.path.exists(os.path.abspath(bpy.path.abspath(getattr(mat, "thea_extMat")))):
                    row = layout.row()
                    row.operator("thea.copy_material_locally")
           if getattr(mat, "thea_extMat"):
                row = layout.row()
                row.operator("thea.list_linked_materials")
#        print("local: ", thea_render_main.isMaterialLinkLocal(getattr(mat, "thea_extMat")))
#        print("exists: ", os.path.exists(os.path.abspath(bpy.path.abspath(getattr(mat, "thea_extMat")))), os.path.abspath(bpy.path.abspath(getattr(mat, "thea_extMat"))))

from bl_ui.properties_material import active_node_mat

def context_tex_datablock(context):
    idblock = context.material
    if idblock:
        return active_node_mat(idblock)

    idblock = context.lamp
    if idblock:
        return idblock

    idblock = context.world
    if idblock:
        return idblock

    idblock = context.brush
    if idblock:
        return idblock

    idblock = context.line_style
    if idblock:
        return idblock

    if context.particle_system:
        idblock = context.particle_system.settings

    return idblock


class TextureSlotPanel(TextureButtonsPanel):
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        if not hasattr(context, "texture_slot"):
            return False

        engine = context.scene.render.engine
        return TextureButtonsPanel.poll(cls, context) and (engine in cls.COMPAT_ENGINES)


# Texture Type Panels #


class TextureTypePanel(TextureButtonsPanel):

    @classmethod
    def poll(cls, context):
        tex = context.texture
        engine = context.scene.render.engine
        return tex and ((tex.type == cls.tex_type and not tex.use_nodes) and (engine in cls.COMPAT_ENGINES))

class TEXTURE_PT_Thea_mapping(TextureSlotPanel, Panel):
    bl_label = "Mapping"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        idblock = context_tex_datablock(context)
#         if isinstance(idblock, Brush) and not context.sculpt_object:
#             return False

        if (not getattr(context, "texture_slot", None)) or (context.texture_slot.name == ''):
            return False

        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
        layout = self.layout

        idblock = context_tex_datablock(context)

        tex = context.texture_slot


        if tex.rna_type.identifier=="MaterialTextureSlot":
            split = layout.split(percentage=0.3)
            col = split.column()
            col.label(text="Coordinates:")
            col = split.column()
            col.prop(tex, "texture_coords", text="")
            if tex.texture_coords == 'UV':
                split = layout.split(percentage=0.3)
                split.label(text="UV Channel:")
                split.prop(tex.texture, 'thea_TexUVChannel', text="")
#                 ob = context.object
#                 if ob and ob.type == 'MESH':
#                     split.prop_search(tex, "uv_layer", ob.data, "uv_textures", text="")
#                 else:
#                     split.prop(tex, "uv_layer", text="")
            split = layout.split(percentage=0.3)
            split.label(text="Projection:")
            split.prop(tex, "mapping", text="")
            split = layout.split(percentage=0.3)
            split.label(text="Channel:")
            split.prop(tex.texture, "thea_TexChannel", text="")

        row = layout.row()
        row.column().prop(tex, "offset")
        row.column().prop(tex, "scale")
        row = layout.row()
        row.prop(context.texture,"thea_TexRotation")


class TEXTURE_PT_Thea_ToneMap(TextureButtonsPanel, bpy.types.Panel):
    bl_label = "Tone"
    COMPAT_ENGINES = {'THEA_RENDER'}

    @classmethod
    def poll(cls, context):
        if (not getattr(context, "texture_slot", None)) or (context.texture_slot.name == ''):
            return False
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
        layout = self.layout

        tex = context.texture
        split = layout.split()
        row = layout.row()
        colL = split.column()
        colL.prop(tex,"thea_TexInvert")
        colL.prop(tex,"thea_TexGamma")
        colL.prop(tex,"thea_TexRed")
        colL.prop(tex,"thea_TexGreen")
        colL.prop(tex,"thea_TexBlue")
        colL.prop(tex,"thea_TexSaturation")
        colL.prop(tex,"thea_TexBrightness")
        colL.prop(tex,"thea_TexContrast")
        colL.prop(tex,"thea_TexClampMin")
        colL.prop(tex,"thea_TexClampMax")


# class TEXTURE_PT_Thea_Component(TextureButtonsPanel, bpy.types.Panel):
#     bl_label = "Mapping"
#     COMPAT_ENGINES = {'THEA_RENDER'}
#
#
#     def draw(self, context):
#         layout = self.layout
#
#         tex = context.texture
#         split = layout.split()
#         row = layout.row()
#         colL = split.column()
#         colR = split.column()
#         colL.prop(tex,"thea_Basic")
#         colR.prop(tex,"thea_Basic2")
#         colL.prop(tex,"thea_Glossy")
#         colR.prop(tex,"thea_Coating")
#         colL.prop(tex,"thea_SSS")
#         colR.prop(tex,"thea_Clipping")
#         colR.prop(tex,"thea_Emittance")
#         colL.prop(tex,"thea_ThinFilm")


class RENDER_PT_theaTools(RenderButtonsPanel, bpy.types.Panel):
    bl_label = "Thea Tools"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw_header(self, context):
       scene = context.scene
       mat  = context.material
       self.layout.prop(scene, "thea_showTools", text="")

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        rd = context.scene.render

        if getattr(scene, "thea_showTools"):

            split = layout.split()
            colL = split.column()
            colR = split.column()
            colL.operator("thea.enable_animation_export", text="Enable animation export")
            colR.operator("thea.disable_animation_export", text="Disable animation export")
            colL.operator("thea.enable_animated", text="Enable mesh animation")
            colR.operator("thea.disable_animated", text="Disable mesh animation")
            colL.operator("thea.enable_caustic_receiver", text="Enable caustic receiver")
            colR.operator("thea.disable_caustic_receiver", text="Disable caustic receiver")
            colL.operator("thea.enable_trace_reflections", text="Enable trace reflections")
            colR.operator("thea.disable_trace_reflections", text="Disable trace reflections")
            colL.operator("thea.export_anim", text="Export Animation")
            colR.operator("thea.export_still_cameras", text="Export Still Cameras")
            colL.operator("thea.sync_with_thea", text="Sync with Thea")
            colR.operator("thea.sync_blender_to_thea", text="Enable basic components")
            colL.operator("thea.sync_cycles_to_thea", text="Convert Cycles materials")

class RENDER_PT_theaLUTTools(RenderButtonsPanel, bpy.types.Panel):
    bl_label = "Use Thea LUT"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw_header(self, context):
       scene = context.scene
       mat  = context.material
       self.layout.prop(scene, "thea_useLUT", text="")

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        rd = context.scene.render

        if(getattr(scene, 'thea_useLUT')):
            split = layout.split()
            col = split.column()
            col.prop(scene, "thea_nameBasedLUT")
            col.prop(scene, "thea_materialsPath")
            col.operator("thea.materials_path", text="Set materials path")
            col.prop(scene, "thea_overwriteLUT")
            col.prop(scene, "thea_LUTScanSubdirectories")
            col.operator("thea.make_lut", text="Generate LUT file from Thea materials")
            try:
                col.label(text=" %s" % scene['thea_lutMessage'])
            except:
                pass


class RENDER_PT_theaRender(RenderButtonsPanel, bpy.types.Panel):
#   CHANGED > Different naming so i made more sense
    bl_label = "Thea Production & Export"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw(self, context):

        layout = self.layout
        scene = context.scene

        rd = context.scene.render

        split = layout.split()

        col = split.column()

        if scene.get('thea_Warning'):
            if len(scene.get('thea_Warning')) > 5:
                row = layout.row()
                row.label(text=scene['thea_Warning'])
        split = layout.split()
        colL = split.column()
        colR = split.column()
        colL.operator("render.render", text="Image", icon='RENDER_STILL')
#      CHANGED > Changged to shorter name
        colR.operator("thea.export_frame", text="Export to Studio" )
        split = layout.split()
        colL = split.column()
        colR = split.column()
        colL.operator("render.render", text="Animation", icon='RENDER_ANIMATION').animation = True
        #colL.operator("thea.render_animation", text="Render Animation")
        #colR.prop(scene,"thea_startTheaAfterExport")
#        CHANGED > Changed to shorter name
        colR.operator("thea.save_frame", text="Save XML file")
        split = layout.split()
        row = layout.row()
        col = split.column()
        col.prop(scene,"thea_ExportAnimation")
        col.prop(scene,"thea_AnimationEveryFrame")
        col.prop(scene,"thea_HideThea")
        col.prop(scene,"thea_ExitAfterRender")
        col.prop(scene,"thea_stopOnErrors")
        col.prop(scene,"thea_Reuse")
        col.prop(scene,"thea_Selected")
        col.prop(scene,"thea_RenderRefreshResult")
        row = layout.row()


class VIEW3D_PT_theaIR(bpy.types.Panel):
    '''
    New GUI layout by Tomasz Muszynski
    '''

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Thea Interactive Render"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
        scene = context.scene
        wm = context.window_manager
        layout = self.layout
        split = layout.split()
        row = layout.row()

        layout.prop(scene,"thea_IRAdvancedIR", text="Use Advanced IR Control")

# --- IR STOPPED -------------------------------------------------------------
        if not thea_globals.IrIsRunning:
            if not getattr(scene, 'thea_IRAdvancedIR'):

                layout.operator("thea.start_ir", text="Start IR", icon='PLAY')
            else:
                layout.label("Launch IR:")
                layout.operator("thea.start_ir", text="Start IR: FULL", icon='PLAY')
                layout.prop(scene,"thea_Selected", text="Export only selected objects")

                layout.separator();
                if not getattr(scene, "thea_Selected"):
                        if getattr(context.scene, 'thea_WasExported'):

                            layout.operator("thea.start_ir_reuse", text="Start IR: FAST", icon='NEXT_KEYFRAME')

                            layout.prop(scene, "thea_IRFullExportSelected", text="Do Full Export For Selected Objects and resue rest")
                layout.separator()

# --- IR is RUNNING -------------------------------------------------------------
        else:
            if not getattr(scene, 'thea_IRAdvancedIR'):

                layout.operator("thea.start_ir", text="Stop IR", icon='CANCEL')
            else:
                layout.label("Running IR Control:")
                layout.operator("thea.start_ir", text="Stop IR", icon='CANCEL')
                layout.separator()
                layout.separator()
                if not thea_globals.IrIsPaused:
                    layout.operator("thea.pause_ir", text="Pause IR", icon='PAUSE')
                else:
                    layout.operator("thea.pause_ir", text="Continue IR", icon='PLAY')
                layout.separator()
                layout.label("Scene objects update section:");
                layout.operator("thea.update_ir", text="Update selected objects", icon='FILE_REFRESH')
                layout.separator()
                layout.label("IR Image Operations:");
                layout.operator("thea.save_ir", text="Save IR result")
                layout.separator()

class VIEW3D_PT_theaIR_Advanced(bpy.types.Panel):
    '''
    New GUI layout by Tomasz Muszynski
    '''

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Thea IR Advanced Settings"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
        scene = context.scene
        wm = context.window_manager
        layout = self.layout
        split = layout.split()
        row = layout.row()
# --- Advanced Settings-------------------------------------------------------------
#         layout.separator()

#         layout.prop(scene, 'thea_IRAdvancedSettings',text="Show Advanced Settings")
#         if getattr(scene, 'thea_IRAdvancedSettings'):

#         layout.separator()
        layout.label(" IR Engine Settings:", icon="FORWARD")
#         box = layout.box()
#         row = box.row()
        row.prop(scene, "thea_IRRenderEngineMenu")
        if getattr(scene, "thea_IRRenderEngineMenu").startswith("Presto"):
#             row = box.row()
            row = layout.row()
            row.prop(scene,"thea_IRDevice")
        if thea_globals.IrIsRunning == False:
#             row = box.row()
            row = layout.row()
            row.prop(scene,"thea_IRResolution")

        layout.separator()
        layout.label(" IR Draw Settings:", icon="FORWARD")
        box = layout.box()
        row = box.row()
        row.prop(scene,"thea_DrawPreviewto3dView")
        row = box.row()
        row.prop(scene,"thea_SavePreviewtoImage")
        if getattr(scene,"thea_DrawPreviewto3dView"):# or getattr(scene,"thea_SavePreviewtoImage"):
            row = box.row()
            row.prop(scene,"thea_Fit3dView")
            row = box.row()
            row.prop(scene,"thea_IRBlendAlpha")


#                 layout.prop(scene,"thea_RefreshDelay")
            row = box.row()
            row.prop(scene,"thea_IRShowTheaWindow")



            layout.separator()
            layout.label(" Export Behaviour:", icon="FORWARD")
            box = layout.box()
            row = box.row()
            row.prop(scene,"thea_IRFullUpdate")
            row = box.row()
            row.prop(scene,"thea_IRExportAnimation")

class VIEW3D_PT_theaIR_Keyboard(bpy.types.Panel):
    '''
    New GUI layout by Tomasz Muszynski
    '''

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Thea IR Keyboard control"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
        scene = context.scene
        wm = context.window_manager
        layout = self.layout
        split = layout.split()
        row = layout.row()
# --- Keyboard control-------------------------------------------------------------


#         layout.separator()
#         layout.label(" Keyboard IR control:", icon="FORWARD")
#         box = layout.box()
#         row = box.row()
        row.prop(scene,"thea_IRRemapIRKeys", text="Use F11&F12 keys for IR" )
        row = layout.row()
#         row = box.row()
        row.label(" Change needs Blender restart.", icon="ERROR")
        row = layout.row()
#         row = box.row()
        row.label("Mapped Keys:")
        row = layout.row()
#         row = box.row()
        row.label("F12 - Start/Pause/Continue IR")
        row = layout.row()
#         row = box.row()
        row.label("CTRL+F12 - Stop IR")
        row = layout.row()
#         row = box.row()
        row.label("F11 - Update Selected")



#         layout.separator()


# class VIEW3D_PT_theaIR(bpy.types.Panel):
#     bl_space_type = 'VIEW_3D'
#     bl_region_type = 'UI'
#     bl_label = "Thea Interactive Render"
#     COMPAT_ENGINES = set(['THEA_RENDER'])
#
#     @classmethod
#     def poll(cls, context):
#         engine = context.scene.render.engine
#         return (engine in cls.COMPAT_ENGINES)
#
#     def draw(self, context):
#         scene = context.scene
#         wm = context.window_manager
#         layout = self.layout
#         split = layout.split()
#         row = layout.row()
# #        col = split.column()
# #         if not scene.thea_ir_running:
#
#         if not thea_globals.IrIsRunning:
#             layout.operator("thea.start_ir", text="Start IR", icon='PLAY')
# #                 layout.prop(scene, "thea_IRFullExportSelected", text="Export selected objects when starting IR")
#         else:
#             layout.operator("thea.start_ir", text="Stop IR", icon='CANCEL')
#             if not thea_globals.IrIsPaused:
#                 layout.operator("thea.pause_ir", text="Pause IR", icon='PAUSE')
#             else:
#                 layout.operator("thea.pause_ir", text="Continue IR", icon='PLAY')
#             layout.operator("thea.save_ir", text="Save IR result",)
# #@        col.prop(scene,"thea_Reuse")
#         #layout.label(getattr(scene, "thea_IRMessage"))
#         layout.prop(scene, 'thea_IRAdvancedSettings')
#         if getattr(scene, 'thea_IRAdvancedSettings'):
#             if getattr(context.scene, 'thea_WasExported'):
#                 if not thea_globals.IrIsRunning:
#                     layout.operator("thea.start_ir", text="Start IR: reuse mesh data", icon='PLAY').reuseProp = True
#                     layout.label("_______________________________________________________________________________________________")
#             layout.prop(scene, "thea_IRRenderEngineMenu")
#             if getattr(scene, "thea_IRRenderEngineMenu").startswith("Presto"):
#                 layout.prop(scene,"thea_IRDevice")
#             if thea_globals.IrIsRunning == False:
#                 layout.prop(scene,"thea_IRResolution")
#             layout.label("_______________________________________________________________________________________________")
#             layout.prop(scene,"thea_DrawPreviewto3dView")
#             layout.prop(scene,"thea_SavePreviewtoImage")
#             if getattr(scene,"thea_DrawPreviewto3dView"):# or getattr(scene,"thea_SavePreviewtoImage"):
#                 layout.prop(scene,"thea_Fit3dView")
#                 layout.prop(scene,"thea_IRBlendAlpha")
#
#
# #                 layout.prop(scene,"thea_RefreshDelay")
#
#             layout.prop(scene,"thea_IRShowTheaWindow")
#             layout.label("_______________________________________________________________________________________________")
#             if thea_globals.IrIsRunning:
# #                 layout.operator("thea.refresh_ir", text="Refresh", icon='FILE_REFRESH')
#                 layout.operator("thea.update_ir", text="Update selected objects", icon='FILE_REFRESH')
#                 layout.label("_______________________________________________________________________________________________")
#             layout.prop(scene,"thea_IRFullUpdate")
#             layout.prop(scene,"thea_Reuse", text="Prevent mesh export")
#             if getattr(scene, "thea_Reuse", False):
#                 layout.prop(scene, "thea_IRFullExportSelected", text="    Always full export selected objects when starting IR")
#             layout.prop(scene,"thea_Selected", text="Export only selected objects")
#             layout.prop(scene,"thea_IRExportAnimation")
#


class RENDER_PT_theaPresets(RenderButtonsPanel, bpy.types.Panel):
    bl_label = "Thea Render Presets"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw_header(self, context):
       scene = context.scene
       mat  = context.material
       self.layout.prop(scene, "thea_enablePresets", text="")

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        if getattr(scene, "thea_enablePresets"):
           layout.prop(scene,"thea_RenderPresetsMenu")


class RENDER_PT_theaMain(RenderButtonsPanel, bpy.types.Panel):
#   CHANGED > Better and more understanding naming
    bl_label = "Thea Engines"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (getattr(context.scene, "thea_enablePresets") != True) and (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
       layout = self.layout

       scene = context.scene
       split = layout.split()
       row = layout.row()
       col = split.column()
       col.prop(scene,"thea_RenderEngineMenu")
       if getattr(context.scene, "thea_RenderEngineMenu") in ("Presto (AO)", "Presto (MC)"):
           col.prop(scene,"thea_IRDevice")
       col.prop(scene,"thea_AASamp")
       col.prop(scene,"thea_RenderTime")
       #col.prop(scene,"thea_RenderMaxPasses")
       col.prop(scene,"thea_RenderMaxSamples")
       col.prop(scene,"thea_RenderMBlur")
       col.prop(scene,"thea_RenderVolS")
       col.prop(scene,"thea_RenderLightBl")
#      CHANGED > Added button to save img.thea file
       col.prop(scene,"thea_ImgTheaFile")
#      CHANGED > Added Clay render
       split = layout.split()
       row = layout.row()
       colL = split.column()
       colR = split.column()
       colL.prop(scene,"thea_clayRender")
       if getattr(scene, "thea_clayRender"):
           colR.prop(scene,"thea_clayRenderReflectance")


class RENDER_PT_theaDisplay(RenderButtonsPanel, bpy.types.Panel):
    bl_label = "Thea Display"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
        scene = context.scene
        layout = self.layout

        layout.prop(scene,"thea_DispISO")
        layout.prop(scene,"thea_DispShutter")
        layout.prop(scene,"thea_DispFNumber")
        layout.prop(scene,"thea_DispGamma")
        layout.prop(scene,"thea_DispBrightness")
        layout.prop(scene,"thea_DispCRFMenu")
        split = layout.split()
        row = layout.row()
        colL = split.column()
        colR = split.column()
#       CHANGED > added the new active/inactive menu's, new sharpness, bloom items and diaphgrama options
        colL.prop(scene,"thea_DispSharpness")
#        if getattr(scene,"thea_DispSharpness"):
#            colR.prop(scene,"thea_DispSharpnessWeight")
        sub = colR.row()
        sub.active = scene.thea_DispSharpness == True
        sub.prop(scene, "thea_DispSharpnessWeight")
        split = layout.split()
        row = layout.row()
        colL = split.column()
        colR = split.column()
        colL.prop(scene,"thea_DispBurn")
#        if getattr(scene,"thea_DispBurn"):
#            colR.prop(scene,"thea_DispBurnWeight")
        sub = colR.row()
        sub.active = scene.thea_DispBurn == True
        sub.prop(scene,"thea_DispBurnWeight")
        split = layout.split()
        row = layout.row()
        colL = split.column()
        colR = split.column()
        colL.prop(scene,"thea_DispTemperature")
#        if getattr(scene,"thea_DispTemperature"):
#            colR.prop(scene,"thea_DispTemperatureWeight")
        sub = colR.row()
        sub.active = scene.thea_DispTemperature == True
        sub.prop(scene,"thea_DispTemperatureWeight")
        split = layout.split()
        row = layout.row()
        colL = split.column()
        colR = split.column()
        colL.prop(scene,"thea_DispContrast")
#        if getattr(scene,"thea_DispContrast"):
#            colR.prop(scene,"thea_DispContrastWeight")
        sub = colR.row()
        sub.active = scene.thea_DispContrast == True
        sub.prop(scene,"thea_DispContrastWeight")
        split = layout.split()
        row = layout.row()
        colL = split.column()
        colR = split.column()
        colL.prop(scene,"thea_DispVignetting")
#        if getattr(scene,"thea_DispVignetting"):
#            colR.prop(scene,"thea_DispVignettingWeight")
        sub = colR.row()
        sub.active = scene.thea_DispVignetting == True
        sub.prop(scene,"thea_DispVignettingWeight")
        split = layout.split()
        row = layout.row()
        colL = split.column()
        colR = split.column()
        colL.prop(scene,"thea_DispChroma")
#        if getattr(scene,"thea_DispChroma"):
#            colR.prop(scene,"thea_DispChromaWeight")
        sub = colR.row()
        sub.active = scene.thea_DispChroma == True
        sub.prop(scene,"thea_DispChromaWeight")
        split = layout.split()
        row = layout.row()
        colL = split.column()
        colR = split.column()
        #        colL.prop(scene,"thea_DispBloom")
        #        #        if getattr(scene,"thea_DispBloom"):
        #        #            colR.prop(scene,"thea_DispBloomWeight")
        #        #            colR.prop(scene,"thea_DispGlareRadius")
        #        sub = colR.row()
        #        sub.active = scene.thea_DispBloom != "0"
        #        print("displayBloom: ", scene.thea_DispBloom)
        #        sub.prop(scene,"thea_DispBloomWeight")
        #        sub.prop(scene,"thea_DispGlareRadius")
        colL.prop(scene,"thea_DispBloom")
        #        if getattr(scene,"thea_DispBloom"):
        #            colR.prop(scene,"thea_DispBloomWeight")
        #            colR.prop(scene,"thea_DispGlareRadius")
        sub = colR.row()
        sub.active = scene.thea_DispBloom == True
        sub.prop(scene,"thea_DispBloomItems")
        split = layout.split()
        row = layout.row()
        if getattr(scene,"thea_DispBloom"):
            colR.prop(scene,"thea_DispBloomWeight")
            colR.prop(scene,"thea_DispGlareRadius")

        layout.prop(scene,"thea_DispMinZ")
        layout.prop(scene,"thea_DispMaxZ")



class RENDER_PT_theaDistribution(RenderButtonsPanel, bpy.types.Panel):
    bl_label = "Distribution"
    COMPAT_ENGINES = set(['THEA_RENDER'])

#   CHANGED > Added this to hide when remote is not active
    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (getattr(context.scene, "thea_showRemoteSetup") != False) and (engine in cls.COMPAT_ENGINES)

#    @classmethod
#    def poll(cls, context):
#        engine = context.scene.render.engine
#        return (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
       layout = self.layout
       scene = context.scene
       split = layout.split()
       row = layout.row()
       col = split.column()
       col.prop(scene,"thea_DistTh")
       col.prop(scene,"thea_DistPri")
       col.prop(scene,"thea_DistNet")
       col.prop(scene,"thea_DistPort")
       col.prop(scene,"thea_DistAddr")
       col.prop(scene,"thea_BucketRendering")

class RENDER_PT_BiasedSettings(RenderButtonsPanel, bpy.types.Panel):
    bl_label = "Biased Settings"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return ((getattr(context.scene, "thea_enablePresets") != True) and
                (getattr(context.scene, "thea_RenderEngineMenu") in ("Adaptive (BSD)"))) and (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
       layout = self.layout
       scene = context.scene
       #split = layout.split()
       #row = layout.row()
       box = layout.box()
       row = box.row()
       row.label("Biased RT")
       row = box.row()
       row.prop(scene,"thea_RTTracingDepth")
       row = box.row()
       row.prop(scene,"thea_RTGlossyDepth")
       row = box.row()
       row.prop(scene,"thea_RTDiffuseDepth")
       row = box.row()
       row.prop(scene,"thea_RTTraceReflections")
       row = box.row()
       row.prop(scene,"thea_RTTraceRefractions")
       row = box.row()
       row.prop(scene,"thea_RTTraceTransparencies")
       row = box.row()
       row.prop(scene,"thea_RTTraceDispersion")
       layout.separator()
       box = layout.box()
       row = box.row()
#        layout.label("_______________________________________________________________________________________________")
       row.label("Biased Antialiasing")
       row = box.row()
       row.prop(scene,"thea_AACont")
       row = box.row()
       row.prop(scene,"thea_AAMinSub")
       row = box.row()
       row.prop(scene,"thea_AAMaxSub")
       row = box.row()

       layout.separator()
       box = layout.box()
       row = box.row()
       row.label("Biased Direct Lighting")
       row.prop(scene, "thea_DLEnable", text="")
       if scene.thea_DLEnable:
           row = box.row()
           row.prop(scene,"thea_DLPerceptualBased")
           row = box.row()
           row.prop(scene,"thea_DLMaxError")

       layout.separator()
       box = layout.box()
       row = box.row()
       row.label("Biased Blurred Reflections")
       row.prop(scene, "thea_BREnable", text="")
       if scene.thea_BREnable:
           row = box.row()
           row.prop(scene,"thea_BRMinSub")
           row = box.row()
           row.prop(scene,"thea_BRMaxSub")

       layout.separator()
       box = layout.box()
       row = box.row()

       row.label("Field Mapping")
       row.prop(scene, "thea_FMEnable", text="")
       row = box.row()
       if scene.thea_FMEnable:
           row = box.row()
           row.prop(scene,"thea_FMFieldDensity")
           row = box.row()
           row.prop(scene,"thea_FMCellSize")

       layout.separator()
       box = layout.box()
       row = box.row()
       row.label("Caustics")
       row.prop(scene, "thea_GICaustics", text="")
       if scene.thea_GICaustics:
           row = box.row()
           row.prop(scene,"thea_CausticLock")
           row = box.row()
           row.prop(scene,"thea_GICausticSharp")
           row = box.row()
           row.prop(scene,"thea_GICausticCaptured")
           row = box.row()
           row.prop(scene,"thea_GICausPh")
       layout.separator()
       box = layout.box()
       row = box.row()
       row.label("Biased Final Gathering")
       row.prop(scene, "thea_FGEnable", text="")
       if scene.thea_FGEnable:
           row = box.row()
           row.prop(scene,"thea_GIRays")
           row = box.row()
           row.prop(scene,"thea_FGAdaptiveSteps")
           row = box.row()
           row.prop(scene,"thea_FGEnableSecondary")
           if scene.thea_FGEnableSecondary:
               row = box.row()
               row.prop(scene,"thea_FGDistanceThreshold")
           row = box.row()
           row.prop(scene,"thea_FGDiffuseDepth")
           row = box.row()
           row.prop(scene,"thea_GITracingDepth")
           row = box.row()
           row.prop(scene,"thea_FGGlossyDepth")
           row.prop(scene,"thea_FGGlossyEvaluation")
           row = box.row()
           row.prop(scene,"thea_FGCausticEvaluation")
       layout.separator()
       box = layout.box()
       row = box.row()
       row.label("Biased Irradiance Cache")
       row = box.row()
       row.prop(scene, "thea_ICEnable", text="")
       if scene.thea_ICEnable:
           row = box.row()
           row.prop(scene,"thea_ICLock")
           row = box.row()
           row.prop(scene,"thea_ICAccuracy")
           row = box.row()
           row.prop(scene,"thea_ICMinDistance")
           row = box.row()
           row.prop(scene,"thea_ICMaxDistance")
           row.prop(scene,"thea_ICPrepass")
           row = box.row()
           row.prop(scene,"thea_ICPrepassBoost")
           row = box.row()
           row.prop(scene,"thea_ICForceInterpolation")


class RENDER_PT_IREngineSettings(RenderButtonsPanel, bpy.types.Panel):
    bl_label = "Interactive Engine Settings"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return ((getattr(context.scene, "thea_enablePresets") != True) and
                (getattr(context.scene, "thea_RenderEngineMenu") in ("Adaptive (AMC)", "Presto (MC)", "Presto (AO)"))) and (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
       layout = self.layout
       scene = context.scene
       #split = layout.split()
       #row = layout.row()
       layout.prop(scene,"thea_RTTracingDepth")
#      CHANGED > Added this to hide with MCp and AMC
       if getattr(context.scene, "thea_RenderEngineMenu") in ("Presto (AO)"):
           layout.prop(scene,"thea_RTGlossyDepth")
           layout.prop(scene,"thea_RTDiffuseDepth")
       layout.prop(scene, "thea_GICaustics", text="Caustics")
#       CHANGED > Extended only for PResto engine
       if getattr(context.scene, "thea_RenderEngineMenu") in ("Presto (AO)", "Presto (MC)"):
           layout.prop(scene, "thea_ExtendedTracing")
       if getattr(scene, 'thea_ExtendedTracing') and getattr(context.scene, "thea_RenderEngineMenu") in ("Presto (AO)", "Presto (MC)"):
           layout.prop(scene, "thea_TransparencyDepth")
           layout.prop(scene, "thea_InternalReflectionDepth")
           layout.prop(scene, "thea_SSSDepth")




class RENDER_PT_theaAO(RenderButtonsPanel, bpy.types.Panel):
    bl_label = "Ambient Occlusion"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return ((getattr(context.scene, "thea_enablePresets") != True) and
#               CHANGED > Added this to hide with MCp and AMC
               (getattr(context.scene, "thea_RenderEngineMenu") in ("Presto (AO)")))and (engine in cls.COMPAT_ENGINES)

    def draw_header(self, context):
       scene = context.scene
       self.layout.prop(scene, "thea_AOEnable", text="")

    def draw(self, context):
       layout = self.layout
       scene = context.scene
       split = layout.split()
       row = layout.row()
       col = split.column()
       if scene.thea_AOEnable:
           col.prop(scene,"thea_AOMultiply")
           col.prop(scene,"thea_AOClamp")
           col.prop(scene,"thea_AOSamples")
           col.prop(scene,"thea_AODistance")
           col.prop(scene,"thea_AOIntensity")
           col.prop(scene,"thea_AOLowColor")
           col.prop(scene,"thea_AOHighColor")



class RENDER_PT_theaSetup(RenderButtonsPanel, bpy.types.Panel):
    bl_label = "Thea Setup"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw_header(self, context):
       scene = context.scene
       mat  = context.material
       self.layout.prop(scene, "thea_showSetup", text="")

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        if getattr(scene, "thea_showSetup"):
            layout.prop(scene,"thea_LogLevel")
            layout.prop(scene,"thea_ApplicationPath")
            layout.prop(scene,"thea_DataPath")
            layout.prop(scene,"thea_IRFontSize")
            layout.label("Merge settigns:")
            layout.prop(scene,"thea_MerModels")
            layout.prop(scene,"thea_MerLights")
            layout.prop(scene,"thea_MerCameras")
            layout.prop(scene,"thea_MerEnv")
            layout.prop(scene,"thea_MerRender")
            layout.prop(scene,"thea_MerMaterials")
            layout.prop(scene,"thea_MerSurfaces")


class RENDER_PT_theaSDKSetup(RenderButtonsPanel, bpy.types.Panel):
    bl_label = "Thea Remote Setup"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw_header(self, context):
       scene = context.scene
       mat  = context.material
       self.layout.prop(scene, "thea_showRemoteSetup", text="")

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        if getattr(scene, "thea_showRemoteSetup"):
           scene = context.scene
           split = layout.split()
           row = layout.row()
           col = split.column()
           col.prop(scene,"thea_SDKPort")
           col.prop(scene,"thea_PreviewSDKPort")
           #col.prop(scene,"thea_StartTheaDelay")

class RENDER_PT_theaMergeScene(RenderButtonsPanel, bpy.types.Panel):
    bl_label = "Thea Merge Scene"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw_header(self, context):
       scene = context.scene
       mat  = context.material
       self.layout.prop(scene, "thea_showMerge", text="")

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        if getattr(scene, "thea_showMerge"):
           split = layout.split()
           row = layout.row()
           col = split.column()

           col.prop(scene,"thea_SceneMerModels")
           col.prop(scene,"thea_SceneMerLights")
           col.prop(scene,"thea_SceneMerCameras")
           col.prop(scene,"thea_SceneMerRender")
           col.prop(scene,"thea_SceneMerEnv")
           col.prop(scene,"thea_SceneMerMaterials")
           col.prop(scene,"thea_SceneMerReverseOrder")
           col.prop(scene,"thea_mergeFilePath")
           col.operator("thea.merge_file", text="Select file")



class RENDER_PT_theaChannels(RenderButtonsPanel, bpy.types.Panel):
    bl_label = "Thea Channels"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw_header(self, context):
       scene = context.scene
       mat  = context.material
       self.layout.prop(scene, "thea_showChannels", text="")

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        if getattr(scene, "thea_showChannels"):
           split = layout.split()
           row = layout.row()
           col = split.column()
           if (getattr(scene, 'thea_RenderEngineMenu') in ("Adaptive (BSD)","Unbiased (TR1)","Unbiased (TR2)","Presto (AO)","Presto (MC)","Adaptive (AMC)")):
               col.prop(scene,"thea_channelNormal")
           if (getattr(scene, 'thea_RenderEngineMenu') in ("Adaptive (BSD)","Unbiased (TR1)","Unbiased (TR2)","Presto (AO)","Presto (MC)","Adaptive (AMC)")):
               col.prop(scene,"thea_channelPosition")
           if (getattr(scene, 'thea_RenderEngineMenu') in ("Adaptive (BSD)","Unbiased (TR1)","Unbiased (TR2)","Presto (AO)","Presto (MC)","Adaptive (AMC)")):
               col.prop(scene,"thea_channelUV")
           if (getattr(scene, 'thea_RenderEngineMenu') in ("Adaptive (BSD)","Unbiased (TR1)","Unbiased (TR2)","Presto (AO)","Presto (MC)","Adaptive (AMC)")):
               col.prop(scene,"thea_channelDepth")
           if (getattr(scene, 'thea_RenderEngineMenu') in ("Adaptive (BSD)","Unbiased (TR1)","Unbiased (TR2)","Presto (AO)","Presto (MC)","Adaptive (AMC)")):
               col.prop(scene,"thea_channelAlpha")
           if (getattr(scene, 'thea_RenderEngineMenu') in ("Adaptive (BSD)","Unbiased (TR1)","Unbiased (TR2)","Presto (AO)","Presto (MC)","Adaptive (AMC)")):
               col.prop(scene,"thea_channelObjectId")
           if (getattr(scene, 'thea_RenderEngineMenu') in ("Adaptive (BSD)","Unbiased (TR1)","Unbiased (TR2)","Presto (AO)","Presto (MC)","Adaptive (AMC)")):
               col.prop(scene,"thea_channelMaterialId")
#            if (getattr(scene, 'thea_RenderEngineMenu') in ("Adaptive (BSD)","Unbiased (TR1)","Unbiased (TR2)","Presto (AO)","Presto (MC)","Adaptive (AMC)")):
#                col.prop(scene,"thea_channelMask")
           if (getattr(scene, 'thea_RenderEngineMenu') in ("Presto (AO)","Presto (MC)")):
               col.prop(scene,"thea_channelShadow")
           if (getattr(scene, 'thea_RenderEngineMenu') in ("Presto (AO)","Presto (MC)")):
               col.prop(scene,"thea_channelRawDiffuseColor")
           if (getattr(scene, 'thea_RenderEngineMenu') in ("Presto (AO)","Presto (MC)")):
               col.prop(scene,"thea_channelRawDiffuseLighting")
           if (getattr(scene, 'thea_RenderEngineMenu') in ("Presto (AO)","Presto (MC)")):
               col.prop(scene,"thea_channelRawDiffuseGI")
           if (getattr(scene, 'thea_RenderEngineMenu') in ("Adaptive (BSD)","Presto (AO)","Presto (MC)")):
               col.prop(scene,"thea_channelDirect")
           if (getattr(scene, 'thea_RenderEngineMenu') in ("Adaptive (BSD)","Presto (AO)")):
               col.prop(scene,"thea_channelAO")
           if (getattr(scene, 'thea_RenderEngineMenu') in ("Adaptive (BSD)","Presto (AO)","Presto (MC)")):
               col.prop(scene,"thea_channelGI")
           if (getattr(scene, 'thea_RenderEngineMenu') in ("Presto (AO)","Presto (MC)")):
               col.prop(scene,"thea_channelSelfIllumination")
#            if (getattr(scene, 'thea_RenderEngineMenu') in ("Presto (MC)")):
#                col.prop(scene,"thea_channelSSS")
           if (getattr(scene, 'thea_RenderEngineMenu') in ("Adaptive (BSD)","Presto (AO)","Presto (MC)")):
               col.prop(scene,"thea_channelReflection")
           if (getattr(scene, 'thea_RenderEngineMenu') in ("Adaptive (BSD)","Presto (AO)","Presto (MC)")):
               col.prop(scene,"thea_channelRefraction")
           if (getattr(scene, 'thea_RenderEngineMenu') in ("Adaptive (BSD)","Presto (AO)")):
               col.prop(scene,"thea_channelTransparent")
           if (getattr(scene, 'thea_RenderEngineMenu') in ("Adaptive (BSD)")):
               col.prop(scene,"thea_channelIrradiance")
#            if (getattr(scene, 'thea_RenderEngineMenu') in ("Presto (AO)","Presto (MC)")):
#                col.prop(scene,"thea_channelSeparatePassesPerLight")
#            if (getattr(scene, 'thea_RenderEngineMenu') in ("Adaptive (BSD)","Unbiased (TR1)","Unbiased (TR2)","Presto (AO)","Presto (MC)","Adaptive (AMC)")):
#                col.prop(scene,"thea_channelInvertMask")


class RENDER_PT_theaIBL(WorldButtonsPanel, bpy.types.Panel):
    bl_label = "Image Based Lighting"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw_header(self, context):
       scene = context.scene
       self.layout.prop(scene, "thea_IBLEnable", text="")

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        if scene.thea_IBLEnable:
           layout.prop(scene,"thea_IBLTypeMenu")
           layout.prop(scene,"thea_IBLWrappingMenu")
           layout.prop(scene,"thea_IBLFilename")
           layout.prop(scene,"thea_IBLRotation")
           layout.prop(scene,"thea_IBLIntensity")

class RENDER_PT_theaBackgroundMapping(WorldButtonsPanel, bpy.types.Panel):
    bl_label = "Background Mapping"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw_header(self, context):
       scene = context.scene
       self.layout.prop(scene, "thea_BackgroundMappingEnable", text="")

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        split = layout.split()
        row = layout.row()
        col = split.column()
        if scene.thea_BackgroundMappingEnable:
          col.prop(scene,"thea_BackgroundMappingWrappingMenu")
          col.prop(scene,"thea_BackgroundMappingFilename")
          #col.operator("thea.backgroundmapping_file", text="Select file")
          col.prop(scene,"thea_BackgroundMappingRotation")
          col.prop(scene,"thea_BackgroundMappingIntensity")

class RENDER_PT_theaReflectionMapping(WorldButtonsPanel, bpy.types.Panel):
    bl_label = "Reflection Mapping"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw_header(self, context):
       scene = context.scene
       self.layout.prop(scene, "thea_ReflectionMappingEnable", text="")

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        split = layout.split()
        row = layout.row()
        col = split.column()
        if scene.thea_ReflectionMappingEnable:
          col.prop(scene,"thea_ReflectionMappingWrappingMenu")
          col.prop(scene,"thea_ReflectionMappingFilename")
          #col.operator("thea.reflectionmapping_file", text="Select file")
          col.prop(scene,"thea_ReflectionMappingRotation")
          col.prop(scene,"thea_ReflectionMappingIntensity")

class RENDER_PT_theaRefractionMapipng(WorldButtonsPanel, bpy.types.Panel):
    bl_label = "Refraction Mapping"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw_header(self, context):
       scene = context.scene
       self.layout.prop(scene, "thea_RefractionMappingEnable", text="")

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        split = layout.split()
        row = layout.row()
        col = split.column()
        if scene.thea_RefractionMappingEnable:
           col.prop(scene,"thea_RefractionMappingWrappingMenu")
           col.prop(scene,"thea_RefractionMappingFilename")
           #col.operator("thea.refractionmapping_file", text="Select file")
           col.prop(scene,"thea_RefractionMappingRotation")
           col.prop(scene,"thea_RefractionMappingIntensity")

class RENDER_PT_theaPhysicalSky(WorldButtonsPanel, bpy.types.Panel):
    bl_label = "Thea Physical Sky"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw_header(self, context):
       scene = context.scene
       self.layout.prop(scene, "thea_EnvPSEnable", text="")

    def draw(self, context):
       layout = self.layout
       scene = context.scene
       split = layout.split()
       row = layout.row()
       col = split.column()
       if scene.thea_EnvPSEnable:
          col.prop(scene,"thea_EnvPSTurb")
          col.prop(scene,"thea_EnvPSOzone")
          col.prop(scene,"thea_EnvPSWatVap")
          col.prop(scene,"thea_EnvPSWatVap")
          col.prop(scene,"thea_EnvPSTurbCo")
          col.prop(scene,"thea_EnvPSWaveExp")

class RENDER_PT_theaLocationTime(WorldButtonsPanel, bpy.types.Panel):
    bl_label = "Thea Location/Time"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
       layout = self.layout
       scene = context.scene
       split = layout.split()
       row = layout.row()
       colL = split.column()
       #colR = split.column()
       #colR.operator("thea.update_loc", text="Update Lat/Long")
       colL.prop(scene,"thea_EnvLocationsMenu")
       split = layout.split()
       row = layout.row()
       col = split.column()
       col.prop(scene,"thea_EnvLat")
       col.prop(scene,"thea_EnvLong")
       col.prop(scene,"thea_EnvTZ")
       col.prop(scene,"thea_EnvDate")
       col.prop(scene,"thea_EnvTime")




class IMAGE_PT_thea_Display(DisplayButtonsPanel, bpy.types.Panel):
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_label = "Thea Display"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)


    def draw(self, context):
        scene = context.scene
        layout = self.layout
        layout.prop(scene,"thea_DispISO")
        layout.prop(scene,"thea_DispShutter")
        layout.prop(scene,"thea_DispFNumber")
        layout.prop(scene,"thea_DispGamma")
        layout.prop(scene,"thea_DispBrightness")
        layout.prop(scene,"thea_DispCRFMenu")
#       CHANGED > alle menus changed to active/inactive option and added the new sharpness and bloom menu items
        split = layout.split()
        row = layout.row()
        colL = split.column()
        colR = split.column()
        colL.prop(scene,"thea_DispSharpness")
        #        if getattr(scene,"thea_DispSharpness"):
        #            colR.prop(scene,"thea_DispSharpnessWeight")
        sub = colR.row()
        sub.active = scene.thea_DispSharpness == True
        sub.prop(scene, "thea_DispSharpnessWeight")
        split = layout.split()
        row = layout.row()
        colL = split.column()
        colR = split.column()
        colL.prop(scene,"thea_DispBurn")
        #        if getattr(scene,"thea_DispBurn"):
        #            colR.prop(scene,"thea_DispBurnWeight")
        sub = colR.row()
        sub.active = scene.thea_DispBurn == True
        sub.prop(scene,"thea_DispBurnWeight")
        split = layout.split()
        row = layout.row()
        colL = split.column()
        colR = split.column()
        colL.prop(scene,"thea_DispTemperature")
        #        if getattr(scene,"thea_DispTemperature"):
        #            colR.prop(scene,"thea_DispTemperatureWeight")
        sub = colR.row()
        sub.active = scene.thea_DispTemperature == True
        sub.prop(scene,"thea_DispTemperatureWeight")
        split = layout.split()
        row = layout.row()
        colL = split.column()
        colR = split.column()
        colL.prop(scene,"thea_DispContrast")
        #        if getattr(scene,"thea_DispContrast"):
        #            colR.prop(scene,"thea_DispContrastWeight")
        sub = colR.row()
        sub.active = scene.thea_DispContrast == True
        sub.prop(scene,"thea_DispContrastWeight")
        split = layout.split()
        row = layout.row()
        colL = split.column()
        colR = split.column()
        colL.prop(scene,"thea_DispVignetting")
        #        if getattr(scene,"thea_DispVignetting"):
        #            colR.prop(scene,"thea_DispVignettingWeight")
        sub = colR.row()
        sub.active = scene.thea_DispVignetting == True
        sub.prop(scene,"thea_DispVignettingWeight")
        split = layout.split()
        row = layout.row()
        colL = split.column()
        colR = split.column()
        colL.prop(scene,"thea_DispChroma")
        #        if getattr(scene,"thea_DispChroma"):
        #            colR.prop(scene,"thea_DispChromaWeight")
        sub = colR.row()
        sub.active = scene.thea_DispChroma == True
        sub.prop(scene,"thea_DispChromaWeight")
        split = layout.split()
        row = layout.row()
        colL = split.column()
        colR = split.column()
#        colL.prop(scene,"thea_DispBloom")
#        #        if getattr(scene,"thea_DispBloom"):
#        #            colR.prop(scene,"thea_DispBloomWeight")
#        #            colR.prop(scene,"thea_DispGlareRadius")
#        sub = colR.row()
#        sub.active = scene.thea_DispBloom != "0"
#        print("displayBloom: ", scene.thea_DispBloom)
#        sub.prop(scene,"thea_DispBloomWeight")
#        sub.prop(scene,"thea_DispGlareRadius")
        colL.prop(scene,"thea_DispBloom")
        #        if getattr(scene,"thea_DispBloom"):
        #            colR.prop(scene,"thea_DispBloomWeight")
        #            colR.prop(scene,"thea_DispGlareRadius")
        sub = colR.row()
        sub.active = scene.thea_DispBloom == True
        sub.prop(scene,"thea_DispBloomItems")
        split = layout.split()
        row = layout.row()
        if getattr(scene,"thea_DispBloom"):
            colR.prop(scene,"thea_DispBloomWeight")
            colR.prop(scene,"thea_DispGlareRadius")

        layout.prop(scene,"thea_DispMinZ")
        layout.prop(scene,"thea_DispMaxZ")

        row = layout.row()
        layout.operator("thea.refresh_render")

class OBJECT_PT_thea_GetMaterials(bpy.types.Operator):
    bl_idname = "thea.get_materials"
    bl_label = "Get materials"

    def invoke(self, context, event):

       scene = context.scene
       sceneMaterials = []
       sceneMaterials.append(("0","None","0"))
       i = 1
       for mat in bpy.data.materials:
           sceneMaterials.append((str(i), mat.name, str(i)))
           i += 1

       propNameIf = ""
       try:
           del scene[propNameIf]
       except:
            pass

       Scene = bpy.types.Scene

       return {'FINISHED'}


# class OBJECT_PT_thea_SetInterface(bpy.types.Operator):
#     bl_idname = "thea.set_interface"
#     bl_label = "Set interface"
#
#     def invoke(self, context, event):
#
#        scene = context.scene
#        propNameIf = "thea_Interface"
#        matInt = bpy.data.materials[scene.get(propNameIf)-1].name
#        if scene['thea_Interface'] > 0:
#            ob = bpy.context.active_object
#            bpy.types.Object.thea_MatInterface = bpy.props.StringProperty()
#            ob.thea_MatInterface=matInt
#
#
#
#        return {'FINISHED'}

class OBJECT_PT_theaMaterialInterface(ObjectButtonsPanel, bpy.types.Panel):
    bl_label = "Thea Container"
    COMPAT_ENGINES = set(['THEA_RENDER'])
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
       layout = self.layout
       obj = context.active_object

       layout.prop(obj, "thea_Container")


class OBJECT_PT_theaTools(ObjectButtonsPanel, bpy.types.Panel):
    bl_label = "Thea object settings"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
       layout = self.layout
       scene = context.scene
       split = layout.split()
       row = layout.row()
       col = split.column()


       Scene = bpy.types.Scene
       col.prop(bpy.context.active_object, "thEnabled")
       col.prop(bpy.context.active_object, "thExportAnimation")
       col.prop(bpy.context.active_object, "thVisible")
       col.prop(bpy.context.active_object, "thShadowTight")
       col.prop(bpy.context.active_object, "thShadowCaster")
       col.prop(bpy.context.active_object, "thShadowReceiver")
       col.prop(bpy.context.active_object, "thCausticsTransmitter")
       col.prop(bpy.context.active_object, "thCausticsReceiver")
       col.prop(bpy.context.active_object, "thNoRecalcNormals")



class DATA_PT_theaCamera(CameraButtonsPanel, bpy.types.Panel):
    bl_label = "Thea Camera"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES) and context.active_object.type=='CAMERA'

    def draw(self, context):
       layout = self.layout
       scene = context.scene
#       split = layout.split()
#       row = layout.row()
#       colL = split.column()
#       colR = split.column()
       object = bpy.context.active_object
       layout.prop(bpy.context.active_object, "thea_projection")
       layout.prop(bpy.context.active_object, "shutter_speed")
       split = layout.split()
       row = layout.row()
       colL = split.column()
       colR = split.column()
#       CHANGED > new menu layout and added options, pinnhole, aperture check, diaphragma and blades
#       VERSION 1 - make sit inactive and dimm
       split = layout.split()
       row.prop(bpy.context.active_object, "autofocus")
#       split = layout.split()
       row = layout.row()
       colL = split.column()
       colR = split.column()
       colL.prop(bpy.context.active_object, "thea_pinhole")
       sub = colR.row()
       sub.active = bpy.data.objects[bpy.context.active_object.name].thea_pinhole == False
#       print(bpy.data.objects[bpy.context.active_object.name].pinhole)
       sub.prop(bpy.context.active_object, "aperture")
#       VERSION 2 - HIdes the aperture
#       colR.prop(bpy.context.active_object, "pinhole")
#       if bpy.data.objects[bpy.context.active_object.name].pinhole == False:
#        colL.prop(bpy.context.active_object, "aperture")
#       colL.prop(bpy.context.active_object, "aperture")
#       colR.prop(bpy.context.active_object, "pinhole")
       split = layout.split()
       row = layout.row()
       colL = split.column()
       colR = split.column()
       colL.prop(bpy.context.active_object, "thea_diaphragma")
       if bpy.data.objects[bpy.context.active_object.name].thea_diaphragma == "Polygonal":
        colR.prop(bpy.context.active_object, "thea_diapBlades")
       split = layout.split()
       row = layout.row()
       colL = split.column()
       colR = split.column()
#      CHANGED > Made active/inactive option
       colL.prop(bpy.context.active_object, "thea_zClippingNear")
       sub = colL.row()
       sub.active = bpy.data.objects[bpy.context.active_object.name].thea_zClippingNear == True
       sub.prop(bpy.data.cameras[bpy.context.active_object.name], "clip_start")
#       if getattr(bpy.context.active_object, "thea_zClippingNear"):
#        colL.prop(bpy.data.cameras[bpy.context.active_object.name], "clip_start")
       row = layout.row()
       colR.prop(bpy.context.active_object, "thea_zClippingFar")
       sub = colR.row()
       sub.active = bpy.data.objects[bpy.context.active_object.name].thea_zClippingFar == True
       sub.prop(bpy.data.cameras[bpy.context.active_object.name], "clip_end")
#       if getattr(bpy.context.active_object, "thea_zClippingFar"):
#        colR.prop(bpy.data.cameras[bpy.context.active_object.name], "clip_end")
#       split = layout.split()
#       row = layout.row()
#       colL = split.column()
#       colR = split.column()
#       colL.prop(bpy.context.active_object, "thea_zClippingNear")
#       if getattr(bpy.context.active_object, "thea_zClippingNear"):
#        colR.prop(bpy.data.cameras[bpy.context.active_object.name], "clip_start")
#       colL.prop(bpy.context.active_object, "thea_zClippingFar")
#       if getattr(bpy.context.active_object, "thea_zClippingFar"):
#        colR.prop(bpy.data.cameras[bpy.context.active_object.name], "clip_end")



class PARTICLE_PT_Thea(ParticleButtonsPanel, bpy.types.Panel):
    bl_label = "Thea"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES) and (context.particle_system is not None)

    def draw(self, context):
       layout = self.layout
       scene = context.scene
       psys = context.particle_system
       part = psys.settings
       split = layout.split()
       row = layout.row()
       split = layout.split()
       row = layout.row()
       col = split.column()
       col.prop(part,"thea_ApplyModifier")


class DataButtonsPanel():
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return context.lamp and (engine in cls.COMPAT_ENGINES)


class DATA_PT_thea_context_lamp(DataButtonsPanel, Panel):
    bl_label = ""
    bl_options = {'HIDE_HEADER'}
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
        layout = self.layout

        ob = context.object
        lamp = context.lamp
        space = context.space_data

        split = layout.split(percentage=0.65)
        if(lamp is not None):

            texture_count = len(lamp.texture_slots.keys())

            if ob:
                split.template_ID(ob, "data")
            elif lamp:
                split.template_ID(space, "pin_id")

            if texture_count != 0:
                split.label(text=str(texture_count), icon='TEXTURE')



class DATA_PT_thea_lamp(DataButtonsPanel, Panel):
    bl_label = "Lamp"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
        layout = self.layout

        lamp = context.lamp
        if(lamp is not None):

            #layout.operator('thea.refresh_lamp', "Refresh lamp data", icon="FILE_REFRESH")
            layout.prop(lamp, "type", expand=True)

            layout.prop(lamp, "thea_enableLamp")
            layout.prop(lamp, "thea_enableShadow")
            row = layout.row()
            row.prop(lamp, "thea_enableSoftShadow")
            if getattr(lamp, "thea_enableSoftShadow"):
                row.prop(lamp, "thea_softRadius")
                if lamp.type == "SUN":
                    layout.prop(lamp, "thea_radiusMultiplier", text="Radius Multiplier")
            row = layout.row()
            layout.prop(lamp, "thea_minRays")
            layout.prop(lamp, "thea_maxRays")
            layout.prop(lamp, "thea_globalPhotons")
            layout.prop(lamp, "thea_causticPhotons")
            layout.prop(lamp, "thea_bufferIndex")



class DATA_PT_thea_Emittance(DataButtonsPanel, Panel):
    bl_label = "Emittance"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return (engine in cls.COMPAT_ENGINES)

    def draw(self, context):

        layout = self.layout
        lamp = context.lamp
        row = layout.row()
        if(lamp is not None):
            if (lamp.thea_TextureFilename==""):
                row.prop(lamp, "color", text="")
            row.prop(lamp, "thea_TextureFilename")


            split = layout.split()
            col = split.column()
            sub = col.column()
            sub.prop(lamp, "energy")
            if lamp.type == 'SUN':
                sub.prop(lamp, "thea_SunEmittanceUnit")
            else:
                sub.prop(lamp, "thea_EmittanceUnit")

            if lamp.type in {'SPOT'}:
                sub.prop(lamp, "thea_IESFilename")

            if lamp.type in {'POINT', 'SPOT', 'AREA'}:
                sub.label(text="Attenuation:")
                sub.prop(lamp, "falloff_type", text="")
                #sub.prop(lamp, "distance")

    #             if lamp.falloff_type == 'LINEAR_QUADRATIC_WEIGHTED':
    #                 col.label(text="Attenuation Factors:")
    #                 sub = col.column(align=True)
    #                 sub.prop(lamp, "linear_attenuation", slider=True, text="Linear")
    #                 sub.prop(lamp, "quadratic_attenuation", slider=True, text="Quadratic")

                #col.prop(lamp, "use_sphere")

            if lamp.type == 'AREA':
                col.prop(lamp, "distance")
                col.prop(lamp, "gamma")







class DATA_PT_thea_shadow(DataButtonsPanel, Panel):
    bl_label = "Shadow"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        lamp = context.lamp
        engine = context.scene.render.engine
        #return (lamp and lamp.type in {'POINT', 'SUN', 'SPOT', 'AREA'}) and (engine in cls.COMPAT_ENGINES)
        return False

    def draw(self, context):
        layout = self.layout

        lamp = context.lamp

        layout.prop(lamp, "shadow_method", expand=True)

        if lamp.shadow_method == 'NOSHADOW' and lamp.type == 'AREA':
            split = layout.split()

            col = split.column()
            col.label(text="Form factor sampling:")

            sub = col.row(align=True)

            if lamp.shape == 'SQUARE':
                sub.prop(lamp, "shadow_ray_samples_x", text="Samples")
            elif lamp.shape == 'RECTANGLE':
                sub.prop(lamp, "shadow_ray_samples_x", text="Samples X")
                sub.prop(lamp, "shadow_ray_samples_y", text="Samples Y")

        if lamp.shadow_method != 'NOSHADOW':
            split = layout.split()

            col = split.column()
            col.prop(lamp, "shadow_color", text="")

            col = split.column()
            col.prop(lamp, "use_shadow_layer", text="This Layer Only")
            col.prop(lamp, "use_only_shadow")

        if lamp.shadow_method == 'RAY_SHADOW':
            split = layout.split()

            col = split.column()
            col.label(text="Sampling:")

            if lamp.type in {'POINT', 'SUN', 'SPOT'}:
                sub = col.row()

                sub.prop(lamp, "shadow_ray_samples", text="Samples")
                sub.prop(lamp, "shadow_soft_size", text="Soft Size")

            elif lamp.type == 'AREA':
                sub = col.row(align=True)

                if lamp.shape == 'SQUARE':
                    sub.prop(lamp, "shadow_ray_samples_x", text="Samples")
                elif lamp.shape == 'RECTANGLE':
                    sub.prop(lamp, "shadow_ray_samples_x", text="Samples X")
                    sub.prop(lamp, "shadow_ray_samples_y", text="Samples Y")

            col.row().prop(lamp, "shadow_ray_sample_method", expand=True)

            if lamp.shadow_ray_sample_method == 'ADAPTIVE_QMC':
                layout.prop(lamp, "shadow_adaptive_threshold", text="Threshold")

            if lamp.type == 'AREA' and lamp.shadow_ray_sample_method == 'CONSTANT_JITTERED':
                row = layout.row()
                row.prop(lamp, "use_umbra")
                row.prop(lamp, "use_dither")
                row.prop(lamp, "use_jitter")

        elif lamp.shadow_method == 'BUFFER_SHADOW':
            col = layout.column()
            col.label(text="Buffer Type:")
            col.row().prop(lamp, "shadow_buffer_type", expand=True)

            if lamp.shadow_buffer_type in {'REGULAR', 'HALFWAY', 'DEEP'}:
                split = layout.split()

                col = split.column()
                col.label(text="Filter Type:")
                col.prop(lamp, "shadow_filter_type", text="")
                sub = col.column(align=True)
                sub.prop(lamp, "shadow_buffer_soft", text="Soft")
                sub.prop(lamp, "shadow_buffer_bias", text="Bias")

                col = split.column()
                col.label(text="Sample Buffers:")
                col.prop(lamp, "shadow_sample_buffers", text="")
                sub = col.column(align=True)
                sub.prop(lamp, "shadow_buffer_size", text="Size")
                sub.prop(lamp, "shadow_buffer_samples", text="Samples")
                if lamp.shadow_buffer_type == 'DEEP':
                    col.prop(lamp, "compression_threshold")

            elif lamp.shadow_buffer_type == 'IRREGULAR':
                layout.prop(lamp, "shadow_buffer_bias", text="Bias")

            split = layout.split()

            col = split.column()
            col.prop(lamp, "use_auto_clip_start", text="Autoclip Start")
            sub = col.column()
            sub.active = not lamp.use_auto_clip_start
            sub.prop(lamp, "shadow_buffer_clip_start", text="Clip Start")

            col = split.column()
            col.prop(lamp, "use_auto_clip_end", text="Autoclip End")
            sub = col.column()
            sub.active = not lamp.use_auto_clip_end
            sub.prop(lamp, "shadow_buffer_clip_end", text=" Clip End")


class DATA_PT_thea_area(DataButtonsPanel, Panel):
    bl_label = "Area Shape"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        lamp = context.lamp
        engine = context.scene.render.engine
        return (lamp and lamp.type == 'AREA') and (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
        layout = self.layout

        lamp = context.lamp

        col = layout.column()
        col.row().prop(lamp, "shape", expand=True)
        sub = col.row(align=True)

        if lamp.shape == 'SQUARE':
            sub.prop(lamp, "size")
        elif lamp.shape == 'RECTANGLE':
            sub.prop(lamp, "size", text="Size X")
            sub.prop(lamp, "size_y", text="Size Y")


class DATA_PT_thea_spot(DataButtonsPanel, Panel):
    bl_label = "Spot Shape"
    COMPAT_ENGINES = set(['THEA_RENDER'])

    @classmethod
    def poll(cls, context):
        lamp = context.lamp
        engine = context.scene.render.engine
        return (lamp and lamp.type == 'SPOT') and (engine in cls.COMPAT_ENGINES)

    def draw(self, context):
        layout = self.layout

        lamp = context.lamp

        split = layout.split()

        col = split.column()
        sub = col.column()
        sub.prop(lamp, "spot_size", text="Size")
        sub.prop(lamp, "spot_blend", text="Blend", slider=True)
        col.prop(lamp, "use_square")
        col.prop(lamp, "show_cone")

        col = split.column()

        col.prop(lamp, "use_halo")
        sub = col.column(align=True)
        sub.active = lamp.use_halo
        sub.prop(lamp, "halo_intensity", text="Intensity")
        if lamp.shadow_method == 'BUFFER_SHADOW':
            sub.prop(lamp, "halo_step", text="Step")

            
