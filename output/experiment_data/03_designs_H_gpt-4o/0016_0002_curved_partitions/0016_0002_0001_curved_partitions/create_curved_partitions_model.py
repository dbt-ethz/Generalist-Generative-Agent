# Created for 0016_0002_curved_partitions.json

""" Summary:
The function `create_curved_partitions_model` generates an architectural concept model inspired by the metaphor of "curved partitions." It creates a series of layered, sweeping curves that mimic natural landscapes, embodying fluidity and organic movement. Each layer is spaced vertically, with wave-like patterns formed by sine functions, simulating hills or waves. This design fosters dynamic spatial relationships and encourages exploration. The model incorporates variations in light and shadow through surface geometry, providing aesthetic and functional qualities. Ultimately, the resulting model visually and spatially represents the metaphor, inviting interaction and enhancing the sensory experience within the space."""

#! python 3
function_code = """def create_curved_partitions_model(num_layers=4, layer_spacing=2.5, curve_resolution=20, wave_amplitude=1.5, wave_frequency=2.0, seed=42):
    \"""
    Create an architectural Concept Model based on the 'curved partitions' metaphor using RhinoCommon.
    
    This function generates a landscape-like form composed of layered, sweeping curves that mimic natural
    landscapes, creating a sense of movement and dynamic spatial relationships. The design emphasizes fluidity
    and the interplay of light and shadow.

    Parameters:
    - num_layers (int): Number of curved layers to generate.
    - layer_spacing (float): Vertical distance between each layer.
    - curve_resolution (int): Number of points defining each wave curve.
    - wave_amplitude (float): Amplitude of the wave patterns in the partitions.
    - wave_frequency (float): Frequency of the wave patterns in the partitions.
    - seed (int): Random seed for replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the model.
    \"""
    import Rhino.Geometry as rg
    import math
    import random
    
    # Set the random seed for replicability
    random.seed(seed)
    
    geometries = []
    
    base_length = 30.0  # Length of the model in meters
    base_width = 15.0   # Width of the model in meters
    
    for layer_index in range(num_layers):
        # Calculate current layer's base height
        base_height = layer_index * layer_spacing
        
        # Create a wave pattern across the length of the model
        wave_points = []
        for point_index in range(curve_resolution + 1):
            x = base_length * (point_index / curve_resolution)
            y = wave_amplitude * math.sin(wave_frequency * math.pi * (point_index / curve_resolution))
            z = base_height + wave_amplitude * random.uniform(-0.5, 0.5)
            wave_points.append(rg.Point3d(x, y, z))
        
        # Create a NurbsCurve from the wave points
        wave_curve = rg.Curve.CreateInterpolatedCurve(wave_points, 3)
        
        # Create a surface by extruding the curve along the Y-axis
        extrusion_vector = rg.Vector3d(0, base_width, 0)
        surface = rg.Surface.CreateExtrusion(wave_curve, extrusion_vector)
        
        # Convert the surface to a Brep and add to the list
        brep = surface.ToBrep()
        geometries.append(brep)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions_model(num_layers=5, layer_spacing=3.0, curve_resolution=30, wave_amplitude=2.0, wave_frequency=1.5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_model(num_layers=6, layer_spacing=2.0, curve_resolution=25, wave_amplitude=1.0, wave_frequency=3.0, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_model(num_layers=3, layer_spacing=4.0, curve_resolution=15, wave_amplitude=2.5, wave_frequency=1.0, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_model(num_layers=4, layer_spacing=2.0, curve_resolution=40, wave_amplitude=1.0, wave_frequency=2.5, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_model(num_layers=7, layer_spacing=3.5, curve_resolution=35, wave_amplitude=2.2, wave_frequency=1.8, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
