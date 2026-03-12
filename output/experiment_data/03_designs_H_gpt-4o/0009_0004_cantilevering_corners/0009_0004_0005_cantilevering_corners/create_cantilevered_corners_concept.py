# Created for 0009_0004_cantilevering_corners.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "Cantilevering corners" by creating a central core structure from which angular, cantilevered volumes extend. It defines a base size and parameters for the cantilevers, including their length, height, and rotation angle. The function uses randomness to add variation to the angles of the cantilevers, enhancing the sense of dynamism and tension. By forming a series of interlocking volumes with bold overhangs, the model embodies the interplay between stability and motion, creating unique spatial relationships that invite exploration and play with light and shadow."""

#! python 3
function_code = """def create_cantilevered_corners_concept(base_size, cantilever_length, cantilever_height, cantilever_angle, seed=42):
    \"""
    Create an architectural Concept Model capturing the essence of 'Cantilevering corners'.

    This function generates an architectural form with a central core and angular, cantilevered volumes
    extending from its corners, creating dynamic overhangs and spatial interactions.

    Parameters:
    - base_size (float): The size of the square base core structure in meters.
    - cantilever_length (float): The length of the cantilevered sections in meters.
    - cantilever_height (float): The height of the cantilevered sections in meters.
    - cantilever_angle (float): The angle in degrees to rotate the cantilevered sections.
    - seed (int): Seed for random number generator to ensure replicable results. Default is 42.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the architectural Concept Model.
    \"""
    import Rhino
    import Rhino.Geometry as rg
    import math
    import random

    # Set seed for reproducibility
    random.seed(seed)

    # Create the core structure
    core = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_size), rg.Interval(0, base_size), rg.Interval(0, base_size))
    core_brep = core.ToBrep()

    # Initialize list of geometries
    geometries = [core_brep]

    # Define corner points for cantilevering
    corner_points = [
        rg.Point3d(base_size, base_size, base_size),
        rg.Point3d(0, base_size, base_size),
        rg.Point3d(base_size, 0, base_size),
        rg.Point3d(0, 0, base_size)
    ]

    for corner in corner_points:
        # Determine direction vector with randomness in angle
        angle = math.radians(cantilever_angle + random.uniform(-5, 5))
        direction = rg.Vector3d(math.cos(angle), math.sin(angle), 0)
        direction.Unitize()
        direction *= cantilever_length

        # Create a cantilevered box
        cantilever_box = rg.Box(
            rg.Plane(corner, rg.Vector3d(0, 0, 1)),
            rg.Interval(0, cantilever_length),
            rg.Interval(0, cantilever_length),
            rg.Interval(0, cantilever_height)
        )

        # Rotate the box around its base corner
        rotation = rg.Transform.Rotation(angle, corner)
        cantilever_box.Transform(rotation)

        # Translate the box to create the cantilever effect
        translation = rg.Transform.Translation(direction)
        cantilever_box.Transform(translation)

        # Add to geometries
        geometries.append(cantilever_box.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_corners_concept(10, 5, 3, 30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_corners_concept(15, 7, 4, 45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_corners_concept(12, 6, 3.5, 60)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_corners_concept(20, 8, 5, 50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_corners_concept(18, 9, 4.5, 75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
