# Created for 0009_0002_cantilevering_corners.json

""" Summary:
The function `create_dynamic_cantilever_model` generates an architectural concept model inspired by the metaphor of "Cantilevering corners." It creates a central core structure, represented as a cube, from which multiple cantilevered volumes extend outward in various directions and sizes. This design emphasizes dynamic equilibrium by balancing the anchored core with projecting elements, reflecting the metaphor's themes of stability and motion. The function incorporates randomness in the positioning, size, and orientation of the cantilevers, allowing for a diverse interplay of volumes. The result is a model that visually captures the essence of cantilevering, inviting exploration and interaction with its environment."""

#! python 3
function_code = """def create_dynamic_cantilever_model(core_size=10, num_cantilevers=6, max_cantilever_distance=8, cantilever_variation=2, seed=42):
    \"""
    Generates an architectural Concept Model based on the metaphor of 'Cantilevering corners'.
    
    The model features a central core structure with multiple cantilevered volumes projecting outward, 
    emphasizing dynamic equilibrium and interplay between stability and motion. The design involves 
    varying scales, orientations, and layering techniques to create an intricate composition of volumes.

    Parameters:
    - core_size (float): The size of the central core cube in meters.
    - num_cantilevers (int): The number of cantilevered volumes to attach.
    - max_cantilever_distance (float): Maximum distance a cantilever can extend from the core.
    - cantilever_variation (float): Variation factor for the size and orientation of cantilevers.
    - seed (int): Seed for randomness to ensure replicability.

    Returns:
    - List of Rhino.Geometry.Brep: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set a seed for randomness
    random.seed(seed)

    # Create the central core as a cube
    core = rg.Box(rg.Plane.WorldXY, rg.Interval(-core_size / 2, core_size / 2), rg.Interval(-core_size / 2, core_size / 2), rg.Interval(0, core_size))
    geometries = [core.ToBrep()]

    # Function to create a cantilevered box
    def create_cantilever(origin, direction, size, height_variation):
        cantilever_box = rg.Box(
            rg.Plane(origin, rg.Vector3d.ZAxis),
            rg.Interval(0, size),
            rg.Interval(-size / 4, size / 4),
            rg.Interval(-height_variation, height_variation)
        )
        return cantilever_box.ToBrep()

    # Generate cantilevered volumes
    for _ in range(num_cantilevers):
        # Randomly determine the direction and distance of the cantilever
        direction = rg.Vector3d(random.choice([-1, 1]), random.choice([-1, 1]), 0)
        direction.Unitize()
        distance = random.uniform(core_size / 2, max_cantilever_distance)
        direction *= distance

        # Randomly determine the size and height variation of the cantilever
        size = random.uniform(core_size / 4, core_size / 2)
        height_variation = random.uniform(-cantilever_variation, cantilever_variation)

        # Calculate the origin of the cantilever
        origin = rg.Point3d(core_size / 2 * direction.X, core_size / 2 * direction.Y, core_size / 2)

        # Create and add the cantilevered volume
        cantilever = create_cantilever(origin, direction, size, height_variation)
        geometries.append(cantilever)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dynamic_cantilever_model(core_size=15, num_cantilevers=8, max_cantilever_distance=10, cantilever_variation=3, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dynamic_cantilever_model(core_size=12, num_cantilevers=5, max_cantilever_distance=9, cantilever_variation=1, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dynamic_cantilever_model(core_size=20, num_cantilevers=10, max_cantilever_distance=12, cantilever_variation=4, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dynamic_cantilever_model(core_size=18, num_cantilevers=7, max_cantilever_distance=15, cantilever_variation=5, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dynamic_cantilever_model(core_size=14, num_cantilevers=9, max_cantilever_distance=11, cantilever_variation=2, seed=45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
