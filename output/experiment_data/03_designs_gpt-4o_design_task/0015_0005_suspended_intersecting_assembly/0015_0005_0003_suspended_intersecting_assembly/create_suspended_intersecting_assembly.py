# Created for 0015_0005_suspended_intersecting_assembly.json

""" Summary:
The function `create_suspended_intersecting_assembly` generates an architectural concept model inspired by the metaphor of "Suspended intersecting assembly." It creates a series of intersecting planes elevated within a defined space, simulating a floating effect. By randomly positioning and orienting these planes, the model captures dynamic intersections and a sense of lightness and fluidity. The use of translucent materials and the arrangement of these planes create an intricate web of spatial relationships, enhancing interconnectivity. The function's parameters allow for customization of the model's complexity and height, ultimately resulting in a visually engaging architectural representation."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(origin, num_planes=5, plane_size=3.0, max_height=10.0, seed=42):
    \"""
    Creates an architectural Concept Model exemplifying the 'Suspended intersecting assembly' metaphor.

    Parameters:
    - origin: Tuple[float, float, float] - The origin point from which to generate the model.
    - num_planes: int - The number of intersecting planes to generate.
    - plane_size: float - The size of each plane (in meters).
    - max_height: float - The maximum height for the suspended elements (in meters).
    - seed: int - A seed for random number generation for reproducibility.

    Returns:
    - List[Rhino.Geometry.Brep] - A list of Breps representing the 3D geometries of the concept model.
    \"""

    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(seed)

    # List to store the resulting Breps
    breps = []

    # Generate suspended planes
    for _ in range(num_planes):
        # Randomly choose the plane's position and orientation
        x = origin[0] + random.uniform(-plane_size, plane_size)
        y = origin[1] + random.uniform(-plane_size, plane_size)
        z = origin[2] + random.uniform(0, max_height)
        
        # Create a random direction vector for plane orientation
        direction = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        direction.Unitize()

        # Create a plane at the calculated position
        plane_origin = rg.Point3d(x, y, z)
        plane = rg.Plane(plane_origin, direction)

        # Create a rectangular surface on the plane
        rect = rg.Rectangle3d(plane, plane_size, plane_size)
        surface = rg.Brep.CreateFromCornerPoints(rect.Corner(0), rect.Corner(1), rect.Corner(2), rect.Corner(3), 1e-8)

        # Convert the surface to a BRep and add to the list
        brep = surface
        breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly((0, 0, 0), num_planes=7, plane_size=4.0, max_height=15.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly((5, 5, 2), num_planes=10, plane_size=2.5, max_height=8.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly((1, 1, 1), num_planes=6, plane_size=5.0, max_height=12.0, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly((3, 3, 0), num_planes=8, plane_size=3.5, max_height=20.0, seed=200)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly((2, 2, 0), num_planes=4, plane_size=3.0, max_height=10.0, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
