# Created for 0016_0003_curved_partitions.json

""" Summary:
The provided function, `create_dynamic_curved_partitions_model`, generates an architectural concept model that embodies the metaphor of "curved partitions." It creates a series of interconnected, curvilinear surfaces that reflect fluidity and dynamic spatial transitions. By varying the number and radius of curves, along with their height, the model captures the essence of organic forms, allowing for smooth transitions between different spatial zones. These partitions facilitate light interaction, enhancing the atmosphere and encouraging exploration. The design evokes a sense of tranquility and curiosity, aligning with the metaphor's emphasis on balance, movement, and the interplay of openness and enclosure."""

#! python 3
function_code = """def create_dynamic_curved_partitions_model(curve_count=6, max_radius=8, min_radius=2, height=4, seed=85):
    \"""
    Generates an architectural Concept Model based on the 'curved partitions' metaphor.

    This function creates a series of dynamic, interconnected curvilinear partitions that embody fluidity
    and spatial transitions, enhancing the interplay of light and shadow to evoke tranquility and exploration.

    Parameters:
    - curve_count (int): Number of curved partitions to create.
    - max_radius (float): Maximum radius for the curve arrangement.
    - min_radius (float): Minimum radius for the curve arrangement.
    - height (float): Height of each partition in meters.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List of Breps: A list of 3D Brep geometries representing the curved partitions.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    breps = []

    for i in range(curve_count):
        angle = 2 * math.pi * i / curve_count
        radius = random.uniform(min_radius, max_radius)
        center_point = rg.Point3d(radius * math.cos(angle), radius * math.sin(angle), 0)

        control_points = [
            rg.Point3d(center_point.X, center_point.Y, 0),
            rg.Point3d(center_point.X + random.uniform(-1, 1), center_point.Y + random.uniform(-1, 1), height / 2),
            rg.Point3d(center_point.X, center_point.Y, height)
        ]

        nurbs_curve = rg.NurbsCurve.Create(False, 2, control_points)
        revolve_axis = rg.Line(center_point, rg.Point3d(center_point.X, center_point.Y, height))
        surface = rg.RevSurface.Create(nurbs_curve, revolve_axis)

        brep = surface.ToBrep()
        breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dynamic_curved_partitions_model(curve_count=10, max_radius=10, min_radius=3, height=5, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dynamic_curved_partitions_model(curve_count=8, max_radius=6, min_radius=4, height=3, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dynamic_curved_partitions_model(curve_count=12, max_radius=9, min_radius=1, height=6, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dynamic_curved_partitions_model(curve_count=5, max_radius=7, min_radius=2.5, height=4.5, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dynamic_curved_partitions_model(curve_count=7, max_radius=12, min_radius=5, height=3.5, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
