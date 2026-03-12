# Created for 0004_0002_interlocking_layers.json

""" Summary:
The provided function generates an architectural concept model based on the "Interlocking Layers" metaphor by creating a series of overlapping and interwoven layers. Each layer is defined by parameters such as base dimensions, height, and thickness, allowing for a customizable model. The function employs randomness in rotation to enhance the complexity and visual depth of the structure, mimicking the intricate spatial hierarchy implied by the metaphor. By stacking these layers with varying heights and orientations, the model illustrates dynamic spatial relationships and connectivity, embodying the essence of the metaphor through a tangible architectural representation."""

#! python 3
function_code = """def create_interlocking_layers_model(base_length, base_width, num_layers, layer_height, layer_thickness):
    \"""
    Creates an architectural Concept Model based on the 'Interlocking Layers' metaphor. The model consists of overlapping
    and interwoven planes or volumes that establish spatial hierarchy and dynamic spatial relationships.

    Parameters:
    - base_length (float): The base length of the model in meters.
    - base_width (float): The base width of the model in meters.
    - num_layers (int): The number of interlocking layers to generate.
    - layer_height (float): The height of each layer in meters.
    - layer_thickness (float): The thickness of each layer in meters.

    Returns:
    - List of Rhino.Geometry.Brep: A list of 3D breps representing the interlocking layered structure.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a seed for randomness to ensure replicability
    random.seed(42)

    # List to store the generated breps
    breps = []

    # Base plane for the model
    base_plane = rg.Plane.WorldXY

    # Start position for stacking layers
    current_height = 0

    for i in range(num_layers):
        # Random rotation angle for each layer
        angle = random.uniform(-0.5, 0.5)  # Radians

        # Create a base rectangle for the layer
        rectangle = rg.Rectangle3d(base_plane, base_length, base_width)

        # Create a surface from the rectangle
        surface = rg.Surface.CreateExtrusion(rectangle.ToNurbsCurve(), rg.Vector3d(0, 0, layer_thickness))

        # Rotate the surface randomly around the Z-axis
        rotation_transform = rg.Transform.Rotation(angle, rg.Vector3d.ZAxis, rectangle.Center)
        surface.Transform(rotation_transform)

        # Translate the layer to the current height
        translation_transform = rg.Transform.Translation(0, 0, current_height)
        surface.Transform(translation_transform)

        # Add the surface to the breps list
        breps.append(surface.ToBrep())

        # Increase the height for the next layer
        current_height += layer_height

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(5.0, 3.0, 10, 0.2, 0.05)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(4.0, 2.5, 8, 0.15, 0.04)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(6.0, 4.0, 12, 0.25, 0.06)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(7.0, 5.0, 15, 0.3, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(3.5, 2.0, 5, 0.1, 0.03)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
