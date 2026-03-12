# Created for 0003_0002_a_labyrinth_of_blocks.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor "A labyrinth of blocks" by creating a series of interlocking geometric volumes. It randomizes the position, size, height, and rotation of each block, resulting in a complex arrangement that reflects the metaphor's emphasis on disorientation and exploration. The height variation and non-linear pathways enhance the labyrinthine experience, while varying block orientations create dynamic interactions of light and shadow. By encapsulating these design elements, the function successfully embodies the metaphor's traits, fostering an engaging spatial experience that encourages users to navigate and discover hidden areas within the structure."""

#! python 3
function_code = """def create_labyrinth_of_blocks(base_size, num_blocks, height_variation, rotation_variation, seed):
    \"""
    Generates a concept model representing "A labyrinth of blocks" using interlocking geometric volumes.

    Parameters:
    - base_size (float): The base size for the blocks in meters; serves as the primary dimension for the blocks.
    - num_blocks (int): The number of blocks to generate, representing the complexity of the labyrinth.
    - height_variation (float): The maximum variation in height for the blocks.
    - rotation_variation (float): The maximum rotation angle in degrees for blocks.
    - seed (int): Random seed for replicable results.

    Returns:
    - list[Rhino.Geometry.Brep]: A list of Brep objects representing the blocks in the labyrinth.
    \"""
    import Rhino.Geometry as rg
    import random
    from math import radians

    random.seed(seed)
    blocks = []

    for _ in range(num_blocks):
        # Randomize block position
        x = random.uniform(-base_size * 2, base_size * 2)
        y = random.uniform(-base_size * 2, base_size * 2)

        # Randomize block size
        width = base_size * random.uniform(0.5, 1.5)
        depth = base_size * random.uniform(0.5, 1.5)
        height = base_size + random.uniform(-height_variation, height_variation)

        # Create a cuboid block
        box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(0, width),
            rg.Interval(0, depth),
            rg.Interval(0, height)
        )
        block = box.ToBrep()

        if block is None:
            continue  # Skip this block if it couldn't be created

        # Randomize block rotation
        rotation_angle = radians(random.uniform(-rotation_variation, rotation_variation))
        rotation_axis = rg.Vector3d(0, 0, 1)  # Z-axis for horizontal rotation
        rotation_center = rg.Point3d(x, y, 0)

        # Transform the block
        translation = rg.Transform.Translation(x, y, 0)
        rotation = rg.Transform.Rotation(rotation_angle, rotation_axis, rotation_center)

        # Apply transformations
        block.Transform(translation)
        block.Transform(rotation)

        # Add block to list
        blocks.append(block)

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks(1.0, 50, 2.0, 45.0, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(0.5, 100, 1.0, 30.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(1.5, 75, 3.0, 60.0, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(2.0, 30, 4.0, 90.0, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(0.8, 60, 2.5, 15.0, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
