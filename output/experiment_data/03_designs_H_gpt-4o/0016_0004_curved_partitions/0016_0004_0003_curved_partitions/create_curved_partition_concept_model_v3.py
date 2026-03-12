# Created for 0016_0004_curved_partitions.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "curved partitions." It creates a series of interwoven curved surfaces that embody fluidity and organic movement, reflecting the design principles of harmony and connectivity. By defining parameters such as the number of partitions, their dimensions, and a random seed for variation, the function utilizes mathematical calculations to position and shape each partition in a spiral layout. The curves are constructed using interpolated points and then extruded to form three-dimensional surfaces. This process results in a model that enhances spatial relationships, promotes smooth transitions, and invites exploration, embodying the metaphor's essence."""

#! python 3
function_code = """def create_curved_partition_concept_model_v3(num_partitions=6, base_radius=12.0, partition_thickness=0.5, height=4.0, seed=123):
    \"""
    Generates a conceptual architectural model using the metaphor of 'curved partitions'.

    This function creates a set of interwoven curved partitions that suggest dynamic movement
    and harmonious spatial relationships. The partitions are crafted to evoke a sense of flow 
    and continuity, enhancing the sensory experience through smooth transitions and organic forms.

    Inputs:
        num_partitions (int): The number of curved partitions to generate.
        base_radius (float): The radius defining the initial placement of partition bases.
        partition_thickness (float): The thickness of each partition.
        height (float): The height of each partition.
        seed (int): A seed for randomness to ensure replicable results.

    Outputs:
        list: A list of RhinoCommon Brep geometries representing the curved partitions.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for reproducibility
    random.seed(seed)

    # Container for the partition geometries
    partitions = []

    # Generate partitions with a spiral effect
    for i in range(num_partitions):
        # Calculate angle for the spiral layout
        angle = (2 * math.pi / num_partitions) * i
        offset = (i / num_partitions) * base_radius

        # Define the starting point of the partition
        start_point = rg.Point3d(
            (base_radius - offset) * math.cos(angle),
            (base_radius - offset) * math.sin(angle),
            0
        )

        # Define the curve path for the partition
        curve_points = []
        for j in range(6):  # Control points for the curve
            x = start_point.X + partition_thickness * math.sin(j * math.pi / 3)
            y = start_point.Y + partition_thickness * math.cos(j * math.pi / 3)
            z = height * (j / 5.0) + random.uniform(-0.2, 0.2)
            curve_points.append(rg.Point3d(x, y, z))
        
        # Create an interpolated curve
        curve = rg.Curve.CreateInterpolatedCurve(curve_points, 3)
        
        # Extrude the curve to form a partition
        if curve:
            extrusion_vector = rg.Vector3d(0, 0, height)
            partition_surface = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(curve, extrusion_vector))
            partitions.append(partition_surface)
    
    return partitions"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partition_concept_model_v3(num_partitions=8, base_radius=15.0, partition_thickness=0.7, height=5.0, seed=456)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partition_concept_model_v3(num_partitions=10, base_radius=10.0, partition_thickness=0.3, height=3.0, seed=789)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partition_concept_model_v3(num_partitions=5, base_radius=14.0, partition_thickness=0.6, height=6.0, seed=321)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partition_concept_model_v3(num_partitions=7, base_radius=11.0, partition_thickness=0.4, height=4.5, seed=654)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partition_concept_model_v3(num_partitions=9, base_radius=13.0, partition_thickness=0.8, height=7.0, seed=987)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
