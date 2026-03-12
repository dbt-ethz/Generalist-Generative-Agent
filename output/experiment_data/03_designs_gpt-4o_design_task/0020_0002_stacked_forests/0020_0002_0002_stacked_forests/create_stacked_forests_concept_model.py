# Created for 0020_0002_stacked_forests.json

""" Summary:
The function `create_stacked_forests_concept_model` generates an architectural concept model inspired by the "Stacked forests" metaphor. It creates a series of vertically stacked, organically shaped modules that reflect the layered structure of a forest ecosystem. Each layer varies in radius, simulating the organic growth found in nature, while interlocking volumes represent the complexity of forest canopies. The model incorporates vertical pathways that mimic natural trails, enhancing spatial exploration. By balancing density and openness, the design captures the essence of a forest's hierarchy and diversity, resulting in an engaging architectural representation of the metaphor."""

#! python 3
function_code = """def create_stacked_forests_concept_model(base_radius=5.0, num_layers=5, layer_height=3.0, seed=42):
    \"""
    Creates an architectural Concept Model based on the metaphor of 'Stacked forests'.
    
    The model consists of a series of vertically stacked, organically shaped modules 
    that mimic a forest's diverse ecosystem. The design emphasizes density and hierarchy, 
    with interlocking and overlapping volumes to create a complex, layered silhouette.

    Parameters:
    - base_radius: float, the radius of the base layer of the model in meters.
    - num_layers: int, the number of vertical layers representing different forest strata.
    - layer_height: float, the height of each layer in meters.
    - seed: int, the seed for random number generation to ensure replicability.

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    geometries = []

    # Generate layers with varying radii to mimic organic growth
    for i in range(num_layers):
        # Calculate the radius for the current layer
        radius_variation = random.uniform(-0.5, 0.5)
        current_radius = base_radius + radius_variation * (i + 1)
        
        # Create the base circle for the layer
        base_circle = rg.Circle(rg.Plane.WorldXY, current_radius)
        
        # Generate a random number of segments in the layer to create an organic shape
        num_segments = random.randint(3, 6)
        angle_step = 2 * math.pi / num_segments
        
        # Create points along the circle to form a polygon
        points = []
        for j in range(num_segments):
            angle = j * angle_step
            x = base_circle.Center.X + current_radius * math.cos(angle)
            y = base_circle.Center.Y + current_radius * math.sin(angle)
            z = i * layer_height
            points.append(rg.Point3d(x, y, z))
        
        # Create a closed polyline from the points
        polyline = rg.Polyline(points)
        polyline.Add(polyline[0])  # Close the polyline
        
        # Create a planar surface from the polyline
        planar_surface = rg.Brep.CreatePlanarBreps(polyline.ToNurbsCurve())[0]
        geometries.append(planar_surface)
    
    # Create vertical pathways between layers
    for i in range(num_layers - 1):
        for j in range(random.randint(1, 3)):  # Random number of pathways per layer
            # Random start point on the current layer
            start_idx = random.randint(0, num_segments - 1)
            start_point = points[start_idx]
            
            # Random end point on the next layer
            end_idx = random.randint(0, num_segments - 1)
            end_point = rg.Point3d(points[end_idx].X, points[end_idx].Y, points[end_idx].Z + layer_height)
            
            # Create a vertical pathway as a straight line
            line = rg.Line(start_point, end_point)
            line_curve = line.ToNurbsCurve()
            geometries.append(rg.Brep.CreatePipe(line_curve, 0.1, False, rg.PipeCapMode.Flat, True, 0.01, 0.01)[0])
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept_model(base_radius=6.0, num_layers=4, layer_height=2.5, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept_model(base_radius=4.0, num_layers=6, layer_height=3.5, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept_model(base_radius=5.5, num_layers=3, layer_height=4.0, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept_model(base_radius=7.0, num_layers=5, layer_height=2.0, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept_model(base_radius=5.0, num_layers=7, layer_height=2.0, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
