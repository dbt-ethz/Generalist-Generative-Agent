# Created for 0020_0001_stacked_forests.json

""" Summary:
The provided function, `create_stacked_forests_concept`, generates an architectural concept model inspired by the metaphor of "Stacked Forests." It creates a multi-layered, vertical structure that mimics the density and hierarchy of a natural forest. By using parameters for layer heights, base radius, and randomness, it produces varying cylindrical layers that represent tree canopies. Each layer's radius incorporates organic growth variations, while vertical "trunks" enhance connectivity, mirroring natural ecosystems. The function outputs 3D geometries that embody the metaphors principles, allowing for rich spatial experiences and diverse interactions within the architectural model."""

#! python 3
function_code = """def create_stacked_forests_concept(height_layers, base_radius, num_layers, randomness_seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Stacked Forests' metaphor.
    
    This function generates a multi-layered, vertical organization resembling a dense, tiered forest.
    The design emphasizes hierarchy, depth, and organic growth, integrating natural elements 
    and creating spatial richness with varied levels of interaction. The structure embodies vertical 
    connectivity, offering a diverse range of experiences and pathways.

    Inputs:
    - height_layers: A list of floats representing the height of each layer in meters.
    - base_radius: A float representing the base radius of the layers.
    - num_layers: An integer representing the number of layers in the model.
    - randomness_seed: An integer seed for randomness to ensure replicability of results.

    Outputs:
    - A list of RhinoCommon Breps representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the seed for replicable randomness
    random.seed(randomness_seed)

    geometries = []

    # Create each layer
    for i in range(num_layers):
        # Determine the center of each layer based on its index
        center = rg.Point3d(0, 0, sum(height_layers[:i + 1]))

        # Calculate a random variation for the radius to mimic organic growth
        radius_variation = random.uniform(-0.2, 0.2) * base_radius
        layer_radius = base_radius + radius_variation

        # Create a cylindrical layer with random radius variation
        cylinder = rg.Cylinder(rg.Circle(center, layer_radius), height_layers[i]).ToBrep(True, True)
        geometries.append(cylinder)

        # Add vertical connectivity elements (like trunks in a forest)
        trunk_radius = base_radius * 0.1
        trunk = rg.Cylinder(rg.Circle(center, trunk_radius), height_layers[i]).ToBrep(True, True)
        geometries.append(trunk)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept([3.0, 4.0, 5.0], 2.0, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept([2.5, 3.5, 4.5, 5.5], 1.5, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept([1.0, 2.0, 1.5], 2.5, 3, randomness_seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept([2.0, 2.5, 3.0, 3.5], 1.0, 4, randomness_seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept([4.0, 3.0, 2.0, 1.0], 1.0, 4, randomness_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
