# Created for 0005_0003_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_model` generates an architectural concept model inspired by the "Distorted puzzle" metaphor by creating interconnected geometric elements that are slightly twisted and rotated. It uses random dimensions and orientations for each room, ensuring a playful juxtaposition of forms. The function applies transformations to each geometric element, including random rotations and translations, to enhance visual complexity and evoke a sense of dynamic imbalance. By allowing for varying scales and angles, it fosters a spatial network that encourages exploration and movement through the model, reflecting the interconnectedness and unpredictability inherent in the metaphor."""

#! python 3
function_code = """def create_distorted_puzzle_model(room_count, min_size, max_size, twist_angle, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Distorted puzzle' metaphor.

    This function generates a series of interconnected geometric elements that are slightly twisted or rotated
    relative to each other. It emphasizes a dynamic and visually complex form, with varying scales and orientations
    to evoke a sense of exploration and transformation.

    Parameters:
    - room_count (int): The number of rooms or blocks to create in the model.
    - min_size (float): The minimum dimension for the rooms in meters.
    - max_size (float): The maximum dimension for the rooms in meters.
    - twist_angle (float): The maximum angle in degrees for twisting or rotating elements.
    - seed (int): The seed for the random number generator to ensure replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Breps representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    geometries = []

    for _ in range(room_count):
        # Randomly determine room dimensions
        width = random.uniform(min_size, max_size)
        length = random.uniform(min_size, max_size)
        height = random.uniform(min_size, max_size)

        # Create a box
        box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, width), rg.Interval(0, length), rg.Interval(0, height))
        brep_box = box.ToBrep()

        # Apply random rotation around a random axis
        axis = rg.Vector3d(
            random.choice([1, 0, 0]), 
            random.choice([0, 1, 0]), 
            random.choice([0, 0, 1])
        )
        angle = math.radians(random.uniform(-twist_angle, twist_angle))
        rotation_transform = rg.Transform.Rotation(angle, axis, rg.Point3d(0, 0, 0))
        brep_box.Transform(rotation_transform)

        # Randomly position each element
        translate_x = random.uniform(-max_size, max_size)
        translate_y = random.uniform(-max_size, max_size)
        translate_z = random.uniform(0, max_size)
        translation_transform = rg.Transform.Translation(rg.Vector3d(translate_x, translate_y, translate_z))
        brep_box.Transform(translation_transform)

        # Add the transformed brep to the list
        geometries.append(brep_box)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(10, 5.0, 15.0, 45.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(8, 3.0, 10.0, 30.0, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(15, 2.0, 8.0, 60.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(12, 4.0, 12.0, 90.0, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(20, 1.0, 5.0, 75.0, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
