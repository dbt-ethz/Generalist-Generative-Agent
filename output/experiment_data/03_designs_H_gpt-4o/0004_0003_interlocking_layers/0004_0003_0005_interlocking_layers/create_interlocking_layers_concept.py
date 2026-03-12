# Created for 0004_0003_interlocking_layers.json

""" Summary:
The provided function, `create_interlocking_layers_concept`, translates the metaphor of "Interlocking Layers" into an architectural concept model by generating a series of overlapping volumes that create visual complexity and dynamic spatial relationships. It utilizes parameters like height variation and transparency to simulate the intricacies of interwoven layers, ensuring each layer maintains its individuality while contributing to the overall cohesion. The function iteratively creates layered geometries, adjusting their heights and transparency to reflect the metaphors essence. This approach results in a model that embodies both connectivity and distinct functional areas, promoting diverse spatial experiences through interlayer interactions."""

#! python 3
function_code = """def create_interlocking_layers_concept(base_width, base_depth, layer_count, max_layer_height, height_variation, transparency_variation, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Interlocking Layers' metaphor.
    
    This function creates a series of overlapping and interlocking volumes or planes that simulate dynamic movement
    and structural complexity. The design uses varying heights and transparency to emphasize the interconnectedness
    and individuality of each layer.

    Parameters:
    - base_width (float): The base width of the model footprint in meters.
    - base_depth (float): The base depth of the model footprint in meters.
    - layer_count (int): The number of interlocking layers to create.
    - max_layer_height (float): The maximum height for any individual layer in meters.
    - height_variation (float): The maximum height variation for layers in meters.
    - transparency_variation (float): The maximum transparency level for the layers (0.0 to 1.0).
    - seed (int): The seed for random number generation to ensure replicability.

    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometries of the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random

    # Ensure reproducibility
    random.seed(seed)

    geometries = []

    base_plane = rg.Plane.WorldXY
    current_height = 0

    for i in range(layer_count):
        # Randomly determine the height and transparency of each layer
        layer_height = random.uniform(max_layer_height - height_variation, max_layer_height)
        transparency = random.uniform(0.0, transparency_variation)

        # Create a box representing the layer
        box = rg.Box(base_plane, rg.Interval(0, base_width), rg.Interval(0, base_depth), rg.Interval(current_height, current_height + layer_height))
        brep = box.ToBrep()

        # Apply transparency as a user-defined attribute (not directly supported in RhinoCommon)
        # This is for conceptual purposes; Rhino display settings would be needed to visualize transparency
        brep.SetUserString("transparency", str(transparency))

        # Move the base plane for the next layer
        current_height += layer_height * 0.8  # Overlapping factor

        # Add the box to the list of geometries
        geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_concept(10.0, 5.0, 8, 3.0, 1.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_concept(15.0, 7.0, 10, 4.0, 2.0, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_concept(12.0, 6.0, 5, 2.5, 0.5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_concept(20.0, 10.0, 6, 5.0, 1.5, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_concept(8.0, 4.0, 12, 3.5, 1.0, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
