# Created for 0009_0005_cantilevering_corners.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "Cantilevering corners." It constructs a central core that serves as the stable anchor for the design. Multiple cantilevered sections extend outward at varied angles and lengths, creating a dynamic interplay between stability and motion. The function emphasizes the contrast between solid structures and voids, allowing for negative spaces that enhance exploration. By incorporating randomness in cantilever lengths and angles, the model achieves a visually engaging silhouette that conveys tension and balance, ultimately embodying the metaphor in a three-dimensional form."""

#! python 3
function_code = """def create_cantilevered_concept_model(core_dimensions=(4, 4, 10), num_cantilevers=4, cantilever_length_range=(5, 10), cantilever_angle_increment=15, seed=42):
    \"""
    Generates an architectural Concept Model embodying 'Cantilevering corners'.

    The model features a central core with cantilevered sections extending outward,
    creating a dynamic interplay between stability and motion. The design emphasizes
    the contrast between solid and void, and highlights the interaction of light and shadow.

    Parameters:
    - core_dimensions (tuple): Dimensions of the central core as (width, depth, height).
    - num_cantilevers (int): The number of cantilevered sections.
    - cantilever_length_range (tuple): The range of lengths for the cantilevers.
    - cantilever_angle_increment (float): The angle increment between successive cantilevers (in degrees).
    - seed (int): The seed for random number generation, ensuring reproducibility.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)

    # Unpack core dimensions
    core_width, core_depth, core_height = core_dimensions

    # Create the central core as a box
    core_origin = rg.Point3d(0, 0, 0)
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_depth), rg.Interval(0, core_height))
    geometries = [core_box.ToBrep()]

    # Define cantilevered sections
    angle = 0
    for _ in range(num_cantilevers):
        # Calculate the cantilever's direction vector based on the angle
        direction_vector = rg.Vector3d(math.cos(math.radians(angle)), math.sin(math.radians(angle)), 0)
        direction_vector.Unitize()

        # Determine the cantilever origin on the top face of the core
        cantilever_origin = rg.Point3d(core_width / 2, core_depth / 2, core_height)

        # Random cantilever length within the specified range
        cantilever_length = random.uniform(*cantilever_length_range)
        
        # Define cantilever dimensions
        cantilever_width = core_width / 2
        cantilever_height = core_height / 10

        # Create a cantilever box
        cantilever_end_point = cantilever_origin + direction_vector * cantilever_length
        cantilever_plane = rg.Plane(cantilever_end_point, direction_vector)

        cantilever_box = rg.Box(cantilever_plane, rg.Interval(-cantilever_width / 2, cantilever_width / 2), rg.Interval(-cantilever_width / 2, cantilever_width / 2), rg.Interval(-cantilever_height, 0))
        geometries.append(cantilever_box.ToBrep())

        # Increment the angle for the next cantilever
        angle += cantilever_angle_increment

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_concept_model(core_dimensions=(5, 5, 15), num_cantilevers=6, cantilever_length_range=(7, 12), cantilever_angle_increment=30, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_concept_model(core_dimensions=(6, 6, 20), num_cantilevers=5, cantilever_length_range=(4, 9), cantilever_angle_increment=20, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_concept_model(core_dimensions=(3, 3, 12), num_cantilevers=3, cantilever_length_range=(6, 15), cantilever_angle_increment=45, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_concept_model(core_dimensions=(4, 4, 12), num_cantilevers=4, cantilever_length_range=(6, 14), cantilever_angle_increment=25, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_concept_model(core_dimensions=(7, 7, 18), num_cantilevers=8, cantilever_length_range=(3, 8), cantilever_angle_increment=10, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
