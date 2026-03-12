# Created for 0007_0005_rippled_grid.json

""" Summary:
The function `create_rippled_grid_concept_model` generates an architectural concept model based on the "rippled grid" metaphor by creating a grid of 3D points that exhibit wave-like undulations. It utilizes parameters such as grid size, wave amplitude, wave frequency, and grid spacing to define the geometry. The undulating surfaces are formed by connecting grid points to create Brep geometries, reflecting the dynamic interplay between structured order and fluid movement. This approach visually embodies the metaphor by emphasizing rhythm and flow while maintaining an underlying grid structure, thus fulfilling the design task effectively."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size=5, wave_amplitude=1.0, wave_frequency=2.0, grid_spacing=10.0):
    \"""
    Creates an architectural Concept Model embodying the 'rippled grid' metaphor.
    
    This function generates a series of undulating surfaces overlaying a regular grid structure.
    It returns a list of 3D geometries that represent the dynamic interplay between the structured grid 
    and wave-like forms.

    Parameters:
    - grid_size (int): The number of grid cells in each direction (x and y).
    - wave_amplitude (float): The amplitude of the wave-like undulations.
    - wave_frequency (float): The frequency of the undulations across the grid.
    - grid_spacing (float): The distance between grid points in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Initialize list to hold the Brep geometries
    geometries = []

    # Seed random for replicability
    random_seed = 42

    # Create the base grid of points
    grid_points = []
    for i in range(grid_size):
        for j in range(grid_size):
            x = i * grid_spacing
            y = j * grid_spacing
            z = wave_amplitude * math.sin(wave_frequency * (i + j) / grid_size * math.pi)
            grid_points.append(rg.Point3d(x, y, z))

    # Generate undulating surfaces using the grid points
    for i in range(grid_size - 1):
        for j in range(grid_size - 1):
            # Create a surface from four corner points of a grid cell
            p0 = grid_points[i * grid_size + j]
            p1 = grid_points[i * grid_size + (j + 1)]
            p2 = grid_points[(i + 1) * grid_size + j]
            p3 = grid_points[(i + 1) * grid_size + (j + 1)]
            brep = rg.Brep.CreateFromCornerPoints(p0, p1, p3, p2, 0.01)
            if brep:
                geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model(grid_size=8, wave_amplitude=2.0, wave_frequency=3.0, grid_spacing=5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model(grid_size=6, wave_amplitude=1.5, wave_frequency=1.0, grid_spacing=15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model(grid_size=10, wave_amplitude=0.5, wave_frequency=4.0, grid_spacing=12.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model(grid_size=7, wave_amplitude=3.0, wave_frequency=2.5, grid_spacing=8.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model(grid_size=4, wave_amplitude=2.5, wave_frequency=1.5, grid_spacing=20.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
