# Created for 0016_0005_curved_partitions.json

""" Summary:
The provided function, `create_curved_partition_model`, generates an architectural concept model by creating a series of undulating, curved partitions that embody the metaphor of 'curved partitions'. It utilizes random parameters within specified ranges to define the base radius and height of each partition, producing a wavy profile that mimics organic forms found in nature. The function constructs NURBS curves from these points and extrudes them vertically, resulting in smooth, flowing surfaces. This design approach fosters a dynamic spatial organization, encouraging fluid movement and interaction, while enhancing light interplay, thus creating an inviting and tranquil environment."""

#! python 3
function_code = """def create_curved_partition_model(num_partitions, radius_range, height_range, undulation_factor):
    \"""
    Generates an architectural Concept Model embodying the metaphor of 'curved partitions'.
    This model creates a series of interconnected spaces defined by smooth, undulating curves.

    Parameters:
    - num_partitions (int): Number of curved partitions to create.
    - radius_range (tuple of float): Min and max radius for the circular base of partitions.
    - height_range (tuple of float): Min and max height for the partitions.
    - undulation_factor (float): Factor that controls the degree of undulation in the partitions.

    Returns:
    - List of Rhino.Geometry.Brep: A list of 3D geometries representing the curved partitions.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Seed for reproducibility
    random.seed(42)

    # List to store resulting Breps
    partitions = []

    for _ in range(num_partitions):
        # Randomly determine the parameters for each partition
        base_radius = random.uniform(*radius_range)
        partition_height = random.uniform(*height_range)

        # Create a base circle for the partition
        base_circle = rg.Circle(rg.Plane.WorldXY, base_radius)

        # Generate wavy profile by modifying control points
        points = []
        num_points = 20
        for i in range(num_points):
            angle = (2 * math.pi / num_points) * i
            x = base_circle.Center.X + base_radius * math.cos(angle)
            y = base_circle.Center.Y + base_radius * math.sin(angle)
            z = partition_height * math.sin(undulation_factor * angle)
            points.append(rg.Point3d(x, y, z))
        
        # Create a NURBS curve from the points
        nurbs_curve = rg.NurbsCurve.Create(False, 3, points)

        # Extrude the curve vertically to form a surface
        extrusion_vector = rg.Vector3d(0, 0, partition_height)
        surface = rg.Surface.CreateExtrusion(nurbs_curve, extrusion_vector)

        # Convert surface to Brep and add to the list
        brep = surface.ToBrep()
        partitions.append(brep)

    return partitions"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partition_model(5, (1.0, 3.0), (2.0, 5.0), 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partition_model(10, (0.5, 2.0), (1.0, 4.0), 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partition_model(7, (1.5, 4.0), (3.0, 6.0), 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partition_model(8, (2.0, 5.0), (1.0, 3.0), 1.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partition_model(6, (0.8, 2.5), (2.5, 6.0), 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
