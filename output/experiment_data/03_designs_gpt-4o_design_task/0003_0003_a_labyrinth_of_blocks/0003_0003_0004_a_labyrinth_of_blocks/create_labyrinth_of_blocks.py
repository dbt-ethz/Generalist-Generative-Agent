# Created for 0003_0003_a_labyrinth_of_blocks.json

""" Summary:
The function `create_labyrinth_of_blocks` generates an architectural concept model based on the metaphor "A labyrinth of blocks" by creating a series of interlocking, randomly-sized blocks with varied heights and orientations. This non-linear arrangement simulates a labyrinthine structure, encouraging exploration through winding pathways and layered circulation. The design incorporates voids and openings to allow natural light to create dynamic shadows, enhancing the sense of mystery. By specifying parameters like the number of blocks, their dimensions, and height variation, the function produces a visually complex form that embodies the metaphor's themes of intrigue and engagement."""

#! python 3
function_code = """def create_labyrinth_of_blocks(base_point, num_blocks, min_dim, max_dim, height_variation, seed):
    \"""
    Creates an architectural Concept Model embodying the metaphor 'A labyrinth of blocks'.
    
    This function generates a series of interlocking blocks with varying dimensions and orientations to form a complex
    and multi-tiered massing. The arrangement is intentionally non-linear, simulating a labyrinthine quality with 
    winding pathways and layered circulation. The design incorporates voids and openings to allow natural light to 
    filter through, creating dynamic shadows.

    Parameters:
    - base_point: A tuple of (x, y, z) representing the starting point of the model.
    - num_blocks: An integer specifying the number of blocks to generate.
    - min_dim: A float indicating the minimum dimension for any side of a block.
    - max_dim: A float indicating the maximum dimension for any side of a block.
    - height_variation: A float representing the maximum variation in height for the blocks.
    - seed: An integer used to seed the random number generator for replicable results.

    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometries of the blocks.
    \"""

    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    blocks = []

    for _ in range(num_blocks):
        # Randomly determine dimensions for the block
        length = random.uniform(min_dim, max_dim)
        width = random.uniform(min_dim, max_dim)
        height = random.uniform(min_dim, height_variation)

        # Create a base point for the block
        x_offset = random.uniform(-max_dim, max_dim)
        y_offset = random.uniform(-max_dim, max_dim)
        z_offset = random.uniform(0, height_variation)

        block_base_point = rg.Point3d(base_point[0] + x_offset, base_point[1] + y_offset, base_point[2] + z_offset)

        # Create the block as a box
        block = rg.Box(rg.Plane(block_base_point, rg.Vector3d.ZAxis), rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))

        # Introduce a random rotation
        rotation_angle = random.uniform(0, 360)
        rotation_axis = rg.Line(block_base_point, rg.Vector3d.ZAxis)
        rotation_transform = rg.Transform.Rotation(rotation_angle, rotation_axis.Direction, block_base_point)
        block.Transform(rotation_transform)

        # Convert the box to a Brep and add it to the list
        blocks.append(block.ToBrep())

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks((0, 0, 0), 10, 1.0, 5.0, 3.0, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks((10, 10, 0), 20, 0.5, 4.0, 2.0, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks((-5, -5, 0), 15, 0.8, 3.5, 1.5, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks((5, 5, 0), 25, 1.5, 6.0, 4.0, 123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks((2, 3, 0), 12, 0.6, 2.5, 2.5, 56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
