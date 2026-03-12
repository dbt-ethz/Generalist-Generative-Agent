# Created for 0004_0001_interlocking_layers.json

""" Summary:
The function `create_interlocking_layers_model` generates an architectural concept model based on the metaphor of "Interlocking Layers" by creating multiple overlapping and interlocked volumes. It takes parameters such as base dimensions, number of layers, and variations in rotation and height to define the complexity and dynamism of the structure. Each layer is randomly sized and oriented, simulating the metaphor's idea of depth and movement. By allowing for distinct yet connected spaces, the model embodies the balance of openness and privacy, illustrating the intricate spatial relationships and visual depth inherent in the "Interlocking Layers" design approach."""

#! python 3
function_code = """def create_interlocking_layers_model(base_dims, num_layers, layer_thickness, rotation_variation, height_variation, seed):
    \"""
    Creates an architectural Concept Model based on the 'Interlocking Layers' metaphor.

    This function generates a series of interconnected volumes that embody the idea of interlocking layers.
    It utilizes overlapping and interlocking forms to create dynamic spatial relationships and visual depth.

    Parameters:
    - base_dims: A tuple (width, depth, height) representing the overall base dimensions of the model.
    - num_layers: Integer specifying the number of layers to create.
    - layer_thickness: Float representing the thickness of each layer.
    - rotation_variation: Float representing the maximum angle variation for layer orientations in degrees.
    - height_variation: Float representing maximum variation in height for interlocking layers.
    - seed: Integer for the random seed to ensure consistent results.

    Returns:
    - List of RhinoCommon Brep objects representing the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for reproducibility
    random.seed(seed)

    # Unpack base dimensions
    width, depth, height = base_dims

    # Initialize a list to hold the Brep geometries
    layers = []

    # Calculate spacing between layers
    vertical_spacing = height / num_layers

    for i in range(num_layers):
        # Base plane for the layer
        base_plane = rg.Plane.WorldXY
        base_plane.Translate(rg.Vector3d(0, 0, i * vertical_spacing))

        # Dimensions of the current layer
        layer_width = random.uniform(width * 0.6, width * 1.4)
        layer_depth = random.uniform(depth * 0.6, depth * 1.4)

        # Create a box as the solid representation of the layer
        box = rg.Box(base_plane, rg.Interval(-layer_width / 2, layer_width / 2), rg.Interval(-layer_depth / 2, layer_depth / 2), rg.Interval(0, layer_thickness))

        # Randomly rotate the box around its center to create interlocking effect
        angle = random.uniform(-rotation_variation, rotation_variation)
        rotation = rg.Transform.Rotation(math.radians(angle), base_plane.ZAxis, box.Center)
        box.Transform(rotation)

        # Random height offset for additional interlocking complexity
        height_offset = random.uniform(-height_variation, height_variation)
        translation_vector = rg.Vector3d(0, 0, height_offset)
        box.Transform(rg.Transform.Translation(translation_vector))

        # Convert the box to a Brep and add it to the list
        brep_layer = box.ToBrep()
        layers.append(brep_layer)

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model((10, 10, 20), 5, 1, 15, 2, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model((15, 15, 30), 7, 1.5, 20, 3, 100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model((12, 12, 24), 6, 2, 10, 4, 2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model((8, 8, 16), 4, 0.5, 30, 1, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model((20, 15, 40), 8, 2, 25, 5, 55)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
