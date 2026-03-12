# Created for 0003_0005_a_labyrinth_of_blocks.json

""" Summary:
The function `generate_labyrinth_of_blocks` creates an architectural concept model inspired by the metaphor "A labyrinth of blocks." It generates a specified number of 3D block geometries with random dimensions, positions, and orientations, fostering an irregular arrangement that aligns with the design task's emphasis on complexity and exploration. By varying the size and height of these blocks, the function creates non-linear circulation routes and overlaps, enhancing the labyrinthine experience. The blocks are extruded from randomly positioned rectangles, allowing for dynamic light and shadow play, thereby inviting user interaction and discovery within the architectural ensemble."""

#! python 3
function_code = """def generate_labyrinth_of_blocks(seed: int, num_blocks: int, min_size: float, max_size: float, max_height: float) -> list:
    \"""
    Generates an architectural Concept Model based on the metaphor 'A labyrinth of blocks'.

    Parameters:
    - seed (int): Seed for the random number generator to ensure replicability.
    - num_blocks (int): The number of blocks to generate.
    - min_size (float): Minimum size of the blocks in meters.
    - max_size (float): Maximum size of the blocks in meters.
    - max_height (float): Maximum height of the blocks in meters.

    Returns:
    - list: A list of Brep objects representing the 3D geometries of the blocks.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(seed)

    blocks = []

    for _ in range(num_blocks):
        # Randomly determine the dimensions of the block within the specified limits
        length = random.uniform(min_size, max_size)
        width = random.uniform(min_size, max_size)
        height = random.uniform(min_size, max_height)

        # Randomly determine the position of the block
        x = random.uniform(-max_size * num_blocks / 2, max_size * num_blocks / 2)
        y = random.uniform(-max_size * num_blocks / 2, max_size * num_blocks / 2)

        # Create the base rectangle for the block
        base_plane = rg.Plane.WorldXY
        base_plane.Origin = rg.Point3d(x, y, 0)
        rectangle = rg.Rectangle3d(base_plane, length, width)

        # Create the block as an extrusion of the rectangle
        extrusion_vector = rg.Vector3d(0, 0, height)
        extrusion = rg.Extrusion.Create(rectangle.ToNurbsCurve(), height, True)

        # Optionally rotate the block to create orientation diversity
        angle = random.uniform(0, 2 * 3.14159)  # Random angle in radians
        axis = rg.Vector3d(0, 0, 1)  # Rotate around the Z-axis
        rotation = rg.Transform.Rotation(angle, axis, base_plane.Origin)
        extrusion.Transform(rotation)

        # Append the resulting block (extrusion) to the list
        blocks.append(extrusion.ToBrep())

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_labyrinth_of_blocks(seed=42, num_blocks=10, min_size=1.0, max_size=5.0, max_height=10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_labyrinth_of_blocks(seed=7, num_blocks=20, min_size=0.5, max_size=3.0, max_height=8.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_labyrinth_of_blocks(seed=99, num_blocks=15, min_size=2.0, max_size=6.0, max_height=12.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_labyrinth_of_blocks(seed=3, num_blocks=25, min_size=0.8, max_size=4.5, max_height=9.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_labyrinth_of_blocks(seed=10, num_blocks=30, min_size=0.6, max_size=4.0, max_height=15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
