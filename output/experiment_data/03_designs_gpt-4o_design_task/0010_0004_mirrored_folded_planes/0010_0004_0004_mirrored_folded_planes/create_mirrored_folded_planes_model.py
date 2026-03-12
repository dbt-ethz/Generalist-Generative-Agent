# Created for 0010_0004_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes_model` generates an architectural concept model based on the metaphor of "Mirrored folded planes." It creates a series of angular, folded surfaces that exhibit bilateral or radial symmetry, emphasizing depth and movement through strategic folding and mirroring. By defining parameters like base dimensions, height, and fold angle, the function generates a base plane, applies a folding transformation, and mirrors the resulting geometric form. This process results in a dynamic interplay between light and shadow, creating a visually complex structure that reflects the cascading organization of spaces, encouraging exploration and interaction within the design."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(base_length=10, base_width=5, height=3, fold_angle=30, mirror_axis='x'):
    \"""
    Create an architectural Concept Model that embodies the 'Mirrored folded planes' metaphor.
    
    This function creates a series of angular, folded surfaces that exhibit bilateral or radial symmetry.
    The design focuses on creating a sense of depth and movement through strategic folding and mirroring,
    with an emphasis on the interplay between solid and void, light and shadow.

    Parameters:
    - base_length (float): The length of the base of the folded planes in meters.
    - base_width (float): The width of the base of the folded planes in meters.
    - height (float): The height of each folded plane in meters.
    - fold_angle (float): The angle at which planes are folded in degrees.
    - mirror_axis (str): The axis along which the planes are mirrored ('x' or 'y').

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the folded planes and their mirrored counterparts.
    \"""
    import Rhino
    import Rhino.Geometry as rg
    import math
    
    def create_folded_plane(base_length, base_width, height, fold_angle):
        # Create base rectangle
        base_corners = [
            rg.Point3d(0, 0, 0),
            rg.Point3d(base_length, 0, 0),
            rg.Point3d(base_length, base_width, 0),
            rg.Point3d(0, base_width, 0)
        ]
        base_curve = rg.Polyline(base_corners + [base_corners[0]]).ToNurbsCurve()
        
        # Create a plane and fold it
        fold_radians = math.radians(fold_angle)
        fold_vector = rg.Vector3d(math.sin(fold_radians) * height, 0, math.cos(fold_radians) * height)
        fold_transform = rg.Transform.Translation(fold_vector)
        
        top_curve = base_curve.Duplicate()
        top_curve.Transform(fold_transform)
        
        # Create surface from lofting base and top curves
        loft = rg.Brep.CreateFromLoft([base_curve, top_curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        return loft[0] if loft else None

    # Generate the original folded plane
    folded_plane = create_folded_plane(base_length, base_width, height, fold_angle)
    
    # Mirror the folded plane
    if mirror_axis == 'x':
        mirror_transform = rg.Transform.Mirror(rg.Plane.WorldYZ)
    else:
        mirror_transform = rg.Transform.Mirror(rg.Plane.WorldXY)
    
    mirrored_plane = folded_plane.DuplicateBrep()
    mirrored_plane.Transform(mirror_transform)
    
    # Return both the original and mirrored folded planes
    return [folded_plane, mirrored_plane]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(base_length=12, base_width=6, height=4, fold_angle=45, mirror_axis='y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(base_length=15, base_width=7, height=2, fold_angle=60, mirror_axis='x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(base_length=8, base_width=4, height=5, fold_angle=90, mirror_axis='x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(base_length=20, base_width=10, height=3, fold_angle=15, mirror_axis='y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(base_length=18, base_width=9, height=6, fold_angle=75, mirror_axis='x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
