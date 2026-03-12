# Created for 0004_0004_interlocking_layers.json

""" Summary:
The provided function, `create_interlocking_layers_concept`, generates an architectural concept model inspired by the metaphor of "Interlocking Layers." It constructs multiple overlapping volumes that reflect spatial interaction and connectivity, simulating the metaphor's essence. Each layer is placed at varying heights and oriented randomly, creating dynamic relationships and visual depth. The model emphasizes both separation and unity, showcasing distinct yet interconnected spaces. By manipulating parameters like layer thickness and dimensions, the function captures the complexity and fluidity of the architectural experience, aligning with the metaphor's focus on interwoven elements that enhance user journeys through the design."""

#! python 3
function_code = """def create_interlocking_layers_concept(length=15, width=10, total_height=8, num_layers=4, layer_thickness=0.6, randomness_seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Interlocking Layers' metaphor.
    
    This function creates a series of interlocking volumes that emphasize spatial interaction
    and connectivity. The layers are differentiated by their position and orientation, which
    showcases the balance between open and enclosed spaces, underlining the dynamic interplay
    of separation and unity in the design.

    Parameters:
    - length (float): The length of the model in meters.
    - width (float): The width of the model in meters.
    - total_height (float): The overall height of the model in meters.
    - num_layers (int): The number of interlocking layers to generate.
    - layer_thickness (float): The thickness of each layer in meters.
    - randomness_seed (int): Random seed for replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(randomness_seed)
    layers = []

    # Calculate vertical spacing
    vertical_spacing = total_height / (num_layers + 1)

    for i in range(num_layers):
        # Determine position and random rotation angle
        z_position = vertical_spacing * (i + 1)
        rotation_angle = random.uniform(-10, 10)  # Random rotation in degrees

        # Base plane for each layer
        base_plane = rg.Plane.WorldXY
        base_plane.OriginZ = z_position

        # Create an offset rectangle for each layer
        x_offset = random.uniform(-length * 0.1, length * 0.1)
        y_offset = random.uniform(-width * 0.1, width * 0.1)

        rectangle = rg.Rectangle3d(base_plane, length, width)
        rectangle.Transform(rg.Transform.Translation(x_offset, y_offset, 0))

        # Extrude rectangle to create layer volume
        extrusion_vector = rg.Vector3d(0, 0, layer_thickness)
        layer_brep = rg.Brep.CreateFromBox([rectangle.Corner(0), rectangle.Corner(1), rectangle.Corner(2), rectangle.Corner(3), extrusion_vector])

        # Apply rotation
        if layer_brep:
            center_point = rg.Point3d(x_offset + length/2, y_offset + width/2, z_position + layer_thickness / 2)
            rotation_transform = rg.Transform.Rotation(rg.Math.ToRadians(rotation_angle), rg.Vector3d.ZAxis, center_point)
            layer_brep.Transform(rotation_transform)
            layers.append(layer_brep)

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_concept(length=20, width=15, total_height=10, num_layers=5, layer_thickness=0.7, randomness_seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_concept(length=25, width=20, total_height=12, num_layers=6, layer_thickness=0.5, randomness_seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_concept(length=30, width=25, total_height=15, num_layers=3, layer_thickness=0.8, randomness_seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_concept(length=18, width=12, total_height=9, num_layers=4, layer_thickness=0.4, randomness_seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_concept(length=22, width=16, total_height=11, num_layers=5, layer_thickness=0.9, randomness_seed=33)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
