# Created for 0010_0001_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes_model` generates an architectural concept model based on the metaphor of "Mirrored folded planes." It constructs a series of angular, folded surfaces that are symmetrically arranged around a central axis, embodying dynamic movement and depth. By introducing random variations in the folds, the model enhances visual complexity while maintaining coherence through reflective symmetry. Mirroring these geometries creates a rhythm of interconnected spaces that echo across the central axis, emphasizing the interplay of light and shadow. This approach invites exploration of layered geometries, aligning with the metaphor's key traits of symmetry and complexity."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(central_axis_length=12.0, plane_height=3.0, plane_depth=2.0, num_planes=4, fold_variation=1.0):
    \"""
    Create an Architectural Concept Model embodying the 'Mirrored folded planes' metaphor.

    This function generates a series of angular, folded surfaces arranged symmetrically around a central axis,
    demonstrating movement and depth through the interplay of shadows and reflections. The model features a
    mirrored organization with interconnected spaces that repeat across a central spine.

    Parameters:
    - central_axis_length (float): The length of the central axis about which the planes are mirrored (in meters).
    - plane_height (float): The height of each folded plane (in meters).
    - plane_depth (float): The depth of each folded plane (in meters).
    - num_planes (int): The number of planes on each side of the central axis.
    - fold_variation (float): Variation in fold angle to introduce randomness (in meters).

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the folded planes.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(42)  # Ensure the randomness is replicable

    geometries = []
    central_axis = rg.Line(rg.Point3d(0, 0, 0), rg.Point3d(central_axis_length, 0, 0))

    # Create folded planes on one side of the central axis
    for i in range(num_planes):
        # Define the base of the fold
        start_point = rg.Point3d(i * (central_axis_length / num_planes), 0, 0)
        end_point = rg.Point3d((i + 1) * (central_axis_length / num_planes), 0, 0)

        # Random variation in fold
        random_fold = random.uniform(-fold_variation, fold_variation)

        # Define the peak of the fold
        peak_point = rg.Point3d((start_point.X + end_point.X) / 2, plane_depth + random_fold, plane_height)

        # Create the folded surface as a Brep
        fold_curve1 = rg.PolylineCurve([start_point, peak_point, end_point, start_point])
        loft = rg.Brep.CreateFromLoft([fold_curve1], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        if loft:
            geometries.append(loft[0])

    # Mirror the geometries to the other side of the central axis
    mirror_plane = rg.Plane(rg.Point3d(central_axis_length / 2, 0, 0), rg.Vector3d(1, 0, 0))
    mirrored_geometries = [geo.DuplicateBrep().Transform(rg.Transform.Mirror(mirror_plane)) for geo in geometries]
    geometries.extend(mirrored_geometries)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(central_axis_length=15.0, plane_height=4.0, plane_depth=3.0, num_planes=5, fold_variation=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(central_axis_length=10.0, plane_height=2.5, plane_depth=1.5, num_planes=3, fold_variation=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(central_axis_length=20.0, plane_height=5.0, plane_depth=4.0, num_planes=6, fold_variation=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(central_axis_length=18.0, plane_height=6.0, plane_depth=2.5, num_planes=7, fold_variation=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(central_axis_length=14.0, plane_height=3.5, plane_depth=2.0, num_planes=4, fold_variation=1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
