# Created for 0003_0001_a_labyrinth_of_blocks.json

""" Summary:
The provided function, `create_labyrinth_of_blocks`, generates an architectural concept model based on the metaphor "A labyrinth of blocks." It produces a collection of blocks with varying sizes, heights, and orientations, creating a complex spatial arrangement that encourages exploration and challenges navigation. By using randomization, the function introduces unexpected pathways and hidden spaces, enhancing the sense of mystery. The model emphasizes light and shadow interplay, fostering dynamic circulation routes. The blocks are defined as Brep objects, which can be visualized and manipulated in architectural design software, aligning with the metaphor's intent for intricate, engaging environments."""

#! python 3
function_code = """def create_labyrinth_of_blocks(num_blocks, block_size_range, height_range, seed=None):
    \"""
    Creates an architectural Concept Model based on the metaphor of 'A labyrinth of blocks'.
    
    This function generates a complex and intricate spatial configuration of blocks that 
    challenge navigation and orientation, creating a sense of mystery and exploration. 
    The arrangement of blocks varies in height, size, and orientation, introducing 
    unexpected pathways and hidden spaces. The design emphasizes the interplay of light 
    and shadow, varying perspectives, and dynamic circulation routes.

    Parameters:
    - num_blocks: int - The number of blocks to generate.
    - block_size_range: tuple(float, float) - The minimum and maximum size for each block (width and depth).
    - height_range: tuple(float, float) - The minimum and maximum height for each block.
    - seed: int (optional) - A seed for the random number generator to ensure reproducibility.

    Returns:
    - List[Rhino.Geometry.Brep] - A list of Brep objects representing the blocks of the labyrinth.
    \"""
    import Rhino.Geometry as rg
    import random

    if seed is not None:
        random.seed(seed)

    blocks = []
    base_plane = rg.Plane.WorldXY

    for _ in range(num_blocks):
        # Random size and height for each block
        width = random.uniform(*block_size_range)
        depth = random.uniform(*block_size_range)
        height = random.uniform(*height_range)

        # Random position within a grid-like area
        x_pos = random.uniform(0, num_blocks * max(block_size_range))
        y_pos = random.uniform(0, num_blocks * max(block_size_range))
        z_pos = 0  # Start at ground level

        # Create a box for the block
        box_corners = [
            rg.Point3d(x_pos, y_pos, z_pos),
            rg.Point3d(x_pos + width, y_pos, z_pos),
            rg.Point3d(x_pos + width, y_pos + depth, z_pos),
            rg.Point3d(x_pos, y_pos + depth, z_pos),
            rg.Point3d(x_pos, y_pos, z_pos + height),
            rg.Point3d(x_pos + width, y_pos, z_pos + height),
            rg.Point3d(x_pos + width, y_pos + depth, z_pos + height),
            rg.Point3d(x_pos, y_pos + depth, z_pos + height)
        ]

        box = rg.Brep.CreateFromBox(box_corners)
        if box:
            blocks.append(box)

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks(10, (1.0, 3.0), (2.0, 5.0), seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(15, (0.5, 2.0), (1.0, 4.0))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(20, (2.0, 4.0), (1.0, 6.0), seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(12, (1.5, 2.5), (3.0, 7.0), seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(8, (0.8, 2.2), (1.5, 3.5), seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
