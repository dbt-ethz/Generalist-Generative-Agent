# Created for 0004_0002_interlocking_layers.json

""" Summary:
The function `create_interlocking_layers_model` generates an architectural concept model based on the 'Interlocking Layers' metaphor by creating multiple overlapping and interwoven planes or volumes. It utilizes specified parameters like base size, number of layers, thickness, gap, and rotation to construct a spatial hierarchy that reflects the metaphor's dynamic nature. Each layer is translated vertically, randomly rotated, and extruded to enhance visual depth, creating a complex interplay of light and shadow. This approach fosters unique spatial relationships, allowing for varied functions and experiences within the architecture, supporting both openness and separation in design."""

#! python 3
function_code = """def create_interlocking_layers_model(base_rect_size, num_layers, layer_thickness, layer_gap, max_rotation_angle):
    \"""
    Creates an architectural concept model based on the 'Interlocking Layers' metaphor.
    
    This function generates a series of overlapping and interwoven planes or volumes to create a complex and engaging
    spatial hierarchy. It emphasizes the interplay of light and shadow, and the dynamic spatial relationships that
    characterize the metaphor.

    Parameters:
    - base_rect_size: Tuple[float, float] representing the width and depth of the base rectangle in meters.
    - num_layers: Integer indicating the number of layers to create.
    - layer_thickness: Float representing the thickness of each layer in meters.
    - layer_gap: Float representing the vertical gap between layers in meters.
    - max_rotation_angle: Float representing the maximum rotation angle in degrees for each layer.

    Returns:
    - List of Rhino.Geometry.Brep objects representing the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set a random seed for reproducibility
    random.seed(42)
    
    width, depth = base_rect_size
    
    layers = []
    base_plane = rg.Plane.WorldXY
    
    for i in range(num_layers):
        # Create the base rectangle for the layer
        rect_corners = [
            rg.Point3d(0, 0, 0),
            rg.Point3d(width, 0, 0),
            rg.Point3d(width, depth, 0),
            rg.Point3d(0, depth, 0),
            rg.Point3d(0, 0, 0)  # Closing the polyline
        ]
        
        # Create a planar surface for this layer
        polyline = rg.Polyline(rect_corners)
        curve = polyline.ToNurbsCurve()
        layer_surface = rg.Brep.CreateEdgeSurface([curve])
        
        if layer_surface is None:
            continue
        
        # Move the layer upwards
        translation = rg.Transform.Translation(0, 0, i * (layer_thickness + layer_gap))
        layer_surface.Transform(translation)
        
        # Randomly rotate the layer
        rotation_angle = random.uniform(-max_rotation_angle, max_rotation_angle)
        rotation = rg.Transform.Rotation(math.radians(rotation_angle), base_plane.ZAxis, rg.Point3d(width / 2, depth / 2, i * (layer_thickness + layer_gap)))
        layer_surface.Transform(rotation)
        
        # Extrude to give thickness
        extrusion_vector = rg.Vector3d(0, 0, layer_thickness)
        extruded_layer = rg.Brep.CreateFromSurface(layer_surface.Surfaces[0])
        extruded_layer = rg.Brep.CreateFromOffsetFace(extruded_layer.Faces[0], extrusion_vector, 0.01, True, True)

        layers.append(extruded_layer)
    
    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model((5, 3), 10, 0.1, 0.2, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model((4, 2), 8, 0.15, 0.25, 20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model((6, 4), 12, 0.2, 0.3, 30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model((3, 5), 6, 0.2, 0.15, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model((7, 5), 15, 0.25, 0.1, 25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
