# Created for 0005_0001_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_model` generates an architectural concept model inspired by the "Distorted puzzle" metaphor by creating a series of interlocking geometric volumes. It employs randomization to determine dimensions, positions, and rotations of each volume, introducing slight misalignments that evoke tension and movement. The model consists of varied shapes that connect coherently, promoting exploration through irregularly shaped rooms and corridors. By ensuring that each volume is related yet distinct, the function encapsulates the metaphor's essence, resulting in a dynamic structure that reflects both unpredictability and interconnectedness, akin to pieces of a puzzle fitting together."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_size=10, num_volumes=5, seed=42):
    \"""
    Create a Concept Model that embodies the 'Distorted puzzle' metaphor by assembling a series of interlocking
    geometric volumes with slight misalignments. The model uses varied shapes and angles to emphasize the distorted
    aspect, ensuring that each volume connects to others in a coherent yet unexpected manner.

    Parameters:
    - base_size: The approximate size of the base of the model in meters.
    - num_volumes: The number of interlocking volumes to create.
    - seed: An integer used to seed the random number generator for reproducibility.

    Returns:
    - A list of Brep geometries representing the interlocking volumes of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    volumes = []

    for i in range(num_volumes):
        # Randomly decide dimensions and position offsets for each volume
        width = random.uniform(base_size * 0.5, base_size * 1.5)
        depth = random.uniform(base_size * 0.5, base_size * 1.5)
        height = random.uniform(base_size * 0.5, base_size * 1.5)

        # Random translation and rotation to create distortion
        x_offset = random.uniform(-base_size * 0.2, base_size * 0.2)
        y_offset = random.uniform(-base_size * 0.2, base_size * 0.2)
        z_offset = random.uniform(0, base_size * 0.2)

        angle_x = random.uniform(-5, 5)  # Small rotation in degrees
        angle_y = random.uniform(-5, 5)
        angle_z = random.uniform(-5, 5)

        # Create a base box
        base_box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(x_offset, x_offset + width),
            rg.Interval(y_offset, y_offset + depth),
            rg.Interval(z_offset, z_offset + height)
        )

        # Convert Box to Brep
        brep = base_box.ToBrep()

        # Apply rotations for distortion
        rotation_x = rg.Transform.Rotation(math.radians(angle_x), rg.Vector3d(1, 0, 0), base_box.Center)
        rotation_y = rg.Transform.Rotation(math.radians(angle_y), rg.Vector3d(0, 1, 0), base_box.Center)
        rotation_z = rg.Transform.Rotation(math.radians(angle_z), rg.Vector3d(0, 0, 1), base_box.Center)

        brep.Transform(rotation_x)
        brep.Transform(rotation_y)
        brep.Transform(rotation_z)

        volumes.append(brep)

    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(base_size=12, num_volumes=8, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(base_size=15, num_volumes=10, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(base_size=8, num_volumes=6, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(base_size=20, num_volumes=4, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(base_size=5, num_volumes=12, seed=101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
