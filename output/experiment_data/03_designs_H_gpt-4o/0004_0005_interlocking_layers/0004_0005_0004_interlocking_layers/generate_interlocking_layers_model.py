# Created for 0004_0005_interlocking_layers.json

""" Summary:
The provided function, `generate_interlocking_layers_model`, creates an architectural concept model inspired by the "Interlocking Layers" metaphor. It generates multiple overlapping layers by calculating their positions, orientations, and dimensions based on specified parameters like base size, maximum height, and layer count. Each layer is randomized in position and angle, enhancing the dynamic relationship between spaces. This results in a model that visually represents complexity and variation in spatial experiences, illustrating the balance between openness and intimacy. The output consists of 3D geometries (Brep objects) that embody the intricacies of the proposed design."""

#! python 3
function_code = """def generate_interlocking_layers_model(base_length, base_width, max_height, num_layers, layer_gap, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Interlocking Layers' metaphor.

    This function creates a structure of overlapping and intersecting volumes, emphasizing dynamic relationships
    between spaces. It demonstrates spatial complexity through layering with varied orientations and gaps.

    Parameters:
    - base_length (float): The length of the base of the model in meters.
    - base_width (float): The width of the base of the model in meters.
    - max_height (float): The maximum height of the model in meters.
    - num_layers (int): The number of interlocking layers.
    - layer_gap (float): The gap between each layer in meters.
    - seed (int): Seed for randomization to ensure replicability (default is 42).

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set random seed for reproducibility
    random.seed(seed)

    # List to store the resulting Breps
    geometries = []

    # Calculate the height per layer
    height_per_layer = (max_height - layer_gap * (num_layers - 1)) / num_layers

    for i in range(num_layers):
        # Calculate the z-position for each layer
        z_position = i * (height_per_layer + layer_gap)

        # Randomize orientation and position offset
        angle = random.uniform(-25, 25)  # Rotation angle in degrees
        offset_x = random.uniform(-base_length * 0.2, base_length * 0.2)
        offset_y = random.uniform(-base_width * 0.2, base_width * 0.2)

        # Create a base plane for the layer
        base_plane = rg.Plane.WorldXY
        base_plane.Translate(rg.Vector3d(offset_x, offset_y, z_position))
        base_plane.Rotate(math.radians(angle), base_plane.ZAxis)

        # Define the box for the layer
        x_interval = rg.Interval(-base_length / 2, base_length / 2)
        y_interval = rg.Interval(-base_width / 2, base_width / 2)
        z_interval = rg.Interval(0, height_per_layer)

        # Create the box representing a layer
        layer_box = rg.Box(base_plane, x_interval, y_interval, z_interval)

        # Convert box to Brep and add to the list
        layer_brep = layer_box.ToBrep()
        geometries.append(layer_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_interlocking_layers_model(10.0, 5.0, 15.0, 4, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_interlocking_layers_model(8.0, 4.0, 12.0, 5, 0.5, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_interlocking_layers_model(15.0, 10.0, 20.0, 6, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_interlocking_layers_model(12.0, 6.0, 18.0, 3, 1.5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_interlocking_layers_model(20.0, 10.0, 25.0, 7, 1.0, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
