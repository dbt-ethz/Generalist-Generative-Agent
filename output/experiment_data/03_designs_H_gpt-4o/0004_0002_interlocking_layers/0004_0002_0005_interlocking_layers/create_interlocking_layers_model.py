# Created for 0004_0002_interlocking_layers.json

""" Summary:
The provided function `create_interlocking_layers_model` generates an architectural concept model based on the "Interlocking Layers" metaphor by creating a series of overlapping and interwoven planes. It takes parameters for dimensions, layer count, and thickness, establishing a spatial hierarchy through calculated layer spacing and random rotation. Each layer is represented as a 3D geometry, promoting dynamic relationships among the volumes. The function emphasizes depth and connectivity, embodying the metaphor's intent to blend openness with separation. Ultimately, it produces a model showcasing intricate spatial organization, aligned with the design task of illustrating varied functions across interlocking layers."""

#! python 3
function_code = """def create_interlocking_layers_model(width, depth, height, num_layers, layer_thickness):
    \"""
    Generates an architectural Concept Model based on the 'Interlocking Layers' metaphor. The function creates a composition
    of overlapping and interwoven volumes that emphasize spatial hierarchy and dynamic spatial relationships.

    Parameters:
    - width (float): The overall width of the model in meters.
    - depth (float): The overall depth of the model in meters.
    - height (float): The overall height of the model in meters.
    - num_layers (int): The number of interlocking layers.
    - layer_thickness (float): The thickness of each layer in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Seed for replicable randomness
    random.seed(42)

    # Calculate spacing between layers
    layer_spacing = height / num_layers
    geometries = []

    for i in range(num_layers):
        # Random rotation angle for each layer
        rotation_angle = random.uniform(-math.pi / 6, math.pi / 6)  # Radians

        # Create a base rectangle for the layer
        base_rectangle = rg.Rectangle3d(rg.Plane.WorldXY, width, depth)

        # Move the base rectangle to the current layer height
        translate_transform = rg.Transform.Translation(0, 0, i * layer_spacing)
        base_rectangle.Transform(translate_transform)

        # Rotate the rectangle randomly around its center
        center = base_rectangle.Center
        rotation_transform = rg.Transform.Rotation(rotation_angle, rg.Vector3d.ZAxis, center)
        base_rectangle.Transform(rotation_transform)

        # Create a planar surface from the rectangle
        layer_surface = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(base_rectangle.ToNurbsCurve(), rg.Vector3d(0, 0, layer_thickness)))

        # Add the surface to the list of geometries
        geometries.append(layer_surface)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(10.0, 5.0, 15.0, 6, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(8.0, 4.0, 20.0, 5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(12.0, 6.0, 18.0, 8, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(15.0, 7.0, 25.0, 10, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(9.0, 3.0, 12.0, 7, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
