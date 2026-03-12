# Created for 0016_0001_curved_partitions.json

""" Summary:
The provided function, `create_curved_partition_model`, generates an architectural concept model inspired by the metaphor of "curved partitions." By creating a series of interlocking, flowing forms, the model embodies fluidity and continuity, reflecting the organic shapes described in the metaphor. The function employs parameters such as radius, height, and curvature to define the partitions' geometry, allowing for seamless spatial transitions. It incorporates perforations to enhance light interaction, emphasizing the interplay of light and shadow. Overall, the model conveys a sense of calm and exploration, encouraging dynamic interactions within the designed environment."""

#! python 3
function_code = """def create_curved_partition_model(radius, height, partition_count, curve_strength, perforation_density, seed=42):
    \"""
    Generates an architectural concept model using the metaphor of 'curved partitions'.

    This function creates a series of interlocking, flowing forms that embody movement and continuity.
    Curved partitions define spaces with soft transitions, enhancing the interplay of light and shadow.
    
    Parameters:
    - radius (float): The base radius of the circular boundary where partitions are formed.
    - height (float): The height of the partitions.
    - partition_count (int): The number of partitions to create.
    - curve_strength (float): The degree of curvature applied to partitions.
    - perforation_density (float): Density of perforations for light interaction, between 0 (none) and 1 (max).
    - seed (int): Seed for random number generation for replicability.

    Returns:
    - list: A list of RhinoCommon Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    geometries = []

    for i in range(partition_count):
        angle = 2 * math.pi * i / partition_count
        base_point = rg.Point3d(radius * math.cos(angle), radius * math.sin(angle), 0)

        # Create a curved partition using a spline
        control_points = [base_point]
        for j in range(1, 5):
            next_angle = angle + curve_strength * (random.random() - 0.5)
            distance = radius * (0.5 + random.random())
            next_point = rg.Point3d(
                distance * math.cos(next_angle),
                distance * math.sin(next_angle),
                random.uniform(0, height)
            )
            control_points.append(next_point)

        if len(control_points) < 4:
            continue

        curve = rg.NurbsCurve.Create(False, 3, control_points)
        extrusion_vector = rg.Vector3d(0, 0, height)
        partition = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(curve, extrusion_vector))

        # Add perforations based on density
        if perforation_density > 0:
            perforation_count = int(perforation_density * 10)
            for _ in range(perforation_count):
                perforation_center = rg.Point3d(
                    random.uniform(curve.PointAtStart.X, curve.PointAtEnd.X),
                    random.uniform(curve.PointAtStart.Y, curve.PointAtEnd.Y),
                    random.uniform(0, height)
                )
                perforation_radius = random.uniform(0.1, 0.3)
                sphere = rg.Sphere(perforation_center, perforation_radius)
                sphere_brep = sphere.ToBrep()
                if sphere_brep:
                    diff_result = rg.Brep.CreateBooleanDifference([partition], [sphere_brep], 0.001)
                    if diff_result:
                        partition = diff_result[0]

        geometries.append(partition)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partition_model(10.0, 5.0, 8, 0.2, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partition_model(15.0, 7.0, 10, 0.3, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partition_model(12.0, 6.0, 6, 0.4, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partition_model(8.0, 4.0, 12, 0.5, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partition_model(20.0, 10.0, 5, 0.1, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
