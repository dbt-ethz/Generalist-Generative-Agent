# Created for 0010_0001_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes_model` generates an architectural concept model by implementing the metaphor of "Mirrored folded planes." It creates a series of angular, folded surfaces arranged symmetrically around a central axis to evoke movement and depth. The model's design incorporates a specified fold angle and the number of folds, generating intricate geometries that reflect a balance of complexity and coherence. By mirroring these surfaces across a central axis, the function emphasizes reflective symmetry, enhancing the interplay of light and shadow. Ultimately, the model embodies the metaphor's essence, inviting exploration of its layered spatial organization."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(width, height, depth, fold_angle, num_folds):
    \"""
    Creates an architectural Concept Model embodying the 'Mirrored folded planes' metaphor,
    using angular, folded surfaces arranged symmetrically around a central axis.

    Parameters:
    width (float): The width of the model, in meters.
    height (float): The height of the model, in meters.
    depth (float): The depth of the model, in meters.
    fold_angle (float): The angle in degrees at which the planes are folded.
    num_folds (int): The number of folds to create on each side of the central axis.

    Returns:
    list: A list of RhinoCommon Brep objects representing the 3D geometries of the model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Create a list to hold the resulting Breps
    breps = []

    # Calculate the fold increment
    fold_increment = width / (num_folds + 1)

    # Create folded planes on one side
    for i in range(num_folds):
        # Calculate the base points for the fold
        base_point1 = rg.Point3d(i * fold_increment, 0, 0)
        base_point2 = rg.Point3d((i + 1) * fold_increment, 0, 0)
        top_point = rg.Point3d((i + 0.5) * fold_increment, depth * math.tan(math.radians(fold_angle)), height)

        # Create the fold as a surface
        fold_points = [base_point1, base_point2, top_point]
        fold_surface = rg.Brep.CreateFromCornerPoints(base_point1, base_point2, top_point, 0.001)

        if fold_surface:
            breps.append(fold_surface)

    # Mirror the folds across a central axis
    mirror_plane = rg.Plane.WorldYZ
    mirrored_breps = [brep.DuplicateBrep() for brep in breps]

    for brep in mirrored_breps:
        brep.Transform(rg.Transform.Mirror(mirror_plane))
        breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(10.0, 5.0, 2.0, 30.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(15.0, 8.0, 3.0, 45.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(12.0, 6.0, 4.0, 60.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(20.0, 10.0, 5.0, 15.0, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(8.0, 4.0, 3.0, 20.0, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
