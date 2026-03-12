# Created for 0010_0002_mirrored_folded_planes.json

""" Summary:
The provided function, `create_mirrored_folded_planes_model`, generates an architectural concept model based on the metaphor "Mirrored folded planes." It creates 3D geometries featuring angular, folded forms that are mirrored across multiple axes, reflecting the dynamic interplay between form and void. By adjusting parameters like base dimensions, fold height, and angle, the function crafts intricate shapes that embody visual movement and tension. The use of mirroring enhances symmetry, while the folds introduce complexity, resulting in interconnected spaces that encourage exploration. This computational approach effectively translates the metaphor into a tangible architectural representation, emphasizing light interaction and spatial dynamics."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(base_length, base_width, fold_height, fold_angle, mirror_axis_count):
    \"""
    Generates an architectural Concept Model inspired by the 'Mirrored folded planes' metaphor. The model features
    angular, folded geometries that are mirrored across multiple axes to create a dynamic and coherent design.
    
    Parameters:
    - base_length (float): The length of the base plane in meters.
    - base_width (float): The width of the base plane in meters.
    - fold_height (float): The height of the folds in meters.
    - fold_angle (float): The angle in degrees to fold each plane.
    - mirror_axis_count (int): The number of axes to mirror the geometry across.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import math
    
    geometries = []
    angle_increment = 360 / mirror_axis_count
    rad_fold_angle = math.radians(fold_angle)

    for axis_index in range(mirror_axis_count):
        rotation_angle = math.radians(axis_index * angle_increment)
        rotation = rg.Transform.Rotation(rotation_angle, rg.Vector3d.ZAxis, rg.Point3d.Origin)
        
        # Create base plane
        base_plane = rg.Plane.WorldXY
        base_plane.Transform(rotation)
        
        # Create fold
        fold_plane = rg.Plane(base_plane)
        fold_plane.Translate(rg.Vector3d(0, 0, fold_height))
        fold_plane.Rotate(rad_fold_angle, base_plane.XAxis, base_plane.Origin)
        
        # Create corner points
        corner_1 = base_plane.Origin
        corner_2 = corner_1 + rg.Vector3d(base_length, 0, 0)
        corner_3 = corner_2 + rg.Vector3d(0, base_width, 0)
        corner_4 = corner_1 + rg.Vector3d(0, base_width, 0)
        
        # Create surface from corner points
        brep = rg.Brep.CreateFromCornerPoints(corner_1, corner_2, corner_3, corner_4, 0.01)
        fold_brep = brep.Duplicate()
        fold_brep.Transform(rg.Transform.Translation(0, 0, fold_height))
        
        # Add to geometries
        geometries.append(fold_brep)
        
        # Mirror across XY plane
        mirrored_folds = fold_brep.Duplicate()
        mirrored_folds.Transform(rg.Transform.Mirror(rg.Plane.WorldXY))
        geometries.append(mirrored_folds)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(10.0, 5.0, 3.0, 45.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(8.0, 4.0, 2.0, 30.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(12.0, 6.0, 4.0, 60.0, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(15.0, 7.0, 5.0, 90.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(5.0, 3.0, 2.0, 75.0, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
