# Created for 0020_0003_stacked_forests.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "Stacked forests." It constructs a vertically tiered structure using staggered volumes that mimic the layers of a forest ecosystem. Each layer varies in size, reflecting hierarchical relationships, while voids represent natural clearings. The function incorporates random branch-like protrusions to enhance the dynamic silhouette, simulating the organic growth of trees. Vertical circulation paths are implied through the structure's design, allowing fluid movement akin to traversing a forest. Overall, the model captures the interplay of solid and void, creating a rich spatial experience reflective of natural environments."""

#! python 3
function_code = """def create_stacked_forests_model(base_size=(10, 10), layer_count=7, height_step=3, void_spaces=0.2, branch_factor=0.5):
    \"""
    Generates a 3D architectural Concept Model based on the 'Stacked forests' metaphor.

    Parameters:
    - base_size (tuple): The base dimensions (width, depth) of the structure in meters.
    - layer_count (int): The number of vertical layers to stack, representing forest strata.
    - height_step (float): The vertical distance between each layer in meters.
    - void_spaces (float): Proportion of each layer that should consist of voids, representing clearings.
    - branch_factor (float): Degree of protruding elements, imitating branches, as a fraction of base size.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a seed for randomness to ensure replicability
    random.seed(42)

    # Initialize a list to store the resulting geometries
    geometries = []

    # Base dimensions
    base_width, base_depth = base_size

    # Iterate to create each layer
    for i in range(layer_count):
        # Calculate the size of the current layer
        layer_width = base_width * (1 - (i / layer_count) * branch_factor)
        layer_depth = base_depth * (1 - (i / layer_count) * branch_factor)

        # Create the main volume for the layer
        solid_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, layer_width), rg.Interval(0, layer_depth), rg.Interval(i * height_step, (i + 1) * height_step))
        solid_brep = solid_box.ToBrep()
        
        # Create voids within the layer, representing clearings
        void_width = layer_width * void_spaces
        void_depth = layer_depth * void_spaces
        void_x = random.uniform(0, layer_width - void_width)
        void_y = random.uniform(0, layer_depth - void_depth)

        void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(void_x, void_x + void_width), rg.Interval(void_y, void_y + void_depth), rg.Interval(i * height_step, (i + 1) * height_step))
        void_brep = void_box.ToBrep()

        # Subtract void from the solid volume
        layer_brep = rg.Brep.CreateBooleanDifference(solid_brep, void_brep, 0.01)
        if layer_brep:
            geometries.append(layer_brep[0])

        # Add protruding branches to create a more dynamic silhouette
        if i < layer_count - 1:
            for _ in range(random.randint(1, 3)):  # Random number of branches
                branch_length = random.uniform(0.1, branch_factor * base_width)
                branch_width = random.uniform(0.1, branch_factor * base_depth)
                branch_x = random.uniform(0, layer_width - branch_width)
                branch_y = random.uniform(0, layer_depth - branch_length)
                branch_z = (i + 1) * height_step

                branch_box = rg.Box(rg.Plane.WorldXY, rg.Interval(branch_x, branch_x + branch_width), rg.Interval(branch_y, branch_y + branch_length), rg.Interval(branch_z, branch_z + height_step / 2))
                branch_brep = branch_box.ToBrep()
                geometries.append(branch_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_model(base_size=(15, 15), layer_count=5, height_step=2, void_spaces=0.3, branch_factor=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_model(base_size=(12, 12), layer_count=10, height_step=4, void_spaces=0.1, branch_factor=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_model(base_size=(8, 8), layer_count=6, height_step=2.5, void_spaces=0.25, branch_factor=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_model(base_size=(20, 10), layer_count=8, height_step=3.5, void_spaces=0.15, branch_factor=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_model(base_size=(10, 20), layer_count=4, height_step=5, void_spaces=0.1, branch_factor=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
