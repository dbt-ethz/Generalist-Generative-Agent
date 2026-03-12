# Created for 0016_0005_curved_partitions.json

""" Summary:
The function `create_curved_partitions_model` generates an architectural concept model based on the metaphor of "curved partitions" by creating a series of undulating, wave-like surfaces. It defines spatial relationships through sinusoidal curves that mimic natural forms, facilitating smooth transitions between interconnected spaces. The model utilizes parameters such as length, width, height, and the number of wave undulations to create variations in partition shapes. By manipulating light and shadow with the curved surfaces, the design fosters an inviting atmosphere that encourages exploration. The resulting 3D geometry embodies fluidity and organic movement, enhancing user engagement with the space."""

#! python 3
function_code = """def create_curved_partitions_model(length=20.0, width=10.0, height=5.0, num_waves=4, seed=42):
    \"""
    Generates an architectural Concept Model inspired by the metaphor of 'curved partitions'.

    This function creates a series of undulating, wave-like surfaces that define and connect spaces,
    promoting fluid transitions and dynamic interaction of light across the surfaces.

    Parameters:
    - length (float): The overall length of the model in meters.
    - width (float): The overall width of the model in meters.
    - height (float): The maximum height of the partitions in meters.
    - num_waves (int): The number of wave-like undulations per partition.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the curved partitions of the model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for reproducibility
    random.seed(seed)

    def create_wave_curve(length, width, num_waves, amplitude):
        \"""Generates a sinusoidal curve along the length.\"""
        points = []
        step = length / num_waves
        for i in range(num_waves + 1):
            x = i * step
            y = amplitude * math.sin(2 * math.pi * i / num_waves)
            points.append(rg.Point3d(x, y, 0))
        return rg.Curve.CreateInterpolatedCurve(points, 3)

    def create_partition_curve(base_curve, height, offset):
        \"""Offsets the curve and extrudes it to create a 3D surface.\"""
        offset_curve = base_curve.DuplicateCurve()
        offset_curve.Translate(rg.Vector3d(0, offset, 0))
        extrusion_vector = rg.Vector3d(0, 0, height)
        return rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(offset_curve, extrusion_vector))

    partitions = []
    for i in range(-1, 2):  # Create three main partitions
        amplitude = random.uniform(0.5, 1.5) * (height / 5.0)
        base_curve = create_wave_curve(length, width, num_waves, amplitude)
        partition = create_partition_curve(base_curve, height, i * (width / 3.0))
        if partition:
            partitions.append(partition)

    return partitions"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions_model(length=30.0, width=15.0, height=7.0, num_waves=6, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_model(length=25.0, width=12.0, height=6.0, num_waves=5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_model(length=40.0, width=20.0, height=10.0, num_waves=8, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_model(length=35.0, width=18.0, height=9.0, num_waves=7, seed=11)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_model(length=22.0, width=11.0, height=4.0, num_waves=3, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
