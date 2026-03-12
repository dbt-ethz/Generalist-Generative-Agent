# Created for 0004_0003_interlocking_layers.json

""" Summary:
The provided function, `create_interlocking_layers_model`, generates an architectural concept model inspired by the metaphor of "Interlocking Layers." It creates a series of overlapping volumes by varying their height and offset, thus embodying the dynamic movement and complexity suggested by the metaphor. Each layer is defined by a rectangular profile, extruded to form a 3D volume, with random offsets applied to promote spatial interaction. This process results in a textured facade with diverse spatial experiences, effectively illustrating the balance between connectivity and autonomy while capturing the intricate relationships among layers, as specified in the design task."""

#! python 3
function_code = """def create_interlocking_layers_model(base_width, base_length, height_variation, num_layers, offset_variation):
    \"""
    Creates an architectural Concept Model based on the 'Interlocking Layers' metaphor.
    
    Parameters:
    - base_width (float): The base width of the structure in meters.
    - base_length (float): The base length of the structure in meters.
    - height_variation (float): The maximum variation in height for the interlocking layers in meters.
    - num_layers (int): The number of interlocking layers to generate.
    - offset_variation (float): The maximum offset variation for each layer in meters.
    
    Returns:
    - list: A list of RhinoCommon Brep objects representing the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(42)  # Ensure replicability

    layers = []
    base_height = 3.0  # Each layer starts with a base height of 3 meters

    for i in range(num_layers):
        # Randomly vary the height of each layer
        height = base_height + random.uniform(-height_variation, height_variation)
        
        # Create a base plane for the layer
        base_plane = rg.Plane.WorldXY
        
        # Randomly offset the layer in x and y direction
        offset_x = random.uniform(-offset_variation, offset_variation)
        offset_y = random.uniform(-offset_variation, offset_variation)
        translation_vector = rg.Vector3d(offset_x, offset_y, 0)
        base_plane.Translate(translation_vector)

        # Create rectangle profile for the layer
        rectangle = rg.Rectangle3d(base_plane, base_width, base_length)
        
        # Extrude the rectangle to create a 3D volume
        extrusion_vector = rg.Vector3d(0, 0, height)
        layer_brep = rg.Brep.CreateFromBox([rectangle.Corner(0), rectangle.Corner(1), rectangle.Corner(2), rectangle.Corner(3), rectangle.Corner(0) + extrusion_vector, rectangle.Corner(1) + extrusion_vector, rectangle.Corner(2) + extrusion_vector, rectangle.Corner(3) + extrusion_vector])
        
        if layer_brep:
            layers.append(layer_brep)

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(5.0, 10.0, 2.0, 4, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(6.0, 12.0, 1.5, 5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(4.0, 8.0, 3.0, 6, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(7.0, 14.0, 2.5, 3, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(8.0, 16.0, 2.0, 5, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
