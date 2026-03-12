# Created for 0007_0005_rippled_grid.json

""" Summary:
The function `create_rippled_grid_concept_model` generates an architectural concept model based on the "rippled grid" metaphor by creating a structured grid of undulating surfaces. It takes parameters like grid size, spacing, wave amplitude, frequency, and material contrast to simulate dynamic wave-like forms over a regular grid. The function calculates the z-coordinates using a sine wave function, yielding a series of points that represent the ripple effect. Each point is transformed into a surface, resulting in a visually engaging interplay between fluidity and order, effectively embodying the metaphor's essence in the architectural model."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size, grid_spacing, wave_amplitude, wave_frequency, wave_phase, material_contrast_factor):
    \"""
    Creates an architectural Concept Model embodying the 'rippled grid' metaphor by developing a series of undulating
    surfaces or facades overlaying a regular grid structure. The model emphasizes the ripple effect in contrast with the grid.

    Parameters:
    grid_size (tuple): A tuple of two integers (rows, cols) representing the number of grid cells in each direction.
    grid_spacing (float): The spacing between grid lines in meters.
    wave_amplitude (float): The amplitude of the wave undulations in meters.
    wave_frequency (float): The frequency of the wave undulations.
    wave_phase (float): The phase shift of the wave undulations.
    material_contrast_factor (float): A value to define the contrast between the ripple effect and grid.

    Returns:
    List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import math

    breps = []
    seed = 42  # Seed for randomness to ensure replicability

    # Create the base grid structure
    rows, cols = grid_size
    for i in range(rows):
        for j in range(cols):
            # Calculate the position of each grid point
            x = i * grid_spacing
            y = j * grid_spacing

            # Calculate the z-coordinate using a wave function to create the ripple effect
            z = wave_amplitude * math.sin(wave_frequency * (x + y) + wave_phase)

            # Create a point at the calculated position
            point = rg.Point3d(x, y, z)

            # Create a vertical surface at each grid point that undulates
            plane = rg.Plane(point, rg.Vector3d.ZAxis)
            circle = rg.Circle(plane, grid_spacing / 2 * material_contrast_factor)
            surface = rg.Brep.CreatePlanarBreps(circle.ToNurbsCurve())[0]
            breps.append(surface)

    # Return the list of Breps
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model((10, 10), 1.0, 0.5, 2.0, 0.0, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model((5, 8), 0.75, 0.3, 1.5, 0.5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((8, 12), 0.5, 0.8, 3.0, 1.0, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((6, 6), 0.6, 0.4, 1.0, 0.2, 1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((12, 15), 0.9, 0.7, 2.5, 0.3, 1.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
