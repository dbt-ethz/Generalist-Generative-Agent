# Created for 0007_0005_rippled_grid.json

""" Summary:
The `create_rippled_grid_concept_model` function generates an architectural concept model based on the "rippled grid" metaphor. It constructs a grid structure where each point is influenced by a sine wave pattern, creating undulating surfaces that reflect fluidity and movement. By adjusting parameters like wave amplitude and frequency, the model showcases dynamic, wave-like forms while adhering to an underlying grid order. The function outputs a list of 3D geometries representing these surfaces, capturing the interplay between structured order and rhythmic fluidity, thus embodying the metaphor effectively in the architectural design."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size, wave_amplitude, wave_frequency, grid_spacing, surface_thickness, seed=42):
    \"""
    Creates an architectural Concept Model that embodies the 'rippled grid' metaphor. The model consists of undulating
    surfaces overlaid on a regular grid structure, creating a dynamic interplay between structure and fluidity.

    Parameters:
    - grid_size: Tuple[int, int] specifying the number of grid cells in the X and Y directions.
    - wave_amplitude: Float specifying the maximum height of the wave undulations.
    - wave_frequency: Float specifying the frequency of the wave pattern.
    - grid_spacing: Float specifying the distance between grid lines.
    - surface_thickness: Float specifying the thickness of the undulating surfaces.
    - seed: Integer used to ensure that the randomness in wave generation is replicable.

    Returns:
    - List of Rhino.Geometry.Brep representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for replicability
    random.seed(seed)

    # Initialize the list to hold the geometries
    geometries = []

    # Create the base grid points
    grid_points = []
    for i in range(grid_size[0] + 1):
        for j in range(grid_size[1] + 1):
            x = i * grid_spacing
            y = j * grid_spacing
            z = math.sin(i * wave_frequency) * wave_amplitude * random.uniform(0.8, 1.2)
            grid_points.append(rg.Point3d(x, y, z))

    # Create undulating surfaces based on the grid points
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            # Define the corners of the grid cell
            pt0 = grid_points[i * (grid_size[1] + 1) + j]
            pt1 = grid_points[i * (grid_size[1] + 1) + (j + 1)]
            pt2 = grid_points[(i + 1) * (grid_size[1] + 1) + (j + 1)]
            pt3 = grid_points[(i + 1) * (grid_size[1] + 1) + j]

            # Create a surface from these points
            corners = [pt0, pt1, pt2, pt3, pt0]
            polyline = rg.Polyline(corners)
            curve = polyline.ToNurbsCurve()
            surface = rg.Brep.CreatePatch([curve], 10, 10, surface_thickness)

            # Add the surface to the list of geometries
            if surface:
                geometries.append(surface)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model((10, 10), 5.0, 0.5, 1.0, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model((15, 15), 3.0, 1.0, 0.5, 0.3, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((8, 12), 4.0, 0.8, 0.75, 0.1, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((12, 8), 6.0, 0.3, 1.5, 0.25, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((20, 20), 2.5, 0.7, 0.8, 0.15, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
