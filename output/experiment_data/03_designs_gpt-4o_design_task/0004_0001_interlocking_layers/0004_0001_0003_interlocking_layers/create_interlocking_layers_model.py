# Created for 0004_0001_interlocking_layers.json

""" Summary:
The function `create_interlocking_layers_model` generates an architectural concept model inspired by the metaphor of "Interlocking Layers." It creates a series of interconnected planes, defined by parameters such as base dimensions, number of layers, and their thickness. Each layer is extruded from a rectangular base and transformed through translation and rotation, simulating overlapping and interlocking effects. This approach visually embodies spatial complexity, allowing for distinct yet connected spaces. By experimenting with layer orientations and thickness, the model captures the dynamic interplay of openness and privacy, reflecting the metaphor's essence in a cohesive architectural form."""

#! python 3
function_code = """def create_interlocking_layers_model(base_length=10.0, base_width=6.0, num_layers=5, layer_thickness=0.5, angle_variation=15.0):
    \"""
    Creates an architectural Concept Model based on the 'Interlocking Layers' metaphor. This model consists of 
    overlapping and interlocking planar volumes that create a dynamic spatial relationship, emphasizing both 
    openness and separation.

    Parameters:
    - base_length: The base length of the layers in meters.
    - base_width: The base width of the layers in meters.
    - num_layers: The number of interlocking layers to create.
    - layer_thickness: The thickness of each layer in meters.
    - angle_variation: The maximum angle variation for the orientation of each layer in degrees.

    Returns:
    - A list of Breps representing the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random
    import math  # Fix: Import math for trigonometric functions
    random.seed(42)  # Ensure replicability

    layers = []
    base_plane = rg.Plane.WorldXY

    for i in range(num_layers):
        # Create a base rectangle for the layer
        rect_corners = [
            rg.Point3d(0, 0, 0),
            rg.Point3d(base_length, 0, 0),
            rg.Point3d(base_length, base_width, 0),
            rg.Point3d(0, base_width, 0),
            rg.Point3d(0, 0, 0)  # Close the polyline by repeating the first point
        ]
        rectangle = rg.Polyline(rect_corners)
        
        # Create a surface from the rectangle
        surface = rg.Brep.CreateFromCornerPoints(rect_corners[0], rect_corners[1], rect_corners[2], rect_corners[3], 0.01)
        
        # Fix: Use the correct extrusion method
        path_curve = rg.Line(rect_corners[0], rg.Point3d(0, 0, layer_thickness)).ToNurbsCurve()
        layer_brep = surface.Faces[0].CreateExtrusion(path_curve, True)
        
        # Apply a transformation to interlock layers
        translation = rg.Transform.Translation(0, 0, i * (layer_thickness * 0.8))  # Overlapping offset
        angle = random.uniform(-angle_variation, angle_variation)
        rotation = rg.Transform.Rotation(math.radians(angle), base_plane.ZAxis, base_plane.Origin)  # Fix: Use math.radians
        
        transformation = translation * rotation
        layer_brep.Transform(transformation)
        
        layers.append(layer_brep)
    
    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(base_length=12.0, base_width=8.0, num_layers=6, layer_thickness=0.4, angle_variation=20.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(base_length=15.0, base_width=10.0, num_layers=4, layer_thickness=0.6, angle_variation=10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(base_length=14.0, base_width=9.0, num_layers=7, layer_thickness=0.3, angle_variation=25.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(base_length=11.0, base_width=7.0, num_layers=5, layer_thickness=0.5, angle_variation=30.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(base_length=13.0, base_width=7.5, num_layers=8, layer_thickness=0.7, angle_variation=15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
