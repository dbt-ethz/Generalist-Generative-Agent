# Created for 0010_0005_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes_model` generates an architectural concept model based on the metaphor "Mirrored folded planes" by creating a series of interlocked, angular forms. It starts by defining a base plane and applies a specified folding angle to create dynamic, angular surfaces that suggest movement. The function then mirrors these folded planes across a chosen axis, enhancing the visual complexity and reflective symmetry. By interlocking these geometries, the model achieves a rhythmic interplay of light and shadow, embodying the metaphor's essence of coherent complexity and inviting exploration of its layered spatial experience."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(base_length, base_height, fold_angle, mirror_axis, seed=None):
    \"""
    Creates a Concept Model for the architectural metaphor 'Mirrored folded planes'.
    The model consists of interlocked, angular forms that reflect across multiple axes,
    creating a dynamic equilibrium with rhythmic interplay of light and shadow.

    Parameters:
    - base_length (float): The length of the base plane in meters.
    - base_height (float): The height of the folded planes in meters.
    - fold_angle (float): The angle at which the planes are folded in degrees.
    - mirror_axis (str): The axis ('X', 'Y', or 'Z') along which the planes are mirrored.
    - seed (int, optional): Seed for randomness to ensure replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries.
    \"""

    import Rhino
    import Rhino.Geometry as rg
    import math
    import random

    if seed is not None:
        random.seed(seed)

    # Create the base plane
    base_plane = rg.Plane.WorldXY
    base_rect_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(base_length, 0, 0),
        rg.Point3d(base_length, base_length, 0),
        rg.Point3d(0, base_length, 0)
    ]
    base_surface = rg.Brep.CreateFromCornerPoints(base_rect_corners[0], base_rect_corners[1],
                                                  base_rect_corners[2], base_rect_corners[3], 0.01)

    # Fold the plane
    fold_vector = rg.Vector3d(0, 0, base_height)
    axis_vector = rg.Vector3d(base_length / 2, 0, 0)
    axis = rg.Line(base_rect_corners[0], axis_vector)
    fold_angle_rad = math.radians(fold_angle)

    fold_transform = rg.Transform.Rotation(fold_angle_rad, axis.Direction, base_rect_corners[0])
    folded_surface = base_surface.Duplicate()
    folded_surface.Transform(fold_transform)

    # Mirror the folded plane
    if mirror_axis == 'X':
        mirror_plane = rg.Plane.WorldYZ
    elif mirror_axis == 'Y':
        mirror_plane = rg.Plane.WorldZX
    else:
        mirror_plane = rg.Plane.WorldXY

    mirrored_surface = folded_surface.Duplicate()
    mirror_transform = rg.Transform.Mirror(mirror_plane)
    mirrored_surface.Transform(mirror_transform)

    # Interlock the geometries
    interlock_transform = rg.Transform.Translation(0, base_length / 2, 0)
    folded_surface.Transform(interlock_transform)
    mirrored_surface.Transform(interlock_transform)

    # Return the list of Brep objects
    return [base_surface, folded_surface, mirrored_surface]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(10.0, 5.0, 30.0, 'Y', seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(8.0, 4.0, 45.0, 'X')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(12.0, 6.0, 60.0, 'Z', seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(15.0, 7.5, 75.0, 'X', seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(20.0, 10.0, 90.0, 'Y', seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
