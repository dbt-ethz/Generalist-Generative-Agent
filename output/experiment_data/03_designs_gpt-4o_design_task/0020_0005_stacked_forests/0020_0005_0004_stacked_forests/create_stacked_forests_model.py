# Created for 0020_0005_stacked_forests.json

""" Summary:
The function `create_stacked_forests_model` generates an architectural concept model inspired by the metaphor of "Stacked forests." It creates a series of cascading terraces that represent different ecological layers of a forest, emphasizing vertical integration. Each layer is designed with varying thickness and proportions, allowing light to penetrate and create dynamic shadow play. The model incorporates randomness in width, depth, and rotation, mimicking the organic growth patterns of natural forests. By focusing on a stepped silhouette, the function visually captures the essence of a cascading forest, enhancing spatial richness and connectivity reminiscent of a natural ecosystem."""

#! python 3
function_code = """def create_stacked_forests_model(base_width, base_depth, num_layers, max_height, min_layer_thickness, max_layer_thickness):
    \"""
    Generates a conceptual architectural model based on the 'Stacked forests' metaphor. The model consists of a series of cascading terraces or ledges that represent different ecological layers, with vertical integration allowing for light penetration and shadow play.

    Parameters:
    - base_width (float): The width of the base layer in meters.
    - base_depth (float): The depth of the base layer in meters.
    - num_layers (int): The number of layers (terraces) to create.
    - max_height (float): The maximum height of the entire structure in meters.
    - min_layer_thickness (float): The minimum thickness of each layer in meters.
    - max_layer_thickness (float): The maximum thickness of each layer in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the terraces.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a random seed for reproducibility
    random.seed(42)

    # Calculate the total height available for layers
    total_height = 0
    layers = []

    # Create each layer with varying thickness and proportions
    for i in range(num_layers):
        # Calculate layer thickness randomly within the specified range
        layer_thickness = random.uniform(min_layer_thickness, max_layer_thickness)
        
        # Ensure the total height doesn't exceed the maximum height
        if total_height + layer_thickness > max_height:
            break
        
        # Define the width and depth for this layer
        width = base_width * (0.8 + 0.2 * random.random())
        depth = base_depth * (0.8 + 0.2 * random.random())
        
        # Create a base rectangle for the layer
        base_rect = rg.Rectangle3d(rg.Plane.WorldXY, width, depth)
        
        # Extrude the rectangle to create a layer
        extrusion_vector = rg.Vector3d(0, 0, layer_thickness)
        layer_brep = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(base_rect.ToNurbsCurve(), extrusion_vector))
        
        # Transform the layer to cascade it (translate and rotate)
        translation_vector = rg.Vector3d(random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), total_height)
        translation = rg.Transform.Translation(translation_vector)
        
        rotation_angle = random.uniform(-0.1, 0.1)  # Small rotation for organic feel
        rotation = rg.Transform.Rotation(rotation_angle, rg.Vector3d(0, 0, 1), rg.Point3d(0, 0, total_height))
        
        # Apply transformations
        layer_brep.Transform(translation)
        layer_brep.Transform(rotation)
        
        # Add to list of layers
        layers.append(layer_brep)
        
        # Update total height
        total_height += layer_thickness

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_model(10.0, 5.0, 8, 30.0, 1.0, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_model(12.0, 6.0, 5, 25.0, 2.0, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_model(15.0, 7.0, 10, 35.0, 1.5, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_model(9.0, 4.0, 6, 20.0, 1.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_model(8.0, 3.0, 7, 28.0, 0.5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
