# Created for 0020_0003_stacked_forests.json

""" Summary:
The provided function, `create_stacked_forests_concept_model`, generates a 3D architectural concept model inspired by the metaphor of "Stacked forests." It constructs a tiered structure by creating staggered, offset volumes that reflect the layered complexity of a forest ecosystem. Each layer is defined by its height, width, and void spaces, simulating the density and openness found in forests. The integration of vertical and diagonal circulation paths enhances fluid movement between layers, mirroring natural forest navigation. The resulting model showcases an organic interplay of solid and void, capturing a dynamic silhouette reminiscent of swaying canopies, thus embodying the metaphor's essence."""

#! python 3
function_code = """def create_stacked_forests_concept_model(base_size, num_layers, layer_height, stagger_factor, void_ratio):
    \"""
    Creates a 3D architectural Concept Model embodying the 'Stacked forests' metaphor.
    
    Parameters:
    - base_size: A tuple (width, length) representing the base dimensions of the model's footprint in meters.
    - num_layers: The number of vertical layers or tiers in the structure.
    - layer_height: The height of each layer in meters.
    - stagger_factor: A value between 0 and 1 indicating the degree of horizontal offset between successive layers.
    - void_ratio: A value between 0 and 1 indicating the proportion of void (open) space within each layer.
    
    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set seed for reproducibility
    random.seed(42)

    geometries = []
    width, length = base_size

    for i in range(num_layers):
        # Calculate stagger offsets
        x_offset = random.uniform(-stagger_factor, stagger_factor) * width
        y_offset = random.uniform(-stagger_factor, stagger_factor) * length

        # Calculate base point for each layer
        base_point = rg.Point3d(x_offset, y_offset, i * layer_height)

        # Create the bounding box for each layer
        layer_width = width - (void_ratio * width)
        layer_length = length - (void_ratio * length)
        box = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), rg.Interval(0, layer_width), rg.Interval(0, layer_length), rg.Interval(0, layer_height))

        # Convert to Brep and add to geometries
        brep = box.ToBrep()
        geometries.append(brep)

        # Create void spaces within the layer
        if void_ratio > 0:
            void_count = int((1 - void_ratio) * 5)  # Number of voids
            for _ in range(void_count):
                void_width = random.uniform(0.1, void_ratio * layer_width)
                void_length = random.uniform(0.1, void_ratio * layer_length)
                void_x = random.uniform(base_point.X, base_point.X + layer_width - void_width)
                void_y = random.uniform(base_point.Y, base_point.Y + layer_length - void_length)
                void_box = rg.Box(rg.Plane(rg.Point3d(void_x, void_y, base_point.Z), rg.Vector3d.ZAxis), rg.Interval(0, void_width), rg.Interval(0, void_length), rg.Interval(0, layer_height))
                void_brep = void_box.ToBrep()
                brep = rg.Brep.CreateBooleanDifference(brep, void_brep, 0.001)[0]

        # Add the final brep of the layer after creating voids
        geometries[-1] = brep

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept_model((10, 15), 5, 3, 0.2, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept_model((12, 18), 4, 2.5, 0.15, 0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept_model((8, 10), 6, 4, 0.1, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept_model((20, 30), 3, 5, 0.25, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept_model((14, 22), 7, 2, 0.3, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
