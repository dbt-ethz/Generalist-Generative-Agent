# Created for 0005_0001_distorted_puzzle.json

""" Summary:
The provided function `create_distorted_puzzle_model` generates an architectural concept model inspired by the "Distorted puzzle" metaphor. It creates a series of interlocking geometric volumes with slight misalignments, embodying the tension and movement suggested by the metaphor. Each volume's dimensions and positions are randomized to enhance the irregularity, while skew transformations applied to the boxes create a visually intriguing distortion. The final output is a collection of Brep geometries that interconnect coherently, fostering exploration within the space. This model captures the essence of a dynamic, interconnected structure that invites discovery, much like a jigsaw puzzle."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_dimension=10, num_volumes=6, skew_angle=10, seed=123):
    \"""
    Create an architectural Concept Model that embodies the 'Distorted puzzle' metaphor by assembling a series of interlocking
    geometric volumes with slight misalignments. The model emphasizes the spatial logic of interlocking and overlapping forms to
    generate dynamic pathways and spaces that invite exploration.

    Parameters:
    - base_dimension: The approximate size of the base dimension of each volume in meters.
    - num_volumes: The number of interlocking volumes to create.
    - skew_angle: The maximum skew angle in degrees to apply for distortion.
    - seed: An integer used to seed the random number generator for reproducibility.

    Returns:
    - A list of Brep geometries representing the interlocking volumes of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    volumes = []

    for i in range(num_volumes):
        # Randomly decide dimensions and position offsets for each volume
        width = random.uniform(base_dimension * 0.8, base_dimension * 1.2)
        depth = random.uniform(base_dimension * 0.8, base_dimension * 1.2)
        height = random.uniform(base_dimension * 0.8, base_dimension * 1.2)

        # Create a base box
        base_box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(0, width),
            rg.Interval(0, depth),
            rg.Interval(0, height)
        )

        # Convert Box to Brep
        brep = base_box.ToBrep()

        # Apply skew transformation to create distortion
        skew_x = random.uniform(-math.radians(skew_angle), math.radians(skew_angle))
        skew_y = random.uniform(-math.radians(skew_angle), math.radians(skew_angle))
        
        # Corrected skew transformations
        skew_transform_x = rg.Transform.Identity
        skew_transform_x.M21 = math.tan(skew_x)
        brep.Transform(skew_transform_x)
        
        skew_transform_y = rg.Transform.Identity
        skew_transform_y.M12 = math.tan(skew_y)
        brep.Transform(skew_transform_y)
        
        # Random translation to create interlocking effect
        translation_vector = rg.Vector3d(
            random.uniform(-base_dimension * 0.5, base_dimension * 0.5),
            random.uniform(-base_dimension * 0.5, base_dimension * 0.5),
            random.uniform(-base_dimension * 0.5, base_dimension * 0.5)
        )
        brep.Translate(translation_vector)

        volumes.append(brep)

    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(base_dimension=15, num_volumes=8, skew_angle=15, seed=456)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(base_dimension=12, num_volumes=5, skew_angle=20, seed=789)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(base_dimension=8, num_volumes=10, skew_angle=5, seed=321)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(base_dimension=20, num_volumes=4, skew_angle=30, seed=654)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(base_dimension=18, num_volumes=7, skew_angle=25, seed=999)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
