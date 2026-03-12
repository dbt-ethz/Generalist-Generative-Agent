# Created for 0004_0003_interlocking_layers.json

""" Summary:
The function `generate_interlocking_layers_model` creates an architectural concept model based on the metaphor of "Interlocking Layers." It generates 3D geometries that embody overlapping planes and volumes, simulating a dynamic interplay of layers. By using random offsets for each layer, the function achieves a sense of complexity and movement, reflecting the metaphor's emphasis on unity and distinction. The parameters allow for customization in size, thickness, and the number of layers, facilitating diverse spatial experiences. Ultimately, the model showcases interconnectedness while maintaining unique functional areas, embodying the metaphor's essence through thoughtful design."""

#! python 3
function_code = """def generate_interlocking_layers_model(base_length, base_width, num_layers, layer_thickness, max_offset, seed):
    \"""
    Generates an architectural Concept Model based on the 'Interlocking Layers' metaphor.

    This function creates a structure with volumes or planes that intricately weave and intersect each other,
    using varying heights and offsets to simulate layers folding over one another, highlighting both unity and distinction.

    Parameters:
    - base_length (float): The length of the base footprint of the model in meters.
    - base_width (float): The width of the base footprint of the model in meters.
    - num_layers (int): The number of interlocking layers to create.
    - layer_thickness (float): The thickness of each layer in meters.
    - max_offset (float): The maximum offset for each layer in meters to create an interlocking effect.
    - seed (int): A seed for random number generation to ensure replicability.

    Returns:
    - List of Rhino.Geometry.Brep objects representing the 3D geometries of the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set random seed for reproducibility
    random.seed(seed)

    # List to store the resulting 3D geometries
    geometries = []

    for i in range(num_layers):
        # Calculate offsets for interlocking effect
        offset_x = random.uniform(-max_offset, max_offset)
        offset_y = random.uniform(-max_offset, max_offset)
        offset_z = i * layer_thickness

        # Define the base plane for the layer
        plane = rg.Plane.WorldXY
        plane.Translate(rg.Vector3d(offset_x, offset_y, offset_z))

        # Create a rectangle profile for the layer
        rectangle = rg.Rectangle3d(plane, base_length, base_width)

        # Extrude the rectangle to create a 3D layer
        extrusion_vector = rg.Vector3d(0, 0, layer_thickness)
        layer_brep = rg.Brep.CreateFromBox([
            rectangle.Corner(0), rectangle.Corner(1), rectangle.Corner(2), rectangle.Corner(3),
            rectangle.Corner(0) + extrusion_vector, rectangle.Corner(1) + extrusion_vector,
            rectangle.Corner(2) + extrusion_vector, rectangle.Corner(3) + extrusion_vector
        ])

        # Add the layer to the list of geometries
        if layer_brep:
            geometries.append(layer_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_interlocking_layers_model(10.0, 5.0, 6, 0.2, 1.0, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_interlocking_layers_model(15.0, 10.0, 4, 0.3, 2.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_interlocking_layers_model(12.0, 8.0, 5, 0.25, 1.5, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_interlocking_layers_model(20.0, 15.0, 8, 0.5, 3.0, 100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_interlocking_layers_model(8.0, 4.0, 3, 0.4, 0.8, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
