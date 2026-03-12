# Created for 0020_0003_stacked_forests.json

""" Summary:
The provided function, `create_stacked_forests_structure`, generates an architectural concept model inspired by the metaphor of "Stacked forests." It creates a multi-layered structure using staggered and offset volumes to mimic the depth and hierarchy of a forest ecosystem. Each layer's dimensions and positioning are randomized within specified parameters, emulating natural variability. Vertical and diagonal pathways integrate fluid circulation, facilitating movement akin to traversing forest layers. The resulting geometries reflect a dynamic silhouette, balancing solid and void elements, reminiscent of a forest canopy. This approach fosters spatial richness and diverse experiences, embodying the organic growth suggested by the metaphor."""

#! python 3
function_code = """def create_stacked_forests_structure(num_layers=5, initial_size=(10, 15), layer_height=3, offset_magnitude=2, diagonal_path_width=1):
    \"""
    Generates a conceptual architectural model based on the 'Stacked forests' metaphor.
    
    The function creates staggered and offset volumes that form a tiered structure,
    emulating the layered complexity of a forest. It integrates vertical and diagonal
    paths to represent natural movement through the structure, enhancing the organic feel.

    Parameters:
    - num_layers (int): The number of stacked layers to create in the model.
    - initial_size (tuple): A tuple (width, depth) specifying the base dimensions of the structure in meters.
    - layer_height (float): The height of each layer in meters.
    - offset_magnitude (float): The maximum offset for each layer in meters.
    - diagonal_path_width (float): The width of diagonal paths between layers in meters.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a seed for randomness to ensure replicability
    random.seed(42)

    # Initialize a list to hold the geometries
    geometries = []

    # Base dimensions
    width, depth = initial_size

    # Initialize variables for position
    current_x = 0
    current_y = 0

    for i in range(num_layers):
        # Determine offset for this layer
        offset_x = random.uniform(-offset_magnitude, offset_magnitude)
        offset_y = random.uniform(-offset_magnitude, offset_magnitude)

        # Create the main volume for the layer
        box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(current_x + offset_x, current_x + offset_x + width),
            rg.Interval(current_y + offset_y, current_y + offset_y + depth),
            rg.Interval(i * layer_height, (i + 1) * layer_height)
        )
        brep = box.ToBrep()
        geometries.append(brep)

        # Create diagonal paths to mimic forest pathways
        if i < num_layers - 1:
            start_point = rg.Point3d(current_x + offset_x + width / 2, current_y + offset_y + depth / 2, (i + 0.5) * layer_height)
            end_point = rg.Point3d(
                current_x + offset_x + random.uniform(-diagonal_path_width, diagonal_path_width) + width / 2,
                current_y + offset_y + random.uniform(-diagonal_path_width, diagonal_path_width) + depth / 2,
                (i + 1.5) * layer_height
            )
            diagonal_path = rg.Line(start_point, end_point).ToNurbsCurve()
            diagonal_brep = rg.Brep.CreatePipe(diagonal_path, diagonal_path_width / 2, True, rg.PipeCapMode.Flat, True, 0.01, 0.01)
            geometries.append(diagonal_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_structure(num_layers=7, initial_size=(12, 18), layer_height=4, offset_magnitude=3, diagonal_path_width=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_structure(num_layers=6, initial_size=(15, 20), layer_height=5, offset_magnitude=1, diagonal_path_width=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_structure(num_layers=4, initial_size=(8, 10), layer_height=2.5, offset_magnitude=1.5, diagonal_path_width=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_structure(num_layers=8, initial_size=(14, 16), layer_height=3.5, offset_magnitude=2.5, diagonal_path_width=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_structure(num_layers=5, initial_size=(10, 12), layer_height=3, offset_magnitude=1, diagonal_path_width=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
