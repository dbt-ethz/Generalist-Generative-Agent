# Created for 0015_0001_suspended_intersecting_assembly.json

""" Summary:
The function `create_suspended_intersecting_assembly` generates an architectural concept model by creating a series of intersecting planes within a specified bounding box. It uses randomization to determine the position and orientation of each plane, embodying the metaphor of "Suspended intersecting assembly." This results in a dynamic arrangement of lightweight, transparent geometries that appear to float and intersect, highlighting lightness and fluidity. The model emphasizes structural transparency and balance, aligning with the design task by utilizing materials and techniques that enhance visual interconnectivity and suggest movement within the space."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(width, height, depth, num_planes, seed=42):
    \"""
    Creates an architectural concept model that embodies the 'Suspended intersecting assembly'.
    The function generates a series of intersecting planes that give a sense of lightness, fluidity,
    and structural transparency.

    Parameters:
    - width (float): The overall width of the bounding box for the assembly.
    - height (float): The overall height of the bounding box for the assembly.
    - depth (float): The overall depth of the bounding box for the assembly.
    - num_planes (int): The number of intersecting planes to generate.
    - seed (int, optional): The seed for random number generation to ensure replicability.

    Returns:
    - list of Rhino.Geometry.Brep: A list of Brep objects representing the intersecting planes.
    \"""
    import Rhino
    import System
    import random
    from Rhino.Geometry import Plane, Point3d, Vector3d, Brep, Box, Interval

    # Seed the random number generator
    random.seed(seed)

    # Define the bounding box of the assembly
    bounding_box = Box(Plane.WorldXY, Interval(0, width), Interval(0, depth), Interval(0, height))

    # Store the generated Breps
    breps = []

    # Generate planes
    for _ in range(num_planes):
        # Randomly choose a position within the bounding box
        x = random.uniform(0, width)
        y = random.uniform(0, depth)
        z = random.uniform(0, height)
        origin = Point3d(x, y, z)

        # Randomly create a vector to define the plane's normal
        normal_x = random.uniform(-1, 1)
        normal_y = random.uniform(-1, 1)
        normal_z = random.uniform(-1, 1)
        normal = Vector3d(normal_x, normal_y, normal_z)
        normal.Unitize()

        # Create a plane using the origin and the normal
        plane = Plane(origin, normal)

        # Create a surface from the plane that extends beyond the bounding box
        plane_surface = Brep.CreateFromCornerPoints(
            plane.PointAt(-width/2, -depth/2, 0),
            plane.PointAt(width/2, -depth/2, 0),
            plane.PointAt(width/2, depth/2, 0),
            plane.PointAt(-width/2, depth/2, 0),
            0.01
        )

        if plane_surface:
            breps.append(plane_surface)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(10.0, 15.0, 5.0, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(20.0, 10.0, 10.0, 5, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(25.0, 20.0, 15.0, 12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(30.0, 40.0, 25.0, 10, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(15.0, 25.0, 10.0, 6, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
