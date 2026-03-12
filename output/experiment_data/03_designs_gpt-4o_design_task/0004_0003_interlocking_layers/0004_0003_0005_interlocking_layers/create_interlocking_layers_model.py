# Created for 0004_0003_interlocking_layers.json

""" Summary:
The function `create_interlocking_layers_model` generates an architectural concept model based on the metaphor of "Interlocking Layers." It constructs a 3D representation where various layers overlap and intertwine, enhancing dynamic movement and spatial complexity. By adjusting the dimensions and positions of each layer, the function reflects the metaphor's essence, creating a visually intricate facade that emphasizes connectivity and individuality. The use of varying heights and depths, along with different materials, highlights the interrelations between spaces, allowing for interactive hubs and secluded areas. This approach captures the balance between unity and distinction within the architectural design."""

#! python 3
function_code = """def create_interlocking_layers_model(base_width, base_depth, base_height, num_layers, layer_variation):
    \"""
    Creates a 3D architectural concept model based on the 'Interlocking Layers' metaphor.
    
    This function generates a building form where volumes or planes overlap and intertwine, 
    reflecting a sense of dynamic movement and complexity. The layers vary in height and depth 
    to create the perception of interlocking elements, using different materials to highlight 
    their interconnectedness and individuality.

    Parameters:
    - base_width (float): The width of the base structure in meters.
    - base_depth (float): The depth of the base structure in meters.
    - base_height (float): The height of the base structure in meters.
    - num_layers (int): The number of interlocking layers to generate.
    - layer_variation (float): The maximum variation in size for each layer in meters.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the model.
    \"""
    
    import Rhino.Geometry as rg
    import random
    
    # Set a seed for reproducibility
    random.seed(42)
    
    # Base geometry
    base = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_width), rg.Interval(0, base_depth), rg.Interval(0, base_height))
    breps = [base.ToBrep()]
    
    # Create interlocking layers
    for i in range(num_layers):
        # Randomize dimensions for variation
        width_variation = random.uniform(-layer_variation, layer_variation)
        depth_variation = random.uniform(-layer_variation, layer_variation)
        height_variation = random.uniform(-layer_variation, layer_variation)
        
        # Create layer box
        layer_width = base_width + width_variation
        layer_depth = base_depth + depth_variation
        layer_height = base_height / num_layers + height_variation
        
        layer_box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(0, layer_width),
            rg.Interval(0, layer_depth),
            rg.Interval(i * (base_height / num_layers), (i + 1) * (base_height / num_layers) + height_variation)
        )
        
        # Offset the plane for layering effect
        offset_x = random.uniform(-layer_variation, layer_variation)
        offset_y = random.uniform(-layer_variation, layer_variation)
        move_vector = rg.Vector3d(offset_x, offset_y, 0)
        
        # Move the layer
        layer_box.Transform(rg.Transform.Translation(move_vector))
        
        # Convert to Brep and add to list
        breps.append(layer_box.ToBrep())
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(10.0, 15.0, 30.0, 5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(12.0, 18.0, 25.0, 4, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(8.0, 10.0, 20.0, 6, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(5.0, 7.0, 15.0, 3, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(20.0, 25.0, 40.0, 7, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
