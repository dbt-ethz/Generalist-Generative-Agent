# Created for 0005_0001_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_model` generates an architectural concept model inspired by the "Distorted puzzle" metaphor by creating interlocking geometric volumes that are slightly misaligned. It takes parameters such as base dimensions, volume count, and skew angle to define the characteristics of the model. Using random transformations, it skews and translates each volume to evoke movement and tension, reminiscent of a puzzle's complexity. The result is a list of Brep geometries that embody the metaphor's dynamic interplay of forms, promoting exploration through irregularly shaped rooms and corridors, while ensuring an underlying coherence reflective of interconnectedness."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_dimensions=(10, 10, 10), volume_count=7, skew_angle_degrees=10, seed=123):
    \"""
    Generate an architectural Concept Model based on the 'Distorted puzzle' metaphor. The model consists of interlocking
    geometric volumes that are slightly misaligned and skewed to evoke movement and tension, promoting exploration.

    Parameters:
    - base_dimensions: A tuple (length, width, height) representing the approximate dimensions of each base volume.
    - volume_count: The number of interlocking volumes to create.
    - skew_angle_degrees: The maximum skew angle in degrees applied to distort the volumes.
    - seed: An integer to seed the random number generator for reproducibility.

    Returns:
    - A list of Brep geometries representing the interlocking volumes of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)

    def skew_transform(angle_degrees, center):
        \"""Create a skew transformation matrix.\"""
        angle_radians = math.radians(angle_degrees)
        skew_matrix = rg.Transform.Identity
        skew_matrix.M11 = 1
        skew_matrix.M12 = math.tan(angle_radians)
        skew_matrix.M21 = math.tan(angle_radians)
        skew_matrix.M22 = 1
        skew_matrix.M44 = 1
        return rg.Transform.Translation(center) * skew_matrix * rg.Transform.Translation(-center)

    volumes = []
    base_length, base_width, base_height = base_dimensions

    for _ in range(volume_count):
        # Randomly skew and position each volume
        skew_angle = random.uniform(-skew_angle_degrees, skew_angle_degrees)
        x_shift = random.uniform(-base_length * 0.5, base_length * 0.5)
        y_shift = random.uniform(-base_width * 0.5, base_width * 0.5)
        z_shift = random.uniform(-base_height * 0.5, base_height * 0.5)

        # Create a base box
        box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(0, base_length),
            rg.Interval(0, base_width),
            rg.Interval(0, base_height)
        )

        # Convert Box to Brep
        brep = box.ToBrep()

        # Apply skew transformation
        skew_center = rg.Point3d(base_length / 2, base_width / 2, base_height / 2)
        skew_transform_matrix = skew_transform(skew_angle, skew_center)
        brep.Transform(skew_transform_matrix)

        # Apply translation for interlocking effect
        translation = rg.Transform.Translation(x_shift, y_shift, z_shift)
        brep.Transform(translation)

        volumes.append(brep)

    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(base_dimensions=(12, 12, 12), volume_count=5, skew_angle_degrees=15, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(base_dimensions=(8, 10, 6), volume_count=10, skew_angle_degrees=20, seed=456)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(base_dimensions=(15, 15, 15), volume_count=8, skew_angle_degrees=25, seed=789)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(base_dimensions=(14, 14, 14), volume_count=6, skew_angle_degrees=18, seed=321)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(base_dimensions=(9, 11, 10), volume_count=4, skew_angle_degrees=30, seed=999)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
