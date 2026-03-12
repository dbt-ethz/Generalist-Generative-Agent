# Created for 0010_0005_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes_model` generates an architectural concept model by translating the metaphor of "Mirrored folded planes" into a 3D geometric representation. It creates a base plane and applies a specified fold angle to introduce angular surfaces, evoking movement and complexity. The function then mirrors this folded plane across designated axes, enhancing the visual symmetry and depth. This interplay of folded and mirrored elements forms a cohesive yet intricate design. The resulting model emphasizes the rhythmic interaction of light and shadow, inviting exploration of the interconnected spaces and their dynamic equilibrium, aligned with the design task's goals."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(base_length, base_width, height, fold_angle, mirror_axis, seed=None):
    \"""
    Generate an architectural Concept Model using the 'Mirrored folded planes' metaphor.
    
    The function creates a configuration of interlocked, angular forms that reflect across specified axes.
    It uses folded planes and mirroring to achieve dynamic equilibrium, emphasizing the rhythmic interplay of light and shadow.

    Parameters:
    - base_length (float): The length of the base plane in meters.
    - base_width (float): The width of the base plane in meters.
    - height (float): The height of the folded planes in meters.
    - fold_angle (float): The angle at which the planes are folded, in degrees.
    - mirror_axis (str): The axis across which the planes are mirrored ('X', 'Y', or 'Z').
    - seed (int, optional): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    if seed is not None:
        random.seed(seed)

    # Create initial base plane
    base_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(base_length, 0, 0),
        rg.Point3d(base_length, base_width, 0),
        rg.Point3d(0, base_width, 0)
    ]
    base_plane = rg.Brep.CreateFromCornerPoints(base_corners[0], base_corners[1], base_corners[2], base_corners[3], 0.01)

    # Fold the plane
    fold_angle_rad = math.radians(fold_angle)
    fold_vector = rg.Vector3d(0, 0, height)
    axis_vector = rg.Vector3d(base_length / 2, 0, 0)
    fold_axis = rg.Line(base_corners[0], axis_vector)
    fold_transform = rg.Transform.Rotation(fold_angle_rad, fold_axis.Direction, base_corners[0])
    folded_plane = base_plane.Duplicate()
    folded_plane.Transform(fold_transform)

    # Mirror the folded plane
    if mirror_axis.upper() == 'X':
        mirror_plane = rg.Plane.WorldYZ
    elif mirror_axis.upper() == 'Y':
        mirror_plane = rg.Plane.WorldZX
    else:
        mirror_plane = rg.Plane.WorldXY

    mirrored_plane = folded_plane.Duplicate()
    mirror_transform = rg.Transform.Mirror(mirror_plane)
    mirrored_plane.Transform(mirror_transform)

    # Create additional interlocking by translating the mirrored plane
    interlock_transform = rg.Transform.Translation(base_length / 2, base_width / 2, 0)
    folded_plane.Transform(interlock_transform)
    mirrored_plane.Transform(interlock_transform)

    # Return the list of Brep objects representing the folded and mirrored planes
    return [base_plane, folded_plane, mirrored_plane]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(10.0, 5.0, 3.0, 45.0, 'Y', seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(8.0, 4.0, 2.5, 30.0, 'X')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(12.0, 6.0, 4.0, 60.0, 'Z', seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(15.0, 7.0, 5.0, 90.0, 'X', seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(9.0, 3.5, 2.0, 75.0, 'Y', seed=101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
