# Created for 0005_0003_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_model` generates an architectural concept model inspired by the "Distorted puzzle" metaphor by creating geometric elements that are interlocked yet misaligned, simulating a dynamic imbalance. It achieves this by defining a series of boxes, each randomly scaled and twisted within specified ranges. The twisting adds visual complexity, while the random translations create a spatial network of interconnected rooms and corridors that encourage exploration. The output is a collection of 3D geometries that embody the metaphor's essence, balancing disorder with structural coherence, ultimately evoking a sense of transformation as one navigates through the space."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_size, num_elements, twist_angle_range, scale_range, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Distorted puzzle' metaphor.
    
    This function generates a series of geometric elements that are slightly twisted or rotated relative to each other,
    forming a cohesive spatial network of interconnected rooms and pathways. The design emphasizes a visual dialogue
    between elements through varying scales and orientations to convey a sense of dynamic imbalance and exploration.

    Parameters:
    - base_size (float): The base size of the geometric elements in meters.
    - num_elements (int): The number of geometric elements to create.
    - twist_angle_range (tuple of float): Min and max angle in degrees for twisting the elements.
    - scale_range (tuple of float): Min and max scale factor for elements.
    - seed (int): A seed for the random number generator to ensure replicability.

    Returns:
    - list of Rhino.Geometry.Brep: A list of 3D brep geometries representing the concept model.
    \"""
    import Rhino
    import random
    import math
    from Rhino.Geometry import Box, Plane, Point3d, Vector3d, Transform, Brep

    random.seed(seed)
    elements = []
    current_position = Point3d(0, 0, 0)

    for _ in range(num_elements):
        # Define the base box dimensions with random scaling
        scale_x = base_size * random.uniform(*scale_range)
        scale_y = base_size * random.uniform(*scale_range)
        scale_z = base_size * random.uniform(*scale_range)

        # Create a box centered on the origin
        base_plane = Plane.WorldXY
        box_corners = [
            Point3d(0, 0, 0),
            Point3d(scale_x, 0, 0),
            Point3d(scale_x, scale_y, 0),
            Point3d(0, scale_y, 0),
            Point3d(0, 0, scale_z),
            Point3d(scale_x, 0, scale_z),
            Point3d(scale_x, scale_y, scale_z),
            Point3d(0, scale_y, scale_z)
        ]
        box = Box(base_plane, box_corners)

        # Convert box to Brep
        brep = box.ToBrep()

        # Apply a random twist to the box around its center
        twist_angle = random.uniform(*twist_angle_range)
        twist_axis = Vector3d(0, 0, 1)
        twist_transform = Transform.Rotation(math.radians(twist_angle), twist_axis, box.Center)
        brep.Transform(twist_transform)

        # Randomly translate the box to create a dynamic spatial network
        translate_x = random.uniform(-base_size, base_size)
        translate_y = random.uniform(-base_size, base_size)
        translate_z = random.uniform(0, base_size)
        translation_transform = Transform.Translation(Vector3d(translate_x, translate_y, translate_z))
        brep.Transform(translation_transform)

        # Add the transformed Brep to the list
        elements.append(brep)

    return elements"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(5.0, 10, (0, 360), (0.5, 2.0))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(3.0, 15, (30, 150), (1.0, 3.0), seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(4.0, 8, (45, 90), (0.8, 1.5), seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(6.0, 12, (15, 180), (0.3, 1.8), seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(2.5, 20, (10, 90), (0.6, 2.5), seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
