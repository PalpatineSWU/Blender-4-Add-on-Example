import bpy

class ExamplePanel(bpy.types.Panel):
    bl_label = "Example Scripts"
    bl_idname = "OBJECT_PT_Example_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Example"

    def draw(self, context):
        layout = self.layout

        layout.operator("example.create_cube", text="Create Cube")
        layout.operator("example.create_sphere", text="Create Sphere")
