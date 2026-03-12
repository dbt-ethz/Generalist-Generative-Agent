# Created for 0005_0002_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_concept_model` generates an architectural concept model by creating a series of fragmented modules that embody the "Distorted puzzle" metaphor. It defines a base module size and utilizes random variations in dimensions to create visually dynamic forms, ensuring each module appears slightly misaligned. By applying random translations, the modules overlap and stack in a labyrinthine arrangement, fostering unexpected spatial relationships. This method encourages exploration and interaction, aligning with the metaphor's emphasis on complexity and playful cohesion. The result is a coherent yet intriguing architectural composition that invites curiosity in its users."""

#! python 3
function_code = """def create_distorted_puzzle_concept_model(module_size, num_modules, max_overlap, seed):
    \"""
    Generates an architectural Concept Model based on the 'Distorted puzzle' metaphor.

    Parameters:
    - module_size (float): The base size of each module in meters.
    - num_modules (int): The number of modules to create.
    - max_overlap (float): The maximum amount of overlap between modules in meters.
    - seed (int): The seed for random number generation to ensure replicability.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometry of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Initialize list to hold the created geometries
    geometries = []
    
    # Define a helper function to create a distorted module
    def create_module(base_size):
        width = base_size + random.uniform(-0.2, 0.2) * base_size
        depth = base_size + random.uniform(-0.2, 0.2) * base_size
        height = base_size + random.uniform(-0.2, 0.2) * base_size
        return rg.Box(rg.Plane.WorldXY, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height)).ToBrep()
    
    # Generate modules with random positions and overlaps
    for i in range(num_modules):
        module = create_module(module_size)
        
        # Randomly position the module within the allowed overlap range
        x_offset = random.uniform(-max_overlap, max_overlap)
        y_offset = random.uniform(-max_overlap, max_overlap)
        z_offset = random.uniform(-max_overlap, max_overlap)
        
        # Move the module to its final position
        translation = rg.Transform.Translation(x_offset, y_offset, z_offset)
        module.Transform(translation)
        
        # Add the module to the list of geometries
        geometries.append(module)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_concept_model(5.0, 10, 1.0, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_concept_model(3.5, 15, 2.0, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_concept_model(4.0, 8, 0.5, 25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_concept_model(6.0, 12, 0.8, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_concept_model(7.5, 20, 1.5, 57)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
