# Created for 0004_0003_interlocking_layers.json

""" Summary:
The function `create_interlocking_layers_concept` generates an architectural concept model by simulating the metaphor of "Interlocking Layers." It creates a series of overlapping volumes, each with randomized dimensions and heights, thereby embodying the complexity and dynamism suggested by the metaphor. By adjusting width and depth offsets for each layer, it emphasizes a textured facade and varied silhouette. The function also incorporates rotation to enhance the interlocking effect, promoting interaction between spaces. This results in a model that visually and spatially embodies connectivity and autonomy, as different layers serve both as separators and connectors within the architecture."""

#! python 3
function_code = """def create_interlocking_layers_concept(base_width, base_depth, num_layers, max_height, seed):
    \"""
    Generates an architectural Concept Model based on the 'Interlocking Layers' metaphor.
    
    The function creates a structure with volumes or planes that intricately weave and intersect,
    using varying heights and offsets to emulate layers folding over each other. This enhances the
    perception of dynamic movement and complexity, promoting spatial interaction and diversity.
    
    Parameters:
    - base_width (float): The width of the base layer in meters.
    - base_depth (float): The depth of the base layer in meters.
    - num_layers (int): The number of interlocking layers to create.
    - max_height (float): The maximum height of the entire structure in meters.
    - seed (int): Seed for random number generation to ensure replicability.
    
    Returns:
    - List of RhinoCommon Brep objects representing the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    # Set random seed for reproducibility
    random.seed(seed)
    
    # Create a list to store the resulting Breps
    breps = []
    
    # Define the base plane
    base_plane = rg.Plane.WorldXY

    # Calculate the height for each layer
    layer_height = max_height / num_layers
    
    for i in range(num_layers):
        # Randomize width and depth offset for each layer
        width_offset = random.uniform(-0.1, 0.1) * base_width
        depth_offset = random.uniform(-0.1, 0.1) * base_depth
        
        # Calculate current layer dimensions
        current_width = base_width + width_offset
        current_depth = base_depth + depth_offset
        
        # Define the height intervals for the current layer
        height_interval = rg.Interval(i * layer_height, (i + 1) * layer_height)
        
        # Create a box for the current layer
        layer_box = rg.Box(base_plane, rg.Interval(0, current_width), rg.Interval(0, current_depth), height_interval)
        
        # Optional rotation to enhance interlocking effect
        rotation_angle = random.uniform(-5, 5)  # degrees
        rotation_axis = rg.Vector3d(0, 0, 1)  # Z-axis
        rotation_center = rg.Point3d(current_width / 2, current_depth / 2, height_interval.Mid)
        rotation_transform = rg.Transform.Rotation(math.radians(rotation_angle), rotation_axis, rotation_center)
        layer_box.Transform(rotation_transform)
        
        # Convert to Brep and add to list
        breps.append(layer_box.ToBrep())
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_concept(10.0, 5.0, 4, 20.0, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_concept(15.0, 7.5, 6, 30.0, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_concept(8.0, 4.0, 5, 15.0, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_concept(12.0, 6.0, 3, 25.0, 100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_concept(20.0, 10.0, 8, 40.0, 56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
