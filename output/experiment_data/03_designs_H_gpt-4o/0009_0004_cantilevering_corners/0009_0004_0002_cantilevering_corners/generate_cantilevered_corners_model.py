# Created for 0009_0004_cantilevering_corners.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "Cantilevering corners." It constructs a central core structure from which multiple layers of cantilevered volumes extend asymmetrically, reflecting a dynamic relationship between stability and motion. By adjusting the dimensions of each layer based on an extension factor and applying random rotations, the model achieves angular projections that challenge conventional gravity. The interplay of solid and void is emphasized, creating unique spaces beneath the cantilevers that invite exploration. The result is a visually striking representation of bold overhangs, enhancing the perception of light, shadow, and movement."""

#! python 3
function_code = """def generate_cantilevered_corners_model(core_dim, extension_factor, num_layers, angle_variation, seed=42):
    \"""
    Generate an architectural Concept Model based on 'Cantilevering corners', using layered, interlocking volumes.

    This function creates a core structure from which multiple layers of cantilevered volumes extend,
    forming dynamic, angular projections that challenge conventional support structures.

    Parameters:
    - core_dim (tuple of float): Dimensions of the central core structure (width, depth, height) in meters.
    - extension_factor (float): Factor by which each layer extends relative to the core dimensions.
    - num_layers (int): Number of layers of cantilevered volumes extending from the core.
    - angle_variation (float): Maximum angle variation in degrees for each layer to create dynamic forms.
    - seed (int): Seed for random number generator to ensure replicability. Default is 42.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries (breps) representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    core_width, core_depth, core_height = core_dim
    geometries = []

    # Create the central core structure
    core = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_depth), rg.Interval(0, core_height))
    geometries.append(core.ToBrep())

    # Generate cantilevered layers
    for layer in range(1, num_layers + 1):
        # Calculate layer dimensions
        layer_width = core_width * (1 + layer * extension_factor)
        layer_depth = core_depth * (1 + layer * extension_factor)
        layer_height = core_height * (1 + layer * extension_factor / 2)

        # Calculate layer position (offset each layer from the core)
        offset_x = (layer_width - core_width) / 2
        offset_y = (layer_depth - core_depth) / 2
        offset_z = core_height + (layer - 1) * core_height

        # Create the layer box
        layer_box = rg.Box(
            rg.Plane(rg.Point3d(-offset_x, -offset_y, offset_z), rg.Vector3d.ZAxis),
            rg.Interval(0, layer_width),
            rg.Interval(0, layer_depth),
            rg.Interval(0, layer_height)
        )

        # Apply random rotation to create angular variation
        angle = random.uniform(-angle_variation, angle_variation)
        rotation_axis = rg.Vector3d(0, 0, 1)
        rotation_center = rg.Point3d(layer_width / 2 - offset_x, layer_depth / 2 - offset_y, offset_z + layer_height / 2)
        rotation = rg.Transform.Rotation(math.radians(angle), rotation_axis, rotation_center)
        layer_box.Transform(rotation)

        # Add the transformed layer to the list
        geometries.append(layer_box.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cantilevered_corners_model((5, 3, 2), 0.2, 4, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cantilevered_corners_model((10, 6, 3), 0.15, 5, 20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cantilevered_corners_model((8, 4, 5), 0.1, 3, 30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cantilevered_corners_model((7, 5, 4), 0.25, 6, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cantilevered_corners_model((6, 4, 3), 0.3, 5, 25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
