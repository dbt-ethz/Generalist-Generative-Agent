# Created for 0010_0001_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes_model` generates an architectural concept model based on the metaphor "Mirrored folded planes" by creating a series of angular, dynamically folded surfaces arranged symmetrically around a central axis. It utilizes parameters such as base dimensions, height variance, and the number of planes to define the model's complexity and coherence. The function constructs each folded surface, introducing variations in height to enhance depth and movement. By mirroring these geometries across a specified axis, it effectively represents reflective symmetry, allowing for a layered spatial organization that invites exploration of its intricate design."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(base_dimensions=(10.0, 5.0, 3.0), fold_height_variance=0.5, mirror_offset=2.0, plane_count=4):
    \"""
    Create an Architectural Concept Model that embodies the 'Mirrored folded planes' metaphor.

    This function generates a series of angular, folded surfaces arranged symmetrically around a central axis,
    demonstrating movement and depth through the interplay of shadows and reflections. The model emphasizes
    symmetry with mirrored organization and interconnected spaces repeating across a central spine.

    Parameters:
    - base_dimensions (tuple of float): Dimensions (length, width, height) of the base plane (in meters).
    - fold_height_variance (float): Variation in height to create dynamic folds (in meters).
    - mirror_offset (float): Offset distance for the mirrored axis from the central plane (in meters).
    - plane_count (int): Number of folded planes on each side of the central axis.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the folded and mirrored planes.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(42)  # Ensure the randomness is replicable
    
    length, width, height = base_dimensions
    geometries = []
    fold_width = width / plane_count

    # Create folded planes on one side of the central axis
    for i in range(plane_count):
        # Define base points of the fold
        p1 = rg.Point3d(i * fold_width, 0, 0)
        p2 = rg.Point3d((i + 1) * fold_width, 0, 0)
        p3 = rg.Point3d((i + 1) * fold_width, length, 0)
        p4 = rg.Point3d(i * fold_width, length, 0)

        # Adjust height randomly within specified variance
        h_variation = random.uniform(-fold_height_variance, fold_height_variance)
        folding_peak = rg.Point3d((i + 0.5) * fold_width, length / 2, height + h_variation)

        # Create the folded surface
        fold_srf = rg.Brep.CreateFromCornerPoints(p1, p2, folding_peak, p1, 0.01)
        fold_srf2 = rg.Brep.CreateFromCornerPoints(p2, p3, folding_peak, p2, 0.01)
        fold_srf3 = rg.Brep.CreateFromCornerPoints(p3, p4, folding_peak, p3, 0.01)
        fold_srf4 = rg.Brep.CreateFromCornerPoints(p4, p1, folding_peak, p4, 0.01)
        
        for srf in [fold_srf, fold_srf2, fold_srf3, fold_srf4]:
            if srf:
                geometries.append(srf)

    # Mirror the geometries to the other side with an offset
    mirror_plane = rg.Plane(rg.Point3d(mirror_offset, length / 2, 0), rg.Vector3d(0, 1, 0))
    mirrored_geometries = [geo.DuplicateBrep().Transform(rg.Transform.Mirror(mirror_plane)) for geo in geometries]
    geometries.extend(mirrored_geometries)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(base_dimensions=(12.0, 6.0, 4.0), fold_height_variance=0.75, mirror_offset=3.0, plane_count=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(base_dimensions=(15.0, 8.0, 5.0), fold_height_variance=0.3, mirror_offset=1.5, plane_count=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(base_dimensions=(8.0, 4.0, 2.0), fold_height_variance=0.2, mirror_offset=1.0, plane_count=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(base_dimensions=(20.0, 10.0, 6.0), fold_height_variance=1.0, mirror_offset=4.0, plane_count=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(base_dimensions=(14.0, 7.0, 4.5), fold_height_variance=0.4, mirror_offset=2.5, plane_count=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
