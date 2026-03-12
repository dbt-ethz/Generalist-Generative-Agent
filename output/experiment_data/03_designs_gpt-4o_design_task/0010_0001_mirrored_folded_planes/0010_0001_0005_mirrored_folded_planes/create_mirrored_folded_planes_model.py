# Created for 0010_0001_mirrored_folded_planes.json

""" Summary:
The provided function, `create_mirrored_folded_planes_model`, generates an architectural concept model that embodies the metaphor of "Mirrored folded planes." By taking parameters such as axis length, number of planes, fold angle, height, and width, it creates a series of angular, folded surfaces arranged symmetrically around a central axis. Each plane is generated, then mirrored to enhance symmetry, creating a dynamic interplay of light and shadow. This approach results in a complex yet coherent spatial organization, reflecting the metaphor's themes of movement, depth, and rhythmic repetition, inviting exploration of its layered geometries."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(axis_length=10.0, plane_count=5, fold_angle=30.0, plane_height=4.0, plane_width=2.0):
    \"""
    This function creates an architectural Concept Model that embodies the 'Mirrored folded planes' metaphor.
    It generates a series of angular, folded surfaces arranged symmetrically around a central axis.
    
    Parameters:
    - axis_length: The length of the central axis around which the planes are mirrored (in meters).
    - plane_count: The number of folded planes on each side of the axis.
    - fold_angle: The angle at which each plane is folded (in degrees).
    - plane_height: The height of each plane (in meters).
    - plane_width: The width of each plane (in meters).
    
    Returns:
    - A list of Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    # List to store the generated geometries
    geometries = []
    
    # Central axis line
    central_axis = rg.Line(rg.Point3d(0, 0, 0), rg.Point3d(axis_length, 0, 0))
    
    # Angle conversion
    fold_angle_rad = math.radians(fold_angle)
    
    # Create folded planes
    for i in range(plane_count):
        # Position of the plane along the central axis
        offset = (i + 0.5) * (axis_length / plane_count)
        
        # Define the base plane
        base_point = rg.Point3d(offset, 0, 0)
        fold_vector = rg.Vector3d(math.cos(fold_angle_rad), 0, math.sin(fold_angle_rad))
        fold_vector.Unitize()
        fold_vector *= plane_width
        
        # Create the folded plane surface
        corner1 = base_point + fold_vector
        corner2 = corner1 + rg.Vector3d(0, plane_height, 0)
        corner3 = base_point + rg.Vector3d(0, plane_height, 0)
        folded_plane = rg.Brep.CreateFromCornerPoints(base_point, corner1, corner2, corner3, 0.001)

        # Mirror the plane across the central axis
        mirror_transform = rg.Transform.Mirror(rg.Plane(rg.Point3d(offset, 0, 0), rg.Vector3d(0, 1, 0)))
        mirrored_plane = folded_plane.DuplicateBrep()
        mirrored_plane.Transform(mirror_transform)

        # Add both the original and mirrored plane to the geometries list
        geometries.append(folded_plane)
        geometries.append(mirrored_plane)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(axis_length=15.0, plane_count=6, fold_angle=45.0, plane_height=5.0, plane_width=3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(axis_length=12.0, plane_count=4, fold_angle=60.0, plane_height=3.0, plane_width=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(axis_length=20.0, plane_count=3, fold_angle=25.0, plane_height=6.0, plane_width=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(axis_length=8.0, plane_count=7, fold_angle=15.0, plane_height=2.0, plane_width=4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(axis_length=18.0, plane_count=5, fold_angle=75.0, plane_height=7.0, plane_width=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
