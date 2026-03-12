# Created for 0004_0001_interlocking_layers.json

""" Summary:
The provided function, `create_interlocking_layers`, generates an architectural concept model based on the metaphor of "Interlocking Layers." It creates a series of overlapping, interconnected planes, each representing a layer of the structure. By taking parameters like width, depth, height, number of layers, and layer thickness, the function computes dimensions for each layer with some randomness to enhance the interlocking effect. This results in a model that emphasizes dynamic spatial relationships and visual complexity. The function outputs a list of 3D geometries, which can be utilized in design tasks to explore architectural possibilities inspired by the metaphor."""

#! python 3
function_code = """def create_interlocking_layers(width, depth, height, num_layers, layer_thickness):
    \"""
    Creates an architectural Concept Model based on the metaphor of "Interlocking Layers".
    
    The model is composed of overlapping and interconnected planes representing different layers of a structure.
    These layers create dynamic spatial relationships and visual depth, emphasizing structural and spatial complexity.

    Parameters:
    width (float): The total width of the model.
    depth (float): The total depth of the model.
    height (float): The total height of the model.
    num_layers (int): Number of interlocking layers to create.
    layer_thickness (float): Thickness of each layer.

    Returns:
    list: A list of 3D Brep geometries representing the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set random seed for replicability
    random.seed(42)

    layers = []
    offset = 0

    for i in range(num_layers):
        # Calculate layer dimensions with some randomness for interlocking effect
        layer_width = width * (0.8 + 0.4 * random.random())
        layer_depth = depth * (0.8 + 0.4 * random.random())
        layer_height = height / num_layers
        
        # Create a base plane for each layer
        base_plane = rg.Plane(rg.Point3d(offset, 0, i * layer_height), rg.Vector3d.ZAxis)

        # Create a box representing the layer
        layer_box = rg.Box(base_plane, rg.Interval(0, layer_width), rg.Interval(0, layer_depth), rg.Interval(0, layer_thickness))
        
        # Convert the box to a Brep and add to the list
        layers.append(layer_box.ToBrep())

        # Adjust offset for next layer to create interlocking effect
        offset += layer_width * 0.25

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers(10.0, 5.0, 15.0, 5, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers(8.0, 4.0, 12.0, 6, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers(15.0, 10.0, 20.0, 4, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers(12.0, 6.0, 18.0, 3, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers(20.0, 10.0, 30.0, 8, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
