# Created for 0016_0005_curved_partitions.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of 'curved partitions' by creating a series of undulating, wave-like forms. It uses parameters like base radius, height, wave amplitude, and frequency to define the curvature and spatial organization of the partitions. By applying mathematical transformations to control points of a base circle, the function produces dynamic surfaces that embody fluidity and organic movement, allowing for smooth transitions between interconnected spaces. The model emphasizes light interaction through translucent or reflective materials, fostering an inviting environment that encourages exploration and engagement with the design."""

#! python 3
function_code = """def create_curved_partitions_concept_model(seed, num_partitions, base_radius, height, wave_amplitude, wave_frequency):
    \"""
    Generates an architectural Concept Model based on the metaphor of 'curved partitions'. This function creates
    a series of undulating forms that define and connect spaces using fluid, wave-like contours.

    Parameters:
    seed (int): Seed for random number generation to ensure replicability.
    num_partitions (int): Number of curved partitions to generate.
    base_radius (float): Base radius for the partitions' curves.
    height (float): Height of the partitions.
    wave_amplitude (float): Amplitude of the wave-like curves.
    wave_frequency (float): Frequency of the wave-like curves.

    Returns:
    list: A list of Breps representing the 3D geometries of the curved partitions.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set seed for randomness
    random.seed(seed)

    # List to store resulting Breps
    partitions = []

    # Generate base circle for the partitions
    base_circle = rg.Circle(rg.Plane.WorldXY, base_radius)

    # Create partitions
    for i in range(num_partitions):
        # Calculate offset angle for each partition
        offset_angle = (2 * math.pi / num_partitions) * i

        # Create a wave-like curve
        wave_curve = rg.NurbsCurve.CreateFromCircle(base_circle)
        control_points = wave_curve.Points
        for j in range(1, control_points.Count - 1):
            # Apply wave transformation to each control point
            point = control_points[j].Location
            wave_offset = wave_amplitude * math.sin(wave_frequency * point.X + offset_angle)
            control_points[j].Location = rg.Point3d(point.X, point.Y + wave_offset, point.Z)

        # Loft the wave curve to create a partition surface
        surface = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(wave_curve, rg.Vector3d(0, 0, height)))

        # Add partition to the list
        partitions.append(surface)

    return partitions"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions_concept_model(seed=42, num_partitions=5, base_radius=10.0, height=3.0, wave_amplitude=1.5, wave_frequency=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_concept_model(seed=7, num_partitions=8, base_radius=12.0, height=4.0, wave_amplitude=2.0, wave_frequency=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_concept_model(seed=100, num_partitions=6, base_radius=15.0, height=5.0, wave_amplitude=3.0, wave_frequency=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_concept_model(seed=21, num_partitions=4, base_radius=8.0, height=2.5, wave_amplitude=1.0, wave_frequency=3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_concept_model(seed=15, num_partitions=10, base_radius=9.0, height=6.0, wave_amplitude=2.5, wave_frequency=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
