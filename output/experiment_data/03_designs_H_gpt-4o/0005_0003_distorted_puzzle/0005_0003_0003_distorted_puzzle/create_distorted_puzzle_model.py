# Created for 0005_0003_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_model` generates an architectural concept model based on the "Distorted puzzle" metaphor by creating a variety of geometric elements that are twisted and rotated relative to one another. It begins by defining parameters such as the number of rooms, their dimensions, and the maximum twist angle. Each room is represented as a box, which is then randomly twisted and translated to create a dynamic arrangement. This results in a spatial network with interdependent rooms that evoke exploration and transformation, reflecting the metaphor's themes of visual complexity and interconnectedness while maintaining structural coherence."""

#! python 3
function_code = """def create_distorted_puzzle_model(room_count, min_dim, max_dim, max_twist_angle, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Distorted puzzle' metaphor.

    This function generates a series of geometric elements that are slightly twisted or rotated relative to each other,
    forming interconnected rooms and corridors. The model emphasizes a sense of dynamic imbalance and exploration.

    Parameters:
    - room_count (int): Number of room-like elements to create.
    - min_dim (float): Minimum dimension size for the rooms in meters.
    - max_dim (float): Maximum dimension size for the rooms in meters.
    - max_twist_angle (float): Maximum angle in degrees for twisting each room element.
    - seed (int): Seed for the random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)

    geometries = []
    current_position = rg.Point3d(0, 0, 0)

    for _ in range(room_count):
        # Randomly determine room size
        width = random.uniform(min_dim, max_dim)
        depth = random.uniform(min_dim, max_dim)
        height = random.uniform(min_dim / 2, max_dim / 2)

        # Create a base box
        base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))
        brep_box = base_box.ToBrep()

        # Apply a random twist
        twist_angle = random.uniform(-max_twist_angle, max_twist_angle)
        twist_axis = rg.Line(base_box.Center, rg.Point3d(base_box.Center.X, base_box.Center.Y, base_box.Center.Z + height))
        twist_transform = rg.Transform.Rotation(math.radians(twist_angle), twist_axis.Direction, twist_axis.From)
        brep_box.Transform(twist_transform)

        # Randomly translate the box to simulate dynamic spatial arrangement
        translation_vector = rg.Vector3d(
            random.uniform(-width * 0.5, width * 0.5),
            random.uniform(-depth * 0.5, depth * 0.5),
            random.uniform(0, height * 0.5)
        )
        translation_transform = rg.Transform.Translation(translation_vector)
        brep_box.Transform(translation_transform)

        # Add to the list of geometries
        geometries.append(brep_box)

        # Update current position for the next room
        current_position += translation_vector

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(10, 3.0, 7.0, 45.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(5, 2.0, 5.0, 30.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(8, 4.0, 10.0, 60.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(12, 1.5, 6.0, 90.0, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(15, 2.5, 8.0, 75.0, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
