# Created for 0018_0002_perforated_vertical_landscape.json

""" Summary:
The provided function, `create_vertical_landscape_with_perforations`, generates a 3D architectural concept model inspired by the "Perforated vertical landscape" metaphor. It creates a series of staggered, layered platforms with varying sizes and heights to embody verticality. Each layer incorporates random perforations that allow light and air to permeate the structure, enhancing spatial interconnection and movement. By adjusting parameters like base size, height, number of layers, and perforation density, the model reflects the metaphor's essence of permeability and dynamic visual experiences, ultimately resembling a natural landscape reimagined in a vertical orientation."""

#! python 3
function_code = """def create_vertical_landscape_with_perforations(base_size, height, num_layers, perforation_density, randomness_seed=42):
    \"""
    Generates a 3D architectural concept model inspired by the 'Perforated vertical landscape' metaphor.

    This function creates a series of staggered and layered platforms that integrate solid and void elements
    to embody verticality and permeability. The design features terraces and niches, allowing light and air
    to permeate through the structure, and creating visual connections between levels.

    Parameters:
    - base_size (float): The base size of the lowest platform in meters.
    - height (float): The total height of the structure in meters.
    - num_layers (int): The number of layered platforms.
    - perforation_density (float): A value between 0 and 1 indicating the density of perforations.
    - randomness_seed (int): Seed for randomness to ensure replicable results. Default is 42.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(randomness_seed)

    # Calculate layer height
    layer_height = height / num_layers

    # Initialize list to store geometries
    geometries = []

    # Create each layer
    for i in range(num_layers):
        # Calculate current layer position and size
        size_scale = 1 - (i / num_layers) * 0.2  # Reduce size for upper layers
        layer_size = base_size * size_scale

        # Calculate random offset for staggered effect
        offset_x = random.uniform(-0.1, 0.1) * base_size
        offset_y = random.uniform(-0.1, 0.1) * base_size
        z_position = i * layer_height

        # Create the base rectangle for the current layer
        plane = rg.Plane.WorldXY
        plane.Origin = rg.Point3d(offset_x, offset_y, z_position)
        rect = rg.Rectangle3d(plane, layer_size, layer_size)

        # Create the extrusion for the layer
        extrusion = rg.Extrusion.Create(rect.ToNurbsCurve(), layer_height, True)
        layer_brep = extrusion.ToBrep()

        # Create perforations
        num_perforations = int(perforation_density * 10)
        for _ in range(num_perforations):
            perf_radius = random.uniform(0.05, 0.15) * layer_size
            perf_x = random.uniform(rect.Corner(0).X, rect.Corner(2).X)
            perf_y = random.uniform(rect.Corner(0).Y, rect.Corner(2).Y)
            perf_center = rg.Point3d(perf_x, perf_y, z_position + layer_height / 2)
            perf_circle = rg.Circle(perf_center, perf_radius)
            perf_extrusion = rg.Extrusion.Create(perf_circle.ToNurbsCurve(), layer_height, True)
            perf_brep = perf_extrusion.ToBrep()

            # Subtract perforation from layer
            result_brep = rg.Brep.CreateBooleanDifference([layer_brep], [perf_brep], 0.01)
            if result_brep:
                layer_brep = result_brep[0]

        # Add the final layer with perforations to the list
        geometries.append(layer_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_vertical_landscape_with_perforations(base_size=10.0, height=30.0, num_layers=5, perforation_density=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_vertical_landscape_with_perforations(base_size=8.0, height=25.0, num_layers=4, perforation_density=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_vertical_landscape_with_perforations(base_size=12.0, height=40.0, num_layers=6, perforation_density=0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_vertical_landscape_with_perforations(base_size=15.0, height=35.0, num_layers=3, perforation_density=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_vertical_landscape_with_perforations(base_size=5.0, height=20.0, num_layers=8, perforation_density=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
