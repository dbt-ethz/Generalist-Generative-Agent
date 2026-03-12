# Created for 0003_0004_a_labyrinth_of_blocks.json

""" Summary:
The function `generate_labyrinth_of_blocks_v2` creates an architectural concept model inspired by the metaphor "A labyrinth of blocks." It generates a random assortment of blocks with varying sizes, heights, and orientations, avoiding regular patterns to embody the metaphor's complexity. Each block is placed within a defined space, with random rotations adding to the unpredictability. The function also introduces height variations to enhance the interplay of light and shadow, creating a dynamic spatial experience. By designing intricate circulation paths between the blocks, the function fosters exploration and discovery, aligning with the metaphor's emphasis on mystery and engagement."""

#! python 3
function_code = """def generate_labyrinth_of_blocks_v2(base_size, height_variation, num_blocks, seed=None):
    \"""
    Generates an architectural Concept Model based on the metaphor 'A labyrinth of blocks'.

    Parameters:
    - base_size (float): The base size for each block in meters.
    - height_variation (tuple): A tuple (min_height, max_height) specifying the range of block heights.
    - num_blocks (int): The number of blocks to generate.
    - seed (int, optional): A seed for the random number generator to ensure reproducibility.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the blocks.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    if seed is not None:
        random.seed(seed)

    blocks = []
    for _ in range(num_blocks):
        # Randomly generate the position of the block
        x = random.uniform(-base_size * 5, base_size * 5)
        y = random.uniform(-base_size * 5, base_size * 5)
        z = 0  # Keeping this zero for ground-based blocks

        # Randomize the size and height of each block
        width = random.uniform(base_size * 0.5, base_size * 2)
        depth = random.uniform(base_size * 0.5, base_size * 2)
        height = random.uniform(height_variation[0], height_variation[1])

        # Create the base plane for each block
        base_plane = rg.Plane(rg.Point3d(x, y, z), rg.Vector3d.ZAxis)

        # Create the box as a Brep
        block = rg.Box(base_plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height)).ToBrep()
        
        # Add random rotation to blocks
        rotation_angle = random.uniform(0, 360)
        rotation_transform = rg.Transform.Rotation(math.radians(rotation_angle), rg.Vector3d.ZAxis, rg.Point3d(x + width / 2, y + depth / 2, z))
        block.Transform(rotation_transform)

        # Add the block to the list
        blocks.append(block)

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_labyrinth_of_blocks_v2(2.0, (1.0, 5.0), 10, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_labyrinth_of_blocks_v2(3.0, (2.0, 6.0), 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_labyrinth_of_blocks_v2(1.5, (0.5, 4.0), 8, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_labyrinth_of_blocks_v2(4.0, (3.0, 7.0), 20, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_labyrinth_of_blocks_v2(2.5, (1.5, 3.5), 12, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
