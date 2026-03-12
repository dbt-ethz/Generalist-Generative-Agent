# Created for 0004_0004_interlocking_layers.json

""" Summary:
The function `create_interlocking_layers_model_v2` generates an architectural concept model based on the metaphor of "Interlocking Layers." It constructs a series of overlapping planes or volumes that embody the themes of interaction and connectivity. By varying layer thickness, orientation, and horizontal displacement, the model visually represents the complexity and dynamic nature of interlocking elements, ensuring a rich spatial experience. The function uses randomization to create unique arrangements, emphasizing both openness and separation, aligning with the metaphor's intent to foster distinct yet interconnected spaces. The result is a cohesive architectural form that embodies the conceptual vision."""

#! python 3
function_code = """def create_interlocking_layers_model_v2(base_length, base_width, total_height, num_layers, layer_thickness, displacement_factor, randomness_seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Interlocking Layers' metaphor. This model consists of overlapping
    and integrated planes or volumes illustrating interaction and connectivity with a focus on varying orientations and 
    offsets to enhance the spatial complexity.

    Parameters:
    - base_length (float): The length of the base footprint of the model in meters.
    - base_width (float): The width of the base footprint of the model in meters.
    - total_height (float): The total height of the model in meters.
    - num_layers (int): The number of layers to create in the model.
    - layer_thickness (float): The thickness of each layer in meters.
    - displacement_factor (float): Factor to control the horizontal displacement of layers for interlocking effect.
    - randomness_seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - list of Rhino.Geometry.Brep: A list of 3D geometries representing the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random
    from math import sin, cos, radians

    # Set seed for reproducibility
    random.seed(randomness_seed)

    # Calculate vertical spacing and initialize list for layers
    vertical_spacing = total_height / num_layers
    layers = []

    for i in range(num_layers):
        # Base plane for the current layer
        z_position = i * vertical_spacing
        base_plane = rg.Plane.WorldXY
        base_plane.OriginZ = z_position

        # Randomize rotation and displacement for interlocking effect
        angle = random.uniform(-30, 30)  # Rotation angle in degrees
        displacement = displacement_factor * sin(radians(angle))
        x_offset = displacement * cos(radians(angle))
        y_offset = displacement * sin(radians(angle))

        # Create a rectangle for the layer with random rotation and offset
        rectangle = rg.Rectangle3d(base_plane, base_length, base_width)
        rectangle.Transform(rg.Transform.Translation(x_offset, y_offset, 0))
        rectangle.Transform(rg.Transform.Rotation(radians(angle), rg.Vector3d.ZAxis, rectangle.Center))

        # Extrude the rectangle to create a solid volume
        extrusion_vector = rg.Vector3d(0, 0, layer_thickness)
        layer_brep = rg.Brep.CreateFromBox([rectangle.Corner(0), rectangle.Corner(1), rectangle.Corner(2), 
                                            rectangle.Corner(3), extrusion_vector])

        if layer_brep:
            layers.append(layer_brep)

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model_v2(5.0, 3.0, 10.0, 4, 0.5, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model_v2(7.0, 4.0, 15.0, 6, 0.3, 0.1, randomness_seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model_v2(6.0, 2.5, 12.0, 5, 0.4, 0.15, randomness_seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model_v2(4.0, 2.0, 8.0, 3, 0.6, 0.25, randomness_seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model_v2(8.0, 5.0, 20.0, 8, 0.4, 0.3, randomness_seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
