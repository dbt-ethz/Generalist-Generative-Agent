# Created for 0004_0005_interlocking_layers.json

""" Summary:
The provided function generates an architectural concept model based on the 'Interlocking Layers' metaphor by creating a series of overlapping layers represented as geometric boxes. Each layer's position and orientation are randomized within specified parameters, resulting in a dynamic structure that reflects the metaphor's essence. The function allows customization of base dimensions, height, number of layers, and thickness, which ensures a variety of spatial experiences. By manipulating these layers, the model illustrates complex spatial relationships and varying degrees of openness and seclusion, ultimately creating a visually intriguing representation of interconnected architectural elements."""

#! python 3
function_code = """def create_interlocking_layers_model_v2(base_length, base_width, height, num_layers, layer_thickness, seed=42):
    \"""
    Create an architectural Concept Model based on the 'Interlocking Layers' metaphor.

    This function generates a structure composed of intersecting and overlapping planes or volumes,
    designed to reflect a dynamic and multifaceted architectural form. The layers are oriented and
    positioned to highlight structural complexity and spatial relationships, offering varied experiences
    of openness and seclusion.

    Parameters:
    - base_length (float): The length of the base of the model in meters.
    - base_width (float): The width of the base of the model in meters.
    - height (float): The maximum height of the model in meters.
    - num_layers (int): The number of interlocking layers to create.
    - layer_thickness (float): The thickness of each layer in meters.
    - seed (int): A seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the 3D model.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    random.seed(seed)
    geometries = []

    # Calculate the maximum vertical spacing
    max_vertical_spacing = height / num_layers

    for i in range(num_layers):
        # Calculate random offsets and rotations for dynamic layering
        offset_x = random.uniform(-base_length * 0.1, base_length * 0.1)
        offset_y = random.uniform(-base_width * 0.1, base_width * 0.1)
        rotation_angle = random.uniform(-15, 15)  # Rotation angle in degrees

        # Define the base plane for each layer
        base_plane = rg.Plane(rg.Point3d(offset_x, offset_y, i * max_vertical_spacing), rg.Vector3d.ZAxis)
        base_plane.Rotate(math.radians(rotation_angle), base_plane.ZAxis)

        # Create the layer as a box
        x_interval = rg.Interval(-base_length / 2, base_length / 2)
        y_interval = rg.Interval(-base_width / 2, base_width / 2)
        z_interval = rg.Interval(0, layer_thickness)
        layer_box = rg.Box(base_plane, x_interval, y_interval, z_interval)

        # Convert the box to a Brep and add to the list
        layer_brep = layer_box.ToBrep()
        geometries.append(layer_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model_v2(10.0, 5.0, 15.0, 6, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model_v2(8.0, 4.0, 12.0, 5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model_v2(15.0, 10.0, 20.0, 8, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model_v2(12.0, 6.0, 18.0, 7, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model_v2(20.0, 10.0, 25.0, 10, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
