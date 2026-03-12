# Created for 0009_0001_cantilevering_corners.json

""" Summary:
The provided function, `create_cantilevering_corners`, generates an architectural concept model inspired by the metaphor of "cantilevering corners." It constructs a base structure defined by specified dimensions and adds cantilevered overhangs at each corner, reflecting a dynamic interplay between stability and motion. Each overhang projects outward, creating dramatic, gravity-defying forms that embody the metaphor's key traits. By manipulating parameters like overhang length, height, and offsets, the function produces a variety of geometries, which are then compiled into a conceptual model that visually interprets the metaphor while exploring innovative architectural possibilities."""

#! python 3
function_code = """def create_cantilevering_corners(base_length, base_width, base_height, overhang_length, overhang_height, overhang_offset):
    \"""
    Creates a conceptual architectural model with cantilevering corners, emphasizing dynamic interaction between stability and motion.

    Parameters:
        base_length (float): The length of the base structure in meters.
        base_width (float): The width of the base structure in meters.
        base_height (float): The height of the base structure in meters.
        overhang_length (float): The length of the cantilevering overhang in meters.
        overhang_height (float): The height of the cantilevering overhang in meters.
        overhang_offset (float): The vertical offset from the top of the base structure to the bottom of the overhang in meters.

    Returns:
        list: A list of 3D geometries (breps) representing the conceptual model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Create the base structure
    base = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    
    # Create overhangs at each corner
    overhangs = []
    for corner in [(0, 0), (1, 0), (1, 1), (0, 1)]:
        if corner == (0, 0):
            # Bottom-left corner
            anchor_point = rg.Point3d(0, 0, base_height - overhang_offset)
            direction = rg.Vector3d(-overhang_length, -overhang_length, overhang_height)
        elif corner == (1, 0):
            # Bottom-right corner
            anchor_point = rg.Point3d(base_length, 0, base_height - overhang_offset)
            direction = rg.Vector3d(overhang_length, -overhang_length, overhang_height)
        elif corner == (1, 1):
            # Top-right corner
            anchor_point = rg.Point3d(base_length, base_width, base_height - overhang_offset)
            direction = rg.Vector3d(overhang_length, overhang_length, overhang_height)
        elif corner == (0, 1):
            # Top-left corner
            anchor_point = rg.Point3d(0, base_width, base_height - overhang_offset)
            direction = rg.Vector3d(-overhang_length, overhang_length, overhang_height)

        overhang_corners = [
            anchor_point,
            anchor_point + rg.Point3d(direction.X, 0, 0),
            anchor_point + rg.Point3d(direction.X, direction.Y, 0),
            anchor_point + rg.Point3d(0, direction.Y, 0),
            anchor_point + rg.Point3d(0, 0, direction.Z),
            anchor_point + rg.Point3d(direction.X, 0, direction.Z),
            anchor_point + rg.Point3d(direction.X, direction.Y, direction.Z),
            anchor_point + rg.Point3d(0, direction.Y, direction.Z),
        ]
        overhang = rg.Box(rg.BoundingBox(overhang_corners))
        overhangs.append(overhang)

    # Combine the base and overhangs into the final model
    concept_model = [base.ToBrep()] + [oh.ToBrep() for oh in overhangs]

    return concept_model"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevering_corners(10, 5, 3, 2, 1, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevering_corners(8, 4, 2, 3, 1.5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevering_corners(12, 6, 4, 2.5, 1.2, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevering_corners(15, 7, 5, 4, 2, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevering_corners(9, 3, 2, 1.5, 0.8, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
