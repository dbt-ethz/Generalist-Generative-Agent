# Created for 0003_0001_a_labyrinth_of_blocks.json

""" Summary:
The provided function, `create_labyrinth_of_blocks`, generates an architectural concept model based on the metaphor of a "labyrinth of blocks." By utilizing parameters like base size, height variation, and block count, the function creates a complex arrangement of blocks with varying sizes and orientations. Each block is randomly positioned, enhancing the intricate spatial configuration that challenges navigation. The design emphasizes dynamic circulation routes and unexpected pathways, fostering exploration. By manipulating light and shadow through different heights and orientations, the model encapsulates a sense of mystery, inviting users to engage with and discover hidden spaces within the architecture."""

#! python 3
function_code = """def create_labyrinth_of_blocks(base_size, height_variation, block_count, seed):
    \"""
    Creates an architectural concept model inspired by a 'labyrinth of blocks'.
    
    The function generates a complex and intricate spatial configuration with varying 
    block sizes and orientations, designed to challenge navigation and orientation.
    The arrangement of blocks emphasizes dynamic circulation, interplay of light 
    and shadow, and hidden spaces that encourage exploration.
    
    Parameters:
    - base_size (float): The base dimension for each block in meters.
    - height_variation (float): The range of variation in height for the blocks in meters.
    - block_count (int): The number of blocks to generate in the labyrinth.
    - seed (int): The seed for the random number generator to ensure replicability.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the blocks.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # List to store the resulting Breps
    breps = []
    
    for i in range(block_count):
        # Randomize position and dimensions
        x = random.uniform(-base_size * 5, base_size * 5)
        y = random.uniform(-base_size * 5, base_size * 5)
        z = 0
        width = random.uniform(base_size * 0.5, base_size * 1.5)
        depth = random.uniform(base_size * 0.5, base_size * 1.5)
        height = base_size + random.uniform(-height_variation, height_variation)
        
        # Create a base rectangle for the block
        base_rect = rg.Rectangle3d(rg.Plane.WorldXY, width, depth)
        
        # Move the rectangle to the randomized position
        translation = rg.Transform.Translation(x, y, z)
        base_rect.Transform(translation)
        
        # Extrude the rectangle to create a block
        extrusion = rg.Extrusion.Create(base_rect.ToNurbsCurve(), height, True)
        brep = extrusion.ToBrep()
        
        if brep:
            breps.append(brep)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks(2.0, 3.0, 15, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(1.5, 2.5, 20, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(3.0, 4.0, 10, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(2.5, 5.0, 12, 56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(4.0, 6.0, 8, 13)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
