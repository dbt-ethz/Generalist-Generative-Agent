# Created for 0020_0003_stacked_forests.json

""" Summary:
The provided function `create_stacked_forests_model` generates an architectural concept model based on the metaphor of "Stacked forests." It constructs a series of staggered, offset volumes that mimic the layered structure of a forest, reflecting its complexity and hierarchy. Each layer varies in height and base size, creating an organic feel, while vertical and diagonal circulation paths enhance movement between layers, resembling navigation through a forest. The geometry balances solid and void elements, evoking clearings and dense clusters. The resulting model showcases a dynamic silhouette that captures the fluidity and stability of a forest ecosystem, embodying the metaphor's essence."""

#! python 3
function_code = """def create_stacked_forests_model(layer_count=6, base_dimension=15, height_variation=3, stagger_range=4, path_width=1.5):
    \"""
    Constructs a 3D architectural Concept Model based on the 'Stacked forests' metaphor. This function creates
    staggered and offset volumes to evoke the tiered structure of a forest, with integrated vertical and diagonal
    circulation paths to mimic natural movement through varying forest layers.

    Parameters:
    - layer_count (int): The number of vertical layers in the model.
    - base_dimension (float): The base dimension (width and depth) of the largest layer in meters.
    - height_variation (float): The variability in height for each layer in meters.
    - stagger_range (float): The maximum offset range for staggering each layer in meters.
    - path_width (float): The width of circulation paths in meters.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Seed for replicable randomness
    random.seed(42)

    # Initialize a list to store the generated geometries
    geometries = []

    # Base position and size for the first layer
    base_size = base_dimension
    current_position = rg.Point3d(0, 0, 0)

    for i in range(layer_count):
        # Create a box for the current layer
        layer_height = random.uniform(2, height_variation)
        box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(current_position.X, current_position.X + base_size),
            rg.Interval(current_position.Y, current_position.Y + base_size),
            rg.Interval(current_position.Z, current_position.Z + layer_height)
        )

        brep = box.ToBrep()
        geometries.append(brep)

        # Determine the offset and positioning for the next layer
        offset_x = random.uniform(-stagger_range, stagger_range)
        offset_y = random.uniform(-stagger_range, stagger_range)
        current_position = rg.Point3d(current_position.X + offset_x, current_position.Y + offset_y, current_position.Z + layer_height)

        # Adjust the base size for the next layer to create variation
        base_size = max(base_dimension / 2, base_size * random.uniform(0.7, 0.9))

        # Add vertical and diagonal circulation paths
        if i > 0:
            # Vertical path
            path_start = rg.Point3d(0, 0, (i - 1) * height_variation)
            path_end = rg.Point3d(0, 0, i * height_variation)
            vertical_path = rg.Line(path_start, path_end).ToNurbsCurve()
            vertical_brep = rg.Brep.CreatePipe(vertical_path, path_width / 2, True, rg.PipeCapMode.Flat, True, 0.01, 0.01)
            geometries.append(vertical_brep)

            # Diagonal path
            diag_start = rg.Point3d(random.uniform(-path_width, path_width), random.uniform(-path_width, path_width), (i - 1) * height_variation)
            diag_end = rg.Point3d(random.uniform(-path_width, path_width), random.uniform(-path_width, path_width), i * height_variation)
            diagonal_path = rg.Line(diag_start, diag_end).ToNurbsCurve()
            diagonal_brep = rg.Brep.CreatePipe(diagonal_path, path_width / 3, True, rg.PipeCapMode.Flat, True, 0.01, 0.01)
            geometries.append(diagonal_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_model(layer_count=8, base_dimension=20, height_variation=5, stagger_range=3, path_width=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_model(layer_count=10, base_dimension=25, height_variation=4, stagger_range=5, path_width=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_model(layer_count=5, base_dimension=18, height_variation=2, stagger_range=6, path_width=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_model(layer_count=7, base_dimension=30, height_variation=6, stagger_range=2, path_width=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_model(layer_count=4, base_dimension=12, height_variation=3, stagger_range=2, path_width=1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
