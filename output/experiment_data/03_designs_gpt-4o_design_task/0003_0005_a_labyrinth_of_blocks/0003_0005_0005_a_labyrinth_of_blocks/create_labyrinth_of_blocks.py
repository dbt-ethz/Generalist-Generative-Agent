# Created for 0003_0005_a_labyrinth_of_blocks.json

""" Summary:
The provided function, `create_labyrinth_of_blocks`, generates an architectural concept model based on the metaphor of "A labyrinth of blocks." It creates a network of interconnected, block-like structures with varied sizes and heights, arranged in a non-linear, irregular manner to encourage exploration. By incorporating features like light wells, the function enhances the interplay of light and shadow, promoting a dynamic spatial experience. The randomization of block dimensions and placements aligns with the metaphor's emphasis on complexity and surprise, resulting in a multifaceted design that invites users to navigate through diverse pathways and unexpected spaces."""

#! python 3
function_code = """def create_labyrinth_of_blocks(base_size, height_variation, block_count, seed=42):
    \"""
    Generates an architectural Concept Model representing 'A labyrinth of blocks'.
    
    This function creates a network of interconnected block-like structures with varying shapes 
    and sizes. The blocks are arranged in a non-linear and seemingly random manner, incorporating 
    vertical variations to create a dynamic and exploratory spatial experience. The design 
    incorporates light wells to enhance the interplay of light and shadow.
    
    Parameters:
    - base_size: float, the average size of the blocks' footprint.
    - height_variation: float, the range of height variation for each block.
    - block_count: int, the number of blocks to generate.
    - seed: int, optional, the seed for random number generation to ensure replicability.
    
    Returns:
    - List of Rhino.Geometry.Brep objects representing the blocks in the labyrinth.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the seed for randomness
    random.seed(seed)
    
    # List to store generated block geometries
    blocks = []

    # Generate blocks
    for _ in range(block_count):
        # Determine the base location for the block
        x = random.uniform(-base_size * block_count / 2, base_size * block_count / 2)
        y = random.uniform(-base_size * block_count / 2, base_size * block_count / 2)
        
        # Randomize the size and height of the block
        width = random.uniform(0.5 * base_size, 1.5 * base_size)
        depth = random.uniform(0.5 * base_size, 1.5 * base_size)
        height = random.uniform(base_size, base_size + height_variation)
        
        # Create a base rectangle for the block
        base_rect = rg.Rectangle3d(rg.Plane.WorldXY, width, depth)
        base_rect.Transform(rg.Transform.Translation(x, y, 0))
        
        # Create a box to form the block
        block = rg.Brep.CreateFromBox(rg.Box(base_rect.Plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height)))

        # Create a light well (void) in some blocks
        if random.random() > 0.7:  # 30% chance to have a light well
            void_width = random.uniform(0.2 * width, 0.5 * width)
            void_depth = random.uniform(0.2 * depth, 0.5 * depth)
            void_height = random.uniform(0.5 * height, 0.8 * height)
            
            void_rect = rg.Rectangle3d(rg.Plane.WorldXY, void_width, void_depth)
            void_rect.Transform(rg.Transform.Translation(x + 0.25 * width, y + 0.25 * depth, height - void_height))
            
            void = rg.Brep.CreateFromBox(rg.Box(void_rect.Plane, rg.Interval(0, void_width), rg.Interval(0, void_depth), rg.Interval(0, void_height)))
            
            # Subtract the void from the block
            block = rg.Brep.CreateBooleanDifference(block, void, 0.01)[0]

        # Add the block to the list of geometries
        blocks.append(block)

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks(base_size=3.0, height_variation=5.0, block_count=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(base_size=2.5, height_variation=4.0, block_count=15, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(base_size=4.0, height_variation=6.0, block_count=20, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(base_size=1.5, height_variation=3.0, block_count=8, seed=57)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(base_size=2.0, height_variation=2.5, block_count=12, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
