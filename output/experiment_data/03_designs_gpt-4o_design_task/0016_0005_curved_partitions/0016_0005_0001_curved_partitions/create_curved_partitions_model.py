# Created for 0016_0005_curved_partitions.json

""" Summary:
The function `create_curved_partitions_model` generates an architectural concept model by creating a series of undulating, wave-like partitions that embody the metaphor of fluidity and organic movement. By defining parameters such as the number of partitions, curve length, height, wave amplitude, and frequency, the function constructs smooth, interconnected surfaces resembling natural forms. The model emphasizes seamless transitions between spaces, fostering a sense of movement and exploration. These curved partitions manipulate light and shadow, enhancing the atmospheric quality and inviting user interaction, ultimately translating the metaphor into a tangible architectural representation that embodies tranquility and elegance."""

#! python 3
function_code = """def create_curved_partitions_model(num_partitions, base_curve_length, height, wave_amplitude, wave_frequency):
    \"""
    Creates an architectural Concept Model based on the metaphor of 'curved partitions'.
    
    This function generates a series of curved partitions that define and connect spaces with fluid, wave-like forms.
    The partitions are created as undulating surfaces, resembling natural elements like water currents or sand dunes.
    The design emphasizes smooth transitions and light interplay.

    Parameters:
    - num_partitions (int): Number of curved partitions to create.
    - base_curve_length (float): Length of the base curves that define the partitions.
    - height (float): Height of the partitions.
    - wave_amplitude (float): Amplitude of the wave-like curves.
    - wave_frequency (float): Frequency of the wave-like curves.

    Returns:
    - List of Rhino.Geometry.Brep: A list of 3D geometries representing the curved partitions.
    \"""
    import Rhino.Geometry as rg
    import random
    import math  # Fix: Import the math module

    # Seed for reproducibility
    random.seed(42)

    partitions = []

    # Create base curves with wave-like shapes for each partition
    for i in range(num_partitions):
        points = []
        for j in range(0, int(base_curve_length * 10)):  # More points for smoother curves
            x = j * 0.1
            y = wave_amplitude * random.uniform(0.8, 1.2) * math.sin(x * wave_frequency + random.uniform(-0.2, 0.2))
            points.append(rg.Point3d(x, y, 0))

        # Create interpolated curve through points
        base_curve = rg.Curve.CreateInterpolatedCurve(points, 3)

        # Create a surface by extruding the base curve in the Z direction
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
    geometry = create_curved_partitions_model(5, 10.0, 3.0, 2.0, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_model(8, 15.0, 4.0, 3.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_model(6, 12.0, 2.5, 1.5, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_model(4, 20.0, 5.0, 4.0, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_model(10, 25.0, 6.0, 5.0, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
