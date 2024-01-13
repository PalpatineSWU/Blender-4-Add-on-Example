bl_info = {
    "name": "Example Addon",
    "author": "Vortex",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > Example",
    "description": "Activates scripts from external Python files",
    "category": "Development"
}

import bpy
from . import operators
from . import create_cube
from . import create_sphere

classes = (
    operators.ExamplePanel,
    create_cube.CreateCubeOperator,  # Register the Create Cube operator
    create_sphere.CreateSphereOperator,  # Register the Create Sphere operator
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
