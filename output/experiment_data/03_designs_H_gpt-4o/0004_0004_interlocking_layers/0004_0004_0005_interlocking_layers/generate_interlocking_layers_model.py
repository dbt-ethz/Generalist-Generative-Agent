# Created for 0004_0004_interlocking_layers.json

""" Summary:
The function `generate_interlocking_layers_model` creates an architectural concept model based on the "Interlocking Layers" metaphor by generating overlapping and integrated volumes. It defines a specified number of layers, each with a unique height and random horizontal offsets to reflect spatial complexity and connectivity. The model emphasizes both separation and unity through varying thickness and arrangement of layers, showcasing distinct yet interconnected spaces. By employing randomization within set parameters, the function captures the dynamic and cohesive nature of the metaphor, ultimately producing a visually rich and interactive architectural representation."""

#! python 3
function_code = """def generate_interlocking_layers_model(length=30, width=15, total_height=10, num_layers=6, layer_thickness=1.0, seed=123):
    \"""
    Generates an architectural Concept Model based on the 'Interlocking Layers' metaphor. The model is composed of a series
    of overlapping and integrated volumes that illustrate the concept of interaction and connectivity.

    Parameters:
    - length (float): The length of the model in meters.
    - width (float): The width of the model in meters.
    - total_height (float): The maximum height of the model in meters.
    - num_layers (int): The number of interlocking layers to create.
    - layer_thickness (float): The thickness of each layer in meters.
    - seed (int): The seed for random number generation to ensure replicability.

    Returns:
    - list of Rhino.Geometry.Brep: A list of 3D geometries representing the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the seed for reproducibility
    random.seed(seed)

    layers = []
    vertical_spacing = total_height / num_layers

    for i in range(num_layers):
        # Determine the base height and vertical offset for each layer
        base_height = i * vertical_spacing
        vertical_offset = random.uniform(-layer_thickness / 2, layer_thickness / 2)

        # Define the base plane and its transformation for interlocking
        base_plane = rg.Plane(rg.Point3d(0, 0, base_height + vertical_offset), rg.Vector3d.ZAxis)
        x_shift = random.uniform(-length * 0.1, length * 0.1)
        y_shift = random.uniform(-width * 0.1, width * 0.1)

        # Create the base rectangle for the layer
        rectangle = rg.Rectangle3d(base_plane, rg.Interval(-length / 2, length / 2), rg.Interval(-width / 2, width / 2))
        
        # Transform the rectangle to achieve interlocking effect
        transformation = rg.Transform.Translation(x_shift, y_shift, 0)
        rectangle.Transform(transformation)

        # Create a box from the rectangle
        box_corners = [
            rectangle.Corner(0), rectangle.Corner(1), rectangle.Corner(2), rectangle.Corner(3),
            rectangle.Corner(0) + rg.Vector3d(0, 0, layer_thickness),
            rectangle.Corner(1) + rg.Vector3d(0, 0, layer_thickness),
            rectangle.Corner(2) + rg.Vector3d(0, 0, layer_thickness),
            rectangle.Corner(3) + rg.Vector3d(0, 0, layer_thickness)
        ]
        
        # Convert the box to a Brep and add to the list
        layer_brep = rg.Brep.CreateFromBox(box_corners)
        layers.append(layer_brep)

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_interlocking_layers_model(length=25, width=10, total_height=12, num_layers=8, layer_thickness=1.5, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_interlocking_layers_model(length=40, width=20, total_height=15, num_layers=5, layer_thickness=2.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_interlocking_layers_model(length=35, width=18, total_height=20, num_layers=10, layer_thickness=1.2, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_interlocking_layers_model(length=50, width=25, total_height=18, num_layers=7, layer_thickness=1.0, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_interlocking_layers_model(length=45, width=22, total_height=14, num_layers=6, layer_thickness=1.8, seed=11)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
