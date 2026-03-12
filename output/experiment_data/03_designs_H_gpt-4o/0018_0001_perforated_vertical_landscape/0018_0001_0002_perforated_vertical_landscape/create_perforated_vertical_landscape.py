# Created for 0018_0001_perforated_vertical_landscape.json

""" Summary:
The provided function generates an architectural concept model based on the "Perforated vertical landscape" metaphor by creating a vertical structure comprising alternating solid and void elements. It defines parameters such as height, width, depth, and the number of layers to simulate a natural landscape with a dynamic silhouette. Using randomization, the function creates voids within each layer, allowing light and air to penetrate, thus enhancing spatial relationships. The resulting geometries, represented as 3D objects, embody the metaphor's essence of verticality and permeability, reflecting the interplay between interior and exterior spaces while suggesting geological formations."""

#! python 3
function_code = """def create_perforated_vertical_landscape(height=30, width=10, depth=10, num_layers=6, void_pattern_seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Perforated vertical landscape' metaphor.

    Generates a vertical structure with alternating solid and void elements, designed to resemble
    a natural landscape with layers and textures that suggest geological formations. The structure
    focuses on maximizing light penetration and views through its form, creating dynamic spatial
    interactions between interior and exterior.

    Parameters:
    - height (float): Total height of the structure in meters.
    - width (float): Width of the structure's base in meters.
    - depth (float): Depth of the structure's base in meters.
    - num_layers (int): Number of vertical layers or zones in the structure.
    - void_pattern_seed (int): Seed for random number generator to ensure replicable void patterns.

    Returns:
    - List of RhinoCommon Brep objects: The generated 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(void_pattern_seed)

    # Calculate the height of each layer
    layer_height = height / num_layers

    # Initialize an empty list to store the geometries
    geometries = []

    # Generate the layers
    for i in range(num_layers):
        # Base height of the current layer
        base_height = i * layer_height

        # Create solid part of the layer
        base_plane = rg.Plane.WorldXY
        base_plane.OriginZ = base_height
        solid_box = rg.Box(base_plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, layer_height))
        solid_brep = solid_box.ToBrep()

        # Create a pattern of voids
        num_voids = random.randint(2, 4)
        for _ in range(num_voids):
            void_width = random.uniform(0.5, width / 3)
            void_depth = random.uniform(0.5, depth / 3)
            void_x = random.uniform(0, width - void_width)
            void_y = random.uniform(0, depth - void_depth)
            void_plane = rg.Plane.WorldXY
            void_plane.Origin = rg.Point3d(void_x, void_y, base_height)

            void_box = rg.Box(void_plane, rg.Interval(0, void_width), rg.Interval(0, void_depth), rg.Interval(0, layer_height))
            void_brep = void_box.ToBrep()

            # Subtract the void from the solid
            result = rg.Brep.CreateBooleanDifference([solid_brep], [void_brep], 0.001)
            if result:
                solid_brep = result[0]

        # Add the modified solid to the geometries list
        geometries.append(solid_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(height=40, width=15, depth=15, num_layers=8, void_pattern_seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(height=25, width=20, depth=5, num_layers=4, void_pattern_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(height=35, width=12, depth=8, num_layers=5, void_pattern_seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(height=50, width=25, depth=20, num_layers=10, void_pattern_seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(height=45, width=18, depth=12, num_layers=7, void_pattern_seed=88)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
