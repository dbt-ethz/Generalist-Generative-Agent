# Created for 0004_0003_interlocking_layers.json

""" Summary:
The provided function, `create_interlocking_layers_model`, generates an architectural concept model inspired by the metaphor of "Interlocking Layers." It constructs a series of overlapping and intersecting planes, simulating dynamic movement and complexity inherent in the metaphor. By adjusting the width, depth, height, and offset of each layer, the function creates a textured facade that reflects the intricate silhouette described in the design task. The resulting 3D model emphasizes connectivity and autonomy, producing transitional spaces that foster interaction while allowing for distinct functional areas. This approach captures both the fluidity and complexity of the proposed architectural experience."""

#! python 3
function_code = """def create_interlocking_layers_model(base_width, base_depth, base_height, num_layers, layer_offset):
    \"""
    Generate an architectural Concept Model based on the 'Interlocking Layers' metaphor.
    
    The function creates a series of overlapping and intersecting planes that form a complex 
    and dynamic structure. Each layer is slightly offset to enhance the perception of 
    interlocking volumes.

    Parameters:
    - base_width (float): The width of the base layer in meters.
    - base_depth (float): The depth of the base layer in meters.
    - base_height (float): The height of the base layer in meters.
    - num_layers (int): The number of layers to create.
    - layer_offset (float): The offset distance in meters for each subsequent layer to create interlocking effect.

    Returns:
    - List of RhinoCommon Brep objects representing the interlocking layers.
    \"""
    
    import Rhino
    import Rhino.Geometry as rg
    
    breps = []
    random_seed = 42
    
    # Loop through each layer, creating and offsetting it
    for i in range(num_layers):
        # Calculate the dimensions for each layer
        current_width = base_width - (i * layer_offset * 0.5)
        current_depth = base_depth - (i * layer_offset * 0.5)
        current_height = base_height + (i * layer_offset)
        
        # Create a box for the current layer
        plane = rg.Plane.WorldXY
        base_point = rg.Point3d(-current_width/2, -current_depth/2, i * layer_offset * 0.5)
        box = rg.Box(plane, rg.Interval(base_point.X, base_point.X + current_width), 
                             rg.Interval(base_point.Y, base_point.Y + current_depth), 
                             rg.Interval(base_point.Z, base_point.Z + current_height))
        
        # Convert the box to a Brep
        brep = box.ToBrep()
        breps.append(brep)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(10.0, 5.0, 3.0, 4, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(8.0, 4.0, 2.0, 6, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(12.0, 6.0, 4.0, 5, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(15.0, 7.0, 5.0, 3, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(9.0, 4.5, 2.5, 7, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
