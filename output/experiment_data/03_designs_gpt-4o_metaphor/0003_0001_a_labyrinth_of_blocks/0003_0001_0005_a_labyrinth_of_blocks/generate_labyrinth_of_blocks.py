# Created for 0003_0001_a_labyrinth_of_blocks.json

""" Summary:
The function `generate_labyrinth_of_blocks` creates an architectural concept model inspired by the metaphor "A labyrinth of blocks." It generates a series of blocks with randomized positions, heights, and dimensions, reflecting the metaphor's complexity and intrigue. By varying the height and arrangement of blocks, the design fosters unexpected pathways and hidden spaces, enhancing navigation challenges. The interplay of light and shadow is prioritized, as the blocks' varying heights create dynamic visual experiences. This approach encourages exploration and engagement, embodying the metaphor's traits of mystery and discovery within the architectural model."""

#! python 3
function_code = """def generate_labyrinth_of_blocks(base_size, height_variation, block_count, seed=42):
    \"""
    Generates a concept model representing a 'Labyrinth of Blocks'.
    
    Parameters:
    - base_size (tuple): The base dimensions of the blocks as (width, depth).
    - height_variation (tuple): The range of heights for the blocks as (min_height, max_height).
    - block_count (int): The number of blocks to generate.
    - seed (int): Seed for random number generator to ensure replicability. Default is 42.
    
    Returns:
    - list: A list of RhinoCommon Brep geometries representing the blocks.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Point3d, Box, Plane, Interval
    
    # Set the seed for reproducibility
    random.seed(seed)
    
    # Extract base dimensions and height range
    base_width, base_depth = base_size
    min_height, max_height = height_variation
    
    # Initialize an empty list to store the blocks
    blocks = []
    
    # Generate the blocks
    for _ in range(block_count):
        # Randomize position
        x_pos = random.uniform(-10, 10)
        y_pos = random.uniform(-10, 10)
        
        # Randomize height
        height = random.uniform(min_height, max_height)
        
        # Create a rectangular base plane
        base_plane = Plane(Point3d(x_pos, y_pos, 0), Point3d(x_pos + base_width, y_pos, 0), Point3d(x_pos, y_pos + base_depth, 0))
        
        # Create a box from the base plane and height
        x_interval = Interval(0, base_width)
        y_interval = Interval(0, base_depth)
        z_interval = Interval(0, height)
        
        block = Box(base_plane, x_interval, y_interval, z_interval).ToBrep()
        blocks.append(block)
    
    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_labyrinth_of_blocks((2, 3), (1, 5), 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_labyrinth_of_blocks((4, 4), (2, 8), 15, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_labyrinth_of_blocks((1, 2), (0.5, 3), 20, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_labyrinth_of_blocks((3, 5), (2, 6), 12, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_labyrinth_of_blocks((5, 2), (1, 4), 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
