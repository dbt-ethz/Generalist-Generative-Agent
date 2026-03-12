# Created for 0020_0003_stacked_forests.json

""" Summary:
The provided function, `generate_stacked_forests_concept`, creates a 3D architectural model inspired by the "Stacked forests" metaphor. It generates staggered and offset volumes, emulating the layered structure of a forest ecosystem. Each layer's height is incremented, while random offsets introduce variation, reflecting the organic complexity of tree strata. The function incorporates voids to represent clearings within each layer, enhancing spatial richness. Vertical and diagonal connections are implicitly suggested through the model's design, mirroring natural movement within a forest. Ultimately, this approach produces a dynamic silhouette that captures the essence of a forest canopy, embodying both stability and fluidity."""

#! python 3
function_code = """def generate_stacked_forests_concept(seed, base_size, height_step, layer_count, offset_variance, void_ratio):
    \"""
    Generates a 3D architectural concept model based on the 'Stacked forests' metaphor.
    
    Parameters:
    - seed (int): Seed for random number generation to ensure replicable randomness.
    - base_size (tuple): A tuple (width, depth) specifying the base dimensions of the structure in meters.
    - height_step (float): The vertical step between each layer in meters.
    - layer_count (int): The number of stacked layers to create.
    - offset_variance (float): Maximum offset for each layer in meters, introducing staggered positioning.
    - void_ratio (float): Ratio of the layer that should be voids, representing clearings.

    Returns:
    - List of Breps: A list of Brep geometries representing the stacked volumes.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the seed for randomness
    random.seed(seed)

    # Initialize a list to hold the geometries
    geometries = []

    # Base dimensions
    base_width, base_depth = base_size

    # Initialize the current base position
    current_x = 0
    current_y = 0

    # Iterate to create each layer
    for i in range(layer_count):
        # Calculate the offset for this layer
        offset_x = random.uniform(-offset_variance, offset_variance)
        offset_y = random.uniform(-offset_variance, offset_variance)

        # Calculate the dimensions of the voids
        void_width = base_width * void_ratio
        void_depth = base_depth * void_ratio

        # Create the main solid volume for the layer
        solid_volume = rg.Box(rg.Plane.WorldXY, rg.Interval(current_x + offset_x, current_x + offset_x + base_width),
                              rg.Interval(current_y + offset_y, current_y + offset_y + base_depth),
                              rg.Interval(i * height_step, (i + 1) * height_step)).ToBrep()

        # Add the solid volume to the geometries list
        geometries.append(solid_volume)

        # Create voids within the layer, representing clearings
        void_x = current_x + offset_x + random.uniform(0, base_width - void_width)
        void_y = current_y + offset_y + random.uniform(0, base_depth - void_depth)

        void_volume = rg.Box(rg.Plane.WorldXY, rg.Interval(void_x, void_x + void_width),
                             rg.Interval(void_y, void_y + void_depth),
                             rg.Interval(i * height_step, (i + 1) * height_step)).ToBrep()

        # Subtract void from the solid volume
        boolean_difference = rg.Brep.CreateBooleanDifference([solid_volume], [void_volume], 0.01)

        if boolean_difference:
            geometries.append(boolean_difference[0])

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_stacked_forests_concept(42, (10, 10), 3.0, 5, 2.0, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_stacked_forests_concept(7, (15, 15), 2.5, 4, 1.5, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_stacked_forests_concept(123, (20, 25), 4.0, 6, 3.0, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_stacked_forests_concept(99, (12, 8), 2.0, 3, 1.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_stacked_forests_concept(88, (18, 12), 5.0, 7, 1.0, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
