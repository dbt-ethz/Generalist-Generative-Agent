# Created for 0009_0004_cantilevering_corners.json

""" Summary:
The provided function `create_cantilevering_corners` generates an architectural concept model that embodies the metaphor of "Cantilevering corners." By defining a central core structure, the function creates asymmetric cantilevered sections that extend outward, reflecting the dynamic interplay between stability and motion. The cantilevers are positioned at the top corners of the core and randomly oriented to enhance the sense of tension and balance, resulting in bold overhangs. The model's geometries emphasize the contrast between solid forms and voids, facilitating unique spaces that invite exploration while illustrating the impact of light and shadow on the overall structure."""

#! python 3
function_code = """def create_cantilevering_corners(central_width, central_depth, central_height, cantilever_length, cantilever_height, randomness_seed=42):
    \"""
    Creates an architectural Concept Model based on the metaphor of 'Cantilevering corners'.
    The model is composed of a central core structure with asymmetric cantilevered sections.

    Parameters:
    - central_width (float): The width of the central core structure in meters.
    - central_depth (float): The depth of the central core structure in meters.
    - central_height (float): The height of the central core structure in meters.
    - cantilever_length (float): The maximum length of the cantilevered sections in meters.
    - cantilever_height (float): The height of the cantilevered sections in meters.
    - randomness_seed (int): Seed for random number generator to ensure replicability.

    Returns:
    - List of Rhino.Geometry.Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(randomness_seed)

    # Create the central core structure
    center_core = rg.Box(rg.Plane.WorldXY, rg.Interval(0, central_width), rg.Interval(0, central_depth), rg.Interval(0, central_height))
    geometries = [center_core.ToBrep()]

    # Define cantilever positions: top corners of the central core
    cantilever_positions = [
        (central_width, 0, central_height),
        (0, central_depth, central_height),
        (central_width, central_depth, central_height)
    ]

    # Create cantilevered sections
    for pos in cantilever_positions:
        # Randomly choose a direction for each cantilever
        direction_vector = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), 0)
        direction_vector.Unitize()
        # Scale the direction vector by the cantilever length
        direction_vector *= cantilever_length

        # Create a cantilevered box
        cantilever_base = rg.Plane(rg.Point3d(pos[0], pos[1], pos[2]), rg.Vector3d(0, 0, 1))
        cantilever_box = rg.Box(
            cantilever_base,
            rg.Interval(0, cantilever_length),
            rg.Interval(0, cantilever_length),
            rg.Interval(0, cantilever_height)
        )
        # Translate the box to create the cantilever effect
        translation = rg.Transform.Translation(direction_vector)
        cantilever_box.Transform(translation)

        # Add to the list of geometries
        geometries.append(cantilever_box.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevering_corners(5.0, 3.0, 10.0, 2.0, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevering_corners(4.0, 2.5, 8.0, 3.0, 2.0, randomness_seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevering_corners(6.0, 4.0, 12.0, 2.5, 2.5, randomness_seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevering_corners(7.0, 5.0, 15.0, 4.0, 3.0, randomness_seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevering_corners(8.0, 6.0, 14.0, 3.5, 2.0, randomness_seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
