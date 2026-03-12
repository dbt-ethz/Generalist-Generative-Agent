# Created for 0001_0005_house_within_a_house.json

""" Summary:
The provided function `create_concept_model` generates an architectural concept model reflecting the "House within a house" metaphor by creating a series of concentric, layered volumes. Each layer represents a transition from public to private spaces, with varying heights and materials that signify enclosure and intimacy. The central core acts as the inner sanctuary, while outer layers provide a protective shell, enhancing the sense of discovery as users navigate through the model. The function employs randomized height variations and subtractive geometry to articulate these layers, effectively embodying the metaphor's themes of nesting, retreat, and spatial hierarchy in a visual format."""

#! python 3
function_code = """def create_concept_model(core_radius, layer_count, layer_thickness, height_variation):
    \"""
    Creates an architectural Concept Model embodying the 'House within a house' metaphor. 
    The model is composed of concentric, layered volumes with varying heights and forms, 
    representing a transition from public to private spaces.

    Inputs:
        - core_radius: Radius of the central core volume (in meters).
        - layer_count: The number of concentric layers surrounding the core.
        - layer_thickness: The thickness of each concentric layer (in meters).
        - height_variation: A tuple (min_height, max_height) representing the range of height variation for the layers.

    Output:
        - A list of 3D geometries (Brep) representing the layers of the model.

    The function utilizes RhinoCommon to create the geometries.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a seed for randomness to ensure replicable results
    random.seed(42)
    
    geometries = []

    # Create the central core
    core_height = random.uniform(*height_variation)
    core = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, core_radius), core_height).ToBrep(True, True)
    geometries.append(core)

    # Create concentric layers around the core
    for i in range(1, layer_count + 1):
        # Calculate radius and height for the current layer
        radius = core_radius + i * layer_thickness
        height = random.uniform(*height_variation)

        # Create a cylindrical layer
        layer = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, radius), height).ToBrep(True, True)

        # Subtract the previous layer to create a shell effect
        if i == 1:
            layer_shell = rg.Brep.CreateBooleanDifference([layer], [core], 0.01)[0]
        else:
            inner_layer_radius = core_radius + (i - 1) * layer_thickness
            inner_layer_height = random.uniform(*height_variation)
            inner_layer = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, inner_layer_radius), inner_layer_height).ToBrep(True, True)
            layer_shell = rg.Brep.CreateBooleanDifference([layer], [inner_layer], 0.01)[0]

        geometries.append(layer_shell)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(5, 3, 2, (3, 10))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(4, 5, 1.5, (2, 8))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(6, 4, 3, (5, 12))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(7, 2, 2.5, (4, 9))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(3, 6, 1, (1, 5))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
