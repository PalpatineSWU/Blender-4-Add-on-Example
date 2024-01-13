import bpy

class CreateSphereOperator(bpy.types.Operator):
    bl_idname = "example.create_sphere"
    bl_label = "Create Sphere"
    bl_description = "Adds a sphere to the scene"

    def execute(self, context):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=1)  # Adjust radius as needed
        return {'FINISHED'}
