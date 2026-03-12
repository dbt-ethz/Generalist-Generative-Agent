# Created for 0016_0005_curved_partitions.json

""" Summary:
The provided function generates an architectural concept model by creating a series of interconnected, wave-like partitions that embody the metaphor of "curved partitions." It employs sinusoidal curves to shape the partitions, which are extruded into 3D surfaces, enhancing the fluidity and organic movement suggested by the metaphor. By manipulating parameters like curvature, height, and transparency, the model fosters a dynamic interaction of light and space, promoting exploration. These design elements encourage smooth transitions and interconnected spaces, ultimately evoking a serene and inviting atmosphere that aligns with the metaphor's essence of continuity and natural flow."""

#! python 3
function_code = """def create_curved_partition_model(seed, num_partitions, radius, height, curve_amplitude, curve_frequency, transparency_factor):
    \"""
    Generates an architectural Concept Model characterized by 'curved partitions', focusing on fluidity and organic movement.

    This function creates a series of interconnected, wave-like partitions using sinusoidal curves, which are extruded to form 3D surfaces.
    These surfaces symbolize natural elements and seamless transitions, promoting exploration and interaction with light and space.

    Parameters:
    - seed (int): Seed for random number generation to ensure replicability.
    - num_partitions (int): Number of partitions to create.
    - radius (float): Radius of the base layout circle.
    - height (float): Height of the partitions.
    - curve_amplitude (float): Amplitude of the sinusoidal curves.
    - curve_frequency (float): Frequency of the sinusoidal curves.
    - transparency_factor (float): Factor to simulate transparency effects in the partitions.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometry of the conceptual model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for reproducibility
    random.seed(seed)

    # Container for Brep geometries
    breps = []

    # Base circle for partition layout
    base_circle = rg.Circle(rg.Plane.WorldXY, radius)

    for i in range(num_partitions):
        # Calculate angle for partition placement
        angle = (2 * math.pi / num_partitions) * i
        base_point = rg.Point3d(radius * math.cos(angle), radius * math.sin(angle), 0)

        # Generate sinusoidal curve for partition
        points = []
        for t in range(11):  # Create 11 points for smooth curve
            x = base_point.X + curve_amplitude * math.sin(curve_frequency * t + angle)
            y = base_point.Y
            z = height * (t / 10.0)
            points.append(rg.Point3d(x, y, z))

        nurbs_curve = rg.NurbsCurve.Create(False, 3, points)

        # Extrude the curve to form a surface
        extrusion_vector = rg.Vector3d(0, 0, height)
        surface = rg.Surface.CreateExtrusion(nurbs_curve, extrusion_vector)

        # Convert the surface to a Brep
        brep = surface.ToBrep()

        # Implement transparency by altering material properties (conceptual)
        # Note: Transparency simulation can be conceptual since Breps don't have material properties
        # This factor could be used in a rendering context to modify material transparency
        brep.SetUserString("transparency", str(transparency_factor))

        breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partition_model(42, 8, 10.0, 5.0, 1.5, 2.0, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partition_model(100, 6, 15.0, 7.0, 2.0, 1.5, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partition_model(2023, 10, 12.0, 4.0, 2.5, 3.0, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partition_model(7, 5, 20.0, 6.0, 1.0, 1.0, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partition_model(15, 12, 8.0, 10.0, 1.2, 2.5, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
