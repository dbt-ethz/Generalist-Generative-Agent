# Created for 0004_0005_interlocking_layers.json

""" Summary:
The function `create_interlocking_layers_model` generates an architectural concept model based on the "Interlocking Layers" metaphor by creating a series of intersecting and overlapping planes. It takes parameters such as base dimensions, height, number of layers, and gaps between layers, allowing for varied spatial experiences. Each layer is defined with a randomized vertical offset to enhance the dynamic quality of the design. The function constructs 3D geometries, representing the complexity and interplay of spaces, thereby illustrating the metaphor's emphasis on both unity and distinction within the architecture. This results in a visually intriguing structure that embodies the design task."""

#! python 3
function_code = """def create_interlocking_layers_model(base_length, base_width, total_height, num_layers, layer_gap, random_seed=42):
    \"""
    Creates an architectural Concept Model based on the "Interlocking Layers" metaphor.

    This model emphasizes the dynamic interplay of multiple intersecting and overlapping planes,
    illustrating the complexity of interactions between different spaces.

    Parameters:
    - base_length (float): The length of the base of the model in meters.
    - base_width (float): The width of the base of the model in meters.
    - total_height (float): The total height of the model in meters.
    - num_layers (int): The number of interlocking layers to be created.
    - layer_gap (float): The vertical gap between each layer in meters.
    - random_seed (int): Seed for the random number generator to ensure replicability (default is 42).

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(random_seed)

    # Initialize the list to hold the geometry
    geometries = []

    # Calculate the thickness of each layer
    layer_thickness = (total_height - (layer_gap * (num_layers - 1))) / num_layers

    # Create the interlocking layers
    for i in range(num_layers):
        # Determine the y-offset to create interlocking effect
        offset_y = random.uniform(-base_width * 0.1, base_width * 0.1)

        # Create a base plane for the layer
        base_plane = rg.Plane(rg.Point3d(0, offset_y, i * (layer_thickness + layer_gap)), rg.Vector3d.ZAxis)

        # Create intervals for the box dimensions
        x_interval = rg.Interval(-base_length / 2, base_length / 2)
        y_interval = rg.Interval(-base_width / 2, base_width / 2)
        z_interval = rg.Interval(0, layer_thickness)

        # Create a box for the layer
        layer_box = rg.Box(base_plane, x_interval, y_interval, z_interval)

        # Convert the box to a Brep
        layer_brep = layer_box.ToBrep()

        # Add the Brep to the list of geometries
        geometries.append(layer_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(10.0, 5.0, 15.0, 4, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(8.0, 4.0, 12.0, 5, 0.3, random_seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(12.0, 6.0, 18.0, 3, 0.4, random_seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(15.0, 7.0, 20.0, 6, 0.6, random_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(9.0, 4.5, 14.0, 5, 0.2, random_seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
