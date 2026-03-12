# Created for 0005_0004_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_model` generates an architectural concept model based on the "Distorted puzzle" metaphor by creating irregularly shaped units that embody tension and dynamic alignment. It uses parameters like base dimensions, variability, tilt angles, and skew factors to produce a series of interconnected geometric forms. Each unit is randomly tilted and skewed, resulting in a visually complex structure that promotes non-linear spatial arrangements. The design emphasizes niches and alcoves for exploration while aligning key visual axes, ensuring coherence amidst the unpredictability of the spatial relationships, effectively capturing the essence of the metaphor."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_dim, unit_variability, unit_count, tilt_range, skew_range, seed=1):
    \"""
    Create an architectural Concept Model based on the 'Distorted puzzle' metaphor.

    This function generates a series of interconnected units with irregular shapes that imply tension and dynamic
    alignment. The resulting geometry features tilted planes and skewed edges, promoting non-linear spatial
    arrangements with niches and alcoves. The design maintains coherence through key visual axes while inviting
    exploration with unexpected spatial relationships.

    Parameters:
    - base_dim (float): The average dimension for the base size of each unit in meters.
    - unit_variability (float): The variability factor to apply to the size of each unit.
    - unit_count (int): The total number of units to generate.
    - tilt_range (tuple): A tuple of two floats representing the minimum and maximum tilt angles (in degrees).
    - skew_range (tuple): A tuple of two floats representing the minimum and maximum skew factors.
    - seed (int): Seed for the random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for reproducibility
    random.seed(seed)

    # List to store the generated geometry
    breps = []

    for _ in range(unit_count):
        # Determine random dimensions for the unit
        width = base_dim * random.uniform(1 - unit_variability, 1 + unit_variability)
        depth = base_dim * random.uniform(1 - unit_variability, 1 + unit_variability)
        height = base_dim * random.uniform(1 - unit_variability, 1 + unit_variability)

        # Create a base box
        base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))

        # Randomly determine a tilt angle and axis
        tilt_angle = math.radians(random.uniform(tilt_range[0], tilt_range[1]))
        tilt_axis = random.choice([rg.Vector3d.XAxis, rg.Vector3d.YAxis, rg.Vector3d.ZAxis])
        tilt_transform = rg.Transform.Rotation(tilt_angle, tilt_axis, base_box.Center)
        base_box.Transform(tilt_transform)

        # Randomly determine a skew factor and apply a shear transformation
        skew_factor = random.uniform(skew_range[0], skew_range[1])
        shear_transform = rg.Transform.Identity
        if tilt_axis == rg.Vector3d.XAxis:
            shear_transform.M21 = skew_factor
        elif tilt_axis == rg.Vector3d.YAxis:
            shear_transform.M12 = skew_factor
        else:
            shear_transform.M13 = skew_factor
        base_box.Transform(shear_transform)

        # Convert the box to a Brep and add to the list
        brep = base_box.ToBrep()
        breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(5.0, 0.2, 10, (15, 45), (0.1, 0.3))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(3.0, 0.15, 15, (10, 30), (0.05, 0.2))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(4.0, 0.25, 8, (20, 60), (0.2, 0.4))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(6.0, 0.1, 12, (5, 25), (0.3, 0.5))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(7.0, 0.3, 20, (10, 50), (0.2, 0.6))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
