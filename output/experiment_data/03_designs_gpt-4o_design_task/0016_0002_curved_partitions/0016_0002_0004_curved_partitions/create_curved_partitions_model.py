# Created for 0016_0002_curved_partitions.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "curved partitions" by creating a series of layered, undulating surfaces that mimic natural landscapes. It uses parameters like base radius, height, and wave characteristics to define the geometry of each layer. The function constructs wave patterns along circular bases, simulating hills or waves, which guide spatial transitions and circulation. Each layer is extruded to form three-dimensional surfaces, embodying fluidity and organic movement. The resulting model invites exploration and interaction, enhancing light and shadow play while maintaining a cohesive aesthetic that resonates with the metaphor."""

#! python 3
function_code = """def create_curved_partitions_model(base_radius=5.0, height=3.0, layers=5, wave_frequency=2.0, wave_amplitude=0.5):
    \"""
    Creates an architectural Concept Model using the metaphor of 'curved partitions'. The model consists of
    a series of layered, sweeping curves that mimic natural landscapes like hills or waves.

    Parameters:
    - base_radius: float, the radius of the base of the model.
    - height: float, the maximum height of the model.
    - layers: int, the number of curved layers to create.
    - wave_frequency: float, the frequency of the wave patterns in the partitions.
    - wave_amplitude: float, the amplitude of the wave patterns in the partitions.

    Returns:
    - A list of RhinoCommon Brep objects representing the curved partitions of the model.
    \"""

    import Rhino.Geometry as rg
    import random
    import math  # Import the math module

    # Set seed for randomness
    random.seed(42)

    breps = []

    # Calculate the step height for each layer
    step_height = height / layers

    for i in range(layers):
        # Calculate the current layer height
        current_height = i * step_height

        # Create a base circle for this layer
        base_circle = rg.Circle(rg.Plane.WorldXY, base_radius)
        
        # Create a wave pattern along the circle
        wave_points = []
        for j in range(36):  # 36 points for a smooth curve
            angle = (j / 36.0) * 2 * math.pi  # Use math.pi
            x = base_radius * math.cos(angle)  # Use math.cos
            y = base_radius * math.sin(angle)  # Use math.sin
            z = current_height + wave_amplitude * math.sin(wave_frequency * angle)  # Use math.sin
            wave_points.append(rg.Point3d(x, y, z))
        
        # Create a polyline from the wave points and close it
        wave_points.append(wave_points[0])  # Close the polyline by adding the first point at the end
        wave_polyline = rg.Polyline(wave_points)

        # Create a NurbsCurve from the polyline
        wave_curve = wave_polyline.ToNurbsCurve()

        # Extrude the wave curve upwards to create a surface
        extrusion_vector = rg.Vector3d(0, 0, step_height)
        surface = rg.Surface.CreateExtrusion(wave_curve, extrusion_vector)

        # Convert the surface to a Brep and add to the list
        brep = surface.ToBrep()
        breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions_model(base_radius=6.0, height=4.0, layers=7, wave_frequency=3.0, wave_amplitude=0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_model(base_radius=8.0, height=5.0, layers=10, wave_frequency=1.5, wave_amplitude=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_model(base_radius=4.0, height=2.0, layers=6, wave_frequency=2.5, wave_amplitude=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_model(base_radius=7.0, height=3.5, layers=8, wave_frequency=1.0, wave_amplitude=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_model(base_radius=5.5, height=3.2, layers=9, wave_frequency=2.8, wave_amplitude=0.9)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
