# Created for 0010_0002_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes_model` generates an architectural concept model by creating a series of angular, folded geometries that embody the essence of the "Mirrored folded planes" metaphor. Each fold is strategically designed to introduce dynamic movement and visual tension, while being mirrored across specified axes to enhance symmetry and coherence. By adjusting parameters like fold height, distance, and count, the model captures intricate spatial narratives that encourage exploration. The output consists of Brep geometries representing the concept model, reflecting the interplay of light and form, and inviting engagement with layered architectural spaces."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(fold_height, fold_distance, fold_count, mirror_axis):
    \"""
    Generates an architectural Concept Model inspired by the 'Mirrored folded planes' metaphor.
    This model uses a series of interconnected, folded geometries that are strategically mirrored
    to create a dynamic and cohesive architectural form. The interplay of folds and mirrored 
    elements evokes visual movement and tension, encouraging spatial exploration.

    Parameters:
    - fold_height (float): The maximum height of the folded elements in meters.
    - fold_distance (float): The distance between consecutive folds in meters.
    - fold_count (int): The number of folds to generate.
    - mirror_axis (str): The axis along which the model will be mirrored ('x', 'y', or 'z').

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Create a list to hold the folded geometries
    geometries = []

    # Define the base plane for folds
    base_plane = rg.Plane.WorldXY

    # Calculate an angular offset for the folds to create a sense of movement
    angle_offset = math.pi / (fold_count * 2)

    # Generate the folded elements
    for i in range(fold_count):
        # Calculate the angle for the current fold
        angle = angle_offset * i

        # Generate the fold as a triangle for simplicity
        base_point = rg.Point3d(i * fold_distance, 0, 0)
        apex_point = rg.Point3d(base_point.X + fold_distance / 2, fold_height, 0)
        end_point = rg.Point3d(base_point.X + fold_distance, 0, 0)

        # Create the folded plane as a Brep
        fold_brep = rg.Brep.CreateFromCornerPoints(base_point, apex_point, end_point, 0.01)
        geometries.append(fold_brep)

    # Mirroring logic based on the specified axis
    mirror_plane = None
    if mirror_axis == 'x':
        mirror_plane = rg.Plane.WorldYZ
    elif mirror_axis == 'y':
        mirror_plane = rg.Plane.WorldZX
    elif mirror_axis == 'z':
        mirror_plane = rg.Plane.WorldXY
    else:
        raise ValueError("Invalid mirror axis. Use 'x', 'y', or 'z'.")

    # Create mirrored geometries
    mirrored_geometries = []
    for geom in geometries:
        mirrored_geom = geom.Duplicate()
        mirrored_geom.Transform(rg.Transform.Mirror(mirror_plane))
        mirrored_geometries.append(mirrored_geom)

    # Combine all geometries
    complete_geometries = geometries + mirrored_geometries

    return complete_geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(3.0, 2.0, 5, 'y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(2.5, 1.5, 7, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(4.0, 3.0, 6, 'z')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(1.5, 2.5, 4, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(2.0, 3.0, 8, 'z')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
