# Created for 0010_0004_mirrored_folded_planes.json

""" Summary:
The provided function, `create_mirrored_folded_planes_model`, generates an architectural concept model by interpreting the metaphor of "Mirrored folded planes." It creates a series of angular, folded surfaces that exhibit bilateral symmetry, reflecting the metaphor's emphasis on complexity and harmony. The function allows for customizable parameters, such as base dimensions, height, number of folds, and symmetry axis, enabling dynamic variations in geometry. By extruding and mirroring the folded planes, it fosters a sense of depth and movement, while the spatial organization embodies layered reflections, promoting exploration and discovery within the architectural model."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(base_length=10, base_width=5, height=8, folds=3, symmetry_axis='y'):
    \"""
    Create an architectural Concept Model based on the 'Mirrored folded planes' metaphor.
    
    This function generates a series of angular, folded surfaces that exhibit bilateral symmetry. 
    The concept is to create a dynamic interplay of solid and void, light and shadow, with a cascading 
    organization of spaces that reflect each other, embodying a sense of progression and discovery.

    Parameters:
    - base_length (float): The length of the base plane in meters.
    - base_width (float): The width of the base plane in meters.
    - height (float): The height of the structure in meters.
    - folds (int): The number of folds in the plane.
    - symmetry_axis (str): The axis along which the structure will be mirrored ('x' or 'y').

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a seed for reproducibility
    random.seed(42)

    # Helper function to create a folded plane
    def create_folded_plane(base_length, base_width, height, folds):
        points = []
        for i in range(folds + 1):
            x = (i / folds) * base_length
            z = (i % 2) * height
            points.append(rg.Point3d(x, 0, z))
            points.append(rg.Point3d(x, base_width, z))
        # Create polyline and extrude it to form a surface
        polyline = rg.Polyline(points)
        curve = polyline.ToNurbsCurve()
        extrusion = rg.Extrusion.Create(curve, height, True)
        return extrusion.ToBrep() if extrusion else None

    # Create the initial folded plane
    folded_plane = create_folded_plane(base_length, base_width, height, folds)

    # Check if folded_plane is None
    if folded_plane is None:
        return []

    # Mirror the folded plane
    mirrored_planes = []
    transform_axis = rg.Plane.WorldXY
    if symmetry_axis == 'x':
        transform_axis = rg.Plane.WorldZX
    elif symmetry_axis == 'y':
        transform_axis = rg.Plane.WorldXY

    mirrored_planes.append(folded_plane)
    mirrored_planes.append(folded_plane.DuplicateBrep())
    for brep in mirrored_planes:
        brep.Transform(rg.Transform.Mirror(transform_axis))

    # Return the initial and mirrored folded planes
    return mirrored_planes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(base_length=12, base_width=6, height=10, folds=4, symmetry_axis='x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(base_length=15, base_width=7, height=9, folds=5, symmetry_axis='y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(base_length=8, base_width=4, height=6, folds=2, symmetry_axis='x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(base_length=20, base_width=10, height=12, folds=6, symmetry_axis='y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(base_length=14, base_width=7, height=11, folds=3, symmetry_axis='x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
