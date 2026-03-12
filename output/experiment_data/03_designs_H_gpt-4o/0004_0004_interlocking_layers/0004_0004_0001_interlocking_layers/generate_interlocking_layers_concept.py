# Created for 0004_0004_interlocking_layers.json

""" Summary:
The provided function, `generate_interlocking_layers_concept`, creates an architectural concept model based on the metaphor of "Interlocking Layers." It generates a series of overlapping planes or volumes, emphasizing spatial interaction and connectivity. By defining parameters like base dimensions, height, number of layers, and layer thickness, the function produces geometries that reflect the complexity and depth of the metaphor. Each layer is randomly rotated and offset, illustrating the balance of separation and unity while maintaining distinct yet interconnected spaces. This approach captures the dynamic nature of the design, facilitating a rich user experience through varied functional areas."""

#! python 3
function_code = """def generate_interlocking_layers_concept(base_length, base_width, total_height, num_layers, layer_thickness, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Interlocking Layers' metaphor.

    This function creates a series of interlocking planes or volumes that illustrate spatial interaction 
    and connectivity. Each layer is positioned and rotated to reflect the interplay between open and 
    enclosed spaces, showcasing the balance between separation and unity.

    Parameters:
    - base_length (float): The length of the base footprint of the model in meters.
    - base_width (float): The width of the base footprint of the model in meters.
    - total_height (float): The total height of the model in meters.
    - num_layers (int): The number of interlocking layers to generate.
    - layer_thickness (float): The thickness of each layer in meters.
    - seed (int): Random seed for replicable results. Default is 42.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    # Calculate the vertical spacing between layers
    vertical_spacing = total_height / num_layers

    # Initialize list to hold Brep geometries
    layers = []

    for i in range(num_layers):
        # Determine the height for this layer
        z_position = i * vertical_spacing

        # Randomly determine rotation and offset for each layer
        rotation_angle = random.uniform(-30, 30)  # Rotation angle in degrees
        x_offset = random.uniform(-base_length * 0.1, base_length * 0.1)
        y_offset = random.uniform(-base_width * 0.1, base_width * 0.1)

        # Create a base plane for the layer
        base_plane = rg.Plane.WorldXY
        base_plane.OriginZ = z_position

        # Create a rectangle representing the base of the layer
        rectangle = rg.Rectangle3d(base_plane, base_length, base_width)

        # Create an extrusion from the rectangle to form a layer volume
        extrusion_vector = rg.Vector3d(0, 0, layer_thickness)
        layer_brep = rg.Brep.CreateFromBox([rectangle.Corner(0), rectangle.Corner(1), rectangle.Corner(2), rectangle.Corner(3), extrusion_vector])

        if layer_brep:
            # Apply rotation and translation to the layer
            rotation_transform = rg.Transform.Rotation(rg.Math.ToRadians(rotation_angle), rg.Vector3d.ZAxis, base_plane.Origin)
            translation_transform = rg.Transform.Translation(x_offset, y_offset, 0)
            layer_brep.Transform(rotation_transform)
            layer_brep.Transform(translation_transform)

            # Add the transformed layer to the list
            layers.append(layer_brep)

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_interlocking_layers_concept(10.0, 5.0, 15.0, 6, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_interlocking_layers_concept(8.0, 4.0, 12.0, 5, 0.3, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_interlocking_layers_concept(15.0, 7.0, 20.0, 8, 0.4, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_interlocking_layers_concept(12.0, 6.0, 18.0, 7, 0.6, seed=55)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_interlocking_layers_concept(20.0, 10.0, 25.0, 10, 0.8, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
