# Created for 0010_0005_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes_model` generates an architectural concept model based on the metaphor "Mirrored folded planes." It creates interlocked, angular forms that reflect symmetry and complexity by defining a base plane and applying a specified fold angle and depth factor. This results in dynamic surfaces that evoke movement and visual interest. By mirroring these surfaces across selected axes, the model achieves a cohesive interplay of light and shadow. The output is a series of 3D geometries that embody the metaphors essence, facilitating a spatial experience characterized by rhythm, depth, and interaction."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(base_length, base_width, height, fold_angle, depth_factor, mirror_axes):
    \"""
    Constructs an architectural Concept Model based on the 'Mirrored folded planes' metaphor.
    
    This function creates a series of interlocked, angular forms that reflect across specified axes,
    embodying a dynamic equilibrium of light and shadow. The model emphasizes the rhythm and complexity
    of folded and mirrored geometries.

    Parameters:
    - base_length (float): Length of the base plane in meters.
    - base_width (float): Width of the base plane in meters.
    - height (float): Height of the folded planes in meters.
    - fold_angle (float): The angle in degrees at which the planes are folded.
    - depth_factor (float): Factor to modulate the depth of folds.
    - mirror_axes (list of str): Axes ('x', 'y', 'z') across which the geometry will be mirrored.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    from math import radians, tan

    # Base plane creation
    base_plane = rg.Plane.WorldXY
    base_corners = [
        rg.Point3d(-base_length / 2, -base_width / 2, 0),
        rg.Point3d(base_length / 2, -base_width / 2, 0),
        rg.Point3d(base_length / 2, base_width / 2, 0),
        rg.Point3d(-base_length / 2, base_width / 2, 0)
    ]
    base_surface = rg.Brep.CreateFromCornerPoints(base_corners[0], base_corners[1], base_corners[2], base_corners[3], 0.01)

    # Folded plane construction
    fold_radians = radians(fold_angle)
    fold_depth = height * tan(fold_radians) * depth_factor
    fold_vector = rg.Vector3d(0, fold_depth, height)

    # Create initial folded plane
    folded_corners = [
        base_corners[0],
        base_corners[1],
        base_corners[1] + fold_vector,
        base_corners[0] + fold_vector
    ]
    folded_surface = rg.Brep.CreateFromCornerPoints(folded_corners[0], folded_corners[1], folded_corners[2], folded_corners[3], 0.01)

    breps = [folded_surface]

    # Mirroring across specified axes
    for axis in mirror_axes:
        if axis == 'x':
            mirror_plane = rg.Plane.WorldYZ
        elif axis == 'y':
            mirror_plane = rg.Plane.WorldZX
        elif axis == 'z':
            mirror_plane = rg.Plane.WorldXY
        else:
            continue  # Skip invalid axes

        mirrored_brep = folded_surface.Duplicate()
        mirrored_brep.Transform(rg.Transform.Mirror(mirror_plane))
        breps.append(mirrored_brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(10.0, 5.0, 3.0, 45.0, 1.5, ['x', 'y'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(8.0, 4.0, 2.5, 30.0, 1.2, ['z'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(12.0, 6.0, 4.0, 60.0, 1.0, ['x', 'z'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(15.0, 7.0, 5.0, 90.0, 2.0, ['y'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(9.0, 3.0, 2.0, 75.0, 1.3, ['x', 'y', 'z'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
