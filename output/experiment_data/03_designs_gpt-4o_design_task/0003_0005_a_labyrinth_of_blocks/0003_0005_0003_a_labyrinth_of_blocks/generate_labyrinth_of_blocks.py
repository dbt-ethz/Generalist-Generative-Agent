# Created for 0003_0005_a_labyrinth_of_blocks.json

""" Summary:
The function `generate_labyrinth_of_blocks` creates an architectural concept model inspired by the metaphor "A labyrinth of blocks." It generates a series of discrete, block-like structures with varying sizes and orientations, arranged in an interconnected and non-linear layout. This approach fosters complex spatial relationships and encourages exploration, with unexpected pathways and alcoves. The function incorporates vertical variations and strategically placed light wells to enhance the interplay of light and shadow, emphasizing the design's enigmatic nature. By utilizing randomization within defined parameters, the model reflects the metaphor's essence while allowing for diverse interpretations and experiences."""

#! python 3
function_code = """def generate_labyrinth_of_blocks(seed, num_blocks, min_size, max_size, height_variation, lightwell_chance):
    \"""
    Creates an architectural Concept Model based on the metaphor 'A labyrinth of blocks'.
    
    This function generates a composition of discrete block structures with varying shapes and sizes,
    arranged in an interconnected manner with a focus on dynamic spatial relationships, light, and shadow.
    
    Parameters:
    - seed (int): The seed for the random number generator to ensure replicability.
    - num_blocks (int): Number of block-like structures to generate.
    - min_size (tuple): Minimum dimensions (length, width, height) for the blocks.
    - max_size (tuple): Maximum dimensions (length, width, height) for the blocks.
    - height_variation (float): Maximum vertical displacement for blocks to create split levels.
    - lightwell_chance (float): Probability (0 to 1) of a block containing a lightwell or void.
    
    Returns:
    - List of RhinoCommon BRep objects representing the 3D geometries of the blocks.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    geometries = []

    for _ in range(num_blocks):
        # Randomly determine the position of the block
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        z = random.uniform(-height_variation, height_variation)
        
        # Randomly determine the size of the block
        length = random.uniform(min_size[0], max_size[0])
        width = random.uniform(min_size[1], max_size[1])
        height = random.uniform(min_size[2], max_size[2])
        
        # Create the base block
        base_point = rg.Point3d(x, y, z)
        block = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))
        
        # Determine if this block will contain a lightwell
        if random.random() < lightwell_chance:
            lw_x = random.uniform(0.1 * length, 0.4 * length)
            lw_y = random.uniform(0.1 * width, 0.4 * width)
            lw_z = height
            lightwell_base = rg.Point3d(x + 0.3 * length, y + 0.3 * width, z)
            lightwell = rg.Box(rg.Plane(lightwell_base, rg.Vector3d.ZAxis), rg.Interval(0, lw_x), rg.Interval(0, lw_y), rg.Interval(0, lw_z))
            
            # Subtract lightwell from block
            block_brep = block.ToBrep()
            lightwell_brep = lightwell.ToBrep()
            block_with_lightwell = rg.Brep.CreateBooleanDifference(block_brep, lightwell_brep, 0.01)
            if block_with_lightwell:
                geometries.append(block_with_lightwell[0])
            else:
                geometries.append(block_brep)
        else:
            geometries.append(block.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_labyrinth_of_blocks(seed=42, num_blocks=10, min_size=(1, 1, 1), max_size=(5, 5, 5), height_variation=3, lightwell_chance=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_labyrinth_of_blocks(seed=123, num_blocks=20, min_size=(2, 2, 2), max_size=(6, 6, 6), height_variation=4, lightwell_chance=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_labyrinth_of_blocks(seed=7, num_blocks=15, min_size=(0.5, 0.5, 0.5), max_size=(3, 3, 3), height_variation=2, lightwell_chance=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_labyrinth_of_blocks(seed=99, num_blocks=25, min_size=(1.5, 1.5, 1.5), max_size=(4, 4, 4), height_variation=5, lightwell_chance=0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_labyrinth_of_blocks(seed=2023, num_blocks=30, min_size=(0.8, 0.8, 0.8), max_size=(4.5, 4.5, 4.5), height_variation=6, lightwell_chance=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
