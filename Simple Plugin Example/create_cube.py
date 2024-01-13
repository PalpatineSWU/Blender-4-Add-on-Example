import bpy

class CreateCubeOperator(bpy.types.Operator):
    bl_idname = "example.create_cube"
    bl_label = "Create Cube"
    bl_description = "Adds a cube to the scene"

    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add(size=2)  # Adjust size as needed
        return {'FINISHED'}
