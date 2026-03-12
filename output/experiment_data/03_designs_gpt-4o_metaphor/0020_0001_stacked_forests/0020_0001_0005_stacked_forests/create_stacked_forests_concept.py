# Created for 0020_0001_stacked_forests.json

""" Summary:
The provided function, `create_stacked_forests_concept`, generates an architectural concept model inspired by the "Stacked Forests" metaphor. It creates a multi-layered structure that mimics a tiered forest through a series of vertically stacked cylinders, each representing different forest layers. The function incorporates randomness to simulate organic growth, with slight offsets and scaling factors for each layer, enhancing spatial richness and diversity. By adjusting parameters like base size, number of layers, and height, the function produces varied geometries that embody vertical connectivity and hierarchy, reflecting the metaphor's key traits of depth and interaction within a natural ecosystem."""

#! python 3
function_code = """def create_stacked_forests_concept(base_size, num_layers, layer_height, randomness_seed):
    \"""
    Creates an architectural Concept Model based on the "Stacked Forests" metaphor. 
    This function generates a multi-layered, vertical organization resembling a dense, tiered forest.

    Parameters:
    - base_size (float): The base size of the model, determining the footprint of the bottom layer.
    - num_layers (int): The number of vertical layers to create, representing different forest tiers.
    - layer_height (float): The height of each layer, providing vertical separation between the tiers.
    - randomness_seed (int): A seed for randomness to ensure replicability in the variation of layers.

    Returns:
    - list: A list of 3D Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(randomness_seed)
    
    geometries = []
    
    # Base layer
    base_cylinder = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, base_size), layer_height).ToBrep(True, True)
    geometries.append(base_cylinder)
    
    # Create multiple layers with slight offsets and variations
    for i in range(1, num_layers):
        # Calculate a random offset for each layer to mimic organic growth
        offset_x = random.uniform(-0.2 * base_size, 0.2 * base_size)
        offset_y = random.uniform(-0.2 * base_size, 0.2 * base_size)
        
        # Scale factor to create variation between layers
        scale_factor = 1.0 - (0.1 * random.random())
        
        # Define the transformation
        move_vector = rg.Vector3d(offset_x, offset_y, i * layer_height)
        scale_vec = rg.Vector3d(scale_factor, scale_factor, 1.0)
        
        # Apply transformations
        layer_cylinder = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, base_size * scale_factor), layer_height).ToBrep(True, True)
        layer_cylinder.Transform(rg.Transform.Translation(move_vector))
        
        # Add to the list of geometries
        geometries.append(layer_cylinder)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept(5.0, 10, 2.0, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept(3.5, 8, 1.5, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept(4.0, 12, 3.0, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept(6.0, 15, 2.5, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept(2.5, 5, 1.0, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
