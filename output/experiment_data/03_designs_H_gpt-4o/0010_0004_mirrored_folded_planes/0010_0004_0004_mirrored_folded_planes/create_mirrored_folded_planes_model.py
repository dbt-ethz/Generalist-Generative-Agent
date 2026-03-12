# Created for 0010_0004_mirrored_folded_planes.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "Mirrored folded planes" by creating a series of angular, mirrored surfaces that exhibit radial symmetry. It constructs individual folded segments, transforming them to create depth and movement, while emphasizing the interplay of solid and void. The function systematically rotates each segment around a specified axis and mirrors them, resulting in a complex structure that reflects the metaphor's themes of symmetry and layered organization. The output is a collection of 3D geometries that embody visual complexity and structural harmony, encouraging exploration of their intricate forms."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(segment_length=8, segment_width=4, fold_height=5, num_segments=4, mirror_axis='z'):
    \"""
    Creates an architectural Concept Model based on the 'Mirrored folded planes' metaphor.

    This function generates a series of angular, folded surfaces that exhibit radial symmetry.
    The design emphasizes the dynamic interplay of solid and void, light and shadow, and a cascading organization
    of spaces that reflect each other, fostering a sense of progression and discovery.

    Parameters:
    - segment_length (float): The length of each segment of the folded plane in meters.
    - segment_width (float): The width of each segment of the folded plane in meters.
    - fold_height (float): The height of the folds in meters.
    - num_segments (int): The number of segments to create around the symmetry axis.
    - mirror_axis (str): The axis around which the structure will be mirrored ('x', 'y', or 'z').

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Helper function to create a single folded segment
    def create_folded_segment(origin, length, width, height):
        base_points = [
            rg.Point3d(origin.X, origin.Y, origin.Z),
            rg.Point3d(origin.X + length, origin.Y, origin.Z),
            rg.Point3d(origin.X + length, origin.Y + width, origin.Z),
            rg.Point3d(origin.X, origin.Y + width, origin.Z)
        ]
        top_points = [
            rg.Point3d(origin.X, origin.Y, origin.Z + height),
            rg.Point3d(origin.X + length, origin.Y, origin.Z + height),
            rg.Point3d(origin.X + length, origin.Y + width, origin.Z + height),
            rg.Point3d(origin.X, origin.Y + width, origin.Z + height)
        ]
        brep = rg.Brep.CreateFromCornerPoints(base_points[0], base_points[1], base_points[2], base_points[3], 0.01)
        top_brep = rg.Brep.CreateFromCornerPoints(top_points[0], top_points[1], top_points[2], top_points[3], 0.01)
        if brep and top_brep:
            loft = rg.Brep.CreateFromLoft([brep.Edges[0].ToNurbsCurve(), top_brep.Edges[0].ToNurbsCurve()],
                                          rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
            if loft:
                return loft[0]
        return None

    # Symmetric rotation angle
    angle_increment = 360.0 / num_segments
    geometries = []

    for i in range(num_segments):
        angle_rad = math.radians(i * angle_increment)
        rotation = rg.Transform.Rotation(angle_rad, rg.Vector3d(0, 0, 1), rg.Point3d(0, 0, 0))
        segment = create_folded_segment(rg.Point3d(0, 0, 0), segment_length, segment_width, fold_height)
        if segment:
            segment.Transform(rotation)
            geometries.append(segment)

    # Mirror segments around specified axis
    if mirror_axis == 'x':
        mirror_plane = rg.Plane.WorldYZ
    elif mirror_axis == 'y':
        mirror_plane = rg.Plane.WorldZX
    else:
        mirror_plane = rg.Plane.WorldXY

    mirrored_geometries = []
    for geom in geometries:
        mirrored_geom = geom.DuplicateBrep()
        mirrored_geom.Transform(rg.Transform.Mirror(mirror_plane))
        mirrored_geometries.append(mirrored_geom)

    return geometries + mirrored_geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(segment_length=10, segment_width=5, fold_height=6, num_segments=6, mirror_axis='y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(segment_length=12, segment_width=3, fold_height=4, num_segments=5, mirror_axis='x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(segment_length=9, segment_width=4, fold_height=7, num_segments=3, mirror_axis='z')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(segment_length=7, segment_width=2, fold_height=3, num_segments=8, mirror_axis='x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(segment_length=15, segment_width=6, fold_height=5, num_segments=4, mirror_axis='y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
