# Created for 0010_0002_mirrored_folded_planes.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "Mirrored folded planes" by creating angular, folded geometries that respond to specified design parameters. It organizes multiple planes around mirrored axes, employing a defined fold angle and height to achieve a dynamic interplay of light and shadow. The code uses geometric transformations to mimic the folding and mirroring effects, resulting in complex, visually engaging forms. Each iteration produces a unique arrangement of folded planes, emphasizing movement and spatial exploration, while ensuring coherence through symmetry and repetition that reflects the metaphor's essence."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(axis_count, plane_count, fold_angle, fold_height, base_length, base_width):
    \"""
    Creates an architectural Concept Model inspired by the 'Mirrored folded planes' metaphor. The model features
    angular, folded geometries that interact across several mirrored axes, creating a dynamic interplay of form and void.
    
    Parameters:
    - axis_count (int): The number of mirrored axes around which the planes are organized.
    - plane_count (int): The number of folded planes to create.
    - fold_angle (float): The angle in degrees at which each plane is folded.
    - fold_height (float): The height in meters of each folded plane.
    - base_length (float): The base length in meters of each folded plane.
    - base_width (float): The base width in meters of each folded plane.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the folded planes.
    \"""
    import Rhino.Geometry as rg
    import math

    geometries = []
    base_plane = rg.Plane.WorldXY
    rad_fold_angle = math.radians(fold_angle)
    
    # Calculate the mirrored axes
    angle_between_axes = 360.0 / axis_count

    for axis_index in range(axis_count):
        axis_rotation = math.radians(axis_index * angle_between_axes)
        axis_plane = rg.Plane(base_plane)
        axis_plane.Rotate(axis_rotation, base_plane.ZAxis)

        for plane_index in range(plane_count):
            # Create the base rectangle for the folded plane
            base_rect = rg.Rectangle3d(axis_plane, base_length, base_width)

            # Calculate the folding transformation
            fold_transform = rg.Transform.Rotation(rad_fold_angle, axis_plane.YAxis, base_rect.Corner(0))
            fold_transform *= rg.Transform.Translation(0, 0, fold_height)

            # Create the folded plane
            brep_face = rg.Brep.CreateFromCornerPoints(base_rect.Corner(0), base_rect.Corner(1), base_rect.Corner(2), base_rect.Corner(3), 0.01)
            folded_plane = brep_face.Duplicate()
            folded_plane.Transform(fold_transform)

            # Mirror the folded plane across the axis
            mirror_plane = rg.Plane(axis_plane.Origin, axis_plane.XAxis, axis_plane.ZAxis)
            mirrored_folded_plane = folded_plane.Duplicate()
            mirrored_folded_plane.Transform(rg.Transform.Mirror(mirror_plane))

            # Add both the original and mirrored plane to the geometries list
            geometries.append(folded_plane)
            geometries.append(mirrored_folded_plane)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(4, 6, 30, 2.0, 3.0, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(3, 5, 45, 1.5, 2.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(5, 4, 60, 2.5, 4.0, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(2, 8, 15, 3.0, 5.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(6, 3, 90, 1.0, 2.5, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
