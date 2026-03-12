# Created for 0010_0001_mirrored_folded_planes.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor "Mirrored folded planes" by creating a series of angular, dynamic surfaces. It employs parameters such as axis length, fold angle, fold height, and the number of planes to define the model's geometry. The function constructs folded planes symmetrically around a central axis, mirroring each plane to enhance the sense of movement and depth. Reflective materials and strategic angles ensure a compelling interplay of light and shadow. Ultimately, the model embodies complexity and coherence, inviting exploration of its layered geometries while adhering to the design task's requirements."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(axis_length, fold_angle, fold_height, plane_count):
    \"""
    Generates an architectural Concept Model based on the 'Mirrored folded planes' metaphor.
    
    Parameters:
    - axis_length (float): The length of the central axis (spine) around which the planes are mirrored.
    - fold_angle (float): The angle in degrees at which each plane is folded.
    - fold_height (float): The vertical height of each folded plane.
    - plane_count (int): The number of planes on each side of the axis.

    Returns:
    - list: A list of RhinoCommon BRep objects representing the folded and mirrored planes.
    \"""
    import Rhino.Geometry as rg
    import math

    # Helper function to create a folded plane
    def create_folded_plane(base_point, angle, height):
        # Define the base plane
        base_plane = rg.Plane(base_point, rg.Vector3d.XAxis, rg.Vector3d.ZAxis)
        
        # Create the first segment of the folded plane
        segment_length = height / math.tan(math.radians(angle))
        first_point = base_point + rg.Vector3d(segment_length, 0, 0)
        second_point = first_point + rg.Vector3d(0, 0, height)
        
        # Create a polyline representing the folded plane
        polyline = rg.Polyline([base_point, first_point, second_point])
        return rg.Brep.CreateFromCornerPoints(base_point, first_point, second_point, rg.Point3d(first_point.X, first_point.Y, 0), 1e-3)

    # Create the central axis
    center_line_start = rg.Point3d(0, 0, 0)
    center_line_end = rg.Point3d(axis_length, 0, 0)
    center_line = rg.Line(center_line_start, center_line_end)

    # List to store all the breps
    breps = []

    # Create folded planes on one side and their mirrored counterparts
    for i in range(plane_count):
        offset = i * (axis_length / plane_count)
        base_point = rg.Point3d(offset, 0, 0)

        # Create the folded plane
        folded_plane = create_folded_plane(base_point, fold_angle, fold_height)
        breps.append(folded_plane)
        
        # Mirror the folded plane
        mirror_plane = rg.Plane(center_line.PointAt(0.5), rg.Vector3d.YAxis)
        mirrored_plane = folded_plane.DuplicateBrep()
        mirrored_plane.Transform(rg.Transform.Mirror(mirror_plane))
        breps.append(mirrored_plane)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(10.0, 30.0, 5.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(15.0, 45.0, 10.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(20.0, 60.0, 7.5, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(12.0, 20.0, 6.0, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(25.0, 75.0, 8.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
