# Created for 0010_0003_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes_model_v2` generates an architectural concept model inspired by the metaphor "Mirrored folded planes." It creates a series of angular, folded forms, reflecting these geometries across specified axes to enhance symmetry and complexity. The function takes parameters for dimensions and the number of folds, generating a base folded plane. It then duplicates and mirrors this plane along designated axes, creating a harmonious interplay of light and shadow. The resulting model embodies a dynamic spatial layout, ensuring fluid transitions and inviting exploration through its intricate, yet unified, geometric design."""

#! python 3
function_code = """def create_mirrored_folded_planes_model_v2(base_length, base_width, height, num_folds, mirror_axes):
    \"""
    Creates an architectural Concept Model based on the metaphor of "Mirrored folded planes".

    This function generates a series of angular, folded forms and mirrors them across specified axes.
    The design emphasizes symmetry and complexity, achieving a balance between intricate forms and unified spaces.

    Parameters:
    - base_length (float): The base length of the folded plane structure.
    - base_width (float): The base width of the folded plane structure.
    - height (float): The height of the folded planes.
    - num_folds (int): The number of folds to generate in the plane.
    - mirror_axes (str): The axes along which the folds will be mirrored ('x', 'y', 'xy').

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the mirrored folded planes.
    \"""
    import Rhino.Geometry as rg
    import math

    def create_folded_plane(base_length, base_width, height, num_folds):
        # Points to define the base and folds
        points = [rg.Point3d(i * (base_length / num_folds), 0, 0) for i in range(num_folds + 1)]
        fold_height = height / num_folds

        # Create folds by raising alternate points
        for i in range(1, len(points), 2):
            points[i] = rg.Point3d(points[i].X, points[i].Y, fold_height)

        # Create a polyline and loft it
        polyline = rg.Polyline(points + [rg.Point3d(base_length, base_width, 0), rg.Point3d(0, base_width, 0), points[0]])
        curve = polyline.ToNurbsCurve()
        lofted_surface = rg.Brep.CreateFromLoft([curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Straight, False)
        
        return lofted_surface[0] if lofted_surface and len(lofted_surface) > 0 else None

    # Create the initial folded plane
    folded_plane = create_folded_plane(base_length, base_width, height, num_folds)
    
    # Check if the folded_plane was created successfully
    if folded_plane is None:
        return []

    # Prepare for mirroring
    mirrored_planes = []

    # Mirror along specified axes
    if 'x' in mirror_axes:
        mirror_plane_x = rg.Plane.WorldYZ
        mirrored_x = folded_plane.DuplicateBrep()
        mirrored_x.Transform(rg.Transform.Mirror(mirror_plane_x))
        mirrored_planes.append(mirrored_x)

    if 'y' in mirror_axes:
        mirror_plane_y = rg.Plane.WorldXZ
        mirrored_y = folded_plane.DuplicateBrep()
        mirrored_y.Transform(rg.Transform.Mirror(mirror_plane_y))
        mirrored_planes.append(mirrored_y)

    if 'xy' in mirror_axes:
        mirror_plane_xy = rg.Plane.WorldXY
        mirrored_xy = folded_plane.DuplicateBrep()
        mirrored_xy.Transform(rg.Transform.Mirror(mirror_plane_xy))
        mirrored_planes.append(mirrored_xy)

    return [folded_plane] + mirrored_planes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model_v2(10.0, 5.0, 3.0, 4, 'xy')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model_v2(15.0, 7.5, 4.0, 6, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model_v2(12.0, 6.0, 5.0, 3, 'y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model_v2(20.0, 10.0, 2.5, 5, 'xy')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model_v2(8.0, 4.0, 2.0, 2, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
