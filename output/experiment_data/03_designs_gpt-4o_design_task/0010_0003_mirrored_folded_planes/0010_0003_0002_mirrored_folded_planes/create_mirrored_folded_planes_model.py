# Created for 0010_0003_mirrored_folded_planes.json

""" Summary:
The `create_mirrored_folded_planes_model` function generates an architectural concept model based on the metaphor of "Mirrored folded planes." It constructs angular, folded geometries that are mirrored across specified axes, thereby enhancing symmetry and complexity. By defining parameters like base length, height, fold angle, and mirror axis, the function produces a series of Brep geometries that reflect the intricate design intent. The resulting model emphasizes a balance between visual dynamism and spatial continuity, inviting exploration through layered forms that play with light and shadow, ultimately capturing the essence of the provided metaphor and design task."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(base_length, height, fold_angle, mirror_axis):
    \"""
    Creates a Concept Model based on the metaphor of 'Mirrored folded planes'.
    
    This function generates a series of angular, folded forms that are mirrored across a specified axis.
    The design emphasizes symmetry and complexity, achieving a balance between intricate forms and unified spaces.

    Parameters:
    - base_length (float): The base length of each folded plane in meters.
    - height (float): The height of the folded planes in meters.
    - fold_angle (float): The angle at which the planes are folded in degrees.
    - mirror_axis (str): The axis along which the folds are to be mirrored ('x', 'y', or 'z').

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the mirrored folded planes.
    \"""
    import Rhino.Geometry as rg
    import math

    # Helper function to create a folded plane
    def create_folded_plane(base_length, height, fold_angle):
        # Convert angle to radians
        angle_rad = math.radians(fold_angle)
        
        # Define points for the base of the plane
        pt1 = rg.Point3d(0, 0, 0)
        pt2 = rg.Point3d(base_length, 0, 0)
        
        # Define points for the folded part
        pt3 = rg.Point3d(base_length * math.cos(angle_rad), base_length * math.sin(angle_rad), height)
        pt4 = rg.Point3d(0, base_length * math.sin(angle_rad), height)
        
        # Create the folded surface
        corner_points = [pt1, pt2, pt3, pt4]
        polyline = rg.Polyline(corner_points + [corner_points[0]])
        polyline_curve = polyline.ToNurbsCurve()
        return rg.Brep.CreateFromCornerPoints(pt1, pt2, pt3, pt4, 0.01)

    # Create the initial folded plane
    folded_plane = create_folded_plane(base_length, height, fold_angle)
    
    # Create a mirrored version of the folded plane across specified axis
    mirror_plane = None
    if mirror_axis == 'x':
        mirror_plane = rg.Plane.WorldYZ
    elif mirror_axis == 'y':
        mirror_plane = rg.Plane.WorldZX
    elif mirror_axis == 'z':
        mirror_plane = rg.Plane.WorldXY
    else:
        raise ValueError("Invalid mirror axis. Choose from 'x', 'y', or 'z'.")
    
    mirrored_plane = folded_plane.Duplicate()
    mirrored_plane.Transform(rg.Transform.Mirror(mirror_plane))
    
    return [folded_plane, mirrored_plane]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(5.0, 3.0, 45.0, 'y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(2.5, 4.0, 30.0, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(4.0, 2.0, 60.0, 'z')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(6.0, 5.0, 90.0, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(3.0, 2.5, 75.0, 'z')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
