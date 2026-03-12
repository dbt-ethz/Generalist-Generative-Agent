# Created for 0016_0001_curved_partitions.json

""" Summary:
The provided function, `create_curved_partitions_model`, generates an architectural concept model by interpreting the metaphor of "curved partitions." It creates a series of 3D geometries that embody fluidity and organic movement, as suggested by the metaphor. By using random start and end points along a defined base area, the function constructs curves with control points that enhance the curvature, reflecting smooth transitions and softened boundaries. Each curve is extruded to form partitions, allowing for dynamic spatial organization. The resulting model promotes interaction, intimacy, and a sense of elegance, aligning with the metaphor's intent of evoking calmness and exploration."""

#! python 3
function_code = """def create_curved_partitions_model(base_length, base_width, height, num_partitions, curvature_factor):
    \"""
    Creates an architectural concept model based on the metaphor of 'curved partitions'.
    
    Parameters:
    - base_length (float): The length of the base area in meters.
    - base_width (float): The width of the base area in meters.
    - height (float): The height of the partitions in meters.
    - num_partitions (int): Number of curved partitions to create.
    - curvature_factor (float): A factor to control the curvature of the partitions.
    
    Returns:
    - List of 3D geometries (breps) representing the curved partitions.
    \"""
    import Rhino.Geometry as rg
    import random

    # Seed for reproducibility
    random.seed(42)

    partitions = []

    for i in range(num_partitions):
        # Randomly generate start and end points along the base area
        start_x = random.uniform(0, base_length)
        end_x = random.uniform(0, base_length)
        start_point = rg.Point3d(start_x, 0, 0)
        end_point = rg.Point3d(end_x, base_width, 0)

        # Create a curve between the start and end points with a control point
        mid_x = (start_x + end_x) / 2
        mid_y = base_width / 2
        control_point = rg.Point3d(mid_x, mid_y, curvature_factor * height)
        # Fix: Ensure the curve has at least 3 control points for a non-degenerate curve
        curve = rg.NurbsCurve.Create(False, 2, [start_point, control_point, end_point])

        # Extrude the curve to create a partition surface
        if curve and curve.IsValid:
            extrusion = rg.Extrusion.Create(curve, height, True)

            # Convert extrusion to Brep
            brep_partition = extrusion.ToBrep() if extrusion else None

            if brep_partition:
                partitions.append(brep_partition)

    return partitions"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions_model(10.0, 5.0, 3.0, 4, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_model(15.0, 8.0, 4.0, 6, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_model(12.0, 6.0, 2.5, 5, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_model(20.0, 10.0, 5.0, 3, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_model(8.0, 4.0, 2.0, 5, 1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
