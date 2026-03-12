# Created for 0004_0003_interlocking_layers.json

""" Summary:
The function `create_interlocking_layers_concept` generates an architectural concept model reflecting the metaphor of "Interlocking Layers." It creates a 3D structure comprised of multiple overlapping layers, utilizing parameters like length, width, height, and number of layers to define the spatial arrangement. By randomly determining the position, size, and thickness of each layer, the function ensures a dynamic and complex interaction between the volumes. This approach embodies the metaphor's essence, promoting connectivity through transitional spaces while allowing for distinct functional areas. The result is a visually intricate model that captures the interplay of unity and individuality in architectural design."""

#! python 3
function_code = """def create_interlocking_layers_concept(length, width, height, num_layers, layer_thickness, seed):
    \"""
    Creates an architectural Concept Model based on the 'Interlocking Layers' metaphor.
    
    This function generates a structure where volumes or planes are intricately woven and intersected,
    using varying heights and depths to create a perception of layers folding over each other. 

    Parameters:
        length (float): The overall length of the concept model in meters.
        width (float): The overall width of the concept model in meters.
        height (float): The overall height of the concept model in meters.
        num_layers (int): The number of interlocking layers to create.
        layer_thickness (float): The thickness of each layer in meters.
        seed (int): Seed for random number generation to ensure replicability.

    Returns:
        List[Rhino.Geometry.Brep]: A list of Brep objects representing the generated 3D geometries.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    layers = []
    offset_x = length / num_layers
    offset_y = width / num_layers

    for i in range(num_layers):
        # Determine the position and size for each layer
        x_start = random.uniform(0, offset_x * i)
        y_start = random.uniform(0, offset_y * i)
        z_start = random.uniform(0, height * 0.2)
        
        x_end = x_start + random.uniform(offset_x * 0.5, offset_x * 1.5)
        y_end = y_start + random.uniform(offset_y * 0.5, offset_y * 1.5)
        z_end = z_start + layer_thickness
        
        # Ensure layers do not exceed the boundaries
        if x_end > length: x_end = length
        if y_end > width: y_end = width
        if z_end > height: z_end = height

        # Create a box for each layer
        base_point = rg.Point3d(x_start, y_start, z_start)
        layer_box = rg.Box(rg.Plane.WorldXY, rg.Interval(base_point.X, x_end), rg.Interval(base_point.Y, y_end), rg.Interval(base_point.Z, z_end))
        # Convert to Brep
        layer_brep = layer_box.ToBrep()
        
        layers.append(layer_brep)

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_concept(10.0, 5.0, 8.0, 6, 0.5, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_concept(15.0, 10.0, 12.0, 4, 0.3, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_concept(20.0, 15.0, 10.0, 5, 0.4, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_concept(12.0, 8.0, 6.0, 5, 0.2, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_concept(8.0, 6.0, 5.0, 3, 0.6, 27)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
