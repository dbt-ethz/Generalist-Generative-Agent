# Created for 0004_0001_interlocking_layers.json

""" Summary:
The provided function, `create_interlocking_layers_model`, generates an architectural concept model based on the metaphor of "Interlocking Layers." It creates a series of overlapping, interconnected planes defined by parameters such as base dimensions, layer height, and shift factors. Each layer is translated randomly within specified limits to enhance spatial complexity, resulting in a dynamic arrangement that visually embodies the metaphor's key traits. By stacking these layers with varying shifts, the model achieves both openness and separation, fostering distinct functional areas while maintaining a cohesive design. The output is a collection of Brep geometries representing this intricate structure."""

#! python 3
function_code = """def create_interlocking_layers_model(base_length, base_width, layer_height, num_layers, shift_factor):
    \"""
    Creates a Concept Model based on the 'Interlocking Layers' metaphor. This model features overlapping and interconnected
    planes or volumes that create dynamic spatial relationships and visual depth.

    Parameters:
    - base_length: float, the length of the base layer in meters.
    - base_width: float, the width of the base layer in meters.
    - layer_height: float, the height of each individual layer in meters.
    - num_layers: int, the total number of layers to stack.
    - shift_factor: float, the maximum shift distance for each layer in meters, affecting the interlocking nature.

    Returns:
    - A list of Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a seed for randomness
    random.seed(42)

    layers = []

    for i in range(num_layers):
        # Calculate the shift for the current layer
        shift_x = random.uniform(-shift_factor, shift_factor)
        shift_y = random.uniform(-shift_factor, shift_factor)

        # Create a base rectangle for the current layer
        base_plane = rg.Plane.WorldXY
        base_rect = rg.Rectangle3d(base_plane, base_length, base_width)

        # Move the rectangle to the correct height
        translation_vector = rg.Vector3d(shift_x, shift_y, i * layer_height)
        base_rect.Transform(rg.Transform.Translation(translation_vector))

        # Extrude the rectangle to create a solid layer
        extrusion_vector = rg.Vector3d(0, 0, layer_height)
        layer_brep = rg.Brep.CreateFromBox(base_rect.ToNurbsCurve().GetBoundingBox(rg.Plane.WorldXY))

        # Add the current layer to the list
        layers.append(layer_brep)

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(5.0, 3.0, 0.5, 10, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(4.0, 2.0, 0.3, 8, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(6.0, 4.0, 0.4, 12, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(7.0, 5.0, 0.6, 15, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(8.0, 3.5, 0.7, 5, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
