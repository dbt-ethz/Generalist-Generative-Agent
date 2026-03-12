# Created for 0003_0005_a_labyrinth_of_blocks.json

""" Summary:
The provided function, `create_labyrinth_of_blocks`, generates an architectural concept model embodying the metaphor "A labyrinth of blocks." By creating a series of interconnected block-like structures with varying dimensions, orientations, and heights, the function crafts a complex spatial network that encourages exploration. Each block can optionally include lightwells, allowing natural light to filter through, enhancing the play of light and shadow, which is central to the design's mysterious character. The random arrangement of blocks and non-linear circulation routes aligns with the metaphor, promoting unexpected encounters and diverse pathways, inviting users to discover the architecture's intricacies."""

#! python 3
function_code = """def create_labyrinth_of_blocks(seed, block_count, base_size, height_variation, lightwell_probability):
    \"""
    Generates an architectural Concept Model based on the metaphor 'A labyrinth of blocks'.

    This function creates a series of interconnected block-like structures with varying shapes and sizes.
    Each block is uniquely oriented and positioned to form a complex network that encourages exploration.
    The design emphasizes light and shadow interplay, with strategic voids for natural illumination.

    Parameters:
    - seed (int): Seed for the random number generator to ensure replicability.
    - block_count (int): Number of blocks to generate.
    - base_size (float): Average base size for blocks in meters.
    - height_variation (float): Maximum variation in block heights in meters.
    - lightwell_probability (float): Probability (0 to 1) that a block will contain a lightwell.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the blocks.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    blocks = []

    for _ in range(block_count):
        # Determine block dimensions and position
        width = random.uniform(0.5 * base_size, 1.5 * base_size)
        depth = random.uniform(0.5 * base_size, 1.5 * base_size)
        height = random.uniform(base_size, base_size + height_variation)

        x = random.uniform(-base_size * block_count / 2, base_size * block_count / 2)
        y = random.uniform(-base_size * block_count / 2, base_size * block_count / 2)
        z = random.uniform(0, height_variation)

        # Create block
        base_point = rg.Point3d(x, y, z)
        box = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))
        block_brep = box.ToBrep()

        # Optionally create a lightwell
        if random.random() < lightwell_probability:
            lw_width = random.uniform(0.2 * width, 0.5 * width)
            lw_depth = random.uniform(0.2 * depth, 0.5 * depth)
            lw_height = height
            lw_x = x + random.uniform(0.1 * width, 0.4 * width)
            lw_y = y + random.uniform(0.1 * depth, 0.4 * depth)
            lightwell_base = rg.Point3d(lw_x, lw_y, z)
            lightwell_box = rg.Box(rg.Plane(lightwell_base, rg.Vector3d.ZAxis), rg.Interval(0, lw_width), rg.Interval(0, lw_depth), rg.Interval(0, lw_height))
            lightwell_brep = lightwell_box.ToBrep()

            # Subtract lightwell from block
            block_brep = rg.Brep.CreateBooleanDifference(block_brep, lightwell_brep, 0.01)[0]

        # Add block to the list
        blocks.append(block_brep)

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks(seed=42, block_count=10, base_size=2.0, height_variation=3.0, lightwell_probability=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(seed=100, block_count=15, base_size=1.5, height_variation=2.5, lightwell_probability=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(seed=7, block_count=20, base_size=2.5, height_variation=4.0, lightwell_probability=0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(seed=21, block_count=8, base_size=1.0, height_variation=1.5, lightwell_probability=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(seed=56, block_count=12, base_size=3.0, height_variation=5.0, lightwell_probability=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
