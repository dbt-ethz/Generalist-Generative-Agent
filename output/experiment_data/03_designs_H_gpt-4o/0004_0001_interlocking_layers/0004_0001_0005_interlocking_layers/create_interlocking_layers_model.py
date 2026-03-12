# Created for 0004_0001_interlocking_layers.json

""" Summary:
The function `create_interlocking_layers_model` generates an architectural concept model that embodies the metaphor of "Interlocking Layers." It creates multiple overlapping volumes, each representing a distinct layer. By utilizing random variations in size and rotation, the function simulates the dynamic interplay between layers, enhancing visual complexity and spatial depth. The model prioritizes both openness and separation, allowing for intimate spaces while maintaining connectivity. The resulting list of geometries showcases the intricate silhouette and structural complexity, reflecting the metaphor's essence of interconnectedness and diverse spatial interactions, ultimately creating a rich architectural experience."""

#! python 3
function_code = """def create_interlocking_layers_model(base_dimensions, num_layers, layer_thickness, max_rotation, seed):
    \"""
    Creates an architectural Concept Model based on the 'Interlocking Layers' metaphor.
    
    This function generates a series of interconnected volumes that embody the idea of interlocking layers.
    It creates dynamic spatial relationships and visual depth through overlapping and interconnected forms.
    
    Inputs:
    - base_dimensions: A tuple (length, width, height) representing the overall base dimensions of the model.
    - num_layers: Integer specifying the number of layers to create.
    - layer_thickness: Float representing the thickness of each layer.
    - max_rotation: Float for the maximum rotation angle for the layers in degrees.
    - seed: Integer for the random seed to ensure consistent results.
    
    Outputs:
    - List of RhinoCommon Brep objects representing the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for reproducibility
    random.seed(seed)

    # Unpack base dimensions
    length, width, height = base_dimensions

    # Initialize a list to hold the Brep geometries
    geometries = []

    # Calculate the vertical spacing between layers
    vertical_spacing = height / num_layers

    for i in range(num_layers):
        # Define the base plane for the layer
        base_plane = rg.Plane.WorldXY
        base_plane.Translate(rg.Vector3d(0, 0, i * vertical_spacing))

        # Define the dimensions of the current layer
        layer_length = length * random.uniform(0.8, 1.2)
        layer_width = width * random.uniform(0.8, 1.2)

        # Create a box as the solid representation of the layer
        box = rg.Box(base_plane, rg.Interval(-layer_length / 2, layer_length / 2),
                     rg.Interval(-layer_width / 2, layer_width / 2),
                     rg.Interval(-layer_thickness / 2, layer_thickness / 2))

        # Randomly rotate the box around its center
        rotation_angle = math.radians(random.uniform(-max_rotation, max_rotation))
        rotation_transform = rg.Transform.Rotation(rotation_angle, base_plane.ZAxis, box.Center)
        box.Transform(rotation_transform)

        # Convert the box to a Brep and add it to the list
        brep_layer = box.ToBrep()
        geometries.append(brep_layer)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model((10, 10, 30), 5, 2, 45, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model((15, 15, 40), 7, 3, 60, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model((12, 12, 24), 6, 1.5, 30, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model((20, 10, 50), 4, 2.5, 90, 101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model((8, 16, 32), 8, 1, 75, 25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
