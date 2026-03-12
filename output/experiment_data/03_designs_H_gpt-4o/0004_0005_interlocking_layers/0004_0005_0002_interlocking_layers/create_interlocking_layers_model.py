# Created for 0004_0005_interlocking_layers.json

""" Summary:
The provided function generates an architectural concept model based on the "Interlocking Layers" metaphor by creating a series of overlapping and intersecting planes. It utilizes randomization to position and rotate each layer, enhancing the structural complexity and dynamic spatial relationships. Each layer's dimensions are varied slightly to emphasize the multifaceted nature of the design. The function parameters allow customization of the model's size, height, and number of layers, ensuring diverse spatial experiences that balance privacy and openness. Ultimately, the resulting geometries visually represent the metaphor's intent, illustrating the intricate interplay between layers in the architectural form."""

#! python 3
function_code = """def create_interlocking_layers_model(base_length, base_width, height, num_layers, layer_thickness, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Interlocking Layers' metaphor.

    This model is composed of intersecting and overlapping planes or volumes to express the dynamic
    and multifaceted nature of interlocking layers. Each layer is uniquely oriented and positioned
    to enhance the complexity and spatial relationships of the design.

    Parameters:
    - base_length (float): The length of the base plane in meters.
    - base_width (float): The width of the base plane in meters.
    - height (float): The maximum height of the structure in meters.
    - num_layers (int): The number of interlocking layers to generate.
    - layer_thickness (float): The thickness of each individual layer in meters.
    - seed (int): Random seed for reproducible results. Default is 42.

    Returns:
    - List of Rhino.Geometry.Brep: A list of 3D geometries representing the layers of the structure.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    random.seed(seed)
    geometries = []
    z_position = 0

    for i in range(num_layers):
        # Calculate offsets and rotation for dynamic layering effect
        offset_x = random.uniform(-base_length * 0.1, base_length * 0.1)
        offset_y = random.uniform(-base_width * 0.1, base_width * 0.1)
        angle = random.uniform(-15, 15)  # Small rotation angle for interlocking effect

        # Create a base plane for the layer and apply rotation
        plane = rg.Plane(rg.Point3d(offset_x, offset_y, z_position), rg.Vector3d.ZAxis)
        plane.Rotate(math.radians(angle), plane.ZAxis)

        # Define the layer dimensions
        layer_length = base_length * random.uniform(0.8, 1.2)
        layer_width = base_width * random.uniform(0.8, 1.2)

        # Create a surface for the layer and convert to a Brep
        corner1 = plane.PointAt(-layer_length / 2, -layer_width / 2)
        corner2 = plane.PointAt(layer_length / 2, -layer_width / 2)
        corner3 = plane.PointAt(layer_length / 2, layer_width / 2)
        corner4 = plane.PointAt(-layer_length / 2, layer_width / 2)
        surface = rg.NurbsSurface.CreateFromCorners(corner1, corner2, corner3, corner4)

        if surface:
            brep = surface.ToBrep()
            geometries.append(brep)

        # Increment z_position for the next layer
        z_position += height / num_layers

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(10.0, 5.0, 15.0, 5, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(8.0, 4.0, 12.0, 6, 0.3, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(15.0, 10.0, 20.0, 4, 1.0, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(12.0, 6.0, 18.0, 3, 0.4, seed=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(9.0, 4.5, 14.0, 7, 0.6, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
