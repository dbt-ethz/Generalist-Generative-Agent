# Created for 0003_0005_a_labyrinth_of_blocks.json

""" Summary:
The provided function `generate_labyrinth` creates an architectural concept model inspired by the metaphor "A labyrinth of blocks." It generates a collection of block geometries with varying sizes, orientations, and heights, arranged in a non-linear, interconnected manner that encourages exploration. The function incorporates randomness in block placement and dimensions, avoiding uniformity to enhance the labyrinthine quality. Lightwells are strategically added to foster dynamic light and shadow effects, contributing to a sense of mystery and discovery within the design. This approach effectively embodies the metaphor, creating a complex spatial narrative that invites user interaction and engagement."""

#! python 3
function_code = """def generate_labyrinth(seed, block_count, base_size, height_range, lightwell_probability):
    \"""
    Generates an architectural Concept Model based on the metaphor 'A labyrinth of blocks'.

    This function creates a complex network of blocks with varying dimensions, orientations, and heights.
    Blocks are interconnected in a non-linear arrangement, offering multiple exploration paths and creating
    dynamic light and shadow effects through strategically placed lightwells.

    Parameters:
    - seed (int): Seed for random number generation to ensure replicability.
    - block_count (int): Number of blocks to generate.
    - base_size (float): Base size scale for the blocks.
    - height_range (tuple): Minimum and maximum height variations for the blocks.
    - lightwell_probability (float): Probability of a block containing a lightwell (0 to 1).

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the blocks.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    blocks = []

    for _ in range(block_count):
        # Randomly determine block dimensions
        length = random.uniform(0.5 * base_size, 1.5 * base_size)
        width = random.uniform(0.5 * base_size, 1.5 * base_size)
        height = random.uniform(height_range[0], height_range[1])

        # Random position for the block
        x = random.uniform(-base_size * block_count / 2, base_size * block_count / 2)
        y = random.uniform(-base_size * block_count / 2, base_size * block_count / 2)
        z = random.uniform(-height_range[1] / 2, height_range[1] / 2)

        # Create the block
        base_point = rg.Point3d(x, y, z)
        box = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))
        block_brep = box.ToBrep()

        # Determine if the block contains a lightwell
        if random.random() < lightwell_probability:
            lw_length = random.uniform(0.2 * length, 0.4 * length)
            lw_width = random.uniform(0.2 * width, 0.4 * width)
            lw_height = height

            lw_base_point = rg.Point3d(x + 0.2 * length, y + 0.2 * width, z)
            lightwell = rg.Box(rg.Plane(lw_base_point, rg.Vector3d.ZAxis), rg.Interval(0, lw_length), rg.Interval(0, lw_width), rg.Interval(0, lw_height))

            # Subtract lightwell from block
            lw_brep = lightwell.ToBrep()
            block_with_lightwell = rg.Brep.CreateBooleanDifference(block_brep, lw_brep, 0.01)
            if block_with_lightwell:
                blocks.append(block_with_lightwell[0])
            else:
                blocks.append(block_brep)
        else:
            blocks.append(block_brep)

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_labyrinth(seed=42, block_count=10, base_size=5.0, height_range=(1.0, 3.0), lightwell_probability=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_labyrinth(seed=123, block_count=15, base_size=4.0, height_range=(2.0, 5.0), lightwell_probability=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_labyrinth(seed=7, block_count=20, base_size=6.0, height_range=(1.5, 4.0), lightwell_probability=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_labyrinth(seed=98, block_count=12, base_size=3.0, height_range=(0.5, 2.5), lightwell_probability=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_labyrinth(seed=2023, block_count=8, base_size=7.0, height_range=(2.0, 6.0), lightwell_probability=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
