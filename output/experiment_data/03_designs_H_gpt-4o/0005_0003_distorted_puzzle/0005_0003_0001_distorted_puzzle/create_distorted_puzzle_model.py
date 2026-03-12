# Created for 0005_0003_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_model` generates an architectural concept model based on the "Distorted puzzle" metaphor by creating a series of interlocking geometric elements. Each element is slightly twisted and rotated to emphasize dynamic imbalance and visual complexity, reflecting the metaphor's playful nature. The function randomizes dimensions and orientations while ensuring the elements are interconnected, forming a network of uniquely shaped rooms and corridors. This design approach evokes a sense of exploration and transformation, as users navigate through spaces that shift in size and shape, maintaining an underlying structural coherence akin to a puzzle."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_dim, twist_angle_range, num_elements, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Distorted puzzle' metaphor.

    This function generates a series of geometric elements that are slightly twisted or rotated relative to each other,
    emphasizing dynamic imbalance and visual complexity. The elements are interconnected, forming a network of rooms
    and corridors that shift in size and shape, evoking a sense of exploration.

    Parameters:
    - base_dim (tuple of float): Base dimensions (length, width, height) of the geometric elements in meters.
    - twist_angle_range (tuple of float): Min and max angle in degrees for twisting the elements.
    - num_elements (int): Number of geometric elements to create.
    - seed (int): Seed for the random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino
    import random
    import math
    from Rhino.Geometry import Point3d, Box, Plane, Brep, Transform, Vector3d

    random.seed(seed)

    length, width, height = base_dim
    geometries = []
    current_position = Point3d(0, 0, 0)

    for i in range(num_elements):
        # Create a base box with slight random variation in dimensions
        scale_factor = random.uniform(0.8, 1.2)
        box_length = length * scale_factor
        box_width = width * scale_factor
        box_height = height * scale_factor

        box_corners = [
            Point3d(0, 0, 0),
            Point3d(box_length, 0, 0),
            Point3d(box_length, box_width, 0),
            Point3d(0, box_width, 0),
            Point3d(0, 0, box_height),
            Point3d(box_length, 0, box_height),
            Point3d(box_length, box_width, box_height),
            Point3d(0, box_width, box_height)
        ]

        box = Box(Plane.WorldXY, box_corners)
        brep = box.ToBrep()

        # Apply a random twist to each element
        twist_angle = random.uniform(*twist_angle_range)
        twist_transform = Transform.Rotation(math.radians(twist_angle), Vector3d(0, 0, 1), box.Center)
        brep.Transform(twist_transform)

        # Translate the element into position
        translation_vector = Vector3d(
            current_position.X + random.uniform(-length, length),
            current_position.Y + random.uniform(-width, width),
            current_position.Z + random.uniform(0, height)
        )
        translation_transform = Transform.Translation(translation_vector)
        brep.Transform(translation_transform)

        # Add the element to the list
        geometries.append(brep)

        # Update the current position for the next element
        current_position = Point3d.Add(current_position, translation_vector)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model((5, 3, 2), (-30, 30), 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model((4, 4, 3), (-45, 45), 15, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model((6, 2, 4), (-60, 60), 8, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model((7, 5, 3), (-15, 15), 12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model((3, 3, 3), (-90, 90), 20, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
