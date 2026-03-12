# Created for 0004_0001_interlocking_layers.json

""" Summary:
The function `create_interlocking_layers_model` generates an architectural concept model based on the metaphor of "Interlocking Layers." It creates a series of interconnected planes or volumes that overlap and shift, embodying the dynamic, visually complex structure described in the metaphor. By manipulating parameters like layer thickness, offset, and rotation, the function ensures each layer maintains a distinct identity while contributing to a cohesive whole. The output is a collection of Brep geometries that visually represent intricate spatial relationships, balancing openness and privacy, thus capturing the essence of structural complexity and the rich architectural experience intended by the design task."""

#! python 3
function_code = """def create_interlocking_layers_model(base_size, num_layers, layer_thickness, layer_offset, seed):
    \"""
    Creates an architectural Concept Model based on the 'Interlocking Layers' metaphor.
    
    This function generates a series of interconnected planes or volumes that embody the idea of interlocking layers.
    It creates dynamic spatial relationships and visual depth through overlapping and interconnected forms.
    
    Inputs:
    - base_size: A tuple (width, depth, height) representing the overall base dimensions of the model.
    - num_layers: Integer specifying the number of layers to create.
    - layer_thickness: Float representing the thickness of each layer.
    - layer_offset: Float representing the maximum offset distance for interlocking layers.
    - seed: Integer for the random seed to ensure consistent results.
    
    Outputs:
    - List of RhinoCommon Brep objects representing the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random
    import math  # Import the math module to use math.pi

    # Set the random seed for reproducibility
    random.seed(seed)

    # Unpack base size dimensions
    width, depth, height = base_size

    # Initialize a list to hold the Brep geometries
    layers = []

    # Calculate the vertical spacing between layers
    vertical_spacing = height / num_layers

    for i in range(num_layers):
        # Calculate the base plane for the layer
        base_plane = rg.Plane.WorldXY
        base_plane.Translate(rg.Vector3d(0, 0, i * vertical_spacing))

        # Randomly rotate the plane around its origin to create dynamic interlocking
        angle = random.uniform(-0.5, 0.5) * math.pi
        base_plane.Rotate(angle, rg.Vector3d(0, 0, 1))

        # Define the dimensions of the current layer
        layer_width = random.uniform(width * 0.8, width * 1.2)
        layer_depth = random.uniform(depth * 0.8, depth * 1.2)

        # Create a box as the solid representation of the layer
        box_corners = [
            rg.Point3d(-layer_width / 2, -layer_depth / 2, -layer_thickness / 2),
            rg.Point3d(layer_width / 2, -layer_depth / 2, -layer_thickness / 2),
            rg.Point3d(layer_width / 2, layer_depth / 2, -layer_thickness / 2),
            rg.Point3d(-layer_width / 2, layer_depth / 2, -layer_thickness / 2),
            rg.Point3d(-layer_width / 2, -layer_depth / 2, layer_thickness / 2),
            rg.Point3d(layer_width / 2, -layer_depth / 2, layer_thickness / 2),
            rg.Point3d(layer_width / 2, layer_depth / 2, layer_thickness / 2),
            rg.Point3d(-layer_width / 2, layer_depth / 2, layer_thickness / 2),
        ]

        box = rg.Box(base_plane, box_corners)

        # Add randomness to the position of the layer for interlocking effect
        offset_x = random.uniform(-layer_offset, layer_offset)
        offset_y = random.uniform(-layer_offset, layer_offset)
        translation_vector = rg.Vector3d(offset_x, offset_y, 0)
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
    geometry = create_interlocking_layers_model((10, 10, 20), 5, 1, 2, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model((15, 15, 30), 7, 1.5, 3, 24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model((12, 8, 25), 6, 2, 1.5, 36)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model((20, 10, 15), 4, 2, 2.5, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model((8, 12, 18), 3, 0.5, 1, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
