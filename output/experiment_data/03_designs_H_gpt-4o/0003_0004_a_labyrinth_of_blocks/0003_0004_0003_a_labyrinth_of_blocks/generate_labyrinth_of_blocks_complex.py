# Created for 0003_0004_a_labyrinth_of_blocks.json

""" Summary:
The function `generate_labyrinth_of_blocks_complex` creates an architectural concept model inspired by the metaphor "A labyrinth of blocks." It generates a varied assemblage of block-like structures with differing sizes, heights, and orientations to form an intricate, non-linear spatial arrangement. Each block is randomly positioned and rotated, avoiding uniform patterns to enhance the sense of mystery and exploration. The function also introduces vertical elements, such as bridges, which connect various blocks, adding complexity. By manipulating block heights and configurations, the design emphasizes the interplay of light and shadow, facilitating dynamic circulation routes that invite discovery and engagement throughout the architecture."""

#! python 3
function_code = """def generate_labyrinth_of_blocks_complex(num_blocks, base_size, height_range, seed=None):
    \"""
    Generates an architectural Concept Model based on the metaphor 'A labyrinth of blocks'.

    This function creates a complex interlocking structure of blocks, with varied sizes and orientations.
    It emphasizes a mysterious and exploratory spatial arrangement with vertical and horizontal connections.

    Parameters:
    - num_blocks: int, the number of blocks to generate.
    - base_size: float, the average size of each block in meters.
    - height_range: tuple(float, float), the range of block heights.
    - seed: int, optional, a seed for random number generation to ensure replicability.

    Returns:
    - List of Rhino.Geometry.Brep: A list of 3D brep geometries representing the blocks.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    if seed is not None:
        random.seed(seed)

    blocks = []
    center_points = []

    for _ in range(num_blocks):
        # Determine the size and height of the block
        width = random.uniform(base_size * 0.5, base_size * 1.5)
        depth = random.uniform(base_size * 0.5, base_size * 1.5)
        height = random.uniform(height_range[0], height_range[1])

        # Determine the position, ensuring no overlap by using a grid
        x = random.uniform(-base_size * 5, base_size * 5)
        y = random.uniform(-base_size * 5, base_size * 5)
        z = 0  # Ground level

        # Create a box representing the block
        base_plane = rg.Plane(rg.Point3d(x, y, z), rg.Vector3d.ZAxis)
        box = rg.Box(base_plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))
        brep_box = box.ToBrep()

        # Randomly rotate the block around its center
        angle = random.uniform(0, math.pi * 2)
        rotation = rg.Transform.Rotation(angle, base_plane.ZAxis, box.Center)
        brep_box.Transform(rotation)

        # Optionally create vertical connections like bridges
        if random.random() > 0.5:
            bridge_height = random.uniform(height_range[0], height_range[1])
            bridge_length = random.uniform(base_size, base_size * 2)
            bridge_width = random.uniform(base_size * 0.2, base_size * 0.5)
            bridge_plane = rg.Plane(box.Center + rg.Vector3d(0, 0, bridge_height), rg.Vector3d.ZAxis)
            bridge_box = rg.Box(bridge_plane, rg.Interval(-bridge_length / 2, bridge_length / 2), rg.Interval(-bridge_width / 2, bridge_width / 2), rg.Interval(0, bridge_width))
            brep_bridge = bridge_box.ToBrep()
            blocks.append(brep_bridge)

        # Add the block to the list
        blocks.append(brep_box)

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_labyrinth_of_blocks_complex(10, 2.0, (1.0, 3.0), seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_labyrinth_of_blocks_complex(15, 1.5, (0.5, 2.5), seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_labyrinth_of_blocks_complex(20, 3.0, (2.0, 5.0), seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_labyrinth_of_blocks_complex(12, 2.5, (1.5, 4.0), seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_labyrinth_of_blocks_complex(8, 1.0, (0.8, 2.0), seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
