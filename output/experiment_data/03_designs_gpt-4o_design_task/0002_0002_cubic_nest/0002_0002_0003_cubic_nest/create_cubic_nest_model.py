# Created for 0002_0002_cubic_nest.json

""" Summary:
The function `create_cubic_nest_model` generates an architectural concept model based on the "Cubic nest" metaphor by creating a series of nested cubic volumes. It uses parameters such as base size, number of layers, and size variation to define the dimensions and overlaps of the cubes. Each layer is created with a random offset to enhance the interlocking and protective nature of the design, reflecting spatial complexity and inviting exploration. This results in a dynamic architectural form that embodies the metaphor's essence of shelter and interconnectedness, while also allowing for varying material representations and orientations to reinforce these themes."""

#! python 3
function_code = """def create_cubic_nest_model(base_size=5, num_layers=3, cube_size_variation=0.2, overlap_factor=0.3, random_seed=42):
    \"""
    Generate an architectural Concept Model based on the 'Cubic nest' metaphor, using a composition of nested cubic volumes.
    
    Parameters:
    - base_size (float): The base size of the largest cube in meters.
    - num_layers (int): Number of layers of nested cubic volumes.
    - cube_size_variation (float): The factor by which the size of the cubes can vary between layers.
    - overlap_factor (float): The factor determining how much cubes overlap with each other.
    - random_seed (int): Seed for random number generation to ensure replicable results.
    
    Returns:
    - List of Brep: A list of 3D geometries representing the nested cubic volumes.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(random_seed)
    
    geometries = []
    current_size = base_size

    for i in range(num_layers):
        # Calculate cube size with variation
        size_variation = current_size * cube_size_variation * (random.random() - 0.5)
        cube_size = current_size + size_variation
        
        # Create cube base point with random offset to create overlaps
        offset_x = cube_size * overlap_factor * (random.random() - 0.5)
        offset_y = cube_size * overlap_factor * (random.random() - 0.5)
        offset_z = cube_size * overlap_factor * (random.random() - 0.5)
        
        # Create a bounding box for the cube
        base_point = rg.Point3d(offset_x, offset_y, offset_z)
        box = rg.Box(rg.Plane.WorldXY, rg.Interval(base_point.X, base_point.X + cube_size), 
                     rg.Interval(base_point.Y, base_point.Y + cube_size), 
                     rg.Interval(base_point.Z, base_point.Z + cube_size))
        
        # Convert box to Brep
        brep = box.ToBrep()
        geometries.append(brep)
        
        # Decrease the size for the next layer
        current_size *= (1 - cube_size_variation)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_model(base_size=10, num_layers=5, cube_size_variation=0.1, overlap_factor=0.2, random_seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_model(base_size=8, num_layers=4, cube_size_variation=0.15, overlap_factor=0.25, random_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_model(base_size=6, num_layers=6, cube_size_variation=0.3, overlap_factor=0.4, random_seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_model(base_size=7, num_layers=3, cube_size_variation=0.25, overlap_factor=0.1, random_seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_model(base_size=12, num_layers=2, cube_size_variation=0.05, overlap_factor=0.1, random_seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
