# Created for 0009_0001_cantilevering_corners.json

""" Summary:
The provided function, `create_cantilevering_corners`, generates an architectural concept model based on the metaphor of "cantilevering corners." It defines a base structure and adds dynamic cantilevered sections that extend outward from the corners, embodying the tension and balance suggested by the metaphor. By specifying dimensions such as base size and cantilever length, the function creates a 3D model with dramatic overhangs that challenge conventional notions of stability. The randomness in projecting the cantilevers adds variety, resulting in unique architectural forms that reflect the dynamic interaction between stability and motion inherent in the metaphor."""

#! python 3
function_code = """def create_cantilevering_corners(base_length, base_width, base_height, cantilever_length, cantilever_height):
    \"""
    Creates an architectural Concept Model inspired by the metaphor 'Cantilevering corners'.
    The model includes a base structure with dynamic cantilevered sections projecting outward.

    Parameters:
    - base_length (float): Length of the base structure in meters.
    - base_width (float): Width of the base structure in meters.
    - base_height (float): Height of the base structure in meters.
    - cantilever_length (float): Length of the cantilevered sections in meters.
    - cantilever_height (float): Height of the cantilevered sections in meters.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set seed for randomness
    random.seed(42)

    # Create the base structure as a box
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    base_brep = base_box.ToBrep()

    # Create cantilevered sections
    cantilevers = []
    for i in range(4):  # One cantilever for each corner
        # Randomly decide if the cantilever projects along length or width
        project_lengthwise = random.choice([True, False])
        
        if project_lengthwise:
            # Cantilever along the length
            offset = rg.Vector3d(cantilever_length, 0, 0)
            start_point = rg.Point3d(base_length, 0, base_height) if i % 2 == 0 else rg.Point3d(0, base_width, base_height)
        else:
            # Cantilever along the width
            offset = rg.Vector3d(0, cantilever_length, 0)
            start_point = rg.Point3d(base_length, base_width, base_height) if i < 2 else rg.Point3d(0, 0, base_height)

        # Create a cantilevered box
        cantilever_box = rg.Box(rg.Plane(start_point, rg.Vector3d.ZAxis),
                                rg.Interval(-cantilever_height, 0), 
                                rg.Interval(0, cantilever_length if project_lengthwise else base_width),
                                rg.Interval(0, cantilever_height))
        cantilevers.append(cantilever_box.ToBrep())

    # Return the base structure and the cantilevered sections
    return [base_brep] + cantilevers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevering_corners(10, 5, 3, 2, 1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevering_corners(15, 7, 4, 3, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevering_corners(12, 6, 5, 4, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevering_corners(8, 4, 2, 1.5, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevering_corners(20, 10, 6, 5, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
