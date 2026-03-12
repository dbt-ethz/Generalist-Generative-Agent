# Created for 0003_0002_a_labyrinth_of_blocks.json

""" Summary:
The provided function, `create_labyrinth_of_blocks`, generates a three-dimensional architectural model inspired by the metaphor "A labyrinth of blocks." It creates interlocking blocks with varying heights, widths, and orientations, reflecting the complex spatial configuration described in the metaphor. By employing randomization in block positioning and rotation, the function fosters non-linear pathways that enhance exploration and interaction. The inclusion of voids within blocks adds further complexity, allowing for dynamic light and shadow play, thereby amplifying the sense of mystery and discovery, which are key traits of the design task."""

#! python 3
function_code = """def create_labyrinth_of_blocks(seed, num_blocks, base_size, height_range, path_width, void_chance):
    \"""
    Generates a 3D architectural concept model characteristic of 'A labyrinth of blocks'.

    Parameters:
    - seed: int, Seed for random number generation to ensure reproducibility.
    - num_blocks: int, Number of blocks to generate in the labyrinth.
    - base_size: float, Approximate base size for each block in meters.
    - height_range: tuple(float, float), Range of heights for the blocks in meters.
    - path_width: float, Average width of pathways between blocks in meters.
    - void_chance: float, Probability (0 to 1) of creating a void within a block.

    Returns:
    - list of Rhino.Geometry.Brep: A list representing the 3D brep geometries of the labyrinth blocks.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    blocks = []

    for _ in range(num_blocks):
        # Random block size
        width = base_size * random.uniform(0.7, 1.3)
        depth = base_size * random.uniform(0.7, 1.3)
        height = random.uniform(*height_range)

        # Random position with organic offset
        x_offset = random.uniform(-path_width, path_width)
        y_offset = random.uniform(-path_width, path_width)

        # Create a base plane and rectangle for the block
        base_plane = rg.Plane.WorldXY
        base_plane.Origin += rg.Vector3d(x_offset, y_offset, 0)
        rect = rg.Rectangle3d(base_plane, width, depth)

        # Create the main block
        box = rg.Box(rect.Plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))
        block_brep = box.ToBrep()

        # Optionally create a void within the block
        if random.random() < void_chance:
            void_width = width * random.uniform(0.3, 0.6)
            void_depth = depth * random.uniform(0.3, 0.6)
            void_height = height * random.uniform(0.2, 0.5)
            void_box = rg.Box(base_plane, rg.Interval(0, void_width), rg.Interval(0, void_depth), rg.Interval(height * 0.2, height * 0.7))
            void_brep = void_box.ToBrep()
            block_brep = rg.Brep.CreateBooleanDifference([block_brep], [void_brep], 0.01)[0]

        # Apply random rotation to blocks
        angle = random.uniform(0, 2 * 3.14159)
        rotation = rg.Transform.Rotation(angle, base_plane.ZAxis, box.Center)
        block_brep.Transform(rotation)

        blocks.append(block_brep)

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks(seed=42, num_blocks=10, base_size=2.0, height_range=(3.0, 5.0), path_width=1.0, void_chance=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(seed=7, num_blocks=15, base_size=1.5, height_range=(2.0, 4.0), path_width=0.5, void_chance=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(seed=99, num_blocks=20, base_size=1.0, height_range=(1.0, 3.0), path_width=0.8, void_chance=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(seed=12, num_blocks=12, base_size=2.5, height_range=(4.0, 6.0), path_width=1.5, void_chance=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(seed=25, num_blocks=8, base_size=3.0, height_range=(2.5, 5.5), path_width=2.0, void_chance=0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
