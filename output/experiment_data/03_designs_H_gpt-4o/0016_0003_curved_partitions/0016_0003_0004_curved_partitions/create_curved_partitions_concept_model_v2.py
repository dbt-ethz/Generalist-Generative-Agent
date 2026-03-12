# Created for 0016_0003_curved_partitions.json

""" Summary:
The provided function creates an architectural concept model that embodies the metaphor of "curved partitions" through a series of interconnected curvilinear elements. By using parameters like radius, height, and thickness, it generates a radial arrangement of curved surfaces resembling organic forms. The function employs randomness to introduce fluidity in the curves, allowing the partitions to undulate and interact dynamically. Each partition serves as both a separator and connector, facilitating smooth transitions between spaces. The result is a model that promotes exploration and provides an atmospheric interplay of light and shadow, aligning with the metaphor's emphasis on continuity and tranquility."""

#! python 3
function_code = """def create_curved_partitions_concept_model_v2(radius=10, partition_height=3.0, partition_thickness=0.2, num_partitions=6, seed=42):
    \"""
    Creates a Concept Model embodying the metaphor of 'curved partitions' using organic, flowing surfaces.

    This version implements a radial arrangement of partitions, where each partition is a curved surface
    sweeping around a central point, resembling petals or shells. The design aims to create a sense of
    dynamic movement and fluid spatial transitions.

    Parameters:
    - radius (float): The radius of the circle along which the partitions are arranged.
    - partition_height (float): The height of each partition in meters.
    - partition_thickness (float): The thickness of each partition in meters.
    - num_partitions (int): The number of partitions to create.
    - seed (int): A seed for randomness to ensure replicability.

    Returns:
    - List of Breps: A list of 3D Brep geometries representing the curved partitions.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Initialize randomness for replicability
    random.seed(seed)

    # List to store the resulting Breps
    breps = []

    # Angle between each partition
    angle_step = 2 * math.pi / num_partitions

    for i in range(num_partitions):
        # Calculate the angle and position for the current partition
        angle = i * angle_step
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        # Create a base point for the partition
        base_point = rg.Point3d(x, y, 0)

        # Define control points for a curved base line
        control_points = [
            base_point,
            rg.Point3d(x + random.uniform(-1, 1), y + random.uniform(-1, 1), partition_height / 3),
            rg.Point3d(x + random.uniform(-1, 1), y + random.uniform(-1, 1), 2 * partition_height / 3),
            rg.Point3d(x, y, partition_height)
        ]

        # Create a NURBS curve from the control points
        curve = rg.NurbsCurve.Create(False, 3, control_points)

        # Offset the curve to create thickness
        offset_curve = curve.Offset(rg.Plane.WorldXY, partition_thickness, 0.01, rg.CurveOffsetCornerStyle.Smooth)[0]

        # Create a ruled surface between the original curve and the offset curve
        ruled_surface = rg.Brep.CreateFromLoft([curve, offset_curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)[0]

        # Cap the open ends to form a closed Brep
        brep = ruled_surface.CapPlanarHoles(0.01)
        if brep:
            breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions_concept_model_v2(radius=15, partition_height=4.0, partition_thickness=0.3, num_partitions=8, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_concept_model_v2(radius=12, partition_height=5.0, partition_thickness=0.25, num_partitions=10, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_concept_model_v2(radius=20, partition_height=6.0, partition_thickness=0.15, num_partitions=12, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_concept_model_v2(radius=18, partition_height=3.5, partition_thickness=0.4, num_partitions=5, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_concept_model_v2(radius=25, partition_height=2.5, partition_thickness=0.1, num_partitions=4, seed=88)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
