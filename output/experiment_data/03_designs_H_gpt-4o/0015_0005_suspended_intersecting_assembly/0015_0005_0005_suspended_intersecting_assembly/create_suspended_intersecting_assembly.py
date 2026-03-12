# Created for 0015_0005_suspended_intersecting_assembly.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "Suspended intersecting assembly." It creates a visual representation using a specified number of tensioned wires and circular planar surfaces, simulating the floating elements described in the metaphor. By randomly placing the wires and planes within defined bounds, the model emphasizes lightness, transparency, and dynamic intersections. The use of adjustable parameters allows for varied geometric configurations, enhancing the sense of movement and interconnectivity. The resulting 3D geometries reflect the architectural concept's key traits, providing a basis for further exploration and development in design."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(num_strings=6, num_planes=4, string_length=12.0, plane_radius=3.0, seed=1):
    \"""
    Create an architectural Concept Model exemplifying the 'Suspended Intersecting Assembly'.

    This function generates a model using intersecting tensioned wires and circular planar surfaces to represent floating elements.
    The design emphasizes transparency, lightness, and dynamic intersections, suggesting movement and fluidity.

    Parameters:
    - num_strings (int): The number of intersecting tensioned wires.
    - num_planes (int): The number of circular planar surfaces.
    - string_length (float): The length of each tensioned wire.
    - plane_radius (float): The radius of each circular planar surface.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep or Surface]: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)  # Ensure reproducibility

    # Create random points for the ends of strings within a bounding box
    def random_point_within_bounds(bounds):
        return rg.Point3d(
            random.uniform(bounds[0][0], bounds[0][1]),
            random.uniform(bounds[1][0], bounds[1][1]),
            random.uniform(bounds[2][0], bounds[2][1])
        )

    # Define the bounds for the space
    bounds = ((-5, 5), (-5, 5), (0, 10))

    # Generate strings
    strings = []
    for _ in range(num_strings):
        start_pt = random_point_within_bounds(bounds)
        direction = rg.Vector3d(
            random.uniform(-1, 1),
            random.uniform(-1, 1),
            random.uniform(-1, 1)
        )
        direction.Unitize()
        end_pt = start_pt + direction * string_length
        strings.append(rg.LineCurve(start_pt, end_pt))

    # Generate circular planes
    planes = []
    for _ in range(num_planes):
        base_pt = random_point_within_bounds(bounds)
        normal = rg.Vector3d(
            random.uniform(-1, 1),
            random.uniform(-1, 1),
            random.uniform(-1, 1)
        )
        normal.Unitize()
        plane = rg.Plane(base_pt, normal)
        circle = rg.Circle(plane, plane_radius)
        circle_surface = rg.Brep.CreatePlanarBreps(circle.ToNurbsCurve())[0]
        planes.append(circle_surface)

    # Combine all geometries into a single list
    geometries = strings + planes

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(num_strings=8, num_planes=5, string_length=10.0, plane_radius=4.0, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(num_strings=10, num_planes=3, string_length=15.0, plane_radius=2.5, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(num_strings=5, num_planes=6, string_length=8.0, plane_radius=3.5, seed=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(num_strings=7, num_planes=2, string_length=14.0, plane_radius=5.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(num_strings=12, num_planes=8, string_length=9.0, plane_radius=3.0, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
