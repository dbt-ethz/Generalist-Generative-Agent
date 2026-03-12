# Created for 0005_0004_distorted_puzzle.json

""" Summary:
The provided function, `create_distorted_puzzle_concept_model`, generates an architectural concept model based on the "Distorted puzzle" metaphor. It creates a series of interconnected, irregularly shaped units that embody perceived tension through skewed and tilted planes. The model emphasizes non-linear spatial arrangements, resulting in niches and alcoves that encourage exploration. Each unit's dimensions are randomized, ensuring variability while maintaining coherence through key visual axes. The output is a collection of 3D geometries that reflect the metaphor's complexity and unpredictability, encapsulating the essence of a distorted yet cohesive architectural puzzle."""

#! python 3
function_code = """def create_distorted_puzzle_concept_model(base_width, base_depth, base_height, num_units, seed=None):
    \"""
    Creates an architectural Concept Model inspired by the 'Distorted puzzle' metaphor.
    
    This function generates a series of interconnected, irregularly shaped units that fit together
    through perceived tension and dynamic alignment. The design emphasizes tilted planes, skewed edges,
    and a non-linear spatial flow with interlocking spaces forming niches and alcoves. Key visual axes
    maintain coherence, while the arrangement reveals unexpected relationships and connections.
    
    Parameters:
    - base_width (float): The base width of the model in meters.
    - base_depth (float): The base depth of the model in meters.
    - num_units (int): The number of irregular units to create.
    - seed (int, optional): Seed for randomization to ensure replicability.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries (breps) representing the concept model.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Brep, Box, Plane, Point3d, Vector3d, Transform, Interval

    if seed is not None:
        random.seed(seed)

    geometries = []

    # Define base unit dimensions and offsets
    unit_width = base_width / (num_units + random.uniform(0.5, 1.5))
    unit_depth = base_depth / (num_units + random.uniform(0.5, 1.5))
    unit_height = base_height / (num_units + random.uniform(0.5, 1.5))
    
    for i in range(num_units):
        # Randomly skew and tilt each unit
        skew_factor = random.uniform(-0.3, 0.3)
        tilt_angle = random.uniform(-15, 15)  # degrees

        # Create a base unit box
        base_plane = Plane.WorldXY
        origin = Point3d(i * unit_width * 0.8, i * unit_depth * 0.8, i * unit_height * 0.5)
        x_interval = Interval(origin.X, origin.X + unit_width)
        y_interval = Interval(origin.Y, origin.Y + unit_depth)
        z_interval = Interval(origin.Z, origin.Z + unit_height)
        box = Box(base_plane, x_interval, y_interval, z_interval)
        brep_box = box.ToBrep()

        # Apply skew
        xform_shear = Transform.Identity
        xform_shear.M00 = 1
        xform_shear.M01 = skew_factor
        xform_shear.M10 = 0
        xform_shear.M11 = 1
        brep_box.Transform(xform_shear)

        # Apply tilt
        tilt_transform = Transform.Rotation(tilt_angle * (3.14159 / 180), Vector3d(0, 0, 1), origin)
        brep_box.Transform(tilt_transform)

        geometries.append(brep_box)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_concept_model(10.0, 5.0, 3.0, 8, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_concept_model(15.0, 10.0, 4.0, 12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_concept_model(20.0, 15.0, 5.0, 10, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_concept_model(12.0, 8.0, 6.0, 5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_concept_model(25.0, 20.0, 10.0, 15, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
