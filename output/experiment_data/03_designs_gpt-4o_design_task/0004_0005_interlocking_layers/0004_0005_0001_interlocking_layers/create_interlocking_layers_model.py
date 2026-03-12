# Created for 0004_0005_interlocking_layers.json

""" Summary:
The provided function generates an architectural concept model based on the "Interlocking Layers" metaphor by creating multiple overlapping layers that reflect its complexity and spatial dynamics. Parameters such as base dimensions, height, and layer thickness guide the model's overall structure. Each layer is created with random offsets to enhance the interlocking effect, resulting in a visually intricate design. The function constructs 3D geometries using Rhino's geometry library, allowing for variations in material and texture to convey distinct spatial experiences. This method emphasizes the balance between openness and privacy, aligning with the metaphor's essence of interconnected yet distinct spaces."""

#! python 3
function_code = """def create_interlocking_layers_model(base_length, base_width, height, num_layers, layer_thickness, random_seed=42):
    \"""
    Creates an architectural Concept Model based on the "Interlocking Layers" metaphor.
    
    Parameters:
    base_length (float): The length of the base of the model in meters.
    base_width (float): The width of the base of the model in meters.
    height (float): The maximum height of the model in meters.
    num_layers (int): The number of interlocking layers to be created.
    layer_thickness (float): The thickness of each layer in meters.
    random_seed (int): Seed for the random number generator to ensure replicability (default is 42).
    
    Returns:
    List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Point3d, Vector3d, Plane, Box, Interval
    
    # Set the random seed for reproducibility
    random.seed(random_seed)
    
    # Initialize the list to hold the geometry
    geometries = []
    
    # Calculate the step height between the layers
    step_height = height / num_layers
    
    # Create the interlocking layers
    for i in range(num_layers):
        # Random offsets for dynamic interlocking effect
        offset_x = random.uniform(-base_length * 0.1, base_length * 0.1)
        offset_y = random.uniform(-base_width * 0.1, base_width * 0.1)
        
        # Create a base plane for the layer
        base_plane = Plane(Point3d(offset_x, offset_y, i * step_height), Vector3d.ZAxis)
        
        # Create intervals for the box dimensions
        x_interval = Interval(-base_length / 2, base_length / 2)
        y_interval = Interval(-base_width / 2, base_width / 2)
        z_interval = Interval(0, layer_thickness)
        
        # Create a box for the layer
        layer_box = Box(base_plane, x_interval, y_interval, z_interval)
        
        # Convert the box to a Brep
        layer_brep = layer_box.ToBrep()
        
        # Add the Brep to the list of geometries
        geometries.append(layer_brep)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(5.0, 3.0, 10.0, 6, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(4.0, 2.5, 8.0, 5, 0.4, random_seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(6.0, 4.0, 12.0, 8, 0.6, random_seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(7.0, 5.0, 15.0, 10, 0.7, random_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(3.0, 2.0, 7.0, 4, 0.3, random_seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
