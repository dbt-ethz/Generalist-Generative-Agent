# Created for 0016_0001_curved_partitions.json

""" Summary:
The function `create_curved_partition_concept` generates an architectural concept model inspired by the metaphor of "curved partitions" by creating a series of interlocking, fluid 3D forms. It uses a random number generator to ensure variability in the curvature and arrangement of partitions while maintaining consistency through a seed parameter. Each partition is defined by control points, resulting in smooth, flowing curves that suggest movement and encourage spatial continuity. The option for light interaction, via perforations, enhances the interplay of light and shadow, enriching the model's atmospheric quality while fostering a dynamic interplay between public and private spaces."""

#! python 3
function_code = """def create_curved_partition_concept(seed, partition_count, max_radius, height, light_interaction):
    \"""
    Generates a concept model of an architectural space inspired by the metaphor of 'curved partitions'.
    
    This function creates a series of interlocking, flowing 3D forms that suggest movement and continuity.
    It uses randomness to vary curvature, ensuring replicable results with a given seed. The partitions are designed
    to define spaces without fully enclosing them, allowing for smooth transitions and dynamic spatial relationships.

    Parameters:
    seed (int): Seed for random number generation to ensure replicable results.
    partition_count (int): Number of curved partitions to create.
    max_radius (float): Maximum radius for the curvature of partitions.
    height (float): Height of partitions in meters.
    light_interaction (bool): If True, partitions will have perforations to enhance light and shadow interplay.

    Returns:
    list: A list of Brep geometries representing the curved partitions.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    geometries = []

    for i in range(partition_count):
        # Randomly generate a base point for the partition
        base_point = rg.Point3d(random.uniform(-10, 10), random.uniform(-10, 10), 0)
        
        # Create a curve using a series of points to define the partition
        control_points = [base_point]
        for j in range(1, 5):
            angle = random.uniform(0, 2 * 3.14159)
            radius = random.uniform(0.5 * max_radius, max_radius)
            new_point = rg.Point3d(
                base_point.X + radius * random.uniform(0.5, 1.5) * rg.Vector3d.XAxis.X,
                base_point.Y + radius * random.uniform(0.5, 1.5) * rg.Vector3d.YAxis.Y,
                0
            )
            control_points.append(new_point)
        
        # Ensure there are enough control points for the curve
        if len(control_points) < 4:
            continue
        
        curve = rg.NurbsCurve.Create(False, 3, control_points)

        # Extrude the curve to create a 3D partition
        extrusion_vector = rg.Vector3d(0, 0, height)
        partition = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(curve, extrusion_vector))

        # Optionally add perforations for light interaction
        if light_interaction:
            perforation_count = random.randint(3, 6)
            for _ in range(perforation_count):
                perforation_center = rg.Point3d(
                    random.uniform(curve.PointAtStart.X, curve.PointAtEnd.X),
                    random.uniform(curve.PointAtStart.Y, curve.PointAtEnd.Y),
                    random.uniform(0, height)
                )
                perforation_radius = random.uniform(0.1, 0.3)
                sphere = rg.Sphere(perforation_center, perforation_radius)
                sphere_brep = sphere.ToBrep()
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
    geometry = create_curved_partition_concept(seed=42, partition_count=5, max_radius=3.0, height=2.5, light_interaction=True)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partition_concept(seed=100, partition_count=10, max_radius=4.0, height=3.0, light_interaction=False)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partition_concept(seed=7, partition_count=8, max_radius=2.5, height=3.5, light_interaction=True)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partition_concept(seed=25, partition_count=6, max_radius=5.0, height=4.0, light_interaction=True)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partition_concept(seed=15, partition_count=12, max_radius=2.0, height=2.0, light_interaction=False)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
