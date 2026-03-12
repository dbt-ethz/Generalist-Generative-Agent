# Created for 0007_0005_rippled_grid.json

""" Summary:
The function `create_rippled_grid_concept_model` generates an architectural concept model reflecting the "rippled grid" metaphor by producing a series of undulating surfaces that overlay a structured grid. It takes parameters such as grid dimensions, spacing, wave amplitude, and frequency to create a dynamic interplay between fluid shapes and a regular grid. The function calculates 3D points based on a sine wave function, which simulates the ripple effect, while maintaining grid-like order. By generating NURBS surfaces from these points, the model visually represents the balance of movement and structure, embodying the metaphor's essence."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_dimensions, grid_spacing, wave_amplitude, wave_frequency, surface_resolution):
    \"""
    Generates an architectural Concept Model embodying the 'rippled grid' metaphor by creating a series of undulating
    surfaces overlaying a regular grid structure. The model emphasizes the ripple effect in contrast with the grid.

    Parameters:
    grid_dimensions (tuple): A tuple of two integers (rows, cols) representing the number of grid cells in each direction.
    grid_spacing (float): The spacing between grid lines in meters.
    wave_amplitude (float): The amplitude of the wave undulations in meters.
    wave_frequency (float): The frequency of the wave undulations.
    surface_resolution (int): The number of points per grid cell along one dimension for surface detail.

    Returns:
    List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import math

    breps = []
    rows, cols = grid_dimensions

    # Create the base grid structure with additional detail
    for i in range(rows):
        for j in range(cols):
            # Create detailed grid cell with ripple effect
            points = []
            for u in range(surface_resolution + 1):
                for v in range(surface_resolution + 1):
                    # Calculate the local position within the grid cell
                    x_local = u * grid_spacing / surface_resolution
                    y_local = v * grid_spacing / surface_resolution

                    # Calculate global position
                    x = i * grid_spacing + x_local
                    y = j * grid_spacing + y_local

                    # Calculate the z-coordinate using a wave function
                    z = wave_amplitude * math.sin(wave_frequency * (x + y))

                    # Append point to the list of local points
                    points.append(rg.Point3d(x, y, z))

            # Create a nurbs surface from the grid cell points
            if len(points) == (surface_resolution + 1) ** 2:
                surface = rg.NurbsSurface.CreateThroughPoints(
                    points, surface_resolution + 1, surface_resolution + 1, 3, 3, False, False
                )
                if surface:
                    brep = rg.Brep.CreateFromSurface(surface)
                    breps.append(brep)

    # Return the list of Breps
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model((10, 10), 1.0, 0.5, 2.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model((8, 12), 0.5, 0.3, 1.5, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((15, 15), 0.75, 0.4, 3.0, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((5, 7), 2.0, 1.0, 1.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((6, 9), 1.5, 0.8, 2.5, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
