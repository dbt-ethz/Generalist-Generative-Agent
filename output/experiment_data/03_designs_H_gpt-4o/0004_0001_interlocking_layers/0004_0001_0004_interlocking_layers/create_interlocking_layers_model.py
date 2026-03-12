# Created for 0004_0001_interlocking_layers.json

""" Summary:
The provided function generates an architectural concept model by creating a series of interlocking layers, reflecting the metaphor of "Interlocking Layers." It takes parameters such as base dimensions, number of layers, layer thickness, and angle variations to produce distinct yet interconnected volumes. Each layer is randomly adjusted in size, thickness, and rotation, fostering a dynamic interplay that emphasizes structural complexity and spatial variety. The resulting model visually embodies depth and movement, showcasing both open and closed spaces while maintaining functional connections, thereby encapsulating the essence of the metaphor in a tangible architectural form."""

#! python 3
function_code = """def create_interlocking_layers_model(base_dim, num_layers, layer_thickness, angle_variation, seed):
    \"""
    Creates an architectural Concept Model based on the 'Interlocking Layers' metaphor.

    This function generates a series of interconnected volumes that embody the idea of interlocking layers,
    creating a dynamic spatial relationship and visual depth with overlapping forms.

    Parameters:
    - base_dim: A tuple (length, width, height) representing the base dimensions of the model.
    - num_layers: Integer specifying the number of layers to create.
    - layer_thickness: Float representing the thickness of each layer.
    - angle_variation: Float representing the maximum angle variation for each layer orientation in degrees.
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
    length, width, height = base_dim

    # Initialize a list to hold the Brep geometries
    layers = []

    # Calculate the vertical spacing between layers
    vertical_spacing = height / num_layers

    for i in range(num_layers):
        # Create a base plane for each layer
        base_plane = rg.Plane.WorldXY
        base_plane.Translate(rg.Vector3d(0, 0, i * vertical_spacing))

        # Define the base rectangle for the layer with some randomness for variation
        rect_length = random.uniform(length * 0.8, length * 1.2)
        rect_width = random.uniform(width * 0.8, width * 1.2)

        # Create a rectangle for the layer
        rectangle = rg.Rectangle3d(base_plane, rect_length, rect_width)

        # Extrude the rectangle to create a solid layer
        extrusion_vector = rg.Vector3d(0, 0, layer_thickness)
        extrude_curve = rectangle.ToNurbsCurve()
        extrusion = rg.Extrusion.Create(extrude_curve, layer_thickness, True)
        layer_brep = extrusion.ToBrep()

        # Randomly rotate the layer around its center to create the interlocking effect
        rotation_angle = random.uniform(-angle_variation, angle_variation)
        rotation_axis = rg.Vector3d(0, 0, 1)
        rotation_center = rg.Point3d(0, 0, i * vertical_spacing + layer_thickness / 2)
        rotation_transform = rg.Transform.Rotation(math.radians(rotation_angle), rotation_axis, rotation_center)
        layer_brep.Transform(rotation_transform)

        # Add the layer to the list
        layers.append(layer_brep)

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model((10, 5, 20), 5, 2, 15, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model((15, 10, 30), 8, 3, 10, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model((12, 6, 25), 6, 2.5, 20, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model((8, 4, 15), 4, 1.5, 25, 12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model((20, 10, 40), 7, 4, 30, 101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
