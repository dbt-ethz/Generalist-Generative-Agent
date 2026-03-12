# Created for 0003_0005_a_labyrinth_of_blocks.json

""" Summary:
The function `create_labyrinth_of_blocks` generates an architectural concept model inspired by the metaphor "A labyrinth of blocks." It creates a series of interconnected block-like structures with varying dimensions and orientations, arranged in a non-linear manner. This design fosters complex spatial relationships, encouraging exploration and discovery through overlapping routes and hidden spaces. The function incorporates vertical variations and light wells to enhance the interplay of light and shadow, aligning with the metaphor's emphasis on mystery. By using random sizes, orientations, and voids, the generated model reflects the intricate and engaging nature of a labyrinthine environment."""

#! python 3
function_code = """def create_labyrinth_of_blocks(seed, block_count, min_size, max_size, height_variation):
    \"""
    Generates an architectural Concept Model based on the metaphor 'A labyrinth of blocks'.

    This function constructs a series of interconnected block-like structures with varying dimensions
    and orientations. These blocks are arranged to create complex spatial relationships, encouraging
    exploration and discovery. The design incorporates vertical variations and strategic voids to
    enhance light and shadow interplay.

    Parameters:
    - seed (int): Seed for random number generation to ensure replicability.
    - block_count (int): Number of blocks to generate.
    - min_size (float): Minimum size of each block in meters.
    - max_size (float): Maximum size of each block in meters.
    - height_variation (float): Maximum variation in block height in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the blocks.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducible results
    random.seed(seed)

    blocks = []

    for _ in range(block_count):
        # Randomly determine the size and position of the block
        width = random.uniform(min_size, max_size)
        depth = random.uniform(min_size, max_size)
        height = random.uniform(min_size, max_size + height_variation)
        
        x = random.uniform(-max_size * block_count / 3, max_size * block_count / 3)
        y = random.uniform(-max_size * block_count / 3, max_size * block_count / 3)
        z = random.uniform(0, height_variation)

        # Create a base plane for the block
        base_plane = rg.Plane.WorldXY
        base_plane.Origin = rg.Point3d(x, y, z)
        
        # Create a box to represent the block
        box = rg.Box(base_plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))
        block = box.ToBrep()
        
        # Rotate the block for added complexity
        angle = random.uniform(0, 2 * 3.14159)  # Random rotation around the Z-axis
        rotation_axis = rg.Vector3d(0, 0, 1)
        rotation_center = rg.Point3d(x + width / 2, y + depth / 2, z)
        rotation = rg.Transform.Rotation(angle, rotation_axis, rotation_center)
        block.Transform(rotation)
        
        # Create a void for light wells within some blocks
        if random.random() < 0.3:  # 30% chance to create a light well
            void_width = random.uniform(0.2 * width, 0.5 * width)
            void_depth = random.uniform(0.2 * depth, 0.5 * depth)
            void_height = random.uniform(0.5 * height, height)
            
            void_base_plane = rg.Plane.WorldXY
            void_base_plane.Origin = rg.Point3d(x + width/4, y + depth/4, z)
            
            void_box = rg.Box(void_base_plane, rg.Interval(0, void_width), rg.Interval(0, void_depth), rg.Interval(0, void_height))
            void_brep = void_box.ToBrep()
            
            # Subtract the void from the block
            block = rg.Brep.CreateBooleanDifference(block, void_brep, 0.01)[0]

        blocks.append(block)

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks(seed=42, block_count=10, min_size=1.0, max_size=5.0, height_variation=3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(seed=100, block_count=15, min_size=2.0, max_size=4.0, height_variation=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(seed=7, block_count=20, min_size=0.5, max_size=3.0, height_variation=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(seed=21, block_count=12, min_size=0.8, max_size=6.0, height_variation=4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(seed=55, block_count=25, min_size=1.5, max_size=7.0, height_variation=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
