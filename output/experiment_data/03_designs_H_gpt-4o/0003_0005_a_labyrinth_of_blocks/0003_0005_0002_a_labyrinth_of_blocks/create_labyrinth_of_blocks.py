# Created for 0003_0005_a_labyrinth_of_blocks.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor "A labyrinth of blocks." It creates a series of interconnected block-like structures, varying in size, shape, and height, arranged irregularly to evoke exploration and complexity. Each block has a chance of containing voids or light wells, enhancing the interplay of light and shadow, which is crucial for the design's mysterious essence. The function ensures non-linear circulation routes and diverse spatial relationships, inviting users to navigate through the architecture in unexpected ways, embodying the metaphor's themes of discovery and multifaceted experiences."""

#! python 3
function_code = """def create_labyrinth_of_blocks(seed, num_blocks, min_block_size, max_block_size, height_variation, void_probability):
    \"""
    Generate an architectural Concept Model based on the metaphor 'A labyrinth of blocks'.

    This function creates a series of block-like structures with varying shapes and sizes, arranged in an irregular
    and interconnected manner. The design emphasizes non-linear pathways, vertical variations, and the strategic 
    use of voids or light wells to enhance the experience of exploration and discovery.

    Parameters:
    - seed (int): Seed for random number generation to ensure replicability.
    - num_blocks (int): Number of blocks to generate in the labyrinth.
    - min_block_size (float): Minimum size for the blocks in meters.
    - max_block_size (float): Maximum size for the blocks in meters.
    - height_variation (float): Maximum height variation for the blocks in meters.
    - void_probability (float): Probability (0 to 1) of a block containing a void or light well.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the blocks.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(seed)
    
    blocks = []
    
    for _ in range(num_blocks):
        # Define block size
        width = random.uniform(min_block_size, max_block_size)
        depth = random.uniform(min_block_size, max_block_size)
        height = random.uniform(min_block_size, max_block_size)
        
        # Define block position
        x = random.uniform(-max_block_size * num_blocks / 3, max_block_size * num_blocks / 3)
        y = random.uniform(-max_block_size * num_blocks / 3, max_block_size * num_blocks / 3)
        z = random.uniform(-height_variation, height_variation)

        # Create the block
        base_point = rg.Point3d(x, y, z)
        block = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))
        
        # Convert block to Brep
        block_brep = block.ToBrep()
        
        # Determine if this block will contain a void
        if random.random() < void_probability:
            void_width = random.uniform(0.2 * width, 0.5 * width)
            void_depth = random.uniform(0.2 * depth, 0.5 * depth)
            void_height = height
            void_base_point = rg.Point3d(x + 0.25 * width, y + 0.25 * depth, z)
            void = rg.Box(rg.Plane(void_base_point, rg.Vector3d.ZAxis), rg.Interval(0, void_width), rg.Interval(0, void_depth), rg.Interval(0, void_height))

            # Subtract void from block
            void_brep = void.ToBrep()
            difference = rg.Brep.CreateBooleanDifference(block_brep, void_brep, 0.01)
            if difference:
                block_brep = difference[0]
        
        # Append the block to the list
        blocks.append(block_brep)
    
    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks(seed=42, num_blocks=10, min_block_size=1.0, max_block_size=5.0, height_variation=2.0, void_probability=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(seed=123, num_blocks=15, min_block_size=0.5, max_block_size=3.0, height_variation=1.5, void_probability=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(seed=7, num_blocks=20, min_block_size=2.0, max_block_size=6.0, height_variation=3.0, void_probability=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(seed=99, num_blocks=8, min_block_size=0.8, max_block_size=4.0, height_variation=1.0, void_probability=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(seed=2023, num_blocks=12, min_block_size=1.5, max_block_size=4.5, height_variation=2.5, void_probability=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
