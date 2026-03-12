# Created for 0016_0002_curved_partitions.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "curved partitions." By utilizing parameters such as the number of layers, their height, length, and maximum curve amplitude, it creates a series of undulating surfaces that mimic natural landscapes. Each layer is defined by a sine-like curve, which captures the essence of fluidity and organic movement. The model is constructed by extruding these curves vertically, resulting in 3D geometries that embody dynamic spatial relationships. This design invites exploration and interaction, allowing light to filter through, thereby enhancing the overall sensory experience and visual rhythm of the space."""

#! python 3
function_code = """def create_curved_partitions_model(num_layers=5, layer_height=2.0, layer_length=20.0, max_curve_amplitude=3.0, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'curved partitions' metaphor using layered sweeping curves.
    
    Parameters:
    - num_layers: int, number of curved layers to create.
    - layer_height: float, height of each layer in meters.
    - layer_length: float, length of each layer in meters.
    - max_curve_amplitude: float, maximum amplitude of the curves in meters.
    - seed: int, seed for randomness to ensure replicability.
    
    Returns:
    - list of Rhino.Geometry.Brep, representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import System
    import random
    
    # Set the random seed for replicability
    random.seed(seed)
    
    # List to hold the generated geometries
    geometries = []
    
    # Base plane for the first layer
    base_plane = rg.Plane.WorldXY
    
    # Create the layers
    for i in range(num_layers):
        # Calculate the vertical offset for the current layer
        vertical_offset = i * layer_height
        
        # Create a random sine-like curve for the layer
        points = []
        for j in range(int(layer_length) + 1):
            x = j
            y = max_curve_amplitude * random.uniform(0.5, 1.0) * System.Math.Sin(j * System.Math.PI / layer_length)
            z = vertical_offset
            points.append(rg.Point3d(x, y, z))
        
        # Create a polyline and then a curve from the points
        polyline = rg.Polyline(points)
        curve = polyline.ToNurbsCurve()
        
        # Create a surface by extruding the curve vertically to form the partition
        extrusion_vector = rg.Vector3d(0, 0, layer_height)
        extrusion = rg.Extrusion.Create(curve, layer_height, True)
        brep = extrusion.ToBrep()
        
        # Add the brep to the list of geometries
        geometries.append(brep)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions_model(num_layers=7, layer_height=3.0, layer_length=25.0, max_curve_amplitude=4.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_model(num_layers=6, layer_height=2.5, layer_length=30.0, max_curve_amplitude=5.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_model(num_layers=4, layer_height=1.5, layer_length=15.0, max_curve_amplitude=2.0, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_model(num_layers=8, layer_height=2.2, layer_length=22.0, max_curve_amplitude=3.5, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_model(num_layers=5, layer_height=2.0, layer_length=18.0, max_curve_amplitude=2.5, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
