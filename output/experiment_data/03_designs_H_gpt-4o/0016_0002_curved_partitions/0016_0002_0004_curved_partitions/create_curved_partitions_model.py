# Created for 0016_0002_curved_partitions.json

""" Summary:
The provided function `create_curved_partitions_model` generates an architectural concept model based on the metaphor of "curved partitions." It creates a series of concentric, layered geometries that mimic natural forms, such as hills or waves, embodying fluidity and organic movement. Each layer features unique curvature and height variations, enhancing visual rhythm and spatial dynamics. The model emphasizes transitions between spaces, fostering exploration and interaction while allowing light to filter through, thus reinforcing the interplay of enclosure and openness. Ultimately, the function produces a cohesive aesthetic that aligns with the metaphor's implications for design."""

#! python 3
function_code = """def create_curved_partitions_model(num_layers=5, radius_increment=1.0, height_increment=1.5, max_curve_variation=2.0, seed=42):
    \"""
    Creates an architectural Concept Model inspired by the 'curved partitions' metaphor with a focus on radial layers.

    This function generates a series of concentric, curved partitions resembling natural formations, creating a dynamic 
    spatial experience. The partitions form a radial pattern, with each layer having a unique curvature and height variation.

    Parameters:
    - num_layers (int): Number of concentric layers to generate.
    - radius_increment (float): Incremental increase in radius for each layer.
    - height_increment (float): Incremental increase in height for each successive layer.
    - max_curve_variation (float): Maximum variation in curvature for each layer.
    - seed (int): Random seed for replicable results.

    Returns:
    - list of Rhino.Geometry.Brep: A list of Brep objects representing the 3D geometries of the model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    geometries = []

    base_radius = 5.0  # Starting radius in meters

    for layer_index in range(num_layers):
        current_radius = base_radius + layer_index * radius_increment
        current_height = layer_index * height_increment

        # Generate points along a circle with variation in the Z direction
        points = []
        for angle_index in range(36):  # 36 points for a smooth circle
            angle = math.radians(angle_index * 10)  # Convert degrees to radians
            x = current_radius * math.cos(angle)
            y = current_radius * math.sin(angle)
            z = current_height + random.uniform(-max_curve_variation, max_curve_variation)
            points.append(rg.Point3d(x, y, z))

        # Create a closed polyline and convert it to a NurbsCurve
        points.append(points[0])  # Close the loop
        polyline = rg.Polyline(points)
        curve = polyline.ToNurbsCurve()

        # Create a surface by lofting the curve with a shifted copy
        loft_curves = [curve, curve.DuplicateCurve()]
        loft_curves[1].Translate(rg.Vector3d(0, 0, height_increment))
        brep = rg.Brep.CreateFromLoft(loft_curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)

        if brep:
            geometries.extend(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions_model(num_layers=7, radius_increment=1.2, height_increment=2.0, max_curve_variation=1.5, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_model(num_layers=3, radius_increment=2.0, height_increment=1.0, max_curve_variation=3.0, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_model(num_layers=6, radius_increment=1.5, height_increment=2.5, max_curve_variation=2.5, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_model(num_layers=4, radius_increment=1.0, height_increment=1.0, max_curve_variation=1.0, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_model(num_layers=8, radius_increment=1.5, height_increment=2.0, max_curve_variation=2.0, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
