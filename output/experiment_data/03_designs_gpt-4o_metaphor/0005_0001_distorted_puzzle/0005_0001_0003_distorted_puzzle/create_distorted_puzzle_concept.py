# Created for 0005_0001_distorted_puzzle.json

""" Summary:
The provided function, `create_distorted_puzzle_concept`, generates an architectural concept model that embodies the 'Distorted puzzle' metaphor by creating a series of interlocking blocks within a defined bounding box. Each block is randomly sized and placed, with slight misalignments and rotations to evoke a sense of dynamic tension and unpredictability. This aligns with the metaphor's emphasis on complexity and irregularity while maintaining coherence through the interconnected arrangement of the blocks. The randomness ensures varied visual interest, allowing for multiple design iterations, each reflecting the metaphor's essence of interconnectedness and movement."""

#! python 3
function_code = """def create_distorted_puzzle_concept(length, width, height, num_blocks, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Distorted puzzle' metaphor.
    
    The model consists of a series of interlocking blocks that are slightly misaligned
    to convey a sense of dynamic tension and interconnectedness.

    Parameters:
    - length (float): The length of the overall bounding box of the model in meters.
    - width (float): The width of the overall bounding box of the model in meters.
    - height (float): The height of the overall bounding box of the model in meters.
    - num_blocks (int): The number of blocks to generate in the model.
    - seed (int, optional): The seed for randomness to ensure replicable results. Default is 42.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of breps representing the 3D geometries of the concept model.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Point3d, Box, Plane, Vector3d, Brep

    random.seed(seed)
    geometries = []

    # Define the overall bounding box as the base layout
    base_plane = Plane(Point3d(0, 0, 0), Vector3d(1, 0, 0), Vector3d(0, 1, 0))
    bounding_box = Box(base_plane, Rhino.Geometry.Interval(0, length),
                       Rhino.Geometry.Interval(0, width), Rhino.Geometry.Interval(0, height))

    # Generate blocks
    for _ in range(num_blocks):
        # Random dimensions and random offset
        block_length = random.uniform(0.1 * length, 0.3 * length)
        block_width = random.uniform(0.1 * width, 0.3 * width)
        block_height = random.uniform(0.1 * height, 0.5 * height)

        # Random placement within the bounding box
        x_offset = random.uniform(0, length - block_length)
        y_offset = random.uniform(0, width - block_width)
        z_offset = random.uniform(0, height - block_height)

        # Create the base plane for the block with a slight random rotation
        base_point = Point3d(x_offset, y_offset, z_offset)
        rotation_angle = random.uniform(-10, 10)  # Degrees
        block_plane = Plane(base_point, Vector3d(1, 0, 0), Vector3d(0, 1, 0))
        block_plane.Rotate(Rhino.RhinoMath.ToRadians(rotation_angle), Vector3d(0, 0, 1))

        # Create the block as a Brep
        block_box = Box(block_plane, Rhino.Geometry.Interval(0, block_length),
                        Rhino.Geometry.Interval(0, block_width), Rhino.Geometry.Interval(0, block_height))
        block_brep = block_box.ToBrep()
        geometries.append(block_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_concept(10.0, 5.0, 3.0, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_concept(12.0, 6.0, 4.0, 20, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_concept(8.0, 4.0, 2.0, 10, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_concept(15.0, 7.0, 5.0, 25, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_concept(20.0, 10.0, 6.0, 30, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
