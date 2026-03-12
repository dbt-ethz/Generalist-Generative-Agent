# Created for 0012_0002_twisted_volumes.json

""" Summary:
The function `create_twisted_volumes_grid` generates an architectural concept model by creating a grid of twisted modules that embody the metaphor of "Twisted volumes." Each module is twisted around a central axis at varying angles, fostering a sense of movement and tension. The function introduces height variations to enhance spatial dynamics, resulting in overlapping and intersecting spaces that encourage exploration. By manipulating the geometry's solid and void elements, the design emphasizes light and shadow interplay, reflecting the transformative qualities of the metaphor. Ultimately, this approach creates a visually complex and engaging architectural form that captures the essence of fluidity and innovation."""

#! python 3
function_code = """def create_twisted_volumes_grid(twist_angle=30, module_size=5, grid_size=(3, 3), height_variation=2):
    \"""
    Generates a grid of twisted volumes to form an architectural Concept Model based on the 'Twisted volumes' metaphor.
    It creates a sense of movement and tension by varying the twist angle and module heights within a grid layout,
    emphasizing the dynamic interplay of spatial relationships.

    Parameters:
    - twist_angle (float): The angle in degrees by which each module is twisted around its central axis.
    - module_size (float): The size of each module in meters (assumes a cubic form for simplicity).
    - grid_size (tuple): A tuple representing the number of modules in the grid (rows, columns).
    - height_variation (float): The variation in height for each module to introduce dynamic spatial relationships.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the twisted volumes.
    \"""
    import Rhino.Geometry as rg
    import random
    from math import radians

    # Set random seed for replicability
    random.seed(42)

    # List to store the resulting Breps
    breps = []

    # Base plane for the first module
    base_plane = rg.Plane.WorldXY

    for r in range(grid_size[0]):
        for c in range(grid_size[1]):
            # Create a box as the base geometry for the module
            height = module_size + random.uniform(-height_variation, height_variation)
            box_corners = [
                rg.Point3d(0, 0, 0),
                rg.Point3d(module_size, 0, 0),
                rg.Point3d(module_size, module_size, 0),
                rg.Point3d(0, module_size, 0),
                rg.Point3d(0, 0, height),
                rg.Point3d(module_size, 0, height),
                rg.Point3d(module_size, module_size, height),
                rg.Point3d(0, module_size, height)
            ]
            box = rg.Brep.CreateFromBox(box_corners)

            # Determine the twist transformation
            angle_rad = radians(twist_angle)
            twist_axis = rg.Line(base_plane.Origin, base_plane.Origin + rg.Vector3d(0, 0, height))
            twist_transform = rg.Transform.Rotation(angle_rad, twist_axis.Direction, twist_axis.From)

            # Apply the twist transformation to the box
            twisted_box = box.Duplicate()
            twisted_box.Transform(twist_transform)

            # Translate the twisted box to its position in the grid
            translation = rg.Transform.Translation(rg.Vector3d(c * module_size, r * module_size, 0))
            twisted_box.Transform(translation)

            # Add the twisted box to the list of Breps
            breps.append(twisted_box)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_grid(twist_angle=45, module_size=4, grid_size=(5, 5), height_variation=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_grid(twist_angle=60, module_size=6, grid_size=(4, 4), height_variation=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_grid(twist_angle=15, module_size=3, grid_size=(2, 6), height_variation=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_grid(twist_angle=90, module_size=7, grid_size=(3, 2), height_variation=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_grid(twist_angle=75, module_size=8, grid_size=(2, 3), height_variation=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
