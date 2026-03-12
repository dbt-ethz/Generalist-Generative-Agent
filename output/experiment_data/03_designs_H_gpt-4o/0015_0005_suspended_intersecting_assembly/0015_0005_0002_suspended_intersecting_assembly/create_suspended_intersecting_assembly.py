# Created for 0015_0005_suspended_intersecting_assembly.json

""" Summary:
The function `create_suspended_intersecting_assembly` generates an architectural concept model reflecting the metaphor of "Suspended intersecting assembly" by creating a dynamic arrangement of tensioned wires and circular disks. It utilizes random point generation within defined bounds to simulate floating elements that intersect, enhancing the sense of lightness and fluidity. The wires represent connections while the disks suggest planar surfaces at varying angles, creating an intricate web of spatial relationships. The model captures movement and transparency, encouraging visual and interactive pathways, thus embodying the metaphor's essence of balance and interconnectedness within the design."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(seed=42, num_strings=8, num_disks=5, string_length=10.0, disk_radius=2.0):
    \"""
    Creates an architectural Concept Model exemplifying the 'Suspended intersecting assembly' metaphor.

    This function generates a series of tensioned wires and circular disks representing floating elements. 
    The disks intersect with the wires to create a dynamic web of spatial relationships. The design focuses 
    on transparency, fluidity, and dynamic intersections, suggesting movement and continuity.

    Parameters:
    - seed (int): Seed for random number generation to ensure replicability of results.
    - num_strings (int): Number of intersecting tensioned wires to generate.
    - num_disks (int): Number of circular disks to generate.
    - string_length (float): Length of each tensioned wire.
    - disk_radius (float): Radius of each circular disk.

    Returns:
    - List[Rhino.Geometry.GeometryBase]: A list of 3D geometries representing the intersecting wires and disks.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for replicability
    random.seed(seed)

    # Helper function to generate a random point within a given bounding box
    def random_point(bounds):
        return rg.Point3d(
            random.uniform(bounds[0][0], bounds[0][1]),
            random.uniform(bounds[1][0], bounds[1][1]),
            random.uniform(bounds[2][0], bounds[2][1])
        )

    # Define the bounding box for the model space
    bounds = ((-5, 5), (-5, 5), (0, 10))

    # Generate tensioned wires as LineCurves
    wires = []
    for _ in range(num_strings):
        start_pt = random_point(bounds)
        direction = rg.Vector3d(
            random.uniform(-1, 1),
            random.uniform(-1, 1),
            random.uniform(-1, 1)
        )
        direction.Unitize()
        end_pt = start_pt + direction * string_length
        wire = rg.LineCurve(start_pt, end_pt)
        wires.append(wire)

    # Generate circular disks
    disks = []
    for _ in range(num_disks):
        center_pt = random_point(bounds)
        normal = rg.Vector3d(
            random.uniform(-1, 1),
            random.uniform(-1, 1),
            random.uniform(-1, 1)
        )
        normal.Unitize()
        plane = rg.Plane(center_pt, normal)
        circle = rg.Circle(plane, disk_radius)
        disk = rg.Brep.CreatePlanarBreps(circle.ToNurbsCurve())[0]
        disks.append(disk)

    # Combine all geometries into a single list
    geometries = wires + disks

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(seed=123, num_strings=10, num_disks=6, string_length=15.0, disk_radius=3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(seed=1, num_strings=5, num_disks=10, string_length=12.0, disk_radius=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(seed=99, num_strings=12, num_disks=4, string_length=8.0, disk_radius=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(seed=42, num_strings=7, num_disks=8, string_length=20.0, disk_radius=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(seed=200, num_strings=6, num_disks=7, string_length=18.0, disk_radius=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
