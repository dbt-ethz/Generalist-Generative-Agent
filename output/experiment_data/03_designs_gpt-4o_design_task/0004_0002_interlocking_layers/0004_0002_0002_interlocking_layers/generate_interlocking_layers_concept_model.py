# Created for 0004_0002_interlocking_layers.json

""" Summary:
The provided function, `generate_interlocking_layers_concept_model`, creates an architectural concept model based on the "Interlocking Layers" metaphor. It generates a series of overlapping planes or volumes, emphasizing a complex spatial hierarchy. By varying layer heights and incorporating both transparent and opaque materials, the model showcases intricate interactions between layers, reflecting the dynamic relationships described in the metaphor. The function allows for customization through parameters like base dimensions, height, layer count, and transparency ratio. This results in a visually engaging architecture that balances openness and separation, enhancing light and shadow interplay to deepen spatial complexity."""

#! python 3
function_code = """def generate_interlocking_layers_concept_model(base_length, base_width, height, layer_count, transparency_ratio):
    \"""
    Creates an architectural Concept Model representing the 'Interlocking Layers' metaphor. The model consists of overlapping and interwoven planes or volumes to establish a complex spatial hierarchy. It uses transparent and opaque materials to emphasize depth and interaction between layers.

    Parameters:
    - base_length (float): The base length of the model in meters.
    - base_width (float): The base width of the model in meters.
    - height (float): The maximum height of the model in meters.
    - layer_count (int): The number of interlocking layers to create.
    - transparency_ratio (float): A ratio between 0 and 1 indicating the proportion of transparent layers.

    Returns:
    List[Rhino.Geometry.Brep]: A list of 3D geometries representing the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random

    # Ensure replicable randomness
    random.seed(1)

    geometries = []

    # Define the base plane
    base_plane = rg.Plane.WorldXY

    # Calculate the spacing between layers
    layer_height = height / layer_count

    for i in range(layer_count):
        # Randomly decide if the layer is transparent
        is_transparent = random.random() < transparency_ratio

        # Create a bounding box for the layer
        x_offset = random.uniform(-0.2, 0.2) * base_length
        y_offset = random.uniform(-0.2, 0.2) * base_width
        z_offset = i * layer_height

        # Define corner points for the layer rectangle
        pt0 = rg.Point3d(x_offset, y_offset, z_offset)
        pt1 = rg.Point3d(base_length + x_offset, y_offset, z_offset)
        pt2 = rg.Point3d(base_length + x_offset, base_width + y_offset, z_offset)
        pt3 = rg.Point3d(x_offset, base_width + y_offset, z_offset)

        # Create a plane for the layer
        layer_plane = rg.Plane(base_plane)
        layer_plane.Origin = rg.Point3d(0, 0, z_offset)

        # Create a rectangle as the base of the layer
        rect_corners = [pt0, pt1, pt2, pt3]
        rect_curve = rg.Polyline(rect_corners + [pt0]).ToNurbsCurve()

        # Extrude the rectangle to create a volume for the layer
        extrusion_vector = rg.Vector3d(0, 0, layer_height * 0.5)
        extrusion = rg.Extrusion.Create(rect_curve, extrusion_vector.Length, True)

        # Convert extrusion to a Brep
        layer_brep = extrusion.ToBrep()

        # Add the layer to the list of geometries
        geometries.append(layer_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_interlocking_layers_concept_model(5.0, 3.0, 10.0, 6, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_interlocking_layers_concept_model(4.0, 2.5, 8.0, 5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_interlocking_layers_concept_model(6.0, 4.0, 12.0, 8, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_interlocking_layers_concept_model(7.0, 5.0, 15.0, 10, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_interlocking_layers_concept_model(3.5, 2.0, 9.0, 7, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
