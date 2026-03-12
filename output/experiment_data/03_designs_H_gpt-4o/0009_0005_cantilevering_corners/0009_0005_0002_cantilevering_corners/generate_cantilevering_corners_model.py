# Created for 0009_0005_cantilevering_corners.json

""" Summary:
The function `generate_cantilevering_corners_model` creates an architectural concept model inspired by the metaphor of "Cantilevering corners." It establishes a central core representing stability, from which multiple cantilevered sections extend outward at varied angles. This design embodies the contrast between stability and motion, evoking a sense of dynamic tension. By manipulating the angles and lengths of the cantilevers, the function emphasizes interactions between solid and void, enhancing spatial exploration. The use of randomization and geometric parameters enables diverse outcomes, while the interplay of materials plays a crucial role in emphasizing light and shadow, further enriching the architectural narrative."""

#! python 3
function_code = """def generate_cantilevering_corners_model(core_dim=(5, 5, 10), cantilever_numbers=4, cantilever_max_length=8, cantilever_max_angle=60, seed=42):
    \"""
    Generates an architectural Concept Model embodying the 'Cantilevering corners' metaphor.

    The model features a central core with cantilevered sections extending outward at varied angles,
    creating a dynamic interplay between stability and motion. The design emphasizes the interaction
    of light and shadow and highlights the transition between solid and void spaces.

    Parameters:
    - core_dim (tuple): Dimensions of the central core as (width, depth, height) in meters.
    - cantilever_numbers (int): The number of cantilevered sections to extend from the core.
    - cantilever_max_length (float): Maximum possible length for each cantilever.
    - cantilever_max_angle (float): Maximum angle in degrees for cantilever deviation from horizontal.
    - seed (int): Seed for randomness to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Initialize random seed
    random.seed(seed)

    # Create the central core
    core_width, core_depth, core_height = core_dim
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_depth), rg.Interval(0, core_height))
    core_brep = core_box.ToBrep()
    
    geometries = [core_brep]

    # Process to create cantilevered sections
    for _ in range(cantilever_numbers):
        angle = random.uniform(-cantilever_max_angle, cantilever_max_angle)
        length = random.uniform(core_width * 0.5, cantilever_max_length)
        
        # Determine the cantilever base position
        base_x = random.uniform(0, core_width)
        base_y = random.uniform(0, core_depth)
        base_point = rg.Point3d(base_x, base_y, core_height)
        
        # Define direction and plane for cantilever
        direction = rg.Vector3d(math.cos(math.radians(angle)), math.sin(math.radians(angle)), 0)
        direction.Unitize()
        cantilever_plane = rg.Plane(base_point, direction)
        
        # Create the cantilever geometry
        cantilever_box = rg.Box(cantilever_plane, rg.Interval(0, length), rg.Interval(-core_depth * 0.25, core_depth * 0.25), rg.Interval(-core_height * 0.2, 0))
        cantilever_brep = cantilever_box.ToBrep()
        
        geometries.append(cantilever_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cantilevering_corners_model(core_dim=(5, 5, 10), cantilever_numbers=4, cantilever_max_length=8, cantilever_max_angle=60, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cantilevering_corners_model(core_dim=(10, 10, 15), cantilever_numbers=6, cantilever_max_length=10, cantilever_max_angle=45, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cantilevering_corners_model(core_dim=(8, 6, 12), cantilever_numbers=5, cantilever_max_length=7, cantilever_max_angle=75, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cantilevering_corners_model(core_dim=(4, 4, 8), cantilever_numbers=3, cantilever_max_length=9, cantilever_max_angle=50, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cantilevering_corners_model(core_dim=(6, 6, 10), cantilever_numbers=5, cantilever_max_length=9, cantilever_max_angle=30, seed=2022)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
