# Created for 0003_0002_a_labyrinth_of_blocks.json

""" Summary:
The provided function `create_labyrinth_of_blocks` generates an architectural concept model inspired by the metaphor "A labyrinth of blocks." It creates a dynamic assembly of interlocking blocks with varied dimensions and random orientations, reflecting the intricate and disorienting nature of a labyrinth. Each block's placement and size are randomized, facilitating a complex, non-linear spatial configuration that encourages exploration. The function also promotes verticality, allowing for different levels and circulation paths. By incorporating a variety of block heights and orientations, it enhances the interplay of light and shadow, enriching the user experience with moments of surprise and discovery."""

#! python 3
function_code = """def create_labyrinth_of_blocks(seed=42, num_blocks=50, min_size=2, max_size=10):
    \"""
    Creates an architectural Concept Model embodying the metaphor 'A labyrinth of blocks'.
    
    This function generates a complex and intricate network of interlocking volumes
    that encourage exploration and interaction. The blocks vary in size and orientation,
    forming a multi-layered silhouette with dynamic light and shadow effects.

    Parameters:
    - seed (int): Seed for random number generation to ensure replicable results.
    - num_blocks (int): Number of blocks to create.
    - min_size (float): Minimum size of each block in meters.
    - max_size (float): Maximum size of each block in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the blocks.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    blocks = []

    for _ in range(num_blocks):
        # Randomly select dimensions for the block
        width = random.uniform(min_size, max_size)
        depth = random.uniform(min_size, max_size)
        height = random.uniform(min_size, max_size)

        # Randomly position the block
        x = random.uniform(-max_size * num_blocks / 10, max_size * num_blocks / 10)
        y = random.uniform(-max_size * num_blocks / 10, max_size * num_blocks / 10)
        z = random.uniform(0, max_size * 5)  # Encourage vertical stacking

        # Create a box at the random position with the random dimensions
        base_plane = rg.Plane(rg.Point3d(x, y, z), rg.Vector3d(0, 0, 1))
        box = rg.Box(base_plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))

        # Convert the box to a Brep
        brep = box.ToBrep()
        blocks.append(brep)

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks(seed=123, num_blocks=30, min_size=3, max_size=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(seed=99, num_blocks=40, min_size=1, max_size=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(seed=2023, num_blocks=20, min_size=4, max_size=12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(seed=56, num_blocks=60, min_size=2.5, max_size=7.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(seed=77, num_blocks=25, min_size=1.5, max_size=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
