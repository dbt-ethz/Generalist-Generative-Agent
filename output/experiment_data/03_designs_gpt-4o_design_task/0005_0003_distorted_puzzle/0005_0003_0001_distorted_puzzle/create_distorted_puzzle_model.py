# Created for 0005_0003_distorted_puzzle.json

""" Summary:
The provided function, `create_distorted_puzzle_model`, generates an architectural concept model inspired by the "Distorted puzzle" metaphor. It creates a series of geometric elements that are slightly twisted and rotated, reflecting dynamic imbalance and visual complexity. Each element is randomly scaled and positioned, simulating the playful juxtaposition of varying forms. The function incorporates transformations, such as twisting and translating, to develop interconnected rooms and corridors that shift in size and shape, evoking a sense of exploration. This approach captures the essence of interconnectedness and disorder, aligning with the metaphor's emphasis on dynamic spatial relationships and coherence."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_length, base_width, base_height, num_elements, twist_angle_range, scale_variation):
    \"""
    Creates an architectural Concept Model based on the 'Distorted puzzle' metaphor, using a series of geometric elements
    that are slightly twisted or rotated relative to each other. This function focuses on creating a visual dialogue between 
    these elements through varying scales and orientations to emphasize the distorted aspect. It develops a spatial network 
    of interconnected rooms and pathways that shift in size and shape.

    Parameters:
    - base_length (float): Base length of the geometric elements in meters.
    - base_width (float): Base width of the geometric elements in meters.
    - base_height (float): Base height of the geometric elements in meters.
    - num_elements (int): Number of geometric elements to create.
    - twist_angle_range (tuple of float): Min and max angle in degrees for twisting the elements.
    - scale_variation (tuple of float): Min and max scale factor for elements.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Point3d, Box, Plane, BoundingBox, Brep, Transform, Vector3d
    
    # Set seed for randomness
    random.seed(42)

    geometries = []

    for i in range(num_elements):
        # Randomly determine scale factors
        scale_x = random.uniform(*scale_variation)
        scale_y = random.uniform(*scale_variation)
        scale_z = random.uniform(*scale_variation)

        # Create a base box
        base_origin = Point3d(0, 0, 0)
        base_plane = Plane(base_origin, Vector3d(0, 0, 1))
        box_corners = [
            Point3d(0, 0, 0),
            Point3d(base_length * scale_x, 0, 0),
            Point3d(base_length * scale_x, base_width * scale_y, 0),
            Point3d(0, base_width * scale_y, 0),
            Point3d(0, 0, base_height * scale_z),
            Point3d(base_length * scale_x, 0, base_height * scale_z),
            Point3d(base_length * scale_x, base_width * scale_y, base_height * scale_z),
            Point3d(0, base_width * scale_y, base_height * scale_z)
        ]

        box = Box(base_plane, box_corners)

        # Convert box to Brep
        brep = box.ToBrep()

        # Apply a random twist to each element
        twist_angle = random.uniform(*twist_angle_range)
        twist_transform = Transform.Rotation(Rhino.RhinoMath.ToRadians(twist_angle), Vector3d(0, 0, 1), box.Center)
        brep.Transform(twist_transform)

        # Randomly position each element
        translate_x = random.uniform(-base_length, base_length)
        translate_y = random.uniform(-base_width, base_width)
        translate_z = random.uniform(0, base_height)
        translation_transform = Transform.Translation(Vector3d(translate_x, translate_y, translate_z))
        brep.Transform(translation_transform)

        # Add the transformed Brep to the list
        geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(5.0, 3.0, 2.0, 10, (0, 360), (0.5, 1.5))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(4.0, 2.0, 3.0, 15, (15, 90), (0.8, 1.2))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(6.0, 4.0, 1.5, 12, (30, 180), (0.6, 2.0))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(7.0, 5.0, 4.0, 20, (45, 135), (1.0, 2.5))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(8.0, 6.0, 3.0, 8, (10, 300), (0.3, 1.8))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
