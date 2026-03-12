# Created for 0003_0004_a_labyrinth_of_blocks.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor "A labyrinth of blocks" by creating a complex arrangement of block-like structures. It takes parameters for the number of blocks, their base area, and height variations. Each block is randomly sized, positioned, and oriented, ensuring a non-linear configuration that reflects the unpredictable nature of a labyrinth. The function emphasizes exploration through varying block heights and orientations, allowing light to penetrate and cast dynamic shadows. This results in a fragmented yet cohesive silhouette that fosters curiosity, engagement, and a sense of discovery within the spatial environment."""

#! python 3
function_code = """def create_labyrinth_of_blocks_v2(num_blocks, base_area, height_variation, seed=None):
    \"""
    Generates an architectural Concept Model based on the metaphor 'A labyrinth of blocks'.

    This function creates a complex network of block-like structures with varying dimensions,
    positions, and orientations, emphasizing non-linear circulation paths and dynamic spatial
    configurations to foster exploration and discovery.

    Parameters:
    - num_blocks (int): Number of blocks to generate.
    - base_area (tuple): A tuple (width, depth) defining the general area the blocks should occupy.
    - height_variation (tuple): A tuple (min_height, max_height) specifying the range of block heights.
    - seed (int, optional): A seed for the random number generator to ensure replicability.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the blocks.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    if seed is not None:
        random.seed(seed)
    
    blocks = []

    for _ in range(num_blocks):
        # Randomly choose block dimensions
        width = random.uniform(base_area[0] * 0.2, base_area[0] * 0.5)
        depth = random.uniform(base_area[1] * 0.2, base_area[1] * 0.5)
        height = random.uniform(height_variation[0], height_variation[1])

        # Randomly choose a position within the base area
        x = random.uniform(0, base_area[0] - width)
        y = random.uniform(0, base_area[1] - depth)
        z = 0  # Ground level

        # Create a base plane for each block
        base_plane = rg.Plane(rg.Point3d(x, y, z), rg.Vector3d.ZAxis)
        
        # Create the box geometry
        block_box = rg.Box(base_plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))

        # Randomly rotate the block around its center
        angle = random.uniform(0, 2 * math.pi)
        center = block_box.Center
        rotation_transform = rg.Transform.Rotation(angle, rg.Vector3d.ZAxis, center)
        block_box.Transform(rotation_transform)

        # Convert the box to a Brep and add to the list
        blocks.append(block_box.ToBrep())

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks_v2(10, (50, 50), (5, 15), seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks_v2(20, (100, 100), (3, 10), seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks_v2(15, (75, 75), (10, 20), seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks_v2(30, (60, 60), (8, 18), seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks_v2(25, (80, 80), (4, 12), seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
