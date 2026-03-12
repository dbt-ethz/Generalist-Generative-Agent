# Created for 0004_0001_interlocking_layers.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "Interlocking Layers." It creates a series of interconnected planes or volumes by defining parameters such as the base size, number of layers, and layer thickness. Each layer is randomly offset and rotated to enhance visual complexity and dynamic interplay. The function uses geometry transformations to simulate overlapping layers, capturing the essence of both openness and separation. This approach allows for a rich architectural experience, reflecting the metaphor by emphasizing spatial variety and structural intricacies, ultimately producing a cohesive model that embodies the design task's requirements."""

#! python 3
function_code = """def create_interlocking_layers_model(base_size=10, num_layers=5, layer_thickness=0.5):
    \"""
    Creates an architectural Concept Model embodying the 'Interlocking Layers' metaphor.
    
    This function generates a series of interconnected planes or volumes that are physically interlocked,
    highlighting both openness and separation through dynamic spatial relationships and visual depth.
    
    Parameters:
    - base_size (float): The base size of the model in meters. This determines the overall scale.
    - num_layers (int): The number of interlocking layers to create.
    - layer_thickness (float): The thickness of each layer in meters.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the interlocking layers of the model.
    \"""
    import Rhino
    import random
    import math  # Import math to replace RhinoMath
    random.seed(42)  # Ensures replicability
    
    breps = []
    base_plane = Rhino.Geometry.Plane.WorldXY
    
    for i in range(num_layers):
        offset = random.uniform(-base_size * 0.2, base_size * 0.2)
        angle = random.uniform(-15, 15)  # Random angle for dynamic interplay
        
        # Create the base rectangle for the layer
        rectangle = Rhino.Geometry.Rectangle3d(base_plane, base_size, layer_thickness)
        
        # Transform the rectangle to create interlocking effect
        translation = Rhino.Geometry.Transform.Translation(offset, offset, i * (layer_thickness + 0.1))
        rotation = Rhino.Geometry.Transform.Rotation(math.radians(angle), base_plane.Normal, base_plane.Origin)  # Use math.radians
        
        # Apply transformations
        rectangle.Transform(translation)
        rectangle.Transform(rotation)
        
        # Create a Brep from the transformed rectangle extrusion
        extrusion_vector = base_plane.ZAxis * (base_size / num_layers)  # Adjust extrusion height for variety
        brep = Rhino.Geometry.Brep.CreateFromSurface(Rhino.Geometry.Surface.CreateExtrusion(rectangle.ToNurbsCurve(), extrusion_vector))
        
        if brep:
            breps.append(brep)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(base_size=15, num_layers=7, layer_thickness=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(base_size=12, num_layers=4, layer_thickness=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(base_size=20, num_layers=6, layer_thickness=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(base_size=18, num_layers=5, layer_thickness=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(base_size=25, num_layers=3, layer_thickness=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
