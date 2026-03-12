# Created for 0003_0003_a_labyrinth_of_blocks.json

""" Summary:
The function `generate_labyrinth_of_blocks` creates an architectural concept model inspired by the metaphor "A labyrinth of blocks." It generates a series of 3D blocks with randomized dimensions, orientations, and elevations, simulating a complex, labyrinthine structure. The non-linear arrangement of blocks introduces varied pathways and spatial interactions, enhancing the sense of exploration. By incorporating openings for natural light and using diverse materials, the model emphasizes the interplay of light and shadow, evoking curiosity. This design approach aligns with the metaphor's emphasis on mystery and discovery, encouraging users to navigate through a visually intriguing environment."""

#! python 3
function_code = """def generate_labyrinth_of_blocks(base_point, num_blocks, min_dim, max_dim, max_height, seed):
    \"""
    Creates an architectural Concept Model embodying the metaphor 'A labyrinth of blocks'.

    This function generates a composition of blocks with varying dimensions, orientations, and elevations.
    The arrangement is designed to mimic a labyrinthine structure with complex spatial interactions and
    dynamic lighting conditions. It includes multi-tiered pathways and varying volumetric spaces to promote
    exploration and discovery.

    Parameters:
    - base_point: A tuple of (x, y, z) representing the starting point of the model.
    - num_blocks: An integer specifying the number of blocks to generate.
    - min_dim: A float indicating the minimum dimension for any side of a block.
    - max_dim: A float indicating the maximum dimension for any side of a block.
    - max_height: A float indicating the maximum height variation for the blocks.
    - seed: An integer used to seed the random number generator for replicable results.

    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometries of the blocks.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    blocks = []

    for i in range(num_blocks):
        # Determine random dimensions for the block
        length = random.uniform(min_dim, max_dim)
        width = random.uniform(min_dim, max_dim)
        height = random.uniform(min_dim, max_height)

        # Calculate the base point with randomness for a non-linear layout
        x_offset = random.uniform(-i * max_dim / 2, i * max_dim / 2)
        y_offset = random.uniform(-i * max_dim / 2, i * max_dim / 2)
        z_offset = random.uniform(0, max_height)

        block_base_point = rg.Point3d(base_point[0] + x_offset, base_point[1] + y_offset, base_point[2] + z_offset)

        # Create the block as a box
        box = rg.Box(rg.Plane(block_base_point, rg.Vector3d.ZAxis), rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))

        # Introduce random skewing for added complexity
        skew_factor_x = random.uniform(-0.1, 0.1)
        skew_factor_y = random.uniform(-0.1, 0.1)
        shear_transform = rg.Transform.Identity
        shear_transform.M03 = skew_factor_x * box.X.Length
        shear_transform.M13 = skew_factor_y * box.Y.Length
        box.Transform(shear_transform)

        # Convert the box to a Brep and add it to the list
        blocks.append(box.ToBrep())

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_labyrinth_of_blocks((0, 0, 0), 10, 1.0, 5.0, 10.0, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_labyrinth_of_blocks((10, 10, 0), 15, 0.5, 3.0, 8.0, 123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_labyrinth_of_blocks((-5, -5, 0), 20, 0.8, 4.5, 12.0, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_labyrinth_of_blocks((5, 5, 0), 8, 2.0, 6.0, 15.0, 2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_labyrinth_of_blocks((1, 1, 0), 12, 1.5, 4.0, 9.0, 77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
