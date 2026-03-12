# Created for 0010_0003_mirrored_folded_planes.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor "Mirrored folded planes." It creates a series of angular, folded geometries that reflect across specified axes, enhancing symmetry and visual complexity. By defining parameters like length, width, height, number of folds, and mirror axes, the function constructs intricate surfaces using Rhino's geometry library. The folded planes are organized sequentially to promote fluid movement through the spaces, while mirroring amplifies the interplay of light and shadow. The model embodies a harmonious blend of form and function, inviting exploration through its layered and dynamic design."""

#! python 3
function_code = """def create_mirrored_folded_planes_structure(length, width, height, num_folds, mirror_axes):
    \"""
    Generates an architectural Concept Model based on the 'Mirrored folded planes' metaphor. 
    This function creates a series of angular forms that fold and mirror across specified axes.

    Parameters:
    - length (float): The length of the primary folded plane in meters.
    - width (float): The width of the primary folded plane in meters.
    - height (float): The height of the folded planes in meters.
    - num_folds (int): The number of folds to create in the structure.
    - mirror_axes (list of str): The axes along which to mirror the geometry ('x', 'y', 'z').

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the mirrored folded planes.
    \"""
    import Rhino.Geometry as rg
    import math

    def create_folded_plane(base_length, base_width, plane_height, folds):
        # Calculate the spacing between folds
        fold_spacing = base_length / (folds + 1)
        
        # Create a list of points that form the folded geometry
        points = []
        z_offset = 0
        for i in range(folds + 2):
            x = i * fold_spacing
            y = (i % 2) * base_width
            z = z_offset if i % 2 == 0 else plane_height
            points.append(rg.Point3d(x, y, z))
        
        # Create a polyline and loft it to form a surface
        polyline = rg.Polyline(points)
        curve = polyline.ToNurbsCurve()
        loft = rg.Brep.CreateFromLoft([curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Straight, False)
        
        return loft[0] if loft else None

    def mirror_geometry(geometry, axis):
        if axis == 'x':
            mirror_plane = rg.Plane.WorldYZ
        elif axis == 'y':
            mirror_plane = rg.Plane.WorldXZ
        elif axis == 'z':
            mirror_plane = rg.Plane.WorldXY
        else:
            raise ValueError(f"Invalid mirror axis: {axis}. Choose from 'x', 'y', or 'z'.")
        
        mirrored_geom = geometry.DuplicateBrep()
        mirrored_geom.Transform(rg.Transform.Mirror(mirror_plane))
        return mirrored_geom

    # Create the primary folded plane
    folded_plane = create_folded_plane(length, width, height, num_folds)
    if not folded_plane:
        return []

    # Mirror the plane across the specified axes
    mirrored_planes = [folded_plane]
    for axis in mirror_axes:
        mirrored_plane = mirror_geometry(folded_plane, axis)
        mirrored_planes.append(mirrored_plane)

    return mirrored_planes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_structure(5.0, 3.0, 2.0, 4, ['x', 'y', 'z'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_structure(10.0, 5.0, 3.0, 6, ['x', 'z'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_structure(7.5, 4.0, 3.5, 5, ['y'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_structure(8.0, 2.0, 4.0, 3, ['x', 'y'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_structure(6.0, 3.5, 2.5, 2, ['x'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
