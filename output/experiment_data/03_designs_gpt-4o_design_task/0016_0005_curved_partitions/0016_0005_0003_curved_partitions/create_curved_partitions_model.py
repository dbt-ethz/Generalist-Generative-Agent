# Created for 0016_0005_curved_partitions.json

""" Summary:
The provided function generates an architectural concept model by creating a series of curved partitions that embody the metaphor of fluidity and organic movement. It takes parameters like base radius, height, number of partitions, curve amplitude, and frequency to define the spatial arrangement. Utilizing sinusoidal curves, the function constructs undulating forms that connect and delineate spaces, fostering a dynamic circulation flow. Each partition is extruded to form a three-dimensional surface, enhancing the interplay of light and shadow. The resulting model invites exploration and interaction, reflecting the metaphor's essence of seamless transitions and tranquil environments."""

#! python 3
function_code = """def create_curved_partitions_model(base_radius=5.0, height=3.0, num_partitions=6, curve_amplitude=1.0, curve_frequency=2):
    \"""
    Creates an architectural Concept Model characterized by 'curved partitions' that embody fluidity and organic movement.
    
    Parameters:
    - base_radius (float): The radius for the base circle defining the layout of partitions.
    - height (float): The height of the partitions.
    - num_partitions (int): Number of curved partitions to create.
    - curve_amplitude (float): Amplitude of the sinusoidal curves defining the partitions.
    - curve_frequency (int): Frequency of the sinusoidal curves.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the curved partitions.
    \"""
    import Rhino.Geometry as rg
    import random
    import math  # Fix: Import the math module for mathematical functions
    random.seed(42)  # Ensure replicability
    
    # Container for 3D geometries
    breps = []

    # Calculate angle step based on the number of partitions
    angle_step = 360.0 / num_partitions

    for i in range(num_partitions):
        # Calculate angle in radians
        angle_rad = math.radians(i * angle_step)  # Fix: Use math module for radians conversion

        # Determine the base point for each partition
        base_point = rg.Point3d(base_radius * math.cos(angle_rad), base_radius * math.sin(angle_rad), 0)  # Fix: Use math module for trigonometric functions

        # Create a sinusoidal curve for the partition
        curve_points = []
        for t in range(11):  # Using 11 points for the curve
            x = base_point.X + curve_amplitude * math.sin(curve_frequency * t)  # Fix: Use math module for sine function
            y = base_point.Y
            z = height * (t / 10.0)
            curve_points.append(rg.Point3d(x, y, z))

        # Create a NURBS curve from points
        nurbs_curve = rg.NurbsCurve.Create(False, 3, curve_points)

        # Extrude the curve to form a surface
        extrusion_vector = rg.Vector3d(0, 0, height)
        surface = rg.Surface.CreateExtrusion(nurbs_curve, extrusion_vector)

        # Convert the surface to a Brep
        brep = surface.ToBrep()
        breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions_model(base_radius=10.0, height=4.0, num_partitions=8, curve_amplitude=2.0, curve_frequency=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_model(base_radius=7.0, height=5.0, num_partitions=5, curve_amplitude=1.5, curve_frequency=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_model(base_radius=8.0, height=6.0, num_partitions=10, curve_amplitude=2.5, curve_frequency=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_model(base_radius=6.0, height=2.5, num_partitions=4, curve_amplitude=1.0, curve_frequency=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_model(base_radius=9.0, height=3.5, num_partitions=7, curve_amplitude=1.2, curve_frequency=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
