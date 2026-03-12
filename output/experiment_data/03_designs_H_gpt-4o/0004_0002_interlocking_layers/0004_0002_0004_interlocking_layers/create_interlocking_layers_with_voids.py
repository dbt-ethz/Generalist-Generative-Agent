# Created for 0004_0002_interlocking_layers.json

""" Summary:
The function `create_interlocking_layers_with_voids` generates an architectural concept model based on the "Interlocking Layers" metaphor by creating a series of overlapping planes or volumes that feature voids, emphasizing spatial hierarchy and interaction. It divides a specified height into multiple layers, constructing boxes for each layer while randomly introducing voids to enhance complexity. The resulting geometries reflect dynamic relationships between layers, with varying protrusions and recesses that embody the metaphor's essence. This approach allows for both visual depth and functional diversity, supporting a blend of open and secluded spaces within the architectural design."""

#! python 3
function_code = """def create_interlocking_layers_with_voids(base_width, base_depth, base_height, num_layers, void_size):
    \"""
    Creates an architectural Concept Model based on the 'Interlocking Layers' metaphor, incorporating voids to emphasize spatial hierarchy and interaction.

    This function generates a composition of overlapping and interwoven planes or volumes, with void spaces to highlight the complexity and depth of the design.

    Parameters:
    - base_width (float): The width of the base volume in meters.
    - base_depth (float): The depth of the base volume in meters.
    - base_height (float): The height of the entire model in meters.
    - num_layers (int): The number of interlocking layers to create.
    - void_size (float): The size of the voids to be introduced in each layer.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the interlocking layers with voids.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a seed for randomness to ensure reproducibility
    random.seed(42)

    # Calculate the height of each layer
    layer_height = base_height / num_layers
    geometries = []

    for i in range(num_layers):
        # Create a base box for each layer
        layer_box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(0, base_width),
            rg.Interval(0, base_depth),
            rg.Interval(i * layer_height, (i + 1) * layer_height)
        )
        layer_brep = layer_box.ToBrep()
        
        # Introduce voids within the layer
        void_x = random.uniform(0.2, 0.8) * base_width
        void_y = random.uniform(0.2, 0.8) * base_depth
        
        void_box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(void_x - void_size / 2, void_x + void_size / 2),
            rg.Interval(void_y - void_size / 2, void_y + void_size / 2),
            rg.Interval(i * layer_height, (i + 1) * layer_height)
        )
        void_brep = void_box.ToBrep()

        # Subtract void from the layer
        layer_with_void = rg.Brep.CreateBooleanDifference([layer_brep], [void_brep], 0.001)

        if layer_with_void:
            geometries.extend(layer_with_void)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_with_voids(10.0, 5.0, 20.0, 5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_with_voids(15.0, 7.0, 30.0, 6, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_with_voids(12.0, 6.0, 18.0, 4, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_with_voids(8.0, 4.0, 16.0, 3, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_with_voids(20.0, 10.0, 25.0, 7, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
