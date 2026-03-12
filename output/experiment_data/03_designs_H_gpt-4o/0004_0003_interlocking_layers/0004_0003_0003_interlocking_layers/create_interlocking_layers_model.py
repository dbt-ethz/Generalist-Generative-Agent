# Created for 0004_0003_interlocking_layers.json

""" Summary:
The function `create_interlocking_layers_model` generates an architectural concept model based on the metaphor of "Interlocking Layers." It creates a series of overlapping layers, simulating dynamic movement and complexity. By defining parameters like width, depth, height, and number of layers, the function extrudes layers with varying heights and random offsets, embodying the concept of interconnection and individuality. Each layer's thickness and gaps between them enhance the visual texture and spatial relationships, demonstrating both unity and distinction. The resulting geometries reflect the metaphor's emphasis on interactive spaces and varied experiences, capturing the essence of layered architecture."""

#! python 3
function_code = """def create_interlocking_layers_model(width, depth, height, num_layers, layer_thickness, layer_gap, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Interlocking Layers' metaphor.
    
    This function creates a structure composed of interlocking layers with varying heights and overlapping volumes,
    simulating a dynamic facade and complex spatial arrangement. The design emphasizes the interconnectedness 
    and individuality of each layer, capturing the metaphor of interlocking elements.

    Parameters:
    - width (float): The width of the overall structure in meters.
    - depth (float): The depth of the overall structure in meters.
    - height (float): The maximum height of the structure in meters.
    - num_layers (int): The number of layers to create.
    - layer_thickness (float): The thickness of each layer in meters.
    - layer_gap (float): The gap between each layer in meters for interlocking effect.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List of Rhino.Geometry.Brep objects representing the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the seed for reproducibility
    random.seed(seed)

    # List to store the resulting 3D geometries
    geometries = []

    # Base plane for the structure
    base_plane = rg.Plane.WorldXY

    # Calculate the height increment per layer
    height_increment = height / num_layers

    for i in range(num_layers):
        # Random offset for each layer
        offset_x = random.uniform(-layer_gap, layer_gap)
        offset_y = random.uniform(-layer_gap, layer_gap)

        # Calculate the position of the layer
        layer_height = (i + 1) * height_increment
        z_start = i * height_increment

        # Create a base rectangle for the layer
        rect = rg.Rectangle3d(base_plane, width, depth)
        
        # Extrude the rectangle to create a layer with thickness
        extrusion_vector = rg.Vector3d(0, 0, layer_thickness)
        layer_surface = rg.Surface.CreateExtrusion(rect.ToNurbsCurve(), extrusion_vector)

        # Move the layer to simulate interlocking
        translation_vector = rg.Vector3d(offset_x, offset_y, z_start)
        layer_surface.Translate(translation_vector)

        # Convert the surface to a Brep
        layer_brep = layer_surface.ToBrep()
        if layer_brep:
            geometries.append(layer_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(10.0, 5.0, 15.0, 6, 0.5, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(8.0, 4.0, 12.0, 5, 0.3, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(15.0, 10.0, 20.0, 8, 0.4, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(12.0, 6.0, 18.0, 7, 0.6, 0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(20.0, 10.0, 30.0, 10, 0.7, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
