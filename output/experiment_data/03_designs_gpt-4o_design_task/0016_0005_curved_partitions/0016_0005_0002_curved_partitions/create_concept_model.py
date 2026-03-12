# Created for 0016_0005_curved_partitions.json

""" Summary:
The function generates an architectural concept model inspired by the metaphor of 'curved partitions' by creating a series of undulating curves that define interconnected spaces. It begins by defining a base point and uses randomization to generate multiple control points, creating smooth, flowing curves that mimic natural forms. Each curve is transformed into a partition through a sweeping process, resulting in a three-dimensional surface. The model integrates various heights and widths to enhance the dynamic quality, while the use of flexible materials like wire mesh or silicone can further emphasize light interaction, encouraging exploration and evoking tranquility within the space."""

#! python 3
function_code = """def create_concept_model(width, depth, height, curve_count):
    \"""
    Generates a conceptual architectural model based on the metaphor of 'curved partitions'.
    The model is characterized by fluid, wave-like contours that create interconnected spaces.

    Parameters:
    width (float): The overall width of the model in meters.
    depth (float): The overall depth of the model in meters.
    height (float): The overall height of the partitions in meters.
    curve_count (int): The number of curved partitions to generate.

    Returns:
    list: A list of Brep objects representing the curved partitions of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    random.seed(42)  # Ensures replicable results

    def generate_curve(base_point, width, depth, height, num_points=5):
        points = [base_point]
        for i in range(1, num_points):
            x = random.uniform(base_point.X, base_point.X + width)
            y = random.uniform(base_point.Y, base_point.Y + depth)
            z = base_point.Z + (height * (i / num_points))
            points.append(rg.Point3d(x, y, z))
        return rg.Curve.CreateInterpolatedCurve(points, 3)

    def create_partition(curve, thickness=0.2):
        # Offset the curve in the direction of the normal to create a surface
        line = rg.Line(curve.PointAtStart, rg.Point3d(curve.PointAtStart.X, curve.PointAtStart.Y, curve.PointAtStart.Z + thickness))
        sweep = rg.SweepOneRail()
        sweep.AngleToleranceRadians = math.radians(1.0)
        sweep.ClosedSweep = False
        breps = sweep.PerformSweep(curve, line.ToNurbsCurve())
        if breps and len(breps) > 0:
            breps[0].CapPlanarHoles(0.01)
            return breps[0]
        return None

    partitions = []
    for _ in range(curve_count):
        base_point = rg.Point3d(random.uniform(0, width), random.uniform(0, depth), 0)
        curve = generate_curve(base_point, width * 0.5, depth * 0.5, height)
        partition = create_partition(curve)
        if partition:
            partitions.append(partition)

    return partitions"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(10.0, 5.0, 3.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(15.0, 10.0, 6.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(12.0, 8.0, 4.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(20.0, 15.0, 10.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(18.0, 9.0, 5.0, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
