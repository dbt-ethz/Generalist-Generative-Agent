# Created for 0018_0002_perforated_vertical_landscape.json

""" Summary:
The function `create_perforated_vertical_landscape` generates an architectural concept model inspired by the "Perforated vertical landscape" metaphor. It constructs a series of staggered, layered platforms, simulating verticality through varying heights and dimensions. Each layer incorporates perforations, allowing light and air to penetrate, reminiscent of sunlight filtering through canopies. By adjusting parameters like base dimensions and perforation density, the model emphasizes the dynamism of solid and void, creating pathways for interaction between interior and exterior spaces. This approach encapsulates the metaphor's essence, fostering a spatial experience that mirrors a reimagined natural landscape in a vertical format."""

#! python 3
function_code = """def create_perforated_vertical_landscape(base_length, base_width, total_height, num_layers, perforation_density, seed_value=42):
    \"""
    Generates a 3D architectural Concept Model based on the 'Perforated Vertical Landscape' metaphor.

    This function creates a series of staggered, layered platforms with varying perforations to allow light and air
    to flow through the structure. The design emphasizes verticality, permeability, and spatial interconnection.

    Parameters:
    - base_length (float): Length of the base platform in meters.
    - base_width (float): Width of the base platform in meters.
    - total_height (float): Total height of the structure in meters.
    - num_layers (int): Number of staggered layers or platforms.
    - perforation_density (float): A value between 0 and 1 indicating the density of perforations.
    - seed_value (int): Seed for randomness to ensure replicable results. Default is 42.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set seed for randomness
    random.seed(seed_value)

    # Calculate the height of each layer
    layer_height = total_height / num_layers

    # Initialize a list to store the resulting 3D geometries
    geometries = []

    for i in range(num_layers):
        # Define the plane for each layer
        layer_plane = rg.Plane.WorldXY
        layer_plane.Translate(rg.Vector3d(0, 0, i * layer_height))

        # Calculate size and offset for each layer
        length_variation = random.uniform(0.8, 1.0)
        width_variation = random.uniform(0.8, 1.0)
        offset_x = random.uniform(-0.1, 0.1) * base_length
        offset_y = random.uniform(-0.1, 0.1) * base_width

        # Create the rectangle for the current layer
        layer_rect = rg.Rectangle3d(layer_plane, base_length * length_variation, base_width * width_variation)
        layer_rect.Transform(rg.Transform.Translation(offset_x, offset_y, 0))

        # Convert rectangle to a surface
        layer_surface = rg.Brep.CreatePlanarBreps(layer_rect.ToNurbsCurve())[0]

        # Create perforations
        perforations = []
        num_perforations = int(perforation_density * 5)
        for _ in range(num_perforations):
            perf_size = random.uniform(0.1, 0.3) * min(base_length, base_width)
            perf_offset_x = random.uniform(-0.4, 0.4) * base_length
            perf_offset_y = random.uniform(-0.4, 0.4) * base_width
            perf_plane = rg.Plane(layer_plane)
            perf_plane.Translate(rg.Vector3d(perf_offset_x, perf_offset_y, 0))
            perf_circle = rg.Circle(perf_plane, perf_size)
            perf_brep = rg.Brep.CreatePlanarBreps(perf_circle.ToNurbsCurve())
            if perf_brep:
                perforations.append(perf_brep[0])

        # Subtract perforations from the current layer
        for perf in perforations:
            boolean_difference = rg.Brep.CreateBooleanDifference([layer_surface], [perf], 0.01)
            if boolean_difference:
                layer_surface = boolean_difference[0]

        # Append the final layer with perforations to the geometries
        geometries.append(layer_surface)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(10.0, 5.0, 15.0, 4, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(12.0, 6.0, 20.0, 5, 0.5, seed_value=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(8.0, 4.0, 10.0, 3, 0.2, seed_value=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(15.0, 7.0, 25.0, 6, 0.4, seed_value=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(9.0, 4.5, 18.0, 5, 0.6, seed_value=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
