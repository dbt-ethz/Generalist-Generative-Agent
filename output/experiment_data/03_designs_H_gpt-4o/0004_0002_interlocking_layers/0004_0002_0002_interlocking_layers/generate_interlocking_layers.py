# Created for 0004_0002_interlocking_layers.json

""" Summary:
The provided function generates an architectural concept model based on the "Interlocking Layers" metaphor by creating a series of overlapping and interwoven 3D volumes. It takes parameters for dimensions and layering, then randomizes each layer's size and position to emphasize spatial complexity. By calculating gaps between layers, it establishes a dynamic hierarchy, reflecting the metaphor's implications of varied functions and interactions. The result is a collection of geometries that visually demonstrate depth, connectivity, and separation, capturing the essence of the proposed architectural design while allowing for exploration of light and shadow across the interlocking planes."""

#! python 3
function_code = """def generate_interlocking_layers(base_length, base_width, total_height, num_layers, layer_thickness):
    \"""
    Generates an architectural Concept Model based on the 'Interlocking Layers' metaphor. This function creates a composition
    of overlapping and interwoven volumes, emphasizing a complex spatial hierarchy and interaction between layers.

    Parameters:
    - base_length (float): The length of the base volume in meters.
    - base_width (float): The width of the base volume in meters.
    - total_height (float): The total height of the model in meters.
    - num_layers (int): The number of interlocking layers to generate.
    - layer_thickness (float): The thickness of each layer in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random

    # Seed for replicable randomness
    random.seed(42)

    # Calculate the gap between layers
    layer_gap = (total_height - (num_layers * layer_thickness)) / (num_layers - 1)

    # List to store the resulting breps
    layers = []

    # Base plane for the model
    current_height = 0

    for i in range(num_layers):
        # Randomize dimensions and position for dynamic relationships
        length_variation = random.uniform(0.8, 1.2) * base_length
        width_variation = random.uniform(0.8, 1.2) * base_width
        x_offset = random.uniform(-0.2, 0.2) * base_length
        y_offset = random.uniform(-0.2, 0.2) * base_width

        # Create a base box for each layer
        box_corners = [
            rg.Point3d(x_offset, y_offset, current_height),
            rg.Point3d(x_offset + length_variation, y_offset, current_height),
            rg.Point3d(x_offset + length_variation, y_offset + width_variation, current_height),
            rg.Point3d(x_offset, y_offset + width_variation, current_height),
            rg.Point3d(x_offset, y_offset, current_height + layer_thickness),
            rg.Point3d(x_offset + length_variation, y_offset, current_height + layer_thickness),
            rg.Point3d(x_offset + length_variation, y_offset + width_variation, current_height + layer_thickness),
            rg.Point3d(x_offset, y_offset + width_variation, current_height + layer_thickness)
        ]

        box = rg.Box(rg.BoundingBox(box_corners)).ToBrep()
        layers.append(box)

        # Update current height for next layer
        current_height += layer_thickness + layer_gap

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_interlocking_layers(10.0, 5.0, 15.0, 5, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_interlocking_layers(8.0, 4.0, 12.0, 6, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_interlocking_layers(15.0, 7.0, 20.0, 4, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_interlocking_layers(12.0, 6.0, 18.0, 3, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_interlocking_layers(9.0, 4.5, 14.0, 5, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
