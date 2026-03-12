# Created for 0004_0002_interlocking_layers.json

""" Summary:
The provided function generates an architectural concept model based on the "Interlocking Layers" metaphor by creating a series of overlapping planes or volumes. It takes parameters such as dimensions, the number of layers, and transparency ratios to create a visually complex structure. The function incorporates randomness in positioning layers to enhance spatial variety and depth, while also allowing for transparent sections to represent dynamic interactions between layers. By focusing on the arrangement and connectivity of these layers, the model effectively showcases the metaphor's implications of spatial hierarchy, function distribution, and light interplay, resulting in a compelling architectural design."""

#! python 3
function_code = """def create_interlocking_layers(width, depth, height, num_layers, layer_thickness, transparency_ratio):
    \"""
    Generates an architectural Concept Model based on the 'Interlocking Layers' metaphor. The function creates a composition 
    of overlapping and interwoven planes or volumes, emphasizing depth and interaction between layers.

    Parameters:
    - width (float): The overall width of the model in meters.
    - depth (float): The overall depth of the model in meters.
    - height (float): The overall height of the model in meters.
    - num_layers (int): The number of interlocking layers.
    - layer_thickness (float): The thickness of each layer in meters.
    - transparency_ratio (float): A ratio between 0 and 1 indicating the proportion of transparent layers.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random

    # Seed for replicable randomness
    random.seed(42)

    # Calculate spacing between layers
    layer_spacing = height / num_layers
    geometries = []

    for i in range(num_layers):
        # Generate random offsets for each layer
        offset_x = random.uniform(-0.5, 0.5) * width * 0.2
        offset_y = random.uniform(-0.5, 0.5) * depth * 0.2
        offset_z = i * layer_spacing

        # Create a base box for each layer
        box_corners = [
            rg.Point3d(offset_x, offset_y, offset_z),
            rg.Point3d(offset_x + width, offset_y, offset_z),
            rg.Point3d(offset_x + width, offset_y + depth, offset_z),
            rg.Point3d(offset_x, offset_y + depth, offset_z),
            rg.Point3d(offset_x, offset_y, offset_z + layer_thickness),
            rg.Point3d(offset_x + width, offset_y, offset_z + layer_thickness),
            rg.Point3d(offset_x + width, offset_y + depth, offset_z + layer_thickness),
            rg.Point3d(offset_x, offset_y + depth, offset_z + layer_thickness)
        ]

        box = rg.Box(rg.BoundingBox(box_corners)).ToBrep()
        geometries.append(box)

        # Determine if the layer is transparent
        if random.random() < transparency_ratio:
            # Create voids or subtractions here to represent transparency
            void_box = rg.Box(rg.BoundingBox(
                rg.Point3d(offset_x + width * 0.1, offset_y + depth * 0.1, offset_z + layer_thickness * 0.1),
                rg.Point3d(offset_x + width * 0.9, offset_y + depth * 0.9, offset_z + layer_thickness * 0.9)
            )).ToBrep()

            # Subtract the void from the box
            boolean_difference = rg.Brep.CreateBooleanDifference([box], [void_box], 0.001)

            if boolean_difference:
                geometries.extend(boolean_difference)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers(10, 5, 15, 8, 0.2, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers(12, 6, 20, 10, 0.3, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers(15, 10, 25, 5, 0.15, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers(8, 4, 12, 6, 0.25, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers(14, 7, 18, 7, 0.1, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
