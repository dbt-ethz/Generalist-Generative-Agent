# Created for 0004_0001_interlocking_layers.json

""" Summary:
The function `create_interlocking_layers_model` generates an architectural concept model inspired by the metaphor of "Interlocking Layers." It creates multiple interconnected planes or volumes, each transformed through unique orientations and height variations to reflect structural complexity. By varying the dimensions and applying random translations, the model illustrates dynamic spatial relationships, capturing the essence of overlapping layers that provide both openness and privacy. The resulting geometries emphasize visual depth and intricate silhouettes, aligning with the design task's requirement for contrasting open and closed spaces, ultimately creating a rich architectural experience that embodies the metaphor's characteristics."""

#! python 3
function_code = """def create_interlocking_layers_model(layer_count, base_length, base_width, height_variation):
    \"""
    Creates an architectural Concept Model based on the 'Interlocking Layers' metaphor.
    
    This function generates a series of interconnected planes or volumes that are physically interlocked.
    Each layer is differentiated by a unique orientation and height, capturing the structural complexity 
    and spatial variety of the design metaphor.
    
    Parameters:
    - layer_count (int): The number of layers to create in the model.
    - base_length (float): The base length of each layer in meters.
    - base_width (float): The base width of each layer in meters.
    - height_variation (float): The maximum variation in height for each layer in meters.

    Returns:
    - list: A list of Brep geometries representing the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set random seed for replicability
    random.seed(42)

    layers = []

    # Create each layer with a unique transformation
    for i in range(layer_count):
        # Randomly choose a height variation
        height = random.uniform(-height_variation, height_variation)

        # Create a base plane for the layer
        base_plane = rg.Plane.WorldXY
        base_plane.OriginZ = i * (base_width / 2)

        # Create the base rectangle
        rect = rg.Rectangle3d(base_plane, base_length, base_width)

        # Create a surface from the rectangle
        surface = rg.Brep.CreateFromCornerPoints(rect.Corner(0), rect.Corner(1), rect.Corner(2), rect.Corner(3), 0.01)

        # Apply a translation to simulate the interlocking effect
        translation_vector = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), height)
        translation = rg.Transform.Translation(translation_vector)

        # Transform the surface
        surface.Transform(translation)

        # Add the transformed surface to the layers list
        layers.append(surface)

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(5, 10.0, 8.0, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(3, 12.0, 9.0, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(4, 15.0, 10.0, 5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(6, 20.0, 15.0, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(7, 8.0, 6.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
