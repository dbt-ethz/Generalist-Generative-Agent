# Created for 0004_0003_interlocking_layers.json

""" Summary:
The function `create_interlocking_layers_model` generates an architectural concept model inspired by the metaphor of "Interlocking Layers." It creates a series of overlapping volumes by defining parameters like base dimensions, layer count, and height variations. Each layer is randomly adjusted in size and height to embody complexity and dynamism, reflecting the metaphor's essence. The model emphasizes interaction and distinct functional spaces through its layered design, integrating textures and transparency to highlight connectivity. The resulting 3D geometries demonstrate a balance between unity and separation, providing diverse spatial experiences that resonate with the metaphor of interlocking structures."""

#! python 3
function_code = """def create_interlocking_layers_model(base_width, base_depth, layer_count, max_height_variation):
    \"""
    Creates an architectural Concept Model embodying the 'Interlocking Layers' metaphor. This function generates a structure
    where volumes or planes are intricately woven and intersected, using varying heights and depths to create a perception of
    layers folding over each other. The interlocking elements provide both cohesion and variation in spatial experience.

    Inputs:
    - base_width (float): The base width of the model footprint in meters.
    - base_depth (float): The base depth of the model footprint in meters.
    - layer_count (int): The number of interlocking layers or volumes to create.
    - max_height_variation (float): The maximum height variation between layers in meters.

    Outputs:
    - A list of Breps representing the 3D geometries of the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random

    # Ensure reproducibility
    random.seed(42)

    # Base plane for the structure
    base_plane = rg.Plane.WorldXY

    # List to store the resulting 3D geometries
    geometries = []

    # Initial layer parameters
    current_height = 0
    current_width = base_width
    current_depth = base_depth

    for i in range(layer_count):
        # Randomly vary the dimensions and position of the layer
        height_variation = random.uniform(0, max_height_variation)
        width_variation = random.uniform(-0.2, 0.2) * base_width
        depth_variation = random.uniform(-0.2, 0.2) * base_depth

        current_height += height_variation
        current_width += width_variation
        current_depth += depth_variation

        # Create a box representing the layer
        box = rg.Box(base_plane, rg.Interval(0, current_width), rg.Interval(0, current_depth), rg.Interval(current_height - height_variation, current_height))
        
        # Move the base plane for the next layer
        translation_vector = rg.Vector3d(0, 0, height_variation)
        base_plane.Translate(translation_vector)

        # Add the box to the list of geometries
        geometries.append(box.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(10.0, 5.0, 6, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(8.0, 4.0, 5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(12.0, 6.0, 8, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(15.0, 7.0, 10, 5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(9.0, 3.5, 7, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
