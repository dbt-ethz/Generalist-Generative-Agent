# Created for 0015_0005_suspended_intersecting_assembly.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of a "Suspended intersecting assembly" by creating a series of tensioned wires and planar surfaces that embody floating elements. It employs randomization to position these components within defined spatial bounds, ensuring a dynamic and airy composition. The function enables the creation of intersecting strings, representing structural connections, and translucent planes that enhance transparency and fluidity. By varying the number and dimensions of these elements, the model encourages visual interconnectivity and movement, effectively translating the metaphor into a tangible architectural concept."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(num_strings=5, num_planes=3, string_length=10.0, plane_width=5.0, plane_height=5.0):
    \"""
    Create an architectural Concept Model exemplifying the 'Suspended Intersecting Assembly'.
    
    This function generates a series of intersecting tensioned wires and planar surfaces to represent floating elements.
    The geometry emphasizes a light, airy quality with a focus on transparency and fluidity. It returns a list of 3D 
    geometries representing the suspended assembly, promoting dynamic intersections and visual connections.

    Inputs:
    - num_strings: The number of intersecting tensioned wires to create.
    - num_planes: The number of planar surfaces to create.
    - string_length: The length of each tensioned wire.
    - plane_width: The width of each planar surface.
    - plane_height: The height of each planar surface.

    Outputs:
    - List of RhinoCommon Brep or Surface objects representing the concept model.
    \"""

    import Rhino.Geometry as rg
    import random

    random.seed(42)  # Ensure reproducibility

    # Create random points for the end of strings
    def random_point_within_bounds(bounds):
        return rg.Point3d(
            random.uniform(bounds[0][0], bounds[0][1]),
            random.uniform(bounds[1][0], bounds[1][1]),
            random.uniform(bounds[2][0], bounds[2][1])
        )

    # Define bounds for the space
    bounds = ((0, 10), (0, 10), (0, 10))

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

    # Generate planes
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
        plane_surface = rg.PlaneSurface(plane, rg.Interval(-plane_width/2, plane_width/2), rg.Interval(-plane_height/2, plane_height/2))
        planes.append(plane_surface)

    # Combine all geometries into a single list
    geometries = strings + planes

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(num_strings=8, num_planes=4, string_length=12.0, plane_width=6.0, plane_height=6.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(num_strings=6, num_planes=2, string_length=15.0, plane_width=4.0, plane_height=10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(num_strings=10, num_planes=5, string_length=8.0, plane_width=7.0, plane_height=3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(num_strings=7, num_planes=3, string_length=9.0, plane_width=5.0, plane_height=8.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(num_strings=4, num_planes=6, string_length=11.0, plane_width=5.5, plane_height=4.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
