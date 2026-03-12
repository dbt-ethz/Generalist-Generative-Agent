# Created for 0003_0005_a_labyrinth_of_blocks.json

""" Summary:
The function `create_labyrinth_of_blocks` generates an architectural concept model inspired by the metaphor "A labyrinth of blocks." It creates a network of diverse block-like structures with varying sizes, heights, and orientations, arranged in a non-linear, interconnected manner to evoke exploration and discovery. The function incorporates randomness in positioning and rotation to ensure an irregular layout, reflecting the metaphor's complexity. Light wells are introduced to enhance the interplay of light and shadow, creating dynamic spatial experiences. This approach emphasizes the metaphor's themes of mystery and engagement within the architectural design, fulfilling the specified design task."""

#! python 3
function_code = """def create_labyrinth_of_blocks(seed, block_count, min_block_size, max_block_size, max_height_variation, void_probability):
    \"""
    Create an architectural Concept Model based on the metaphor 'A labyrinth of blocks'.
    
    This function generates a complex network of interconnected block-like structures with varying shapes,
    sizes, and orientations. The blocks are arranged to form a labyrinthine space, encouraging exploration
    through distinct pathways and hidden alcoves. The design emphasizes the play of light and shadow through
    strategic voids and height variations.

    Parameters:
    - seed (int): The seed for random number generation to ensure replicability.
    - block_count (int): The number of blocks to generate.
    - min_block_size (float): The minimum size for each block in meters.
    - max_block_size (float): The maximum size for each block in meters.
    - max_height_variation (float): The maximum height variation between blocks in meters.
    - void_probability (float): Probability (0 to 1) of a block containing a lightwell or void.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the blocks with possible voids.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(seed)

    blocks = []
    base_plane = rg.Plane.WorldXY

    for _ in range(block_count):
        # Randomly determine the size of the block
        width = random.uniform(min_block_size, max_block_size)
        depth = random.uniform(min_block_size, max_block_size)
        height = random.uniform(min_block_size, max_block_size)
        
        # Create a base rectangle for the block
        rect = rg.Rectangle3d(base_plane, width, depth)
        extrusion_vector = rg.Vector3d(0, 0, height)

        # Extrude the rectangle to create a block
        box = rg.Box(base_plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))
        block = rg.Brep.CreateFromBox(box)
        
        # Randomly move and orient the block
        move_vector = rg.Vector3d(
            random.uniform(-max_block_size, max_block_size),
            random.uniform(-max_block_size, max_block_size),
            random.uniform(-max_height_variation, max_height_variation)
        )
        move_transform = rg.Transform.Translation(move_vector)
        block.Transform(move_transform)
        
        # Randomly rotate the block around its center
        rotate_angle = random.uniform(0, 2 * 3.14159)  # Rotate between 0 and 360 degrees
        rotate_axis = rg.Line(block.GetBoundingBox(True).Center, block.GetBoundingBox(True).Center + rg.Vector3d.ZAxis)
        rotate_transform = rg.Transform.Rotation(rotate_angle, rotate_axis.Direction, rotate_axis.From)
        block.Transform(rotate_transform)
        
        # Introduce a void/lightwell with some probability
        if random.random() < void_probability:
            void_width = random.uniform(0.2 * width, 0.5 * width)
            void_depth = random.uniform(0.2 * depth, 0.5 * depth)
            void_height = height
            void_box = rg.Box(base_plane, rg.Interval(0, void_width), rg.Interval(0, void_depth), rg.Interval(0, void_height))
            void_box.Transform(rg.Transform.Translation(move_vector))
            void_brep = rg.Brep.CreateFromBox(void_box)
            void_difference = rg.Brep.CreateBooleanDifference(block, void_brep, 0.01)
            if void_difference:
                block = void_difference[0]

        blocks.append(block)

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks(seed=42, block_count=10, min_block_size=1.0, max_block_size=3.0, max_height_variation=2.0, void_probability=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(seed=7, block_count=15, min_block_size=0.5, max_block_size=2.5, max_height_variation=1.5, void_probability=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(seed=101, block_count=20, min_block_size=0.8, max_block_size=4.0, max_height_variation=3.0, void_probability=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(seed=2023, block_count=12, min_block_size=1.5, max_block_size=5.0, max_height_variation=2.5, void_probability=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(seed=100, block_count=25, min_block_size=0.3, max_block_size=2.0, max_height_variation=1.0, void_probability=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
