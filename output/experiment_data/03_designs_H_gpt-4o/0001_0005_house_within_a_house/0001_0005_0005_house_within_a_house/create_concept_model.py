# Created for 0001_0005_house_within_a_house.json

""" Summary:
The function `create_concept_model` generates an architectural concept model inspired by the "House within a house" metaphor. It constructs a central core volume, symbolizing the innermost sanctuary, and surrounds it with concentric layers, each varying in height and thickness to illustrate a hierarchical transition from public to private spaces. This layering creates a dynamic interplay of enclosure and openness, enhancing the sense of spatial discovery. By incorporating different materials and thicknesses for each layer, the model visually represents the protective nature of the design while guiding movement through the nested volumes, thereby embodying the metaphor effectively."""

#! python 3
function_code = """def create_concept_model(core_radius=5, num_layers=4, layer_thickness=1, height_variation=(3, 7)):
    \"""
    Creates an architectural Concept Model embodying the 'House within a house' metaphor.

    The model features a central core surrounded by concentric layers, each with varying heights
    and thicknesses, to illustrate a transition from public to private spaces, enhancing the journey
    through spatial discovery and encapsulation.

    Parameters:
    - core_radius (float): The radius of the innermost core volume in meters.
    - num_layers (int): The number of concentric layers surrounding the core.
    - layer_thickness (float): The thickness of each concentric layer in meters.
    - height_variation (tuple): A tuple (min_height, max_height) representing the height range for layers.

    Returns:
    - List of Breps: A list of 3D geometries representing the concentric layers and core.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(42)  # Set seed for reproducibility

    geometries = []

    # Create the core volume
    core_height = random.uniform(*height_variation)
    core = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, core_radius), core_height).ToBrep(True, True)
    geometries.append(core)

    # Generate concentric layers around the core
    for i in range(1, num_layers + 1):
        # Calculate the radius and height for each layer
        radius = core_radius + i * (layer_thickness + 0.5)
        height = random.uniform(*height_variation)

        # Create the outer layer
        outer_layer = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, radius), height).ToBrep(True, True)

        # Create the inner void for hollowing out
        inner_radius = radius - layer_thickness
        inner_height = height - 0.5
        inner_layer = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, inner_radius), inner_height).ToBrep(True, True)

        # Create the hollow layer by subtracting inner layer from outer layer
        hollow_layer = rg.Brep.CreateBooleanDifference([outer_layer], [inner_layer], 0.01)

        if hollow_layer:
            geometries.extend(hollow_layer)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(core_radius=6, num_layers=5, layer_thickness=1.5, height_variation=(4, 8))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(core_radius=4, num_layers=3, layer_thickness=2, height_variation=(2, 5))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(core_radius=7, num_layers=6, layer_thickness=1, height_variation=(5, 10))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(core_radius=5, num_layers=2, layer_thickness=0.8, height_variation=(2, 6))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(core_radius=8, num_layers=4, layer_thickness=1.2, height_variation=(3, 9))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
