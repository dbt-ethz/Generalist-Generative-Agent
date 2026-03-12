# Created for 0010_0003_mirrored_folded_planes.json

""" Summary:
The function `generate_mirrored_folded_planes` creates an architectural concept model inspired by the metaphor "Mirrored folded planes." It generates a series of angular, folded geometries, using specified dimensions and a defined number of planes. Each plane is created at a fixed angle and then mirrored across a chosen axis (x, y, or z) to establish symmetry and visual complexity. The function emphasizes the interplay of light and shadow through reflective materials and spatial organization, ensuring a fluid transition and continuity between spaces. Ultimately, this results in a coherent, intricate architectural form that invites exploration."""

#! python 3
function_code = """def generate_mirrored_folded_planes(base_length, base_width, height, num_planes, mirror_axis):
    \"""
    Generates an architectural Concept Model based on the metaphor of "Mirrored folded planes".

    This function creates angular, folded forms arranged in a mirrored fashion across specified axes,
    creating a dynamic and symmetrical architectural design.

    Parameters:
    - base_length (float): Length of the base of each folded plane in meters.
    - base_width (float): Width of the base of each folded plane in meters.
    - height (float): Height of the folded planes in meters.
    - num_planes (int): Number of folded planes to generate.
    - mirror_axis (str): Axis across which the planes are mirrored ('x', 'y', or 'z').

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the mirrored folded planes.
    \"""
    import Rhino.Geometry as rg
    import math

    def create_plane(base_length, base_width, height, angle):
        \"""Create a folded plane using base dimensions and angle.\"""
        angle_rad = math.radians(angle)
        pt1 = rg.Point3d(0, 0, 0)
        pt2 = rg.Point3d(base_length, 0, 0)
        pt3 = rg.Point3d(base_length * math.cos(angle_rad), base_width, height)
        pt4 = rg.Point3d(0, base_width, height)
        corner_pts = [pt1, pt2, pt3, pt4]
        polyline = rg.Polyline(corner_pts + [corner_pts[0]])
        return rg.Brep.CreateFromCornerPoints(pt1, pt2, pt3, pt4, 0.01)

    breps = []
    fold_angle = 30  # Fixed angle for simplicity
    for i in range(num_planes):
        offset = i * (base_length + 1.0)  # Adding spacing between planes
        plane = create_plane(base_length, base_width, height, fold_angle)
        translation = rg.Transform.Translation(offset, 0, 0)
        plane.Transform(translation)
        breps.append(plane)
        
        if mirror_axis.lower() == 'x':
            mirror_plane = rg.Plane.WorldYZ
        elif mirror_axis.lower() == 'y':
            mirror_plane = rg.Plane.WorldZX
        else:
            mirror_plane = rg.Plane.WorldXY
        
        mirrored_plane = plane.DuplicateBrep()
        transformation = rg.Transform.Mirror(mirror_plane)
        mirrored_plane.Transform(transformation)
        breps.append(mirrored_plane)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_mirrored_folded_planes(5.0, 3.0, 2.0, 4, 'y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_mirrored_folded_planes(4.0, 2.5, 1.5, 3, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_mirrored_folded_planes(6.0, 4.0, 3.0, 5, 'z')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_mirrored_folded_planes(7.0, 5.0, 2.5, 6, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_mirrored_folded_planes(8.0, 4.5, 3.5, 2, 'y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
