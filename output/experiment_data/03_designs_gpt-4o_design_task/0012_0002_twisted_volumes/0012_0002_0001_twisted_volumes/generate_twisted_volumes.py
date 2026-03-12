# Created for 0012_0002_twisted_volumes.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "Twisted volumes." By creating a series of interlocking modules that twist around a central axis, it embodies the dynamic and fluid characteristics described in the metaphor. Each module's twist angle, height, width, and length can be customized to enhance spatial interactions and encourage exploration. The function emphasizes the contrast between solid and void, facilitating light and shadow play, which highlights various moods throughout the day. Overall, it captures the transformative essence of the metaphor, resulting in a visually complex and coherent architectural model."""

#! python 3
function_code = """def generate_twisted_volumes(twist_angle=45, module_height=3, module_width=5, module_length=10, num_modules=5):
    \"""
    Generates a series of interlocking twisted volumes to form an architectural Concept Model.

    The function creates modules that twist around a central axis, creating dynamic spatial interactions
    and a play of light and shadow. The twisting introduces overlapping spaces and encourages exploration.

    Parameters:
    - twist_angle (float): The angle in degrees by which each module is twisted around its central axis.
    - module_height (float): The height of each module in meters.
    - module_width (float): The width of each module in meters.
    - module_length (float): The length of each module in meters.
    - num_modules (int): The number of modules to generate.

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

    for i in range(num_modules):
        # Create a box as the base geometry for the module
        box_corners = [
            rg.Point3d(0, 0, 0),
            rg.Point3d(module_length, 0, 0),
            rg.Point3d(module_length, module_width, 0),
            rg.Point3d(0, module_width, 0),
            rg.Point3d(0, 0, module_height),
            rg.Point3d(module_length, 0, module_height),
            rg.Point3d(module_length, module_width, module_height),
            rg.Point3d(0, module_width, module_height)
        ]
        box = rg.Brep.CreateFromBox(box_corners)

        # Determine the twist transformation
        angle_rad = radians(twist_angle * (i + 1))
        twist_axis = rg.Line(base_plane.Origin, base_plane.Origin + rg.Vector3d(0, 0, module_height))
        twist_transform = rg.Transform.Rotation(angle_rad, twist_axis.Direction, twist_axis.From)

        # Apply the twist transformation to the box
        twisted_box = box.Duplicate()
        twisted_box.Transform(twist_transform)

        # Add the twisted box to the list of Breps
        breps.append(twisted_box)

        # Update the base plane for the next module
        base_plane = rg.Plane(base_plane.Origin + rg.Vector3d(0, 0, module_height), rg.Vector3d.ZAxis)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_twisted_volumes(twist_angle=60, module_height=4, module_width=6, module_length=12, num_modules=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_twisted_volumes(twist_angle=30, module_height=2, module_width=4, module_length=8, num_modules=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_twisted_volumes(twist_angle=90, module_height=5, module_width=7, module_length=15, num_modules=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_twisted_volumes(twist_angle=75, module_height=3.5, module_width=5.5, module_length=11, num_modules=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_twisted_volumes(twist_angle=45, module_height=2.5, module_width=5, module_length=9, num_modules=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
