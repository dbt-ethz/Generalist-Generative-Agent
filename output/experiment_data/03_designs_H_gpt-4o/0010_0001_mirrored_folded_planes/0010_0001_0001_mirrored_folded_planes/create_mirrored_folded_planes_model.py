# Created for 0010_0001_mirrored_folded_planes.json

""" Summary:
The provided function generates an architectural concept model based on the "Mirrored folded planes" metaphor by creating a series of angular, folded surfaces arranged symmetrically around a central axis. It uses parameters to define the central axis length, height, width of each plane, and the number of planes. The function constructs folded planes on one side of the axis and then mirrors them to achieve reflective symmetry. This results in a visually dynamic structure that emphasizes movement and depth through its angular forms and interplay of shadows. The model encapsulates the balance between complexity and coherence in spatial organization."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(central_axis_length=20.0, fold_height=5.0, fold_width=3.0, plane_count=6):
    \"""
    Creates an architectural Concept Model embodying the 'Mirrored folded planes' metaphor. This model features
    angular, dynamic surfaces folded and mirrored across a central axis, creating an intricate and balanced spatial layout.

    Parameters:
    - central_axis_length (float): The length of the central axis (in meters).
    - fold_height (float): The height of each folded plane (in meters).
    - fold_width (float): The width of each folded plane (in meters).
    - plane_count (int): The number of planes on each side of the axis.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the folded and mirrored planes.
    \"""
    import Rhino.Geometry as rg
    import math
    
    # Helper function to create a single folded plane
    def create_folded_plane(base_point, height, width, angle):
        # Create the base polyline of the folded plane
        direction = rg.Vector3d(math.cos(angle), math.sin(angle), 0)
        corner1 = base_point + direction * width
        corner2 = corner1 + rg.Vector3d(0, 0, height)
        corner3 = base_point + rg.Vector3d(0, 0, height)

        return rg.Brep.CreateFromCornerPoints(base_point, corner1, corner2, corner3, 0.001)

    geometries = []
    angle_increment = math.pi / plane_count

    # Create folded planes on one side of the axis
    for i in range(plane_count):
        angle = i * angle_increment
        base_point = rg.Point3d(i * (central_axis_length / plane_count), 0, 0)
        plane = create_folded_plane(base_point, fold_height, fold_width, angle)
        if plane:
            geometries.append(plane)

    # Mirror the planes to the other side of the axis
    mirror_plane = rg.Plane.WorldYZ
    mirrored_geometries = [geo.DuplicateBrep() for geo in geometries]
    for geo in mirrored_geometries:
        geo.Transform(rg.Transform.Mirror(mirror_plane))
    geometries.extend(mirrored_geometries)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(central_axis_length=30.0, fold_height=7.0, fold_width=4.0, plane_count=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(central_axis_length=25.0, fold_height=6.0, fold_width=2.5, plane_count=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(central_axis_length=15.0, fold_height=10.0, fold_width=5.0, plane_count=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(central_axis_length=40.0, fold_height=8.0, fold_width=6.0, plane_count=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(central_axis_length=50.0, fold_height=12.0, fold_width=3.5, plane_count=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
