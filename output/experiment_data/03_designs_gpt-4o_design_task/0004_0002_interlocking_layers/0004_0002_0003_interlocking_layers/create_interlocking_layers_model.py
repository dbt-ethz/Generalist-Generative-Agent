# Created for 0004_0002_interlocking_layers.json

""" Summary:
The provided function, `create_interlocking_layers_model`, generates an architectural concept model based on the "Interlocking Layers" metaphor. It creates overlapping and interwoven planes or volumes by defining multiple layers, each with varying dimensions and positions. The function introduces randomness in shifts and rotations, enhancing the model's complexity and spatial hierarchy. By adjusting the dimensions and layering techniques, it visually represents the dynamic relationships between spaces, allowing for both openness and separation. The interplay of light and shadow across these layers amplifies the perception of depth, aligning with the metaphor's emphasis on intricate architectural design."""

#! python 3
function_code = """def create_interlocking_layers_model(base_length=10, base_width=5, num_layers=5, layer_height=2):
    \"""
    Creates an architectural Concept Model based on the 'Interlocking Layers' metaphor.
    
    Parameters:
    - base_length (float): The length of the base layer in meters.
    - base_width (float): The width of the base layer in meters.
    - num_layers (int): The number of interlocking layers to generate.
    - layer_height (float): The height of each layer in meters.
    
    Returns:
    - List of RhinoCommon Brep objects representing the interlocking layers.
    
    The function generates a series of overlapping and interwoven planes or volumes, emphasizing
    spatial hierarchy and varying connectivity levels. The model showcases the interplay of light and
    shadow, enhancing the perception of depth and complexity.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Seed randomness for replicability
    random.seed(42)

    # List to store the resulting Breps
    layers = []

    # Base position offset
    x_offset = 0.0
    y_offset = 0.0

    for i in range(num_layers):
        # Randomly determine the shift and rotation for each layer
        shift_x = random.uniform(-1, 1)
        shift_y = random.uniform(-1, 1)
        rotation_angle = random.uniform(-15, 15)  # Degrees

        # Calculate new position and dimensions for the current layer
        x_offset += shift_x
        y_offset += shift_y
        layer_length = base_length * (1 - 0.1 * i)
        layer_width = base_width * (1 + 0.1 * i)

        # Create a base rectangle for the layer
        corner1 = rg.Point3d(x_offset, y_offset, i * layer_height)
        corner2 = rg.Point3d(x_offset + layer_length, y_offset + layer_width, i * layer_height)
        rectangle = rg.Rectangle3d(rg.Plane.WorldXY, corner1, corner2)
        
        # Convert the rectangle to a planar surface
        layer_surface = rg.Brep.CreateFromSurface(rg.NurbsSurface.CreateFromCorners(corner1, 
                                                                                     rg.Point3d(corner1.X, corner2.Y, corner1.Z), 
                                                                                     corner2, 
                                                                                     rg.Point3d(corner2.X, corner1.Y, corner2.Z)))
        
        # Rotate the layer surface around its center
        center = layer_surface.GetBoundingBox(True).Center
        rotation = rg.Transform.Rotation(math.radians(rotation_angle), center)
        layer_surface.Transform(rotation)

        # Add the layer surface to the list
        layers.append(layer_surface)

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(base_length=12, base_width=6, num_layers=4, layer_height=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(base_length=15, base_width=7, num_layers=6, layer_height=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(base_length=8, base_width=4, num_layers=3, layer_height=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(base_length=14, base_width=5, num_layers=5, layer_height=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(base_length=11, base_width=5.5, num_layers=7, layer_height=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
