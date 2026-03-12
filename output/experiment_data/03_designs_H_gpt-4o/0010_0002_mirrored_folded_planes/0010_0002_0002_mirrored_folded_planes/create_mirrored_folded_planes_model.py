# Created for 0010_0002_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes_model` generates an architectural concept model based on the "Mirrored folded planes" metaphor by creating a series of angular, folded geometries. It allows for customizable parameters, such as length, width, height, fold angle, and the number of folds. Each plane is defined and transformed using folding and mirroring techniques, which emphasize symmetry and spatial complexity. The function also mirrors these planes across specified axes, enhancing the visual dynamics and interconnectedness of the design. Ultimately, the output encapsulates the concepts of movement, light interaction, and spatial exploration, aligning with the metaphor's implications."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(length, width, height, fold_angle, num_folds, mirror_axes):
    \"""
    Creates an architectural Concept Model inspired by the 'Mirrored folded planes' metaphor. This function generates 
    a dynamic composition of folded planes mirrored across multiple axes, emphasizing movement, symmetry, and spatial exploration.

    Parameters:
    - length (float): The length of each plane in meters.
    - width (float): The width of each plane in meters.
    - height (float): The height of the folds in meters.
    - fold_angle (float): The angle in degrees at which each plane is folded.
    - num_folds (int): Number of planes to generate and fold.
    - mirror_axes (list of str): Axes along which to mirror the geometry ('x', 'y', 'z').

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the folded and mirrored concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Initialize list to store geometries
    geometries = []

    # Calculate fold transformation
    fold_rad = math.radians(fold_angle)

    for i in range(num_folds):
        # Base plane for each fold
        base_plane = rg.Plane.WorldXY
        base_plane.Origin = rg.Point3d(i * length, 0, 0)

        # Define corners of the base plane
        corners = [
            base_plane.Origin,
            base_plane.Origin + rg.Vector3d(length, 0, 0),
            base_plane.Origin + rg.Vector3d(length, width, 0),
            base_plane.Origin + rg.Vector3d(0, width, 0)
        ]

        # Create initial Brep from base plane
        base_brep = rg.Brep.CreateFromCornerPoints(corners[0], corners[1], corners[2], corners[3], 0.01)

        # Apply fold transformation
        axis = rg.Line(corners[0], corners[1])
        fold_transform = rg.Transform.Rotation(fold_rad, axis.Direction, axis.To)
        folded_brep = base_brep.Duplicate()
        folded_brep.Transform(fold_transform)

        # Translate the folded plane to introduce height
        translate_vector = rg.Vector3d(0, 0, height)
        folded_brep.Transform(rg.Transform.Translation(translate_vector))

        geometries.append(folded_brep)

    # Mirror the geometries across specified axes
    for axis in mirror_axes:
        mirror_plane = {
            'x': rg.Plane.WorldYZ,
            'y': rg.Plane.WorldZX,
            'z': rg.Plane.WorldXY
        }.get(axis, None)

        if mirror_plane is not None:
            mirrored_geometries = []
            for geom in geometries:
                mirrored_geom = geom.Duplicate()
                mirrored_geom.Transform(rg.Transform.Mirror(mirror_plane))
                mirrored_geometries.append(mirrored_geom)
            geometries.extend(mirrored_geometries)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(5.0, 3.0, 2.0, 45.0, 4, ['x', 'y'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(10.0, 5.0, 3.0, 30.0, 6, ['z'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(4.0, 2.5, 1.5, 60.0, 5, ['x'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(7.0, 4.0, 3.0, 90.0, 3, ['y', 'z'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(6.0, 3.5, 2.5, 75.0, 2, ['x'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
