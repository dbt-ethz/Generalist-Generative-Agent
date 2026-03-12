# Created for 0016_0004_curved_partitions.json

""" Summary:
The function `create_curved_partition_concept_model_v3` generates an architectural concept model inspired by the metaphor of "curved partitions." It creates a series of dynamic, fluidly shaped partitions using sinusoidal curves, promoting a sense of harmony and movement. By varying the number, width, and height of partitions, the model reflects the metaphor's essence, allowing for smooth spatial transitions and connectivity. The partitions are then revolved around an axis to form three-dimensional surfaces, enhancing their organic appearance. This approach embodies the desired interplay of light and shadow, inviting exploration and interaction within the designed space."""

#! python 3
function_code = """def create_curved_partition_concept_model_v3(num_partitions=4, partition_width=2, partition_height=5, seed=100):
    \"""
    Creates an architectural concept model based on the metaphor of 'curved partitions'.

    This function generates a series of curved partitions using sinusoidal waveforms to explore dynamic
    and harmonious flow within a space. The partitions are designed to reflect fluidity and continuity,
    fostering smooth spatial transitions and an inviting environment.

    Inputs:
        num_partitions (int): The number of curved partitions to create.
        partition_width (float): The width of each partition.
        partition_height (float): The height of each partition.
        seed (int): A seed for randomness to ensure replicable results.

    Outputs:
        list: A list of RhinoCommon Brep geometries representing the curved partitions.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    partitions = []

    for i in range(num_partitions):
        # Determine the base point for each partition
        base_x = i * partition_width * 1.5  # space out partitions
        base_y = random.uniform(-2, 2)  # slight random offset for organic placement
        base_point = rg.Point3d(base_x, base_y, 0)

        # Create a sinusoidal curve for the partition
        curve_points = []
        for t in range(11):  # 11 points for a smooth curve
            x = base_point.X + t * (partition_width / 10.0)
            y = base_point.Y + math.sin(t * math.pi / 5.0) * partition_width / 2
            z = partition_height * t / 10.0
            curve_points.append(rg.Point3d(x, y, z))

        curve = rg.Curve.CreateInterpolatedCurve(curve_points, 3)

        # Create a surface by revolving the curve around the Z-axis
        axis = rg.Line(base_point, rg.Point3d(base_point.X, base_point.Y, partition_height))
        revolve_surface = rg.Brep.CreateFromRevSurface(rg.RevSurface.Create(curve, axis), False, False)

        if revolve_surface:
            partitions.append(revolve_surface)

    return partitions"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partition_concept_model_v3(num_partitions=6, partition_width=3, partition_height=7, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partition_concept_model_v3(num_partitions=5, partition_width=4, partition_height=6, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partition_concept_model_v3(num_partitions=3, partition_width=2.5, partition_height=4, seed=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partition_concept_model_v3(num_partitions=7, partition_width=3.5, partition_height=8, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partition_concept_model_v3(num_partitions=8, partition_width=2, partition_height=5, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
