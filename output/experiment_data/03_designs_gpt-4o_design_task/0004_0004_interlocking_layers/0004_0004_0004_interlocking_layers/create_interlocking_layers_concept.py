# Created for 0004_0004_interlocking_layers.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "Interlocking Layers" by creating a series of overlapping planes or volumes that embody spatial interaction and connectivity. It uses randomization to determine the orientation, positioning, and thickness of each layer, enabling a complex yet cohesive massing that reflects the metaphor's essence. The function ensures distinct yet interconnected spaces, balancing openness with privacy. By manipulating the arrangement and characteristics of the layers, the model emphasizes the dynamic relationships among spaces, illustrating how they can provide both separation and unity, thereby capturing the metaphor's intricate spatial complexity."""

#! python 3
function_code = """def create_interlocking_layers_concept(width, depth, height, num_layers, layer_thickness, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Interlocking Layers' metaphor.
    
    This function creates a series of interlocking planes or volumes that illustrate spatial interaction 
    and connectivity. Each layer is differentiated by its orientation and position, reflecting the interplay 
    between open and enclosed spaces, and showcasing the balance between separation and unity.

    Parameters:
    - width (float): The total width of the concept model in meters.
    - depth (float): The total depth of the concept model in meters.
    - height (float): The total height of the concept model in meters.
    - num_layers (int): The number of interlocking layers to generate.
    - layer_thickness (float): The thickness of each layer in meters.
    - seed (int): Random seed for replicable results. Default is 42.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the interlocking layers.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Brep, Box, Plane, Point3d, Vector3d, Interval

    random.seed(seed)
    
    # Calculate the spacing between layers
    spacing = height / (num_layers + 1)

    # Initialize list to hold Brep geometries
    layers = []

    for i in range(num_layers):
        # Randomly choose orientation and position for each layer
        orientation = random.choice(['horizontal', 'vertical'])
        x_offset = random.uniform(-width / 4, width / 4)
        y_offset = random.uniform(-depth / 4, depth / 4)
        z_position = spacing * (i + 1)
        
        # Create the base rectangle for the layer
        if orientation == 'horizontal':
            base_plane = Plane(Point3d(x_offset, y_offset, z_position), Vector3d.ZAxis)
            x_interval = Interval(0, width)
            y_interval = Interval(0, depth)
            z_interval = Interval(0, layer_thickness)
            layer_box = Box(base_plane, x_interval, y_interval, z_interval)
        else:
            base_plane = Plane(Point3d(x_offset, y_offset, z_position), Vector3d.YAxis)
            x_interval = Interval(0, width)
            y_interval = Interval(0, layer_thickness)
            z_interval = Interval(0, depth)
            layer_box = Box(base_plane, x_interval, y_interval, z_interval)
        
        # Convert Box to Brep and add to list
        layer_brep = layer_box.ToBrep()
        layers.append(layer_brep)

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_concept(10.0, 5.0, 15.0, 4, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_concept(12.0, 8.0, 20.0, 6, 0.3, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_concept(15.0, 10.0, 25.0, 5, 0.4, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_concept(8.0, 6.0, 10.0, 3, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_concept(20.0, 15.0, 30.0, 5, 0.6, seed=200)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
