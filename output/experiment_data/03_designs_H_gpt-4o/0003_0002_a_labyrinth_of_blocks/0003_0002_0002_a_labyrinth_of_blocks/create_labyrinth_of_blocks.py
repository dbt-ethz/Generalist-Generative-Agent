# Created for 0003_0002_a_labyrinth_of_blocks.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor "A labyrinth of blocks" by creating a series of interlocking blocks with varied dimensions and orientations. It utilizes randomization to establish a complex, organic layout that encourages exploration through non-linear pathways and vertical connections. The blocks vary in height, width, and depth, forming a maze-like configuration enhanced by strategic openings that allow light to create dynamic shadows. This approach captures the essence of the metaphor, promoting a sense of mystery and interaction within the architectural space, ultimately resulting in a visually intriguing and engaging model."""

#! python 3
function_code = """def create_labyrinth_of_blocks(seed: int, num_blocks: int, base_size: float, height_range: tuple, connection_chance: float):
    \"""
    Creates an architectural Concept Model reflecting the metaphor 'A labyrinth of blocks'.

    This function generates a series of interconnected blocks that vary in scale and orientation,
    forming a complex spatial network. The design encourages exploration through non-linear pathways
    and vertical connections, with a focus on light interplay via strategic openings.

    Parameters:
    - seed: int, Seed for random number generation to ensure reproducibility.
    - num_blocks: int, The number of blocks to generate in the labyrinth.
    - base_size: float, The base size of each block in meters.
    - height_range: tuple(float, float), The range of heights the blocks can vary within, in meters.
    - connection_chance: float, Probability (0 to 1) of creating vertical connections (stairs/ramps) between blocks.

    Returns:
    - list of Rhino.Geometry.Brep: A list of 3D brep geometries representing the interlocking blocks of the labyrinth.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Initialize a list to store the generated block breps
    blocks = []
    
    # Reference plane
    base_plane = rg.Plane.WorldXY

    # Generate the blocks
    for _ in range(num_blocks):
        # Randomly determine dimensions and orientation
        width = base_size * random.uniform(0.5, 1.5)
        depth = base_size * random.uniform(0.5, 1.5)
        height = random.uniform(*height_range)
        
        # Random position within a non-linear pattern
        x_offset = random.uniform(-base_size * 2, base_size * 2)
        y_offset = random.uniform(-base_size * 2, base_size * 2)
        
        # Create a base rectangle for the block
        rect = rg.Rectangle3d(base_plane, width, depth)
        
        # Offset the rectangle to create a more organic layout
        translation = rg.Transform.Translation(x_offset, y_offset, 0)
        rect.Transform(translation)
        
        # Create the block
        box = rg.Box(rect.Plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))
        block_brep = box.ToBrep()
        
        # Randomly decide to create a vertical connection
        if random.random() < connection_chance:
            conn_height = height * random.uniform(0.3, 0.7)
            conn_width = width * 0.3
            conn_depth = depth * 0.3
            conn_box = rg.Box(rect.Plane, rg.Interval(0, conn_width), rg.Interval(0, conn_depth), rg.Interval(height, height + conn_height))
            conn_brep = conn_box.ToBrep()
            block_brep = rg.Brep.CreateBooleanUnion([block_brep, conn_brep], 0.01)[0]
        
        # Optionally apply a random rotation around the Z-axis
        angle = random.uniform(0, 2 * 3.14159)
        rotation = rg.Transform.Rotation(angle, base_plane.ZAxis, box.Center)
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
    geometry = create_labyrinth_of_blocks(seed=42, num_blocks=10, base_size=3.0, height_range=(2.0, 5.0), connection_chance=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(seed=123, num_blocks=15, base_size=4.0, height_range=(1.0, 3.0), connection_chance=0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(seed=7, num_blocks=20, base_size=2.5, height_range=(1.5, 4.5), connection_chance=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(seed=99, num_blocks=12, base_size=5.0, height_range=(3.0, 6.0), connection_chance=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(seed=2023, num_blocks=8, base_size=6.0, height_range=(2.5, 7.0), connection_chance=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
