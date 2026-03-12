# Created for 0020_0001_stacked_forests.json

""" Summary:
The function `create_stacked_forests_model` generates an architectural concept model inspired by the "Stacked forests" metaphor. It constructs multiple layers, each resembling forest strata, by creating rectangular bases that vary in size and height. Each layer is positioned at different heights, and random rotations are applied to mimic organic growth. This vertical layering emphasizes connectivity, akin to moving through a forest, and allows for unique spatial interactions. The design incorporates parameters such as base dimensions, layer count, and height variation, resulting in a dynamic structure that reflects the metaphors themes of hierarchy, depth, and organic form."""

#! python 3
function_code = """def create_stacked_forests_model(base_size, num_layers, layer_height_var, max_rotation, seed=42):
    \"""
    Generates a series of geometries representing an architectural Concept Model based on the 'Stacked forests' metaphor.
    
    Parameters:
    - base_size: tuple of two floats (width, depth) in meters, representing the base dimensions of the structure.
    - num_layers: integer, the number of layers or "forest strata" to create.
    - layer_height_var: float, the maximum variation in height between layers in meters.
    - max_rotation: float, maximum rotation in degrees allowed for each layer.
    - seed: integer, a seed for the random number generator to ensure replicability.

    Returns:
    - List of RhinoCommon Brep objects representing the layers of the structure.
    \"""
    import Rhino.Geometry as rg
    import math
    import random
    random.seed(seed)

    layers = []
    current_height = 0

    for i in range(num_layers):
        # Create base rectangle for the layer
        width_variation = random.uniform(0.8, 1.2)
        depth_variation = random.uniform(0.8, 1.2)
        width = base_size[0] * width_variation
        depth = base_size[1] * depth_variation

        # Create a 2D rectangle and move it to current height
        rect = rg.Rectangle3d(rg.Plane.WorldXY, width, depth)
        layer_height = random.uniform(3, 3 + layer_height_var)
        rect.Transform(rg.Transform.Translation(0, 0, current_height))

        # Apply random rotation
        rotation_angle = random.uniform(-max_rotation, max_rotation)
        center = rect.Center
        rotation = rg.Transform.Rotation(math.radians(rotation_angle), rg.Point3d(center.X, center.Y, current_height))
        rect.Transform(rotation)

        # Create a 3D Brep from the rectangle
        brep = rg.Brep.CreateFromCornerPoints(rect.Corner(0), rect.Corner(1), rect.Corner(2), rect.Corner(3), 0.01)
        if brep is not None:
            layers.append(brep)

        # Increment height for next layer
        current_height += layer_height

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_model((10, 10), 5, 2, 30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_model((8, 12), 7, 1.5, 45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_model((15, 15), 4, 3, 60)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_model((12, 8), 6, 2.5, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_model((5, 20), 3, 2, 25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
