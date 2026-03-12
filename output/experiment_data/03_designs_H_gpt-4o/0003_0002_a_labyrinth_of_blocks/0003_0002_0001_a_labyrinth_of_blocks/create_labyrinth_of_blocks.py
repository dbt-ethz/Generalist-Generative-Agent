# Created for 0003_0002_a_labyrinth_of_blocks.json

""" Summary:
The function `create_labyrinth_of_blocks` generates a 3D architectural concept model based on the metaphor "A labyrinth of blocks." It creates a collection of interlocking blocks with varying dimensions, orientations, and heights to form a complex spatial configuration. The randomness in block positioning and sizing fosters unexpected pathways and hidden spaces, embodying the disorienting experience of a labyrinth. Additionally, the design allows for non-linear circulation routes, enhancing exploration. By incorporating variations in height and orientation, the model emphasizes dynamic interactions with light and shadow, further enriching the sense of mystery and engagement within the architectural space."""

#! python 3
function_code = """def create_labyrinth_of_blocks(seed, base_size, num_blocks, height_variation, max_offset):
    \"""
    Generates a 3D architectural concept model inspired by the metaphor 'A labyrinth of blocks'.
    
    This function creates an arrangement of interlocking blocks with varying dimensions and orientations.
    The blocks form an intricate spatial configuration that encourages exploration and engagement through
    non-linear pathways and varying perspectives, enhancing the labyrinthine experience.

    Parameters:
    - seed: int, Seed for random number generation to ensure reproducibility.
    - base_size: float, The base dimension for the initial size of each block in meters.
    - num_blocks: int, The number of blocks to generate.
    - height_variation: float, The range of variation in block heights.
    - max_offset: float, The maximum offset for block placement to achieve an organic pattern.

    Returns:
    - list of Rhino.Geometry.Brep: A list of brep geometries representing the blocks in the labyrinth.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the seed for reproducibility
    random.seed(seed)
    
    # List to store the resulting block geometries
    blocks = []
    
    # Create blocks with varying size, position, and orientation
    for _ in range(num_blocks):
        # Determine random dimensions for the block
        width = base_size * random.uniform(0.8, 1.2)
        depth = base_size * random.uniform(0.8, 1.2)
        height = base_size + random.uniform(-height_variation, height_variation)

        # Randomize the block's position
        x_position = random.uniform(-max_offset, max_offset)
        y_position = random.uniform(-max_offset, max_offset)
        
        # Create a base plane and box for the block
        base_plane = rg.Plane.WorldXY
        base_plane.Origin += rg.Vector3d(x_position, y_position, 0)
        box = rg.Box(base_plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))
        block_brep = box.ToBrep()

        # Randomize the block's orientation
        angle = random.uniform(0, 2 * 3.14159)
        center_point = rg.Point3d(x_position + width / 2, y_position + depth / 2, height / 2)
        rotation = rg.Transform.Rotation(angle, rg.Vector3d(0, 0, 1), center_point)
        block_brep.Transform(rotation)
        
        # Add the block to the list
        blocks.append(block_brep)
    
    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks(seed=42, base_size=2.0, num_blocks=50, height_variation=1.0, max_offset=5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(seed=7, base_size=1.5, num_blocks=30, height_variation=0.5, max_offset=3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(seed=123, base_size=3.0, num_blocks=100, height_variation=2.0, max_offset=10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(seed=99, base_size=2.5, num_blocks=75, height_variation=1.5, max_offset=4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(seed=2023, base_size=1.0, num_blocks=20, height_variation=0.8, max_offset=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
