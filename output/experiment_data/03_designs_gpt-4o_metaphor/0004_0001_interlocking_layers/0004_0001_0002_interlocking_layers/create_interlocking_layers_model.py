# Created for 0004_0001_interlocking_layers.json

""" Summary:
The provided function, `create_interlocking_layers_model`, generates an architectural concept model based on the metaphor of 'Interlocking Layers'. It creates multiple overlapping planes or volumes, reflecting the metaphor's emphasis on dynamic spatial relationships and structural complexity. The function accepts parameters such as base dimensions, number of layers, and layer thickness, allowing for customized outputs. By randomly orienting each layer as either vertical or horizontal, the design achieves visual depth and interaction among layers, thus fulfilling the design task of creating a space that balances openness and separation while enhancing functional variety and user experience."""

#! python 3
function_code = """def create_interlocking_layers_model(base_length, base_width, base_height, num_layers, layer_thickness, seed):
    \"""
    Creates an architectural Concept Model based on the metaphor of 'Interlocking Layers'.
    
    This function generates a series of interlocking planes or volumes to create a dynamic spatial
    arrangement that allows for openness and separation within the architecture. The design aims 
    to emphasize structural and spatial complexity through the interaction of different layers.

    Parameters:
    - base_length (float): The length of the base volume.
    - base_width (float): The width of the base volume.
    - base_height (float): The height of the base volume.
    - num_layers (int): The number of interlocking layers to be created.
    - layer_thickness (float): The thickness of each layer.
    - seed (int): Seed for random number generator to ensure replicable randomness.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(seed)

    geometries = []

    # Base volume to define the area where layers will interlock
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    
    # Calculate step intervals
    step_x = base_length / num_layers
    step_y = base_width / num_layers
    step_z = base_height / num_layers

    for i in range(num_layers):
        # Randomly decide if the layer will be vertical or horizontal
        if random.choice([True, False]):
            # Create a vertical interlocking layer
            plane = rg.Plane(rg.Point3d(i * step_x, 0, 0), rg.Vector3d.ZAxis, rg.Vector3d.YAxis)
            width_range = rg.Interval(0, base_width)
            height_range = rg.Interval(0, random.uniform(0.5, 1.0) * base_height)
        else:
            # Create a horizontal interlocking layer
            plane = rg.Plane(rg.Point3d(0, i * step_y, 0), rg.Vector3d.YAxis, rg.Vector3d.XAxis)
            width_range = rg.Interval(0, base_length)
            height_range = rg.Interval(0, random.uniform(0.5, 1.0) * base_height)

        # Create the layer as a Box
        layer_box = rg.Box(plane, width_range, rg.Interval(0, layer_thickness), height_range)
        brep = layer_box.ToBrep()
        
        # Add the Brep to the list of geometries
        geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(10.0, 5.0, 15.0, 8, 0.2, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(12.0, 6.0, 18.0, 10, 0.3, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(8.0, 4.0, 12.0, 6, 0.25, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(15.0, 7.0, 20.0, 5, 0.15, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(20.0, 10.0, 25.0, 12, 0.5, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
