# Created for 0003_0002_a_labyrinth_of_blocks.json

""" Summary:
The function `create_labyrinth_of_blocks` generates a three-dimensional architectural concept model that embodies the metaphor "A labyrinth of blocks." It creates an array of interlocking blocks with varying dimensions and orientations, reflecting complexity and disorientation. By using randomization for block size, height, and positioning within a defined pathway width, the model achieves an organic layout rather than a strict grid. This results in non-linear pathways and vertical circulation elements that enhance exploration. Additionally, the incorporation of light via openings in the blocks creates dynamic patterns of illumination, emphasizing the labyrinthine experience and encouraging user interaction."""

#! python 3
function_code = """def create_labyrinth_of_blocks(seed, num_blocks, base_size, height_range, pathway_width):
    \"""
    Creates a 3D architectural concept model embodying the metaphor 'A labyrinth of blocks'.
    
    Parameters:
    - seed: int, Seed for random number generation to ensure reproducibility.
    - num_blocks: int, The number of blocks to generate in the labyrinth.
    - base_size: float, The base size of each block in meters.
    - height_range: tuple(float, float), The range of heights the blocks can vary within, in meters.
    - pathway_width: float, The approximate width of pathways between blocks in meters.
    
    Returns:
    - list of Rhino.Geometry.Brep: A list of 3D brep geometries representing the interlocking blocks of the labyrinth.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Initialize a list to store the generated block breps
    blocks = []
    
    # Create a base plane for reference
    base_plane = rg.Plane.WorldXY
    
    # Generate the blocks
    for _ in range(num_blocks):
        # Randomly determine dimensions and orientation
        width = base_size * random.uniform(0.8, 1.2)
        depth = base_size * random.uniform(0.8, 1.2)
        height = random.uniform(*height_range)
        
        # Randomize the position within a grid-like pattern with offsets
        x_offset = random.uniform(-pathway_width, pathway_width)
        y_offset = random.uniform(-pathway_width, pathway_width)
        
        # Create a base rectangle for the block
        rect = rg.Rectangle3d(base_plane, width, depth)
        
        # Offset the rectangle to create a more organic layout
        translation = rg.Transform.Translation(x_offset, y_offset, 0)
        rect.Transform(translation)
        
        # Correct the box creation using the rectangle's bounding box and height
        box = rg.Box(rect.Plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))
        block_brep = rg.Brep.CreateFromBox(box)
        
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
    geometry = create_labyrinth_of_blocks(seed=42, num_blocks=50, base_size=1.0, height_range=(1.0, 3.0), pathway_width=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(seed=100, num_blocks=30, base_size=2.0, height_range=(2.0, 5.0), pathway_width=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(seed=2023, num_blocks=40, base_size=1.5, height_range=(1.5, 4.0), pathway_width=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(seed=7, num_blocks=25, base_size=1.2, height_range=(1.0, 2.5), pathway_width=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(seed=57, num_blocks=60, base_size=0.5, height_range=(0.5, 2.0), pathway_width=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
