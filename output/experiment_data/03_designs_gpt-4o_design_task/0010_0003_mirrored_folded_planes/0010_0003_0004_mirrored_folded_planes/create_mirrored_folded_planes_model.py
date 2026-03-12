# Created for 0010_0003_mirrored_folded_planes.json

""" Summary:
The provided function, `create_mirrored_folded_planes_model`, generates an architectural concept model inspired by the metaphor of "Mirrored folded planes." It constructs a series of angular, folded geometries based on specified dimensions, fold angles, and mirror axes. The function begins by creating a base folded plane, defining its geometry in three-dimensional space. It then mirrors these planes along designated axes, enhancing the visual complexity and symmetry of the design. The resulting model encapsulates a harmonious interplay of light and shadow, embodying the metaphor's essence by promoting fluid transitions and spatial continuity within the architectural layout."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(base_length, base_width, height, fold_angle, mirror_axis):
    \"""
    Creates an architectural Concept Model based on the 'Mirrored folded planes' metaphor.
    
    Parameters:
    - base_length: float, the length of the base plane in meters.
    - base_width: float, the width of the base plane in meters.
    - height: float, the maximum height of the folded planes in meters.
    - fold_angle: float, the angle in degrees at which the planes are folded.
    - mirror_axis: str, the axis along which the folding planes are mirrored ('x', 'y', or 'xy').
    
    Returns:
    - list of Rhino.Geometry.Brep, a list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import math
    
    # Helper function to create a folded plane
    def create_folded_plane(base_length, base_width, height, fold_angle):
        angle_rad = math.radians(fold_angle)
        fold_height = height * math.tan(angle_rad)
        
        # Define base rectangle
        base_corners = [
            rg.Point3d(0, 0, 0),
            rg.Point3d(base_length, 0, 0),
            rg.Point3d(base_length, base_width, 0),
            rg.Point3d(0, base_width, 0)
        ]
        base_polygon = rg.Polyline(base_corners + [base_corners[0]])
        
        # Folded points
        fold_corners = [
            rg.Point3d(0, 0, fold_height),
            rg.Point3d(base_length, 0, fold_height),
            rg.Point3d(base_length, base_width, fold_height),
            rg.Point3d(0, base_width, fold_height)
        ]
        fold_polygon = rg.Polyline(fold_corners + [fold_corners[0]])
        
        # Create surfaces
        base_surface = rg.Brep.CreateFromCornerPoints(base_corners[0], base_corners[1], base_corners[2], base_corners[3], 0.01)
        fold_surface = rg.Brep.CreateFromCornerPoints(fold_corners[0], fold_corners[1], fold_corners[2], fold_corners[3], 0.01)
        
        return [base_surface, fold_surface]
    
    # Create initial folded plane
    folded_planes = create_folded_plane(base_length, base_width, height, fold_angle)
    
    # Mirror the planes based on the specified axis
    mirrored_planes = []
    xform_mirror_x = rg.Transform.Mirror(rg.Plane.WorldYZ)
    xform_mirror_y = rg.Transform.Mirror(rg.Plane.WorldXY)
    
    if 'x' in mirror_axis:
        for plane in folded_planes:
            mirrored_planes.append(plane.DuplicateBrep().Transform(xform_mirror_x))
    
    if 'y' in mirror_axis:
        for plane in folded_planes:
            mirrored_planes.append(plane.DuplicateBrep().Transform(xform_mirror_y))
    
    if 'xy' in mirror_axis:
        for plane in folded_planes:
            mirrored_planes.append(plane.DuplicateBrep().Transform(xform_mirror_x * xform_mirror_y))
    
    # Combine all planes
    all_planes = folded_planes + mirrored_planes
    
    return all_planes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(10.0, 5.0, 3.0, 45.0, 'xy')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(8.0, 4.0, 2.5, 30.0, 'y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(12.0, 6.0, 4.0, 60.0, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(15.0, 7.0, 5.0, 90.0, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(9.0, 3.0, 2.0, 30.0, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
