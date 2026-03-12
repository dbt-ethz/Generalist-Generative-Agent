# Created for 0016_0004_curved_partitions.json

""" Summary:
The provided function, `create_curved_partitions_flexible_ribbons`, generates an architectural concept model that embodies the metaphor of "curved partitions." It creates a series of flexible, ribbon-like geometries that reflect fluidity and organic movement. By utilizing parameters such as base radius, height, and number of ribbons, the function produces interwoven curves that foster a dynamic spatial organization. The use of random offsets in the curve definition enhances the organic quality, while the extruded surfaces of the ribbons interact with light, casting shadows that enrich the sensory experience. This model promotes smooth transitions and connectivity, inviting exploration and engagement within the space."""

#! python 3
function_code = """def create_curved_partitions_flexible_ribbons(base_radius=8.0, height=4.0, num_ribbons=6, ribbon_width=1.0, ribbon_thickness=0.1, seed=42):
    \"""
    Creates an architectural concept model using the metaphor of 'curved partitions', emphasizing fluidity and organic flow.
    
    This function generates a series of flexible ribbon-like partitions that are interwoven to suggest a dynamic and harmonious spatial organization. 
    The ribbons reflect the natural progression and elegance of curves, enhancing the sensory experience through smooth transitions and light interplay.

    Parameters:
        base_radius (float): The base radius for the circular arrangement of ribbons.
        height (float): The height of the ribbons.
        num_ribbons (int): The number of ribbon-like partitions to create.
        ribbon_width (float): The width of each ribbon.
        ribbon_thickness (float): The thickness of each ribbon.
        seed (int): A seed for randomness to ensure replicable results.

    Returns:
        list: A list of RhinoCommon Brep geometries representing the ribbon-like curved partitions.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for reproducibility
    random.seed(seed)

    # Container for the geometries
    geometries = []

    # Create ribbon-like partitions
    for i in range(num_ribbons):
        angle = (2 * math.pi / num_ribbons) * i
        start_point = rg.Point3d(base_radius * math.cos(angle), base_radius * math.sin(angle), 0)

        # Define the curve path for each ribbon
        curve_points = []
        for j in range(4):  # 4 control points for smoother curves
            x_offset = ribbon_width * (random.random() - 0.5)
            y_offset = ribbon_width * (random.random() - 0.5)
            z = height * (j / 3.0)
            curve_points.append(rg.Point3d(start_point.X + x_offset, start_point.Y + y_offset, z))

        # Create an interpolated curve
        ribbon_curve = rg.Curve.CreateInterpolatedCurve(curve_points, 3)

        # Create a planar surface for the ribbon
        if ribbon_curve:
            ribbon_surface = rg.Surface.CreateExtrusion(ribbon_curve, rg.Vector3d(0, 0, ribbon_thickness))
            if ribbon_surface:
                brep_ribbon = rg.Brep.CreateFromSurface(ribbon_surface)
                if brep_ribbon:
                    geometries.append(brep_ribbon)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions_flexible_ribbons(base_radius=10.0, height=5.0, num_ribbons=8, ribbon_width=1.5, ribbon_thickness=0.2, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_flexible_ribbons(base_radius=12.0, height=6.0, num_ribbons=10, ribbon_width=2.0, ribbon_thickness=0.15, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_flexible_ribbons(base_radius=9.0, height=3.0, num_ribbons=5, ribbon_width=1.2, ribbon_thickness=0.1, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_flexible_ribbons(base_radius=7.0, height=4.5, num_ribbons=4, ribbon_width=1.0, ribbon_thickness=0.05, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_flexible_ribbons(base_radius=15.0, height=7.0, num_ribbons=12, ribbon_width=1.8, ribbon_thickness=0.3, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
