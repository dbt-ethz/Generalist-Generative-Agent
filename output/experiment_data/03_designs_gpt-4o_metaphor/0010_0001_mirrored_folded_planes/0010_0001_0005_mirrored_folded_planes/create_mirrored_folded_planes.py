# Created for 0010_0001_mirrored_folded_planes.json

""" Summary:
The provided function, `create_mirrored_folded_planes`, generates an architectural concept model inspired by the metaphor of "Mirrored folded planes." By defining parameters like width, height, depth, number of folds, and fold angle, the function creates dynamic, angular surfaces through a series of calculated folds. The folding process introduces complexity and movement, while mirroring the resulting geometries along specified axes enhances symmetry and visual impact. This approach results in intricate yet coherent models that embody the metaphor's essence, allowing for exploration of layered geometries and harmonious design, effectively translating the metaphor into a tangible architectural concept."""

#! python 3
function_code = """def create_mirrored_folded_planes(width, height, depth, num_folds, fold_angle, mirror_axis):
    \"""
    Creates a conceptual architectural model based on the metaphor of 'Mirrored folded planes'.
    
    Parameters:
    - width (float): The width of the base plane in meters.
    - height (float): The height of the base plane in meters.
    - depth (float): The depth to which the planes extend in meters.
    - num_folds (int): The number of folds along the width of the plane.
    - fold_angle (float): The angle in degrees at which the planes are folded.
    - mirror_axis (str): The axis along which to mirror ('x' or 'y').
    
    Returns:
    - List of Rhino.Geometry.Brep: A list of breps representing the mirrored folded planes.
    \"""
    import Rhino.Geometry as rg
    import math
    
    # Helper function to create a folded plane
    def create_folded_plane(start_point, width, height, depth, num_folds, fold_angle):
        plane = rg.Plane(start_point, rg.Vector3d.ZAxis)
        folds = []
        fold_width = width / num_folds
        current_point = start_point

        for i in range(num_folds):
            fold = rg.Point3d(current_point)
            angle_rad = math.radians(fold_angle) if i % 2 == 0 else -math.radians(fold_angle)
            fold_transform = rg.Transform.Rotation(angle_rad, plane.YAxis, fold)
            fold.Transform(fold_transform)
            folds.append(fold)
            current_point = rg.Point3d(current_point.X + fold_width, current_point.Y, current_point.Z)
        
        # Create a surface through the folded points
        poly_curve = rg.PolyCurve()
        for i in range(len(folds) - 1):
            line = rg.Line(folds[i], folds[i + 1])
            poly_curve.Append(line.ToNurbsCurve())
        
        brep = rg.Brep.CreateFromLoft([poly_curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        return brep[0] if brep else None

    base_point = rg.Point3d(0, 0, 0)
    folded_brep = create_folded_plane(base_point, width, height, depth, num_folds, fold_angle)
    
    # Mirror the folded plane
    mirrored_brep = None
    if mirror_axis == 'x':
        mirror_plane = rg.Plane.WorldYZ
    elif mirror_axis == 'y':
        mirror_plane = rg.Plane.WorldXY
    else:
        raise ValueError("Invalid mirror axis. Choose 'x' or 'y'.")
    
    if folded_brep:
        mirrored_brep = folded_brep.Duplicate()
        mirror_transform = rg.Transform.Mirror(mirror_plane)
        mirrored_brep.Transform(mirror_transform)
    
    geometries = [folded_brep, mirrored_brep] if mirrored_brep else [folded_brep]
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes(5.0, 3.0, 2.0, 4, 45, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes(10.0, 7.0, 4.0, 6, 30, 'y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes(8.0, 5.0, 3.0, 5, 60, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes(12.0, 9.0, 5.0, 3, 90, 'y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes(6.0, 4.0, 2.5, 2, 30, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
