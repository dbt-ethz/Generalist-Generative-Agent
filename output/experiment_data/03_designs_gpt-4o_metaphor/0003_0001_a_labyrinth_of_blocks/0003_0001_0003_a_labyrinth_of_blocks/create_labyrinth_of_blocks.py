# Created for 0003_0001_a_labyrinth_of_blocks.json

""" Summary:
The provided function, `create_labyrinth_of_blocks`, generates an architectural concept model inspired by the metaphor of a "Labyrinth of Blocks." It creates a series of blocks with varying sizes, heights, and orientations, leading to a complex spatial arrangement that embodies mystery and exploration. The randomization of dimensions and positions introduces unexpected pathways and hidden spaces, enhancing the sense of intrigue. By prioritizing the interplay of light and shadow, the model fosters dynamic circulation routes. This intricately designed labyrinth encourages users to navigate and engage with the architecture, aligning with the metaphor's essence of exploration."""

#! python 3
function_code = """def create_labyrinth_of_blocks(base_size, height_variation, block_count, seed):
    \"""
    Creates an architectural Concept Model based on the metaphor of a "Labyrinth of Blocks."
    This model generates a series of blocks with varying heights, sizes, and orientations to create a complex and intriguing spatial configuration.

    Parameters:
    - base_size (float): The base size of the blocks (width and length in meters).
    - height_variation (float): The maximum variation in height for the blocks.
    - block_count (int): The number of blocks to generate.
    - seed (int): Seed for random number generation to ensure replicability of the design.

    Returns:
    - List of Breps: A list of 3D geometries representing the blocks in the labyrinth.
    \"""
    import Rhino.Geometry as rg
    import random

    # Initialize random seed
    random.seed(seed)

    # Create a list to store the generated blocks
    blocks = []

    # Define a base plane for block placement
    base_plane = rg.Plane.WorldXY

    for i in range(block_count):
        # Randomize block size and height
        width = base_size * (0.5 + random.random())
        length = base_size * (0.5 + random.random())
        height = height_variation * random.random()

        # Randomize block position within a predefined grid
        x_position = base_size * (i % 10) + random.uniform(-base_size / 2, base_size / 2)
        y_position = base_size * (i // 10) + random.uniform(-base_size / 2, base_size / 2)

        # Randomize the orientation of each block
        rotation_angle = random.uniform(0, 2 * 3.14159)  # Random rotation in radians
        rotation = rg.Transform.Rotation(rotation_angle, base_plane.ZAxis, base_plane.Origin)

        # Create a block as a box geometry
        block_origin = rg.Point3d(x_position, y_position, 0)
        block_base = rg.Rectangle3d(base_plane, width, length)
        block_base.Transform(rotation)
        block = rg.Box(rg.Plane(block_origin, base_plane.ZAxis), rg.Interval(0, width), rg.Interval(0, length), rg.Interval(0, height))

        # Add the block to the list
        blocks.append(block.ToBrep())

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks(2.0, 5.0, 20, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(1.5, 3.0, 15, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(3.0, 4.0, 10, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(2.5, 6.0, 25, 123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(4.0, 8.0, 30, 11)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
