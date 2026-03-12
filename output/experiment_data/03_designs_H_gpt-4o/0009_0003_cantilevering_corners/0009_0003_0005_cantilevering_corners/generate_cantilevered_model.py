# Created for 0009_0003_cantilevering_corners.json

""" Summary:
The function `generate_cantilevered_model` creates an architectural concept model based on the metaphor of "Cantilevering corners." It constructs a central mass representing stability, from which multiple cantilevered sections extend outward at varying heights and orientations, embodying dynamic tension and balance. By utilizing random parameters for cantilever length, height, and rotation, the model achieves a visually striking silhouette that highlights the contrast between anchored stability and floating projections. These cantilevers generate intriguing voids and spaces, enhancing interaction with light and the environment, while fostering exploration through their dynamic arrangement, as outlined in the design task."""

#! python 3
function_code = """def generate_cantilevered_model(base_dimensions, cantilever_specifications, num_cantilevers):
    \"""
    Generates an architectural Concept Model embodying the 'Cantilevering corners' metaphor. The model consists of a central
    mass with dramatic cantilevers extending from it at various angles and heights, emphasizing the tension between stability
    and motion.

    Parameters:
    - base_dimensions (tuple): A tuple of three floats (width, depth, height) representing the central base's dimensions in meters.
    - cantilever_specifications (tuple): A tuple of three floats (length, max_height, thickness) representing the cantilever's dimensions.
    - num_cantilevers (int): The number of cantilevered sections to create.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Seed for reproducibility
    random.seed(42)

    # Unpack base dimensions and cantilever specifications
    base_width, base_depth, base_height = base_dimensions
    cantilever_length, max_cantilever_height, cantilever_thickness = cantilever_specifications

    # Create the central base mass
    base_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(base_width, 0, 0),
        rg.Point3d(base_width, base_depth, 0),
        rg.Point3d(0, base_depth, 0),
        rg.Point3d(0, 0, base_height),
        rg.Point3d(base_width, 0, base_height),
        rg.Point3d(base_width, base_depth, base_height),
        rg.Point3d(0, base_depth, base_height)
    ]
    base_box = rg.Brep.CreateFromBox(base_corners)

    # Prepare a list to store all geometries
    geometries = [base_box]

    # Create cantilevered sections
    for _ in range(num_cantilevers):
        # Randomly choose a corner of the base to start the cantilever
        corner_index = random.randint(0, 3)
        base_point = base_corners[corner_index]

        # Randomly choose cantilever orientation and height
        direction = rg.Vector3d(random.choice([-1, 1]), random.choice([-1, 1]), 0)
        cantilever_height = random.uniform(base_height, base_height + max_cantilever_height)

        # Determine cantilever endpoints
        cantilever_points = [
            base_point,
            base_point + rg.Vector3d(cantilever_length * direction.X, 0, 0),
            base_point + rg.Vector3d(cantilever_length * direction.X, cantilever_length * direction.Y, 0),
            base_point + rg.Vector3d(0, cantilever_length * direction.Y, 0),
            base_point + rg.Vector3d(0, 0, cantilever_height),
            base_point + rg.Vector3d(cantilever_length * direction.X, 0, cantilever_height),
            base_point + rg.Vector3d(cantilever_length * direction.X, cantilever_length * direction.Y, cantilever_height),
            base_point + rg.Vector3d(0, cantilever_length * direction.Y, cantilever_height)
        ]

        # Create the cantilever geometry
        cantilever_box = rg.Brep.CreateFromBox(cantilever_points)

        # Randomly apply a rotation to simulate dynamic projection
        rotation_angle = random.uniform(-math.pi/4, math.pi/4)  # Random rotation between -45 and 45 degrees
        rotation_center = rg.Point3d(base_width / 2, base_depth / 2, cantilever_height / 2)
        rotation_transform = rg.Transform.Rotation(rotation_angle, rg.Vector3d.ZAxis, rotation_center)
        cantilever_box.Transform(rotation_transform)

        # Add to geometry list
        geometries.append(cantilever_box)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cantilevered_model((10.0, 8.0, 4.0), (3.0, 5.0, 0.2), 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cantilevered_model((12.0, 10.0, 6.0), (4.0, 7.0, 0.15), 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cantilevered_model((15.0, 12.0, 5.0), (5.0, 6.0, 0.3), 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cantilevered_model((9.0, 7.0, 3.0), (2.5, 4.0, 0.25), 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cantilevered_model((14.0, 10.0, 5.0), (3.5, 8.0, 0.1), 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
