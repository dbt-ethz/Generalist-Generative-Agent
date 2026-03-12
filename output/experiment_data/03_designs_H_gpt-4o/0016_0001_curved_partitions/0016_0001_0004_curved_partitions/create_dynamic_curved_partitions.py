# Created for 0016_0001_curved_partitions.json

""" Summary:
The provided function, `create_dynamic_curved_partitions`, generates an architectural concept model by creating a series of interlocking, flowing 3D forms that embody the metaphor of 'curved partitions.' Each partition is formed using random control points to establish smooth, organic curves, which are then extruded to define vertical surfaces. This approach emphasizes fluidity and continuity, facilitating seamless transitions between spaces. The model enhances light and shadow interplay, creating an atmospheric environment with both public and private zones. Ultimately, the generated geometries encourage exploration and interaction, reflecting the metaphor's intent to evoke calmness and elegance through dynamic spatial organization."""

#! python 3
function_code = """def create_dynamic_curved_partitions(num_partitions, max_radius, partition_height, curve_detail, seed=42):
    \"""
    Generates an architectural concept model characterized by dynamic and fluid 'curved partitions'.
    
    This function creates a series of flowing, interlocking 3D forms that convey movement and continuity.
    The partitions are defined by curves that facilitate seamless transitions between spaces, enhancing light
    and shadow interplay.

    Parameters:
    - num_partitions (int): The number of curved partitions to generate.
    - max_radius (float): The maximum radius for the curvature of partitions.
    - partition_height (float): The height of each partition.
    - curve_detail (int): The number of control points defining the detail of the curves.
    - seed (int): Seed for random number generation to ensure replicable results.

    Returns:
    - list: A list of Brep geometries representing the 3D curved partitions.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    breps = []

    for _ in range(num_partitions):
        # Generate random base point for each partition within a defined area
        base_x = random.uniform(-max_radius, max_radius)
        base_y = random.uniform(-max_radius, max_radius)
        base_point = rg.Point3d(base_x, base_y, 0)

        # Create control points for a smooth curve
        control_points = [base_point]
        for _ in range(curve_detail):
            angle = random.uniform(0, 2 * math.pi)
            radius = random.uniform(0.2 * max_radius, max_radius)
            deviation = rg.Vector3d(radius * math.cos(angle), radius * math.sin(angle), 0)
            new_point = base_point + deviation
            control_points.append(new_point)

        # Create a NURBS curve from control points
        nurbs_curve = rg.NurbsCurve.Create(False, 3, control_points)

        # Extrude the curve vertically to create a partition surface
        extrusion_vector = rg.Vector3d(0, 0, partition_height)
        extrusion_surface = rg.Surface.CreateExtrusion(nurbs_curve, extrusion_vector)

        # Convert the surface to a Brep and add to the list
        if extrusion_surface:
            partition_brep = extrusion_surface.ToBrep()
            if partition_brep:
                breps.append(partition_brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dynamic_curved_partitions(5, 10.0, 3.0, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dynamic_curved_partitions(10, 15.0, 4.5, 12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dynamic_curved_partitions(7, 20.0, 5.0, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dynamic_curved_partitions(8, 25.0, 6.0, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dynamic_curved_partitions(6, 12.0, 2.5, 9)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
