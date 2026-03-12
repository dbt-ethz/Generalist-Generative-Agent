# Created for 0009_0004_cantilevering_corners.json

""" Summary:
The provided function, `create_cantilever_corners_model`, generates an architectural concept model based on the metaphor of "Cantilevering corners." It begins by establishing a central core structure from which multiple cantilevered volumes extend in various directions, embodying the dynamic interplay between stability and motion. The function uses randomized positioning for the cantilevers, allowing for diverse angular projections and dramatic overhangs that challenge traditional support concepts. By varying the dimensions and number of cantilevers, the model captures the essence of dynamic spatial relationships and the aesthetic impact of light and shadow, inviting exploration of unexpected spaces."""

#! python 3
function_code = """def create_cantilever_corners_model(core_size, cantilever_size, num_cantilevers, seed=42):
    \"""
    Generate an architectural Concept Model inspired by the metaphor of 'Cantilevering corners'.

    This function creates a central core structure with cantilevered volumes extending from it. The
    design focuses on dynamic interplay between solid and void, emphasizing the tension between stability
    and motion through bold overhangs and angular projections.

    Parameters:
    - core_size (tuple of float): Dimensions of the central core (width, depth, height) in meters.
    - cantilever_size (tuple of float): Dimensions of the cantilever sections (length, width, height) in meters.
    - num_cantilevers (int): Number of cantilevered sections to create.
    - seed (int, optional): Seed for random generation to ensure replicability. Default is 42.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    geometries = []

    # Create the central core structure
    core_width, core_depth, core_height = core_size
    core = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_depth), rg.Interval(0, core_height))
    geometries.append(core.ToBrep())

    # Create cantilevered sections
    for _ in range(num_cantilevers):
        # Randomly choose a position on the core to attach a cantilever
        side = random.choice(['left', 'right', 'front', 'back', 'top'])
        length, width, height = cantilever_size
        base_point = rg.Point3d()

        if side == 'left':
            base_point = rg.Point3d(-length, random.uniform(0, core_depth), random.uniform(0, core_height))
            direction = rg.Vector3d(length, 0, 0)
        elif side == 'right':
            base_point = rg.Point3d(core_width, random.uniform(0, core_depth), random.uniform(0, core_height))
            direction = rg.Vector3d(length, 0, 0)
        elif side == 'front':
            base_point = rg.Point3d(random.uniform(0, core_width), -width, random.uniform(0, core_height))
            direction = rg.Vector3d(0, width, 0)
        elif side == 'back':
            base_point = rg.Point3d(random.uniform(0, core_width), core_depth, random.uniform(0, core_height))
            direction = rg.Vector3d(0, width, 0)
        elif side == 'top':
            base_point = rg.Point3d(random.uniform(0, core_width), random.uniform(0, core_depth), core_height)
            direction = rg.Vector3d(0, 0, height)

        # Create the cantilever box
        cantilever_box = rg.Box(rg.Plane(base_point, rg.Vector3d.XAxis, rg.Vector3d.YAxis),
                                 rg.Interval(0, direction.X), rg.Interval(0, direction.Y), rg.Interval(0, direction.Z))
        geometries.append(cantilever_box.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilever_corners_model((5, 5, 10), (3, 1, 2), 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilever_corners_model((8, 4, 12), (2, 2, 3), 6, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilever_corners_model((6, 3, 8), (4, 1.5, 2.5), 5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilever_corners_model((7, 7, 15), (5, 2, 4), 3, seed=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilever_corners_model((10, 5, 20), (6, 3, 5), 2, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
