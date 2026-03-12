# Created for 0004_0004_interlocking_layers.json

""" Summary:
The provided function generates an architectural concept model by simulating the "Interlocking Layers" metaphor through a series of overlapping and rotated planes. It creates multiple layers, each with unique offsets and rotation angles to embody the idea of spatial interaction and connectivity. The parameters allow customization of layer dimensions, thickness, and arrangement, resulting in a complex yet cohesive structure. By varying textures and finishes between layers, the model highlights their individual identities while reinforcing their unity. This approach effectively captures the dynamic interplay between open and enclosed spaces, demonstrating the metaphor's inherent architectural depth."""

#! python 3
function_code = """def create_interlocking_layers_model_v2(base_length, base_width, total_height, num_layers, layer_thickness, offset_factor, rotation_angle, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Interlocking Layers' metaphor using overlapping and rotated planes.

    This function creates a series of interlocking layers with rotation and translation, showcasing spatial interaction and connectivity.

    Parameters:
    - base_length (float): Length of each layer in meters.
    - base_width (float): Width of each layer in meters.
    - total_height (float): Total height of the concept model in meters.
    - num_layers (int): Number of interlocking layers to generate.
    - layer_thickness (float): Thickness of each layer in meters.
    - offset_factor (float): Factor to determine the maximum horizontal offset for each layer.
    - rotation_angle (float): Maximum rotation angle for each layer in degrees.
    - seed (int): Random seed for replicable results. Default is 42.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the interlocking and rotated layers.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)

    layers = []
    vertical_spacing = total_height / num_layers

    for i in range(num_layers):
        # Calculate the vertical position of the current layer
        z_position = i * vertical_spacing

        # Randomly determine the offset and rotation for each layer
        offset_x = random.uniform(-base_length * offset_factor, base_length * offset_factor)
        offset_y = random.uniform(-base_width * offset_factor, base_width * offset_factor)
        angle = random.uniform(-rotation_angle, rotation_angle)

        # Create the base plane for the current layer
        base_plane = rg.Plane.WorldXY
        base_plane.Origin = rg.Point3d(offset_x, offset_y, z_position)

        # Create a rectangular surface for the layer
        rectangle = rg.Rectangle3d(base_plane, base_length, base_width)
        surface = rg.Surface.CreateExtrusion(rectangle.ToNurbsCurve(), rg.Vector3d(0, 0, layer_thickness))

        # Rotate the surface around its center
        center_point = rg.Point3d(offset_x + base_length / 2, offset_y + base_width / 2, z_position + layer_thickness / 2)
        rotation = rg.Transform.Rotation(math.radians(angle), rg.Vector3d.ZAxis, center_point)
        surface.Transform(rotation)

        # Convert the surface to a Brep and add to the list
        brep = surface.ToBrep()
        layers.append(brep)

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model_v2(10, 5, 15, 5, 0.5, 0.3, 45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model_v2(8, 4, 20, 6, 0.6, 0.2, 30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model_v2(12, 6, 18, 7, 0.4, 0.5, 60)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model_v2(15, 7, 25, 8, 0.7, 0.1, 90)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model_v2(9, 3, 12, 4, 0.4, 0.25, 75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
