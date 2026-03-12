# Created for 0018_0002_perforated_vertical_landscape.json

""" Summary:
The provided function generates an architectural concept model inspired by the "Perforated Vertical Landscape" metaphor by creating a series of staggered platforms that embody verticality and permeability. It defines the structure's height, width, and number of layers, simulating layered terraces with voids. Randomized perforations are introduced in some layers, allowing light and air to penetrate, akin to sunlight filtering through tree canopies. The interplay of solid mass and voids fosters dynamic spatial experiences, while the overall design evokes a natural landscape, reimagined vertically. This approach emphasizes visual connections and spatial interaction between interior and exterior environments."""

#! python 3
function_code = """def create_perforated_vertical_landscape(base_length=20, base_width=15, total_height=50, num_layers=6, perforation_chance=0.3, seed_value=42):
    \"""
    Create an architectural Concept Model inspired by the 'Perforated Vertical Landscape' metaphor.

    This function generates a 3D model consisting of staggered platforms with varying levels of perforation,
    designed to allow light, air, and views to penetrate through the structure. It embodies the concept of a
    vertical landscape with an interplay between solid mass and voids.

    Parameters:
    - base_length (float): The length of the base platform in meters.
    - base_width (float): The width of the base platform in meters.
    - total_height (float): The total height of the structure in meters.
    - num_layers (int): The number of staggered platforms or layers.
    - perforation_chance (float): Probability of a platform having perforations, ranging from 0 to 1.
    - seed_value (int): Seed for randomness to ensure replicable results. Default is 42.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the conceptual model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed
    random.seed(seed_value)

    # Calculate the height of each layer
    layer_height = total_height / num_layers

    # List to store the resulting 3D geometries
    geometries = []

    for i in range(num_layers):
        # Calculate the layer's vertical position
        z_position = i * layer_height

        # Create the base rectangle for the current layer
        layer_plane = rg.Plane.WorldXY
        layer_plane.Translate(rg.Vector3d(0, 0, z_position))
        layer_rect = rg.Rectangle3d(layer_plane, base_length, base_width)

        # Convert rectangle to a planar surface
        layer_surface = rg.Brep.CreatePlanarBreps(layer_rect.ToNurbsCurve())[0]

        # Randomly decide if this layer will have perforations
        if random.random() < perforation_chance:
            # Create random circular perforations
            num_perforations = random.randint(2, 5)
            for _ in range(num_perforations):
                perf_radius = random.uniform(0.5, 2.0)
                perf_x = random.uniform(0.1 * base_length, 0.9 * base_length)
                perf_y = random.uniform(0.1 * base_width, 0.9 * base_width)
                perf_center = rg.Point3d(perf_x, perf_y, z_position)
                perf_circle = rg.Circle(perf_center, perf_radius)
                perf_brep = rg.Brep.CreatePlanarBreps(perf_circle.ToNurbsCurve())
                
                if perf_brep:
                    # Subtract perforation from the current layer
                    layer_surface = rg.Brep.CreateBooleanDifference([layer_surface], [perf_brep[0]], 0.01)[0]

        # Append the final layer to the geometries list
        geometries.append(layer_surface)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(base_length=25, base_width=20, total_height=60, num_layers=8, perforation_chance=0.5, seed_value=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(base_length=30, base_width=25, total_height=75, num_layers=10, perforation_chance=0.4, seed_value=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(base_length=18, base_width=12, total_height=40, num_layers=5, perforation_chance=0.2, seed_value=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(base_length=22, base_width=18, total_height=55, num_layers=7, perforation_chance=0.6, seed_value=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(base_length=15, base_width=10, total_height=45, num_layers=5, perforation_chance=0.3, seed_value=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
