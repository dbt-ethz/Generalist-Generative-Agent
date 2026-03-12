# Created for 0010_0001_mirrored_folded_planes.json

""" Summary:
The provided function `create_mirrored_folded_planes_model` generates an architectural concept model based on the metaphor of "Mirrored folded planes." It creates a series of angular, folded surfaces symmetrically arranged around a central axis, reflecting the metaphor's dynamic and symmetrical qualities. By employing a specified number of folds and varied heights, the model captures movement and depth through its layered geometries. The use of mirrored surfaces emphasizes symmetry, allowing for interconnected spaces that repeat across the central axis. This approach effectively balances complexity and coherence, inviting exploration of the intricate spatial relationships within the design."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(base_length=10.0, base_width=5.0, height=3.0, fold_count=3):
    \"""
    Create an Architectural Concept Model that embodies the 'Mirrored folded planes' metaphor.
    
    This function generates a series of angular, folded surfaces arranged symmetrically around a central axis,
    demonstrating movement and depth through the interplay of shadows and reflections. The model features a
    mirrored organization with interconnected spaces that repeat across a central spine.

    Parameters:
    - base_length (float): The length of the base plane (in meters).
    - base_width (float): The width of the base plane (in meters).
    - height (float): The height of the folded planes (in meters).
    - fold_count (int): The number of folds to create on each side of the central axis.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the folded planes.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(42)  # Ensure the randomness is replicable

    geometries = []
    central_axis = rg.Line(rg.Point3d(0, 0, 0), rg.Point3d(0, base_width, 0))

    # Create folded planes on one side of the central axis
    for i in range(fold_count):
        # Define the points of the base of the fold
        p1 = rg.Point3d(0, i * (base_width / fold_count), 0)
        p2 = rg.Point3d(base_length, i * (base_width / fold_count), 0)
        p3 = rg.Point3d(base_length, (i + 1) * (base_width / fold_count), 0)
        p4 = rg.Point3d(0, (i + 1) * (base_width / fold_count), 0)

        # Randomly adjust the height to create dynamic folds
        h_variation = random.uniform(-0.5, 0.5) * height
        p5 = rg.Point3d(base_length / 2, i * (base_width / fold_count) + (base_width / (2 * fold_count)), height + h_variation)

        # Create the folded surface
        fold_curve1 = rg.PolylineCurve([p1, p2, p5, p1])
        fold_curve2 = rg.PolylineCurve([p2, p3, p5, p2])
        fold_curve3 = rg.PolylineCurve([p3, p4, p5, p3])
        fold_curve4 = rg.PolylineCurve([p4, p1, p5, p4])

        loft = rg.Brep.CreateFromLoft([fold_curve1, fold_curve2, fold_curve3, fold_curve4], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        if loft:
            geometries.append(loft[0])

    # Mirror the geometries to the other side of the central axis
    mirror_plane = rg.Plane(rg.Point3d(0, base_width / 2, 0), rg.Vector3d(0, 1, 0))
    mirrored_geometries = [geo.DuplicateBrep().Transform(rg.Transform.Mirror(mirror_plane)) for geo in geometries]
    geometries.extend(mirrored_geometries)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(base_length=15.0, base_width=7.0, height=4.0, fold_count=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(base_length=12.0, base_width=6.0, height=2.5, fold_count=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(base_length=8.0, base_width=4.0, height=3.5, fold_count=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(base_length=20.0, base_width=10.0, height=5.0, fold_count=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(base_length=18.0, base_width=9.0, height=3.0, fold_count=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
