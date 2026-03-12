# Created for 0016_0003_curved_partitions.json

""" Summary:
The function `generate_curved_partition_model` creates an architectural concept model inspired by the metaphor of "curved partitions." It generates a series of interconnected curvilinear elements that embody fluidity and organic movement. By defining parameters like the number of partitions, their height, and radius, the function produces unique curved surfaces that both divide and connect spaces. The extruded arcs create dynamic forms that allow for seamless transitions, enhancing the interplay of light and shadow within the model. This approach fosters an inviting atmosphere, encouraging exploration while maintaining an elegant aesthetic aligned with the design task's intent."""

#! python 3
function_code = """def generate_curved_partition_model(partition_count=8, max_radius=15, min_height=2, max_height=5, seed=123):
    \"""
    Generates an architectural Concept Model using the metaphor of 'curved partitions'.
    
    This function creates a series of interconnected curvilinear entities with varying heights and radii,
    suggesting division and continuity while enhancing spatial transitions through light and shadow interplay.

    Parameters:
    - partition_count (int): Number of curved partitions to generate.
    - max_radius (float): Maximum radius for the curved partitions.
    - min_height (float): Minimum height for a partition.
    - max_height (float): Maximum height for a partition.
    - seed (int): Seed for randomness for replicability.

    Returns:
    - List: A list of RhinoCommon Brep geometries representing the partitions.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    partitions = []

    # Define a base circle for arranging partitions
    base_circle = rg.Circle(rg.Plane.WorldXY, max_radius)

    # Angle increment for partition placement
    angle_increment = 2 * math.pi / partition_count

    for i in range(partition_count):
        # Calculate position on the circle
        angle = i * angle_increment
        position = base_circle.PointAt(angle)

        # Randomize height and radius
        height = random.uniform(min_height, max_height)
        radius = random.uniform(max_radius / 3, max_radius)

        # Create a base arc for the partition
        arc = rg.Arc(position, radius, angle_increment / 2)
        arc_curve = arc.ToNurbsCurve()

        # Create a vertical extrusion of the arc curve
        extrusion_vector = rg.Vector3d(0, 0, height)
        partition_surface = rg.Surface.CreateExtrusion(arc_curve, extrusion_vector)

        # Convert surface to Brep
        brep_partition = partition_surface.ToBrep()
        if brep_partition:
            partitions.append(brep_partition)

    return partitions"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_curved_partition_model(partition_count=12, max_radius=20, min_height=3, max_height=7, seed=456)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_curved_partition_model(partition_count=10, max_radius=25, min_height=1, max_height=4, seed=789)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_curved_partition_model(partition_count=6, max_radius=18, min_height=2.5, max_height=6, seed=321)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_curved_partition_model(partition_count=15, max_radius=30, min_height=1, max_height=8, seed=101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_curved_partition_model(partition_count=9, max_radius=22, min_height=4, max_height=10, seed=202)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
