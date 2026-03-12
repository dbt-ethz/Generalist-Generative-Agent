# Created for 0010_0001_mirrored_folded_planes.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor "Mirrored folded planes" by creating a series of folded surfaces arranged symmetrically around a central axis. It takes parameters such as axis length, plane dimensions, fold count, and angle to define the complexity of the folded planes. The function constructs these planes and mirrors them across a defined axis, emphasizing reflective symmetry. This approach captures the metaphors essence, showcasing dynamic forms and intricate spatial relationships. The resulting model exhibits movement and depth through light interplay, inviting exploration of its layered geometries while maintaining coherence amidst complexity."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(axis_length, plane_width, plane_height, fold_count, fold_angle, mirror_axis_offset):
    \"""
    Creates an architectural Concept Model that embodies the 'Mirrored folded planes' metaphor.
    
    Parameters:
    axis_length (float): The length of the central axis in meters.
    plane_width (float): The width of each folded plane in meters.
    plane_height (float): The height of each folded plane in meters.
    fold_count (int): The number of folds in each plane.
    fold_angle (float): The angle of each fold in degrees.
    mirror_axis_offset (float): The offset distance of the mirrored axis from the central axis in meters.
    
    Returns:
    List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the folded and mirrored planes.
    \"""
    
    import Rhino.Geometry as rg
    import math
    
    # Helper function to create a folded plane
    def create_folded_plane(start_point, fold_count, fold_angle, plane_width, plane_height):
        folds = [start_point]
        current_point = start_point
        angle_radians = math.radians(fold_angle)
        
        for i in range(1, fold_count + 1):
            # Create vertices for the fold
            next_point = rg.Point3d(current_point.X + plane_width * math.cos(i * angle_radians),
                                    current_point.Y + plane_width * math.sin(i * angle_radians),
                                    current_point.Z + plane_height * (1 if i % 2 == 0 else -1))
            folds.append(next_point)
            current_point = next_point
            
        # Create a folded surface from the folds
        if len(folds) >= 4:
            fold_surface = rg.Brep.CreateFromCornerPoints(folds[0], folds[1], folds[2], folds[3], 0.01)
            return fold_surface
        else:
            return None
    
    # Create central axis
    center_line = rg.Line(rg.Point3d(0, 0, 0), rg.Point3d(axis_length, 0, 0))
    
    # Create folded planes along the central axis
    planes = []
    for i in range(fold_count):
        base_point = rg.Point3d(center_line.PointAt(i / fold_count))
        folded_plane = create_folded_plane(base_point, fold_count, fold_angle, plane_width, plane_height)
        if folded_plane is not None:
            planes.append(folded_plane)
    
    # Mirror the folded planes across the axis
    mirror_planes = []
    mirror_axis = rg.Plane(rg.Point3d(mirror_axis_offset, 0, 0), rg.Vector3d(0, 1, 0))
    
    for plane in planes:
        mirrored_plane = plane.DuplicateBrep()
        mirrored_plane.Transform(rg.Transform.Mirror(mirror_axis))
        mirror_planes.append(mirrored_plane)
    
    # Combine original and mirrored planes
    all_planes = planes + mirror_planes
    
    return all_planes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(10.0, 2.0, 3.0, 5, 30.0, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(15.0, 1.5, 4.0, 6, 45.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(20.0, 3.0, 5.0, 4, 60.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(12.0, 2.5, 3.5, 3, 90.0, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(8.0, 2.0, 3.0, 7, 15.0, 0.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
