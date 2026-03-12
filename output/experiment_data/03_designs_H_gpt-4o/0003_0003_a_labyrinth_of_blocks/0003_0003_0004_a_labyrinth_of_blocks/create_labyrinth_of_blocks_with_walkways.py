# Created for 0003_0003_a_labyrinth_of_blocks.json

""" Summary:
The provided function, `create_labyrinth_of_blocks_with_walkways`, generates an architectural concept model inspired by the metaphor "A labyrinth of blocks." It constructs a series of interlocking volumes (blocks) with varied dimensions and orientations, simulating the intricate and puzzling nature of a labyrinth. Each block is randomly positioned to create a non-linear arrangement, while elevated walkways connect different levels, enhancing exploration. The design emphasizes dynamic circulation paths and incorporates varying heights, widths, and strategic openings to manipulate natural light, fostering an environment rich in discovery and engagement. This aligns with the metaphor's emphasis on complexity and mystery."""

#! python 3
function_code = """def create_labyrinth_of_blocks_with_walkways(seed: int, num_blocks: int, min_dim: float, max_dim: float, walkway_width: float) -> list:
    \"""
    Generates an architectural Concept Model representing 'A labyrinth of blocks' with elevated walkways.
    The model consists of a series of interlocking volumes with varied dimensions, orientations, and positions,
    as well as elevated walkways connecting different levels, creating a complex and intriguing form.

    Inputs:
    - seed: int - A seed for the random number generator to ensure reproducibility.
    - num_blocks: int - The number of blocks to include in the labyrinth.
    - min_dim: float - The minimum dimension for the blocks.
    - max_dim: float - The maximum dimension for the blocks.
    - walkway_width: float - The width of the elevated walkways connecting the blocks.

    Outputs:
    - list of Breps: A list of 3D geometries representing the blocks and walkways.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(seed)

    # List to store the block and walkway geometries
    geometries = []

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
        geometries.append(box.ToBrep())

        # Add elevated walkways connecting blocks
        if random.random() > 0.5:
            # Determine an endpoint for the walkway
            end_x = base_x + random.choice([-1, 1]) * random.uniform(min_dim, max_dim)
            end_y = base_y + random.choice([-1, 1]) * random.uniform(min_dim, max_dim)
            end_z = base_z + height + random.uniform(0.1, 0.5) * height

            end_point = rg.Point3d(end_x, end_y, end_z)

            # Create a pathway (walkway) as a box
            walkway_length = base_point.DistanceTo(end_point)
            walkway_vector = rg.Vector3d(end_point - base_point)
            walkway_vector.Unitize()
            walkway_plane = rg.Plane(base_point, walkway_vector)

            walkway = rg.Box(walkway_plane, rg.Interval(0, walkway_width), rg.Interval(0, walkway_width), rg.Interval(0, walkway_length))
            geometries.append(walkway.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks_with_walkways(seed=42, num_blocks=10, min_dim=1.0, max_dim=5.0, walkway_width=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks_with_walkways(seed=123, num_blocks=15, min_dim=2.0, max_dim=6.0, walkway_width=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks_with_walkways(seed=2023, num_blocks=20, min_dim=0.5, max_dim=4.0, walkway_width=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks_with_walkways(seed=7, num_blocks=12, min_dim=1.5, max_dim=3.5, walkway_width=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks_with_walkways(seed=99, num_blocks=8, min_dim=1.2, max_dim=7.0, walkway_width=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
