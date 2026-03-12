# Created for 0005_0001_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_model` generates an architectural concept model based on the "Distorted puzzle" metaphor by creating interlocking geometric volumes with slight misalignments. It begins by defining a base volume and applies random rotations around each axis to introduce distortion, reflecting the metaphor's themes of complexity and tension. Each volume is then translated randomly to enhance the interlocking effect, promoting exploration and discovery within the design. By varying the number of volumes, their size, and rotation angles, the function produces a visually dynamic and coherent model that embodies the interconnectedness and unpredictability characteristic of a puzzle."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_dimension=10, num_volumes=5, max_rotation=15, seed=42):
    \"""
    Create an Architectural Concept Model that embodies the 'Distorted puzzle' metaphor by assembling a series of
    interlocking geometric volumes with slight misalignments. This function generates volumes with varied shapes
    and angles to emphasize the distorted aspect, ensuring coherent yet unexpected interconnections.

    Parameters:
    - base_dimension (float): The base dimension for the volumes in meters.
    - num_volumes (int): Number of interlocking volumes to create.
    - max_rotation (float): Maximum rotation angle in degrees for misalignment.
    - seed (int): Seed for the random number generator for reproducibility.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the interlocking volumes of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    volumes = []

    def create_base_volume():
        \"""Create a base box volume.\"""
        return rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_dimension), rg.Interval(0, base_dimension), rg.Interval(0, base_dimension)).ToBrep()

    def rotate_volume(brep, max_angle):
        \"""Apply random rotations to the brep around each axis.\"""
        center = brep.GetBoundingBox(True).Center
        angle_x = math.radians(random.uniform(-max_angle, max_angle))
        angle_y = math.radians(random.uniform(-max_angle, max_angle))
        angle_z = math.radians(random.uniform(-max_angle, max_angle))

        rotation_x = rg.Transform.Rotation(angle_x, rg.Vector3d(1, 0, 0), center)
        rotation_y = rg.Transform.Rotation(angle_y, rg.Vector3d(0, 1, 0), center)
        rotation_z = rg.Transform.Rotation(angle_z, rg.Vector3d(0, 0, 1), center)

        brep.Transform(rotation_x)
        brep.Transform(rotation_y)
        brep.Transform(rotation_z)
        return brep

    for _ in range(num_volumes):
        base_volume = create_base_volume()
        rotated_volume = rotate_volume(base_volume, max_rotation)

        # Random translation to create the interlocking effect
        translation_vector = rg.Vector3d(
            random.uniform(-base_dimension * 0.5, base_dimension * 0.5),
            random.uniform(-base_dimension * 0.5, base_dimension * 0.5),
            random.uniform(-base_dimension * 0.5, base_dimension * 0.5)
        )
        transform = rg.Transform.Translation(translation_vector)
        rotated_volume.Transform(transform)

        volumes.append(rotated_volume)

    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(base_dimension=12, num_volumes=8, max_rotation=20, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(base_dimension=15, num_volumes=6, max_rotation=10, seed=27)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(base_dimension=8, num_volumes=10, max_rotation=25, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(base_dimension=14, num_volumes=7, max_rotation=30, seed=11)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(base_dimension=11, num_volumes=9, max_rotation=18, seed=33)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
