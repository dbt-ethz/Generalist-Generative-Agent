# Created for 0016_0005_curved_partitions.json

""" Summary:
The function `create_dynamic_curved_partitions_model` generates an architectural concept model that embodies the metaphor of "curved partitions" by creating a series of fluid, wave-like surfaces. It uses parameters such as width, depth, height, and curvature intensity to define the model's dimensions and the smoothness of the curves. By interpolating points into curves and extruding them, the function produces interconnected partitions that encourage seamless transitions and dynamic light interactions. This design approach fosters a tranquil and engaging environment, reflecting the metaphor's essence of organic movement and fluidity, inviting exploration and interaction within the spatial layout."""

#! python 3
function_code = """def create_dynamic_curved_partitions_model(width, depth, height, num_partitions, curve_detail, curvature_intensity):
    \"""
    Generates an architectural Concept Model based on the metaphor of 'curved partitions'.
    This model emphasizes fluidity and natural flow with interconnected spaces and smooth transitions.

    Parameters:
    - width (float): The overall width of the conceptual model in meters.
    - depth (float): The overall depth of the conceptual model in meters.
    - height (float): The height of the partitions in meters.
    - num_partitions (int): Number of curved partitions to generate.
    - curve_detail (int): Number of points defining the detail level of each curve.
    - curvature_intensity (float): Intensity of the curvature for the wave-like effect.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D curved partitions.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    # Seed for reproducibility
    random.seed(42)

    partitions = []

    # Create each partition
    for i in range(num_partitions):
        # Calculate offset position for each partition
        offset = i * (depth / num_partitions)
        
        # Create points for the base curve with wave-like effect
        points = []
        for j in range(curve_detail):
            x = j * (width / (curve_detail - 1))
            y_offset = curvature_intensity * math.sin(j / float(curve_detail) * 2 * math.pi + random.uniform(-0.1, 0.1))
            y = offset + y_offset
            points.append(rg.Point3d(x, y, 0))
        
        # Create interpolated base curve
        base_curve = rg.Curve.CreateInterpolatedCurve(points, 3)

        # Extrude the base curve to create a partition surface
        vector = rg.Vector3d(0, 0, height)
        partition_surface = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(base_curve, vector))
        
        partitions.append(partition_surface)

    return partitions"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dynamic_curved_partitions_model(10.0, 5.0, 3.0, 4, 20, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dynamic_curved_partitions_model(8.0, 4.0, 2.5, 6, 15, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dynamic_curved_partitions_model(12.0, 6.0, 4.0, 5, 25, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dynamic_curved_partitions_model(15.0, 7.0, 3.5, 3, 30, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dynamic_curved_partitions_model(9.0, 4.5, 3.0, 7, 18, 0.9)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
