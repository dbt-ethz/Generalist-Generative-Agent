# Created for 0020_0003_stacked_forests.json

""" Summary:
The provided function generates a 3D architectural concept model inspired by the metaphor of "Stacked forests." It constructs a vertically tiered structure using staggered layers, simulating the layered complexity of a forest ecosystem. Each layer is defined by a specified base size, height, and random horizontal offsets, creating a sense of depth and hierarchy. Voids within the solid layers represent clearings in the forest, enhancing the organic quality of the design. The function ultimately returns a collection of geometries that embody the dynamic interplay of solid and void, reflecting the natural movement and spatial richness of a forest environment."""

#! python 3
function_code = """def generate_forest_stack_concept(base_size=(20, 20), num_layers=7, layer_height=3, stagger_range=3, void_size_ratio=0.2):
    \"""
    Generates a 3D architectural Concept Model inspired by the 'Stacked forests' metaphor.

    Parameters:
    - base_size (tuple): A tuple (width, depth) specifying the base dimensions of the lowest layer in meters.
    - num_layers (int): The number of layers to stack vertically.
    - layer_height (float): The height of each individual layer in meters.
    - stagger_range (float): The maximum value for staggering each layer horizontally in meters.
    - void_size_ratio (float): Ratio of each layer's size to be void, representing clearings.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set seed for reproducibility
    random.seed(42)

    geometries = []
    width, depth = base_size

    for i in range(num_layers):
        # Calculate the random stagger for each layer
        stagger_x = random.uniform(-stagger_range, stagger_range)
        stagger_y = random.uniform(-stagger_range, stagger_range)

        # Calculate new base position incorporating stagger
        base_origin = rg.Point3d(stagger_x, stagger_y, i * layer_height)

        # Create the bounding box for the layer
        layer_box = rg.Box(rg.Plane(base_origin, rg.Vector3d.ZAxis), 
                           rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, layer_height))
        brep_layer = layer_box.ToBrep()

        # Determine voids within the layer
        void_width = width * void_size_ratio
        void_depth = depth * void_size_ratio
        void_x = random.uniform(0, width - void_width)
        void_y = random.uniform(0, depth - void_depth)
        
        void_box = rg.Box(rg.Plane(base_origin, rg.Vector3d.ZAxis), 
                          rg.Interval(void_x, void_x + void_width), rg.Interval(void_y, void_y + void_depth), rg.Interval(0, layer_height))
        brep_void = void_box.ToBrep()

        # Subtract void from the solid layer
        final_layer_brep = rg.Brep.CreateBooleanDifference(brep_layer, brep_void, 0.001)

        if final_layer_brep:
            geometries.append(final_layer_brep[0])

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_forest_stack_concept(base_size=(30, 30), num_layers=5, layer_height=2.5, stagger_range=4, void_size_ratio=0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_forest_stack_concept(base_size=(25, 25), num_layers=10, layer_height=4, stagger_range=2, void_size_ratio=0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_forest_stack_concept(base_size=(40, 40), num_layers=8, layer_height=3.5, stagger_range=5, void_size_ratio=0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_forest_stack_concept(base_size=(15, 15), num_layers=6, layer_height=3, stagger_range=2, void_size_ratio=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_forest_stack_concept(base_size=(50, 50), num_layers=12, layer_height=2, stagger_range=6, void_size_ratio=0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
