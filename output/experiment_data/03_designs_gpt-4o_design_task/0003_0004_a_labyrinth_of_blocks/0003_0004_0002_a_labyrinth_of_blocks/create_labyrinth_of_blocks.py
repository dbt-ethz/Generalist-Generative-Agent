# Created for 0003_0004_a_labyrinth_of_blocks.json

""" Summary:
The provided function, `create_labyrinth_of_blocks`, generates an architectural concept model by creating an intricate arrangement of blocks inspired by the metaphor "A labyrinth of blocks." It uses randomized parameters to produce blocks of varying sizes, orientations, and heights, resulting in a fragmented yet cohesive structure. The function emphasizes non-linear circulation paths that encourage exploration, reflecting the metaphor's implications of mystery and discovery. By allowing light to interact with the varied block forms, dynamic shadows and multiple perspectives are created, enhancing the spatial complexity and engagement within the architectural model."""

#! python 3
function_code = """def create_labyrinth_of_blocks(seed, num_blocks, min_size, max_size):
    \"""
    Creates an architectural Concept Model based on the metaphor 'A labyrinth of blocks'.
    
    This function generates a complex assemblage of interlocking blocks with varying sizes,
    orientations, and heights, representing an intricate spatial configuration. The design
    encourages exploration and discovery with dynamic circulation paths, varied perspectives,
    and interplay of light and shadow.

    Parameters:
    - seed: int, the seed for random generation to ensure replicability.
    - num_blocks: int, the number of blocks to generate.
    - min_size: float, the minimum size of each block.
    - max_size: float, the maximum size of each block.

    Returns:
    - List of Rhino.Geometry.Brep: A list of 3D brep geometries representing the blocks.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)

    blocks = []

    for _ in range(num_blocks):
        # Randomly choose the position, size, and orientation of each block
        x = random.uniform(0, 50)
        y = random.uniform(0, 50)
        z = random.uniform(0, 10)
        
        width = random.uniform(min_size, max_size)
        depth = random.uniform(min_size, max_size)
        height = random.uniform(min_size, max_size)
        
        # Create a box (block) geometry
        base_plane = rg.Plane(rg.Point3d(x, y, z), rg.Vector3d.ZAxis)
        block = rg.Box(base_plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))
        
        # Optionally rotate blocks for more randomness
        angle = random.uniform(0, 360)
        rotation_axis = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        rotation = rg.Transform.Rotation(math.radians(angle), rotation_axis, block.Center)
        block.Transform(rotation)
        
        # Convert box to brep
        blocks.append(block.ToBrep())

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks(seed=42, num_blocks=10, min_size=1.0, max_size=5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(seed=7, num_blocks=20, min_size=0.5, max_size=3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(seed=15, num_blocks=15, min_size=2.0, max_size=6.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(seed=100, num_blocks=25, min_size=0.8, max_size=4.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(seed=21, num_blocks=30, min_size=1.5, max_size=7.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
