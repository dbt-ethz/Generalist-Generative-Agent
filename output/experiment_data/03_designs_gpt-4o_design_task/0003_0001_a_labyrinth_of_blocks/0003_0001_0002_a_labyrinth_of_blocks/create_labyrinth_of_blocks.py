# Created for 0003_0001_a_labyrinth_of_blocks.json

""" Summary:
The function `create_labyrinth_of_blocks` generates an architectural concept model by simulating a 'labyrinth of blocks' through a systematic yet randomized approach. It uses a grid system to position blocks of varying sizes, heights, and orientations, introducing intentional disruptions to create a non-linear spatial configuration. Each block is represented as a 3D geometry, with random offsets to enhance the labyrinthine quality. The function also incorporates height variations, allowing for dynamic interplay of light and shadow. This results in a complex arrangement that encourages exploration and discovery, embodying the metaphors essence of mystery and engagement."""

#! python 3
function_code = """def create_labyrinth_of_blocks(seed=42, grid_size=10, min_block_size=2, max_block_size=5, height_variation=5):
    \"""
    Generates an architectural Concept Model based on the metaphor 'A labyrinth of blocks'.

    Parameters:
    - seed (int): Seed for random number generator to ensure replicability.
    - grid_size (int): The size of the grid to arrange the blocks.
    - min_block_size (int): Minimum size of the blocks.
    - max_block_size (int): Maximum size of the blocks.
    - height_variation (int): Maximum variation in block heights.

    Returns:
    - list: A list of Brep geometries representing the blocks.
    \"""

    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    blocks = []
    
    # Create a grid system
    for i in range(grid_size):
        for j in range(grid_size):
            # Random size for each block
            block_width = random.randint(min_block_size, max_block_size)
            block_depth = random.randint(min_block_size, max_block_size)
            block_height = random.randint(1, height_variation)
            
            # Introduce randomness in grid position
            x_offset = random.uniform(-1, 1)
            y_offset = random.uniform(-1, 1)
            
            # Base point for each block
            base_point = rg.Point3d(i * max_block_size + x_offset, j * max_block_size + y_offset, 0)
            
            # Create a box for the block
            box = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), rg.Interval(0, block_width), rg.Interval(0, block_depth), rg.Interval(0, block_height))
            brep = box.ToBrep()
            
            # Add to the list of blocks
            blocks.append(brep)
    
    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks(seed=123, grid_size=15, min_block_size=3, max_block_size=7, height_variation=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(seed=99, grid_size=8, min_block_size=1, max_block_size=4, height_variation=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(seed=200, grid_size=12, min_block_size=2, max_block_size=6, height_variation=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(seed=56, grid_size=20, min_block_size=4, max_block_size=10, height_variation=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(seed=77, grid_size=5, min_block_size=1, max_block_size=3, height_variation=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
