# Created for 0003_0003_a_labyrinth_of_blocks.json

""" Summary:
The provided function, `create_labyrinth_of_blocks_v2`, generates an architectural concept model based on the metaphor "A labyrinth of blocks." It creates a collection of interlocking blocks with varying dimensions, orientations, and heights, simulating a complex spatial configuration. These blocks are arranged non-linearly, promoting exploration and navigation through meandering pathways. The function incorporates voids and terraces to enhance natural light penetration, casting dynamic shadows that shift throughout the day. By introducing random rotations and offsets, the model embodies the metaphor's essence, creating an intriguing, mysterious structure that invites user engagement and discovery within its layered spaces."""

#! python 3
function_code = """def create_labyrinth_of_blocks_v2(base_point, num_blocks, min_dim, max_dim, max_height, seed):
    \"""
    Creates an architectural Concept Model that embodies the metaphor 'A labyrinth of blocks'.
    
    This function generates interlocking blocks with varying dimensions, heights, and orientations.
    The arrangement is non-linear, with blocks positioned to create a labyrinthine quality. The
    design incorporates voids and terraces to allow light penetration and create dynamic shadows.
    
    Parameters:
    - base_point: A tuple of (x, y, z) representing the starting point of the model.
    - num_blocks: An integer specifying the number of blocks to generate.
    - min_dim: A float indicating the minimum dimension for any side of a block.
    - max_dim: A float indicating the maximum dimension for any side of a block.
    - max_height: A float representing the maximum height for the blocks.
    - seed: An integer used to seed the random number generator for replicable results.
    
    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometries of the blocks.
    \"""
    
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    blocks = []

    for _ in range(num_blocks):
        # Randomly determine dimensions and height for the block
        length = random.uniform(min_dim, max_dim)
        width = random.uniform(min_dim, max_dim)
        height = random.uniform(min_dim, max_height)

        # Create a base point for the block with some offset for non-linear arrangement
        x_offset = random.uniform(-max_dim * 2, max_dim * 2)
        y_offset = random.uniform(-max_dim * 2, max_dim * 2)
        z_offset = random.uniform(0, max_height / 2)

        block_base_point = rg.Point3d(base_point[0] + x_offset, base_point[1] + y_offset, base_point[2] + z_offset)

        # Create the block as a box
        block = rg.Box(rg.Plane(block_base_point, rg.Vector3d.ZAxis), rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))

        # Introduce a random rotation to enhance the labyrinthine quality
        rotation_angle = random.uniform(0, 360)
        rotation_transform = rg.Transform.Rotation(rotation_angle * (3.14159/180), rg.Vector3d.ZAxis, block_base_point)
        block.Transform(rotation_transform)

        # Convert the box to a Brep and add it to the list
        blocks.append(block.ToBrep())

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks_v2((0, 0, 0), 50, 1.0, 5.0, 10.0, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks_v2((10, 10, 0), 30, 0.5, 3.0, 8.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks_v2((5, 5, 0), 20, 2.0, 6.0, 12.0, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks_v2((1, 1, 0), 40, 0.8, 4.0, 9.0, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks_v2((-10, -10, 0), 60, 0.3, 2.5, 7.0, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
