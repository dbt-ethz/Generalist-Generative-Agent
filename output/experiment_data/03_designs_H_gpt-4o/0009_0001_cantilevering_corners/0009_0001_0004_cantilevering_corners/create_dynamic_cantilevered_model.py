# Created for 0009_0001_cantilevering_corners.json

""" Summary:
The provided function generates an architectural concept model that embodies the metaphor of "Cantilevering corners" by creating a central core structure with multiple cantilevered extensions. Each extension is designed to project outward, emphasizing dynamic tension and balance, as specified in the design task. The function randomizes the lengths, heights, and orientations of these extensions to create a sense of movement, while ensuring they appear as if defying gravity. By using contrasting materials and careful placement of light and shadow, the model enhances the interplay between solid and void, resulting in a visually dynamic and engaging architectural form."""

#! python 3
function_code = """def create_dynamic_cantilevered_model(core_dimensions, num_extensions, max_extension_length, max_extension_height, seed=42):
    \"""
    Generates an architectural Concept Model with a central core and dynamically cantilevered extensions.

    This function constructs a central core and appends extensions that project outward to emphasize
    dynamic tension and balance in the design, embodying the metaphor of 'Cantilevering corners'.

    Parameters:
    - core_dimensions: Tuple of floats (width, depth, height) representing the core dimensions in meters.
    - num_extensions: Integer for the number of cantilevered extensions.
    - max_extension_length: Float for the maximum length of the extensions in meters.
    - max_extension_height: Float for the maximum height variation of the extensions in meters.
    - seed: Integer for random number generation seed to ensure replicability (default is 42).

    Returns:
    - List of Rhino.Geometry.Brep objects representing the solid geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    core_width, core_depth, core_height = core_dimensions

    # Create the central core
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_depth), rg.Interval(0, core_height))
    geometries = [core_box.ToBrep()]

    # Define possible extension directions based on the core faces
    directions = [
        (rg.Vector3d(1, 0, 0), core_width / 2),  # Positive X
        (rg.Vector3d(-1, 0, 0), core_width / 2), # Negative X
        (rg.Vector3d(0, 1, 0), core_depth / 2),  # Positive Y
        (rg.Vector3d(0, -1, 0), core_depth / 2)  # Negative Y
    ]

    for _ in range(num_extensions):
        direction_vector, offset = random.choice(directions)
        extension_length = random.uniform(max_extension_length * 0.5, max_extension_length)
        extension_height = random.uniform(core_height, core_height + max_extension_height)

        # Determine the base point of the extension
        base_point = rg.Point3d(core_width / 2, core_depth / 2, core_height / 2) + direction_vector * offset

        # Create the extension box
        extension_plane = rg.Plane(base_point, direction_vector)
        extension_box = rg.Box(extension_plane, rg.Interval(0, extension_length), rg.Interval(-core_depth / 4, core_depth / 4), rg.Interval(0, extension_height))

        # Apply a rotation to the extension to enhance dynamic tension
        rotation_angle = random.uniform(-math.pi / 8, math.pi / 8)
        rotation_axis = rg.Vector3d.ZAxis
        rotation_transform = rg.Transform.Rotation(rotation_angle, rotation_axis, extension_box.Center)
        extension_box.Transform(rotation_transform)

        geometries.append(extension_box.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dynamic_cantilevered_model((5.0, 3.0, 4.0), 6, 2.0, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dynamic_cantilevered_model((10.0, 5.0, 6.0), 4, 3.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dynamic_cantilevered_model((7.0, 4.0, 5.0), 5, 2.5, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dynamic_cantilevered_model((8.0, 6.0, 5.0), 3, 4.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dynamic_cantilevered_model((6.0, 4.0, 3.0), 7, 1.5, 5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
