# Created for 0016_0005_curved_partitions.json

""" Summary:
The provided function generates an architectural concept model by creating a series of vertical, wave-like partitions that embody the metaphor of "curved partitions." It achieves this through a mathematical approach, where wave curves are calculated based on specified parameters like amplitude and frequency. The function uses Rhino's geometry library to create smooth, undulating surfaces that define and connect spaces, facilitating fluid circulation and interaction. By manipulating these curves and integrating light-responsive materials, the model evokes a serene atmosphere, encouraging exploration and engagement with the environment, thus effectively translating the metaphor into a tangible architectural form."""

#! python 3
function_code = """def create_curved_partitions_model_v2(width, depth, height, num_partitions, wave_amplitude, wave_frequency):
    \"""
    Generates an architectural Concept Model based on the metaphor of 'curved partitions'.
    This version explores a different architectural expression by creating a series of vertical, 
    wave-like surfaces that define and connect spaces with fluid contours.

    Parameters:
    - width (float): The overall width of the model in meters.
    - depth (float): The overall depth of the model in meters.
    - height (float): The height of the partitions in meters.
    - num_partitions (int): Number of curved partitions to create.
    - wave_amplitude (float): Amplitude of the wave-like curves.
    - wave_frequency (float): Frequency of the wave-like curves.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the curved partitions.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    # Seed for reproducibility
    random.seed(42)

    partitions = []

    # Calculate the distance between partitions
    partition_spacing = width / (num_partitions + 1)

    # Create wave-like partitions
    for i in range(num_partitions):
        # Base line for each partition
        start_point = rg.Point3d(partition_spacing * (i + 1), 0, 0)
        end_point = rg.Point3d(partition_spacing * (i + 1), depth, 0)

        # Create points along the wave
        points = []
        for j in range(11):
            x = start_point.X
            y = start_point.Y + (depth / 10) * j
            z = wave_amplitude * math.sin(wave_frequency * y + random.uniform(-0.1, 0.1))
            points.append(rg.Point3d(x, y, z))

        # Create a curve through the points
        wave_curve = rg.Curve.CreateInterpolatedCurve(points, 3)

        # Extrude the curve vertically to create a partition
        extrusion_vector = rg.Vector3d(0, 0, height)
        partition_surface = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(wave_curve, extrusion_vector))

        partitions.append(partition_surface)

    return partitions"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions_model_v2(10.0, 5.0, 3.0, 4, 1.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_model_v2(15.0, 7.0, 4.0, 6, 0.5, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_model_v2(12.0, 6.0, 3.5, 5, 0.8, 1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_model_v2(8.0, 4.0, 2.5, 3, 0.6, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_model_v2(20.0, 10.0, 5.0, 8, 1.5, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
