# Created for 0005_0004_distorted_puzzle.json

""" Summary:
The provided function, `create_distorted_puzzle_concept_model`, generates an architectural concept model inspired by the "Distorted puzzle" metaphor. It creates a collection of irregularly shaped units that exhibit tilted planes and skewed edges, capturing the essence of interconnectedness with visual tension. By varying tilt angles and skew factors, each unit appears misaligned yet coherently assembled, embodying unpredictability and complexity. The function promotes a non-linear spatial flow, facilitating niches and alcoves that encourage exploration. Ultimately, it achieves a balance of visual interest and structural unity, reflecting the metaphor's dynamic interplay and overall coherence in the architectural design."""

#! python 3
function_code = """def create_distorted_puzzle_concept_model(base_size, num_units, tilt_angle_range, skew_factor_range, random_seed):
    \"""
    Creates an architectural Concept Model based on the 'Distorted puzzle' metaphor.
    
    This function generates a series of interconnected yet irregularly shaped units that
    simulate a distorted puzzle. The units feature tilted planes and skewed edges, promoting
    a non-linear spatial flow with niches and alcoves.

    Parameters:
    - base_size (float): The base size of each unit in meters.
    - num_units (int): The number of units to generate.
    - tilt_angle_range (tuple of float): The range (min, max) of tilt angles for the planes in degrees.
    - skew_factor_range (tuple of float): The range (min, max) of factors to skew the units.
    - random_seed (int): Seed for the random number generator to ensure replicability.

    Returns:
    - List of Rhino.Geometry.Brep: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(random_seed)
    
    breps = []
    
    for i in range(num_units):
        # Randomly determine the tilt and skew
        tilt_angle = random.uniform(tilt_angle_range[0], tilt_angle_range[1])
        skew_factor = random.uniform(skew_factor_range[0], skew_factor_range[1])
        
        # Create a base box
        base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_size), rg.Interval(0, base_size), rg.Interval(0, base_size))
        
        # Tilt the box by rotating around the X or Y axis
        axis_choice = random.choice([rg.Vector3d.XAxis, rg.Vector3d.YAxis])
        rotation = rg.Transform.Rotation(math.radians(tilt_angle), axis_choice, base_box.Center)
        base_box.Transform(rotation)
        
        # Skew the box by applying a shear transformation
        shear_transform = rg.Transform.Identity
        if axis_choice == rg.Vector3d.XAxis:
            shear_transform.M13 = skew_factor  # Skew along Z on X axis
        else:
            shear_transform.M23 = skew_factor  # Skew along Z on Y axis
        
        base_box.Transform(shear_transform)
        
        # Convert box to Brep and append to the list
        brep = base_box.ToBrep()
        breps.append(brep)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_concept_model(5.0, 10, (15, 45), (0.1, 0.5), 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_concept_model(3.5, 8, (10, 30), (0.2, 0.6), 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_concept_model(4.0, 12, (5, 35), (0.3, 0.7), 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_concept_model(6.0, 15, (20, 50), (0.05, 0.4), 100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_concept_model(2.5, 6, (0, 60), (0.0, 0.3), 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
