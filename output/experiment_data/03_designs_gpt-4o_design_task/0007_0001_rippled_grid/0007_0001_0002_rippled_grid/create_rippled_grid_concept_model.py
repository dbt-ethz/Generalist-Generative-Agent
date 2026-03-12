# Created for 0007_0001_rippled_grid.json

""" Summary:
The `create_rippled_grid_concept_model` function generates an architectural concept model that embodies the "rippled grid" metaphor. It constructs a modular grid system where each grid cell's height is influenced by a sine wave, creating undulating surfaces that evoke the dynamic quality of ripples. By adjusting parameters like grid size, cell size, wave amplitude, and frequency, the function manipulates the facade and roofline to produce a flowing, rhythmic form while preserving an underlying structural order. The resulting 3D geometries reflect the metaphor's essence, facilitating a harmonious integration of fluidity and organization in both exterior and interior spaces."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size=10, cell_size=5.0, wave_amplitude=2.0, wave_frequency=2.0):
    \"""
    Create an architectural Concept Model that embodies the 'rippled grid' metaphor.
    
    This function generates a series of modular elements forming an undulating facade or roof.
    It uses a grid system as the underlying framework, manipulating it to create wave-like patterns.
    
    Parameters:
    - grid_size: int, the number of cells in one dimension of the grid (e.g., 10 for a 10x10 grid).
    - cell_size: float, the size of each grid cell in meters.
    - wave_amplitude: float, the maximum height of the wave effect.
    - wave_frequency: float, the frequency of the wave patterns.
    
    Returns:
    - list of Rhino.Geometry.Brep: A list of breps representing the 3D geometries of the concept model.
    \"""
    
    import Rhino.Geometry as rg
    import math

    # Seed for randomness
    random_seed = 42
    
    # List to store the generated 3D geometries
    breps = []
    
    # Create a grid of points
    points = []
    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            x = i * cell_size
            y = j * cell_size
            # Calculate the z-coordinate using a sine wave for ripple effect
            z = wave_amplitude * math.sin(wave_frequency * (x + y))
            point = rg.Point3d(x, y, z)
            row.append(point)
        points.append(row)
    
    # Create surfaces from points
    for i in range(grid_size - 1):
        for j in range(grid_size - 1):
            # Define the corners of each grid cell
            pt1 = points[i][j]
            pt2 = points[i+1][j]
            pt3 = points[i+1][j+1]
            pt4 = points[i][j+1]
            
            # Create a surface patch for each cell
            surface = rg.Brep.CreateFromCornerPoints(pt1, pt2, pt3, pt4, 0.01)
            if surface:
                breps.append(surface)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model(grid_size=8, cell_size=4.0, wave_amplitude=3.0, wave_frequency=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model(grid_size=12, cell_size=6.0, wave_amplitude=1.5, wave_frequency=3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model(grid_size=15, cell_size=3.0, wave_amplitude=4.0, wave_frequency=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model(grid_size=6, cell_size=2.0, wave_amplitude=5.0, wave_frequency=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model(grid_size=10, cell_size=5.0, wave_amplitude=2.5, wave_frequency=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
