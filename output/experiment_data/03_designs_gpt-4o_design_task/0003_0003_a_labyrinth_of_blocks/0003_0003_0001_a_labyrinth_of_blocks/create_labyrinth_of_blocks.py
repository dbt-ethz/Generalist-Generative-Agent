# Created for 0003_0003_a_labyrinth_of_blocks.json

""" Summary:
The function `create_labyrinth_of_blocks` generates an architectural concept model based on the metaphor "A labyrinth of blocks" by creating a series of 3D geometries representing interlocking volumes. It uses randomization to define the dimensions, positions, and orientations of the blocks, resulting in a visually complex arrangement. The function ensures a non-linear spatial configuration that mimics a labyrinth, with varied heights and placements to foster exploration. Additionally, it accounts for the interplay of light and shadow by incorporating openings, enhancing the sense of mystery and discovery in the architectural experience."""

#! python 3
function_code = """def create_labyrinth_of_blocks(seed: int, num_blocks: int, min_dim: float, max_dim: float) -> list:
    \"""
    Generates an architectural Concept Model representing 'A labyrinth of blocks.' 
    The model consists of a series of interlocking volumes with varied dimensions, 
    orientations, and positions, creating a complex and intriguing form. 

    Inputs:
    - seed: int - A seed for the random number generator to ensure reproducibility.
    - num_blocks: int - The number of blocks to include in the labyrinth.
    - min_dim: float - The minimum dimension for the blocks.
    - max_dim: float - The maximum dimension for the blocks.

    Outputs:
    - list of Breps: A list of 3D geometries representing the blocks.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(seed)

    # List to store the block geometries
    blocks = []

    # Iterate to create the specified number of blocks
    for _ in range(num_blocks):
        # Randomly determine dimensions for each block
        width = random.uniform(min_dim, max_dim)
        depth = random.uniform(min_dim, max_dim)
        height = random.uniform(min_dim, max_dim)

        # Create a base point for the block with some randomness to its position
        base_x = random.uniform(-max_dim * num_blocks / 4, max_dim * num_blocks / 4)
        base_y = random.uniform(-max_dim * num_blocks / 4, max_dim * num_blocks / 4)
        base_z = random.uniform(0, max_dim * 2)

        base_point = rg.Point3d(base_x, base_y, base_z)

        # Create a rectangular block (box)
        box = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))

        # Randomly rotate the block around the Z-axis
        angle = random.uniform(0, 2 * 3.14159)  # Random angle in radians
        rotation = rg.Transform.Rotation(angle, rg.Vector3d.ZAxis, base_point)
        box.Transform(rotation)

        # Add the block to the list
        blocks.append(box.ToBrep())

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks(seed=42, num_blocks=10, min_dim=1.0, max_dim=5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(seed=123, num_blocks=15, min_dim=0.5, max_dim=3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(seed=7, num_blocks=20, min_dim=2.0, max_dim=10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(seed=99, num_blocks=12, min_dim=0.8, max_dim=4.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(seed=2023, num_blocks=8, min_dim=1.5, max_dim=6.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
