# Created for 0005_0003_distorted_puzzle.json

""" Summary:
The provided function, `create_distorted_puzzle_model`, generates an architectural concept model inspired by the 'Distorted puzzle' metaphor. It constructs a series of geometric elements boxes that are slightly twisted and randomly translated creating a dynamic arrangement that embodies visual complexity and spatial exploration. Each box's dimensions vary, and angles of twist introduce a sense of imbalance. The interconnected elements form a cohesive network of rooms and pathways, echoing the metaphor's theme of irregularity and interdependence. Ultimately, the model reflects the playful, unpredictable nature of a puzzle while ensuring structural coherence, inviting occupants to navigate through evolving spaces."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_size, twist_angle, num_elements, seed=42):
    \"""
    Create an architectural Concept Model based on the 'Distorted puzzle' metaphor.
    
    This function generates a series of geometric elements that are slightly twisted or rotated relative to each other,
    forming a cohesive spatial network of interconnected rooms and pathways. The design emphasizes a visual dialogue
    between elements through varying scales and orientations to convey a sense of dynamic imbalance and exploration.

    Parameters:
    - base_size: float, the base size of the geometric elements in meters.
    - twist_angle: float, the maximum angle in degrees by which each element can be twisted or rotated.
    - num_elements: int, the number of geometric elements to create.
    - seed: int, a seed for the random number generator to ensure replicability.

    Returns:
    - list of Rhino.Geometry.Brep: a list of 3D brep geometries representing the concept model.
    \"""
    import Rhino
    import random
    import math
    from Rhino.Geometry import Box, Plane, Point3d, Vector3d, Transform, Brep

    random.seed(seed)
    elements = []

    for i in range(num_elements):
        # Define the base box dimensions with slight variations
        width = base_size * random.uniform(0.8, 1.2)
        depth = base_size * random.uniform(0.8, 1.2)
        height = base_size * random.uniform(0.5, 1.5)

        # Create a box centered on the origin
        base_plane = Plane.WorldXY
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
        box = Box(base_plane, box_corners)

        # Randomly twist the box around the Z-axis
        angle = random.uniform(-twist_angle, twist_angle)
        twist_transform = Transform.Rotation(math.radians(angle), Vector3d.ZAxis, Point3d.Origin)
        twisted_brep = Brep.CreateFromBox(box)
        twisted_brep.Transform(twist_transform)

        # Randomly translate the box to create a dynamic spatial network
        translation_vector = Vector3d(
            random.uniform(-base_size, base_size),
            random.uniform(-base_size, base_size),
            random.uniform(0, base_size)
        )
        translate_transform = Transform.Translation(translation_vector)
        twisted_brep.Transform(translate_transform)

        elements.append(twisted_brep)

    return elements"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(5.0, 30.0, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(3.0, 45.0, 15, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(4.0, 60.0, 20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(6.0, 15.0, 5, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(2.5, 90.0, 8, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
