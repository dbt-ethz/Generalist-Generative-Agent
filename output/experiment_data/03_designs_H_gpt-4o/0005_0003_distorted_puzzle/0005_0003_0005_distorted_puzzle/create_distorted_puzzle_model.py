# Created for 0005_0003_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_model` generates an architectural concept model that embodies the "Distorted puzzle" metaphor by crafting a series of geometric elements that are slightly twisted and rotated. Each element, represented as a 3D Brep, is created with varying dimensions and orientations, emphasizing visual complexity. The function incorporates randomness in element positioning and twisting angles to evoke a sense of dynamic imbalance and exploration. As the elements interconnect, they form a cohesive spatial network of rooms and pathways, reflecting the metaphor's underlying theme of interconnectedness while maintaining a playful tension between order and disorder."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_scale=10, twist_range=(5, 15), num_elements=6, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Distorted puzzle' metaphor.

    This function generates a series of geometric elements that are slightly twisted or rotated relative to each other,
    forming a cohesive spatial network of interconnected rooms and pathways. The design emphasizes a visual dialogue
    between elements through varying scales and orientations to convey a sense of dynamic imbalance and exploration.

    Parameters:
    - base_scale (float): The base size of the elements in meters.
    - twist_range (tuple of float): Min and max angle in degrees for twisting the elements.
    - num_elements (int): The number of geometric elements to create.
    - seed (int): A seed for the random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the concept model.
    \"""
    import Rhino
    import random
    import math
    from Rhino.Geometry import Box, Plane, Point3d, Vector3d, Transform, Brep

    random.seed(seed)
    elements = []
    current_position = Point3d(0, 0, 0)

    for i in range(num_elements):
        # Define the base box dimensions with slight variations
        width = base_scale * random.uniform(0.7, 1.3)
        depth = base_scale * random.uniform(0.7, 1.3)
        height = base_scale * random.uniform(0.6, 1.4)

        # Create a box centered on the origin
        box_corners = [
            Point3d(-width/2, -depth/2, 0),
            Point3d(width/2, -depth/2, 0),
            Point3d(width/2, depth/2, 0),
            Point3d(-width/2, depth/2, 0),
            Point3d(-width/2, -depth/2, height),
            Point3d(width/2, -depth/2, height),
            Point3d(width/2, depth/2, height),
            Point3d(-width/2, depth/2, height)
        ]
        box = Box(Plane.WorldXY, box_corners)

        # Convert box to Brep
        brep = box.ToBrep()

        # Apply a random twist to each element
        twist_angle = random.uniform(*twist_range)
        twist_center = current_position + Vector3d(0, 0, height / 2)
        twist_transform = Transform.Rotation(math.radians(twist_angle), Vector3d.ZAxis, twist_center)
        brep.Transform(twist_transform)

        # Move the element to a new position
        offset_vector = Vector3d(random.uniform(-base_scale, base_scale),
                                 random.uniform(-base_scale, base_scale),
                                 random.uniform(0, base_scale))
        translation_transform = Transform.Translation(current_position + offset_vector)
        brep.Transform(translation_transform)

        # Add to elements
        elements.append(brep)

        # Update the current position
        current_position += Vector3d(width * 0.5, depth * 0.5, height * 0.1)

    return elements"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(base_scale=12, twist_range=(10, 20), num_elements=8, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(base_scale=15, twist_range=(0, 30), num_elements=10, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(base_scale=8, twist_range=(15, 25), num_elements=5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(base_scale=20, twist_range=(5, 10), num_elements=4, seed=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(base_scale=18, twist_range=(8, 18), num_elements=7, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
