# Created for 0003_0002_a_labyrinth_of_blocks.json

""" Summary:
The function `create_labyrinth_of_blocks` generates a 3D architectural concept model by embodying the metaphor "A labyrinth of blocks." It creates an intricate arrangement of interlocking blocks with varying dimensions, orientations, and heights, facilitating a non-linear, maze-like structure. The use of random positioning, height variations, and rotations introduces complexity and encourages exploration. Pathways are designed with unexpected turns and voids, enhancing user interaction and discovery. Additionally, the model incorporates openings that allow light to play across the surfaces, emphasizing the interplay of light and shadow, which adds depth and mystery to the architectural experience."""

#! python 3
function_code = """def create_labyrinth_of_blocks(seed, block_count, base_size, height_variation, rotation_range):
    \"""
    Generates a 3D architectural concept model inspired by the metaphor 'A labyrinth of blocks'.

    This function produces a complex arrangement of blocks with varying dimensions, orientations, and heights.
    The blocks are placed non-linearly to form a labyrinthine structure, featuring voids and pathways that
    encourage exploration and interaction.

    Parameters:
    - seed: int, Seed for random number generation to ensure reproducibility.
    - block_count: int, The number of blocks to generate.
    - base_size: float, The average base size of each block in meters.
    - height_variation: float, The maximum variation from the base height in meters.
    - rotation_range: float, The range in degrees for block rotation around the Z-axis.

    Returns:
    - list of Rhino.Geometry.Brep: A list of 3D brep geometries representing the blocks of the labyrinth.
    \"""
    import Rhino.Geometry as rg
    import random
    from math import radians

    random.seed(seed)
    blocks = []

    for _ in range(block_count):
        # Randomize block position with a bias towards organic arrangement
        x_pos = random.uniform(-base_size * 5, base_size * 5)
        y_pos = random.uniform(-base_size * 5, base_size * 5)

        # Randomize block dimensions
        width = base_size * random.uniform(0.5, 1.5)
        depth = base_size * random.uniform(0.5, 1.5)
        height = base_size + random.uniform(-height_variation, height_variation)

        # Create a block as a box
        base_plane = rg.Plane.WorldXY
        base_plane.Origin = rg.Point3d(x_pos, y_pos, 0)
        box = rg.Box(base_plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))
        block_brep = box.ToBrep()

        # Apply a random rotation around the block's center
        rotation_angle = radians(random.uniform(-rotation_range, rotation_range))
        rotation_axis = rg.Vector3d(0, 0, 1)
        rotation_center = rg.Point3d(x_pos + width / 2, y_pos + depth / 2, height / 2)
        rotation_transform = rg.Transform.Rotation(rotation_angle, rotation_axis, rotation_center)
        block_brep.Transform(rotation_transform)

        # Randomly decide to create a void within the block
        if random.random() < 0.5:
            void_width = width * random.uniform(0.4, 0.8)
            void_depth = depth * random.uniform(0.4, 0.8)
            void_height = height * random.uniform(0.3, 0.7)
            void_box = rg.Box(base_plane, rg.Interval(0, void_width), rg.Interval(0, void_depth), rg.Interval(0, void_height))
            void_brep = void_box.ToBrep()
            block_brep = rg.Brep.CreateBooleanDifference([block_brep], [void_brep], 0.01)[0]

        # Add the block to the list
        blocks.append(block_brep)

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks(seed=42, block_count=10, base_size=2.0, height_variation=1.0, rotation_range=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(seed=7, block_count=15, base_size=1.5, height_variation=0.5, rotation_range=45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(seed=99, block_count=20, base_size=3.0, height_variation=2.0, rotation_range=60)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(seed=12, block_count=25, base_size=1.0, height_variation=0.8, rotation_range=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(seed=101, block_count=12, base_size=2.5, height_variation=1.5, rotation_range=90)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
