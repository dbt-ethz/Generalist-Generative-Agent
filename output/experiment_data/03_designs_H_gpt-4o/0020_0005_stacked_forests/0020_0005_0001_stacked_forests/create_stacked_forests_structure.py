# Created for 0020_0005_stacked_forests.json

""" Summary:
The function `create_stacked_forests_structure` generates an architectural concept model based on the "Stacked forests" metaphor by creating a series of cascading terraces that reflect the vertical stratification of a forest ecosystem. Each layer represents a unique ecological level, designed with varying dimensions and heights to evoke a sense of depth and organic growth. The model emphasizes vertical integration, allowing light penetration and shadow play, akin to sunlight filtering through trees. By using randomized dimensions and overlaps, the function captures the dynamic, stepped silhouette reminiscent of a forest hillside, embodying the metaphor's essence through architectural form."""

#! python 3
function_code = """def create_stacked_forests_structure(base_size, num_layers, max_layer_height, randomness_seed=42):
    \"""
    Generates a 3D architectural concept model based on the 'Stacked forests' metaphor.

    This function creates a cascading sequence of terraces or ledges, each representing
    a unique ecological layer. The design focuses on vertical integration and a balance
    of enclosed and open spaces, mimicking the natural stratification of a forest.

    Parameters:
    - base_size (tuple of floats): The base dimensions (width, depth) of the building in meters.
    - num_layers (int): The number of cascading layers or terraces in the model.
    - max_layer_height (float): The maximum height per layer in meters.
    - randomness_seed (int): Seed for randomness to ensure replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set seed for randomness to ensure replicable results
    random.seed(randomness_seed)

    # Base dimensions
    base_width, base_depth = base_size

    # Initialize the list to store generated geometries
    concept_model = []

    # Current z height
    current_z = 0

    for i in range(num_layers):
        # Calculate width and depth reduction for cascading effect
        width_reduction = base_width * (0.1 * random.uniform(0.8, 1.2))
        depth_reduction = base_depth * (0.1 * random.uniform(0.8, 1.2))

        # Calculate layer dimensions
        layer_width = max(base_width - i * width_reduction, base_width * 0.5)
        layer_depth = max(base_depth - i * depth_reduction, base_depth * 0.5)
        layer_height = random.uniform(max_layer_height * 0.5, max_layer_height)

        # Create a base plane for the current layer
        base_plane = rg.Plane.WorldXY
        base_plane.Translate(rg.Vector3d(0, 0, current_z))

        # Create a box (Brep) for the current layer
        box = rg.Box(base_plane, rg.Interval(0, layer_width), rg.Interval(0, layer_depth), rg.Interval(0, layer_height))
        brep = box.ToBrep()
        concept_model.append(brep)

        # Update current z position for the next layer
        current_z += layer_height * 0.8  # Overlap for organic integration

    return concept_model"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_structure((10, 10), 5, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_structure((15, 20), 4, 2.5, randomness_seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_structure((8, 12), 6, 4, randomness_seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_structure((20, 15), 3, 5, randomness_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_structure((12, 8), 7, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
