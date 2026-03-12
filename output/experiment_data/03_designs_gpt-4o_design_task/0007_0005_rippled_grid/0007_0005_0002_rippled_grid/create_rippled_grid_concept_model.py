# Created for 0007_0005_rippled_grid.json

""" Summary:
The provided function generates an architectural concept model based on the "rippled grid" metaphor by creating a grid of undulating surfaces. It calculates points in a grid using sine wave patterns to achieve a rhythmic and dynamic form that resembles ripples. The function defines parameters like grid size, wave amplitude, and frequency to control the undulation and spatial arrangement. Each set of points forms a surface that overlays a structured grid, maintaining an underlying order while conveying fluidity. This process results in a visually engaging model that embodies the interplay between structured geometry and dynamic movement, aligning with the design task."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size=10, wave_amplitude=2, wave_frequency=1, cell_size=5):
    \"""
    Creates an architectural Concept Model that embodies the 'rippled grid' metaphor. The model consists of undulating
    surfaces overlaying a regular grid structure, reflecting a dynamic and rhythmic spatial quality.

    Args:
        grid_size (int): The number of cells in one dimension of the grid (total cells = grid_size x grid_size).
        wave_amplitude (float): The amplitude of the wave effect applied to the grid.
        wave_frequency (float): The frequency of the wave effect across the grid.
        cell_size (float): The size of each cell in the grid in meters.

    Returns:
        list: A list of Brep objects representing the rippled grid concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Initialize the list to store Brep geometries
    breps = []

    # Define the base plane
    base_plane = rg.Plane.WorldXY

    # Create the grid of points
    grid_points = []
    for i in range(grid_size):
        for j in range(grid_size):
            x = i * cell_size
            y = j * cell_size
            # Calculate the z coordinate using a sine wave pattern
            z = wave_amplitude * math.sin(wave_frequency * (i + j))
            point = rg.Point3d(x, y, z)
            grid_points.append(point)

    # Create the undulating surfaces by connecting points in the grid
    for i in range(grid_size - 1):
        for j in range(grid_size - 1):
            # Create a 3D surface from four points (a quad)
            pt1 = grid_points[i * grid_size + j]
            pt2 = grid_points[i * grid_size + (j + 1)]
            pt3 = grid_points[(i + 1) * grid_size + (j + 1)]
            pt4 = grid_points[(i + 1) * grid_size + j]

            # Create a nurbs surface from the 4 corner points
            surface = rg.NurbsSurface.CreateFromCorners(pt1, pt2, pt3, pt4)

            # Convert the surface to a Brep and add to the list
            brep = rg.Brep.CreateFromSurface(surface)
            breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model(grid_size=8, wave_amplitude=3, wave_frequency=2, cell_size=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model(grid_size=12, wave_amplitude=1.5, wave_frequency=0.5, cell_size=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model(grid_size=6, wave_amplitude=5, wave_frequency=1, cell_size=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model(grid_size=5, wave_amplitude=4, wave_frequency=1.5, cell_size=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model(grid_size=15, wave_amplitude=2.5, wave_frequency=3, cell_size=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
