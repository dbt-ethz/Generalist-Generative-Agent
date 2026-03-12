# Created for 0010_0004_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes_model` generates an architectural concept model inspired by the metaphor "Mirrored folded planes." It creates a series of angular, folded surfaces that exhibit bilateral or radial symmetry, enhancing spatial depth and movement. The function defines base parameters, calculates fold directions, and generates 3D geometries through polylines and breps. Mirroring these folds around a specified axis further emphasizes the concept's reflective nature. Ultimately, the model showcases a dynamic interplay of solid and void, light and shadow, fostering exploration through its intricately layered organization, aligning with the metaphors implications for architectural design."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(base_length, base_width, height, fold_angle, mirror_axis='x'):
    \"""
    Creates an architectural Concept Model based on the 'Mirrored folded planes' metaphor.
    
    The function generates a series of angular, folded surfaces that exhibit bilateral or radial symmetry.
    It aims to create a dynamic interplay of solid and void, light and shadow, and a vibrant visual rhythm.
    The design reflects a cascading organization, where spaces unfold in layers, mirroring each other.

    Parameters:
    base_length (float): The length of the base plane.
    base_width (float): The width of the base plane.
    height (float): The height of the folds.
    fold_angle (float): The angle of the folds in degrees.
    mirror_axis (str): Axis to perform the mirroring ('x' or 'y').

    Returns:
    list: A list of Rhino.Geometry.Brep objects representing the 3D geometries of the concept model.
    \"""
    
    import Rhino
    import math
    import random
    from Rhino.Geometry import Point3d, Vector3d, Plane, Polyline, PolylineCurve, Brep
    
    # Seed the randomness for replicability
    random.seed(42)
    
    # Convert fold angle to radians
    fold_angle_rad = math.radians(fold_angle)
    
    # Create the base plane
    base_plane = Plane.WorldXY
    base_points = [
        Point3d(0, 0, 0),
        Point3d(base_length, 0, 0),
        Point3d(base_length, base_width, 0),
        Point3d(0, base_width, 0),
        Point3d(0, 0, 0)  # Closing the loop
    ]
    base_polyline = Polyline(base_points)
    base_curve = PolylineCurve(base_polyline)
    
    # Generate folds
    folds = []
    for i in range(3):  # Create 3 folded planes
        fold_start = base_curve.PointAtNormalizedLength(i / 3.0)
        fold_end = base_curve.PointAtNormalizedLength((i + 1) / 3.0)
        
        # Calculate fold direction
        fold_direction = Vector3d(fold_end - fold_start)
        fold_direction.Unitize()
        
        # Rotate fold direction by fold angle
        rotated_direction = fold_direction
        rotated_direction.Rotate(fold_angle_rad, Vector3d.ZAxis)
        
        # Create fold plane
        fold_plane_points = [
            fold_start,
            fold_end,
            fold_end + rotated_direction * height,
            fold_start + rotated_direction * height,
            fold_start  # Closing the loop
        ]
        fold_polyline = Polyline(fold_plane_points)
        fold_curve = PolylineCurve(fold_polyline)
        
        # Convert curve to brep
        brep = Brep.CreateFromCornerPoints(fold_plane_points[0], fold_plane_points[1], fold_plane_points[2], fold_plane_points[3], 0.01)
        if brep:
            folds.append(brep)
    
    # Mirror folds
    mirrored_folds = []
    for fold in folds:
        mirror_plane = Plane.WorldYZ if mirror_axis == 'x' else Plane.WorldZX
        mirrored_fold = fold.Duplicate()
        mirrored_fold.Transform(Rhino.Geometry.Transform.Mirror(mirror_plane))
        mirrored_folds.append(mirrored_fold)
    
    # Combine original and mirrored folds
    all_folds = folds + mirrored_folds
    
    return all_folds"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(10, 5, 3, 45, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(12, 8, 4, 60, 'y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(15, 10, 5, 30, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(20, 15, 6, 75, 'y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(8, 4, 2, 90, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
