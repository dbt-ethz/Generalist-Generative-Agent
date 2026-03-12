# Created for 0003_0003_a_labyrinth_of_blocks.json

""" Summary:
The function `create_labyrinth_of_blocks_with_terraces` generates an architectural concept model inspired by the metaphor "A labyrinth of blocks." It creates a series of interlocking blocks with varying dimensions, orientations, and heights, establishing a complex, non-linear arrangement that simulates a labyrinthine structure. The design incorporates terraces for vertical circulation, enhancing the multi-level experience. Randomly placed voids allow natural light to filter through, casting dynamic shadows that evoke curiosity and exploration. The function's parameters control the randomness of the blocks' sizes and positions, ensuring a unique spatial configuration that invites user engagement and discovery."""

#! python 3
function_code = """def create_labyrinth_of_blocks_with_terraces(seed: int, num_blocks: int, min_dim: float, max_dim: float, terrace_height: float) -> list:
    \"""
    Creates an architectural Concept Model embodying the metaphor 'A labyrinth of blocks' with integrated terraces.

    This function generates a series of interlocking blocks with varying dimensions, orientations, and heights, 
    forming a complex massing with multi-level terraces. The arrangement is non-linear and labyrinthine, 
    encouraging exploration through winding pathways. The design incorporates strategic voids for natural light 
    and terraces for vertical circulation, enhancing the sense of discovery.

    Parameters:
    - seed: int - A seed for the random number generator to ensure reproducibility.
    - num_blocks: int - The number of blocks to generate in the labyrinth.
    - min_dim: float - The minimum dimension for any side of a block.
    - max_dim: float - The maximum dimension for any side of a block.
    - terrace_height: float - The height of terraces included in the blocks.

    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometries of the blocks with terraces.
    \"""

    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(seed)

    # List to store the block geometries
    blocks = []

    # Function to create a terrace
    def create_terrace(base_point, width, depth):
        terrace_plane = rg.Plane(base_point, rg.Vector3d.ZAxis)
        terrace_box = rg.Box(terrace_plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, terrace_height))
        return terrace_box.ToBrep()

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

        # Create the block as a box
        box = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))

        # Randomly rotate the block around the Z-axis
        angle = random.uniform(0, 2 * 3.14159)  # Random angle in radians
        rotation = rg.Transform.Rotation(angle, rg.Vector3d.ZAxis, base_point)
        box.Transform(rotation)

        # Convert the box to a Brep and add it to the list
        blocks.append(box.ToBrep())

        # Add terraces at random heights on the block
        num_terraces = random.randint(1, 3)
        for _ in range(num_terraces):
            terrace_base_z = random.uniform(base_z, base_z + height)
            terrace_base_point = rg.Point3d(base_x, base_y, terrace_base_z)
            terrace = create_terrace(terrace_base_point, width * 0.8, depth * 0.8)
            blocks.append(terrace)

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks_with_terraces(seed=42, num_blocks=10, min_dim=1.0, max_dim=5.0, terrace_height=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks_with_terraces(seed=123, num_blocks=15, min_dim=2.0, max_dim=6.0, terrace_height=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks_with_terraces(seed=7, num_blocks=20, min_dim=1.5, max_dim=4.5, terrace_height=0.75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks_with_terraces(seed=99, num_blocks=5, min_dim=0.5, max_dim=3.0, terrace_height=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks_with_terraces(seed=2023, num_blocks=8, min_dim=0.8, max_dim=2.5, terrace_height=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
