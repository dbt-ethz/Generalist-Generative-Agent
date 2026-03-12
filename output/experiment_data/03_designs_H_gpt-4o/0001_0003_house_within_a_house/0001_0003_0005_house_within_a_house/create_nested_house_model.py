# Created for 0001_0003_house_within_a_house.json

""" Summary:
The provided function, `create_nested_house_model`, generates an architectural concept model based on the "House within a house" metaphor. It constructs a dual-layered structure comprising an outer protective shell and an inner sanctuary. The parameters allow for customized dimensions and spatial shifts, facilitating the exploration of relationships between the layers. By creating openings in the outer shell, the function enhances visual and physical connections, embodying the metaphor's themes of nesting, protection, and privacy. The model highlights dynamic transitions between public and private spaces, fostering a sense of discovery and retreat within its layered arrangement."""

#! python 3
function_code = """def create_nested_house_model(outer_dims, inner_dims, vertical_shift, horizontal_shift, randomness_seed):
    \"""
    Constructs a conceptual architectural model based on the 'House within a house' metaphor.

    This model features a dual-layered structure with an inner sanctuary nested within an outer protective form.
    The design uses vertical and horizontal shifts to create dynamic spatial relationships and enhance the sense of
    discovery and retreat within the layers.

    Parameters:
    - outer_dims: Tuple of 3 floats (length, width, height) for the outer shell dimensions in meters.
    - inner_dims: Tuple of 3 floats (length, width, height) for the inner sanctuary dimensions in meters.
    - vertical_shift: Float representing the vertical offset of the inner volume within the outer volume.
    - horizontal_shift: Float tuple (x_shift, y_shift) for the horizontal offset of the inner volume.
    - randomness_seed: Integer seed for random number generation to ensure replicable results.

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(randomness_seed)

    def create_box(center, dimensions):
        \"""Helper function to create a box Brep given a center point and dimensions.\"""
        length, width, height = dimensions
        corner1 = rg.Point3d(center.X - length / 2, center.Y - width / 2, center.Z - height / 2)
        corner2 = rg.Point3d(center.X + length / 2, center.Y + width / 2, center.Z + height / 2)
        box = rg.Box(rg.Plane.WorldXY, rg.Interval(corner1.X, corner2.X), rg.Interval(corner1.Y, corner2.Y), rg.Interval(corner1.Z, corner2.Z))
        return box.ToBrep()

    # Create the outer shell
    outer_center = rg.Point3d(0, 0, 0)
    outer_volume = create_box(outer_center, outer_dims)

    # Create the inner sanctuary with shifts
    inner_center = rg.Point3d(horizontal_shift[0], horizontal_shift[1], vertical_shift)
    inner_volume = create_box(inner_center, inner_dims)

    # Create openings in the outer shell to enhance connection
    opening_width = random.uniform(outer_dims[1] * 0.1, outer_dims[1] * 0.2)
    opening_height = random.uniform(outer_dims[2] * 0.3, outer_dims[2] * 0.5)
    opening_plane = rg.Plane.WorldXY
    opening_plane.Origin = rg.Point3d(0, outer_dims[1] / 2, 0)
    opening = rg.Box(opening_plane, rg.Interval(0, outer_dims[0] * 0.1), rg.Interval(-opening_width / 2, opening_width / 2), rg.Interval(0, opening_height))
    opening_brep = opening.ToBrep()

    # Subtract opening from the outer shell
    outer_with_opening = rg.Brep.CreateBooleanDifference([outer_volume], [opening_brep], 0.01)

    # Ensure valid geometry results
    if not outer_with_opening or len(outer_with_opening) == 0:
        outer_with_opening = [outer_volume]  # Fallback to original outer_volume if boolean fails

    # Combine geometries
    geometries = [inner_volume] + list(outer_with_opening)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_nested_house_model((10.0, 8.0, 6.0), (6.0, 4.0, 3.0), 1.5, (2.0, 2.0), 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_nested_house_model((12.0, 10.0, 8.0), (7.0, 5.0, 4.0), 2.0, (3.0, 1.0), 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_nested_house_model((15.0, 12.0, 10.0), (8.0, 6.0, 5.0), 2.5, (1.0, 3.0), 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_nested_house_model((14.0, 9.0, 7.0), (5.0, 3.0, 2.0), 1.0, (1.5, 0.5), 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_nested_house_model((20.0, 15.0, 12.0), (10.0, 7.0, 6.0), 3.0, (4.0, 2.0), 55)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
