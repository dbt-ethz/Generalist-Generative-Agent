# Created for 0004_0001_interlocking_layers.json

""" Summary:
The function `create_interlocking_layers_model` generates an architectural concept model inspired by the metaphor of "Interlocking Layers." It constructs a series of interrelated planes or volumes, emphasizing dynamic spatial relationships and visual complexity. The function takes parameters such as base dimensions, the number of layers, and variations in orientation and size. Each layer is created by adjusting its dimensions and applying random rotations to simulate interlocking effects. The result is a collection of Brep geometries that visually represent the metaphor, showcasing a rich interplay of open and closed spaces, depth, and structural integration, reflecting the essence of the design task."""

#! python 3
function_code = """def create_interlocking_layers_model(base_dims, num_layers, layer_variation, seed):
    \"""
    Creates an architectural Concept Model based on the 'Interlocking Layers' metaphor.
    
    This function generates a dynamic architectural form through a series of interlocked layers.
    The model is characterized by overlapping volumes and planes that create varied spatial experiences,
    emphasizing openness, separation, and visual depth.

    Parameters:
    - base_dims: A tuple (width, depth, height) representing the overall base dimensions of the model.
    - num_layers: Integer specifying the number of interlocking layers.
    - layer_variation: Float representing the maximum variation in layer dimensions and orientation.
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
    width, depth, height = base_dims

    # Initialize a list to hold the Brep geometries
    geometries = []

    # Calculate base layer height
    base_layer_height = height / num_layers

    for i in range(num_layers):
        # Define the base plane for the layer
        base_plane = rg.Plane.WorldXY
        base_plane.Translate(rg.Vector3d(0, 0, i * base_layer_height))

        # Randomly adjust the dimensions and orientation for variation
        layer_width = width * random.uniform(0.8, 1.2)
        layer_depth = depth * random.uniform(0.8, 1.2)
        rotation_angle = random.uniform(-layer_variation, layer_variation)

        # Create the base rectangle
        rectangle = rg.Rectangle3d(base_plane, layer_width, layer_depth)

        # Extrude the rectangle to create a solid volume
        extrusion_vector = rg.Vector3d(0, 0, base_layer_height)
        extrude_curve = rectangle.ToNurbsCurve()
        extrusion = rg.Extrusion.Create(extrude_curve, base_layer_height, True)
        layer_brep = extrusion.ToBrep()

        # Apply rotation to introduce the interlocking effect
        rotation_center = rg.Point3d(0, 0, i * base_layer_height)
        rotation_transform = rg.Transform.Rotation(math.radians(rotation_angle), rg.Vector3d(0, 0, 1), rotation_center)
        layer_brep.Transform(rotation_transform)
        
        # Add the transformed layer to the geometries list
        geometries.append(layer_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model((10, 5, 20), 5, 15, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model((15, 10, 30), 4, 10, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model((12, 8, 25), 6, 20, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model((20, 15, 40), 3, 25, 101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model((18, 12, 36), 7, 30, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
