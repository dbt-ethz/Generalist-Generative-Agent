# Created for 0003_0002_a_labyrinth_of_blocks.json

""" Summary:
The function `generate_labyrinth` creates a three-dimensional architectural concept model based on the metaphor "A labyrinth of blocks." By generating an array of interlocking blocks with random dimensions and orientations, it embodies the complexity and intricacy of a labyrinth. Each block's height, width, and depth vary, allowing for a non-linear, maze-like spatial configuration. The function also introduces voids within some blocks to enhance the interplay of light and shadow, creating dynamic illumination patterns. Through this approach, the design encourages exploration and interaction, aligning with the metaphor's implications of mystery and discovery in spatial navigation."""

#! python 3
function_code = """def generate_labyrinth(seed, block_count, min_dim, max_dim, height_variation):
    \"""
    Generates a 3D architectural concept model based on the metaphor 'A labyrinth of blocks'.
    
    This function creates an array of interlocking blocks arranged in a complex, non-linear pattern.
    It emphasizes exploration and interaction, with varied block dimensions and orientations to
    create an intricate spatial configuration. The design incorporates light and shadow effects
    through openings and voids within blocks.

    Parameters:
    - seed: int, Seed for random number generation to ensure reproducibility.
    - block_count: int, The number of blocks to generate in the labyrinth.
    - min_dim: float, The minimum dimension (width/depth) of the blocks in meters.
    - max_dim: float, The maximum dimension (width/depth) of the blocks in meters.
    - height_variation: float, The range of variation for the block heights in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the 3D blocks of the labyrinth.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    blocks = []

    for _ in range(block_count):
        # Random dimensions for the block
        width = random.uniform(min_dim, max_dim)
        depth = random.uniform(min_dim, max_dim)
        height = random.uniform(min_dim, max_dim) + random.uniform(-height_variation, height_variation)

        # Random position and orientation
        x = random.uniform(-max_dim * 2, max_dim * 2)
        y = random.uniform(-max_dim * 2, max_dim * 2)
        z = random.uniform(0, max_dim)  # Encourage vertical stacking

        # Create the block with a potential void
        base_plane = rg.Plane(rg.Point3d(x, y, z), rg.Vector3d(0, 0, 1))
        box = rg.Box(base_plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))
        block_brep = box.ToBrep()

        # Randomly decide to add a void
        if random.random() > 0.6:  # 40% chance to create a void
            void_width = width * random.uniform(0.3, 0.7)
            void_depth = depth * random.uniform(0.3, 0.7)
            void_height = height * random.uniform(0.3, 0.7)
            void_box = rg.Box(base_plane, rg.Interval(0, void_width), rg.Interval(0, void_depth), rg.Interval(0, void_height))
            void_brep = void_box.ToBrep()
            # Ensure the boolean difference operation returns a valid result
            difference_result = rg.Brep.CreateBooleanDifference([block_brep], [void_brep], 0.01)
            if difference_result:
                block_brep = difference_result[0]

        blocks.append(block_brep)

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_labyrinth(seed=42, block_count=50, min_dim=1.0, max_dim=5.0, height_variation=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_labyrinth(seed=7, block_count=100, min_dim=0.5, max_dim=3.0, height_variation=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_labyrinth(seed=21, block_count=30, min_dim=2.0, max_dim=4.0, height_variation=3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_labyrinth(seed=15, block_count=75, min_dim=0.8, max_dim=6.0, height_variation=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_labyrinth(seed=99, block_count=40, min_dim=1.5, max_dim=4.5, height_variation=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
