# Created for 0004_0004_interlocking_layers.json

""" Summary:
The function `create_interlocking_layers_model` generates an architectural concept model based on the metaphor of "Interlocking Layers" by creating a series of overlapping planes or volumes. It takes parameters such as base dimensions, height, number of layers, and offsets to define the model's structure. Each layer is positioned vertically and offset horizontally to illustrate spatial complexity and interaction, reflecting the metaphor's emphasis on connectivity and distinctiveness. The model visually represents the balance between openness and separation, enabling fluid transitions between spaces while maintaining their unique identities. This approach fosters a rich user experience through layered architectural forms."""

#! python 3
function_code = """def create_interlocking_layers_model(base_length, base_width, height, num_layers, layer_thickness, layer_offset):
    \"""
    Creates an architectural Concept Model based on the 'Interlocking Layers' metaphor. This model consists of overlapping and integrated planes or volumes that illustrate interaction and connectivity.

    Parameters:
    - base_length (float): The length of the base footprint of the model in meters.
    - base_width (float): The width of the base footprint of the model in meters.
    - height (float): The total height of the model in meters.
    - num_layers (int): The number of layers to create in the model.
    - layer_thickness (float): The thickness of each layer in meters.
    - layer_offset (float): The horizontal offset between consecutive layers in meters.

    Returns:
    - list: A list of Brep geometries representing the interlocking layers of the model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set seed for reproducibility
    random.seed(42)

    # Calculate vertical spacing based on total height and number of layers
    vertical_spacing = height / num_layers

    # List to hold the resulting geometry
    layers = []

    for i in range(num_layers):
        # Calculate layer position and offset
        z_position = i * vertical_spacing
        x_offset = (i % 2) * layer_offset
        y_offset = ((i + 1) % 2) * layer_offset

        # Create a base rectangle for the layer
        base_plane = rg.Plane.WorldXY
        base_plane.OriginZ = z_position
        rectangle = rg.Rectangle3d(base_plane, base_length, base_width)

        # Offset the rectangle to create an interlocking effect
        rectangle.Transform(rg.Transform.Translation(x_offset, y_offset, 0))

        # Create a solid extrusion to form a layer volume
        extrusion_vector = rg.Vector3d(0, 0, layer_thickness)
        layer_brep = rg.Brep.CreateFromBox([rectangle.Corner(0), rectangle.Corner(1), rectangle.Corner(2), rectangle.Corner(3), extrusion_vector])

        if layer_brep:
            layers.append(layer_brep)

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(5.0, 3.0, 10.0, 4, 0.5, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(6.0, 4.0, 12.0, 5, 0.6, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(7.0, 5.0, 15.0, 6, 0.4, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(8.0, 6.0, 20.0, 3, 0.7, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(4.0, 2.5, 8.0, 3, 0.3, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
