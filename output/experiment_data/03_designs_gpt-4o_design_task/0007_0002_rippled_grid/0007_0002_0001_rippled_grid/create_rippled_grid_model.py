# Created for 0007_0002_rippled_grid.json

""" Summary:
The provided function generates an architectural concept model based on the "rippled grid" metaphor by establishing a grid structure that serves as a foundation. It calculates control points in a 3D space, where the z-coordinate is modified by a sine function to create undulating surfaces that mimic ripples. This results in a dynamic interplay between the structured grid and the flowing ripple patterns, embodying the metaphor's essence of rhythm and fluidity. The model can be visualized as a series of 3D geometries, illustrating how spaces can flow while adhering to an underlying order, effectively communicating the desired architectural concept."""

#! python 3
function_code = """def create_rippled_grid_model(grid_size=10, cell_size=2, ripple_amplitude=1.0, ripple_frequency=2.0):
    \"""
    Create an architectural Concept Model based on the 'rippled grid' metaphor.
    
    This function generates a grid-based structure and applies a rippling effect across it,
    resulting in a dynamic and rhythmic spatial form. The model is composed of undulating
    surfaces that interact with the underlying grid, simulating the effect of ripples.

    Parameters:
    - grid_size (int): The number of cells along one edge of the square grid.
    - cell_size (float): The size of each cell in the grid (in meters).
    - ripple_amplitude (float): The amplitude of the ripple effect (in meters).
    - ripple_frequency (float): The frequency of the ripple effect.

    Returns:
    List of 3D geometries (Rhino.Geometry.Brep) representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Create a list to store the resulting geometries
    geometries = []

    # Define the base grid dimensions
    grid_dim = grid_size * cell_size

    # Iterate over the grid to create control points for the surface
    for i in range(grid_size + 1):
        for j in range(grid_size + 1):
            # Calculate the x and y position of each grid point
            x = i * cell_size
            y = j * cell_size

            # Apply the ripple effect to the z-coordinate
            z = ripple_amplitude * math.sin(ripple_frequency * (x + y))

            # Create a control point and add it to the list
            point = rg.Point3d(x, y, z)
            geometries.append(point)

    # Create a surface from the control points
    surface = rg.NurbsSurface.CreateFromPoints(
        geometries, 
        grid_size + 1, 
        grid_size + 1, 
        3, 
        3
    )

    # Optionally, create a solid brep from the surface for more architectural context
    if surface:
        brep = rg.Brep.CreateFromSurface(surface)
        geometries = [brep]

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_model(grid_size=15, cell_size=3, ripple_amplitude=2.0, ripple_frequency=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_model(grid_size=8, cell_size=1.5, ripple_amplitude=0.5, ripple_frequency=3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_model(grid_size=12, cell_size=2.5, ripple_amplitude=1.5, ripple_frequency=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_model(grid_size=5, cell_size=4, ripple_amplitude=0.8, ripple_frequency=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_model(grid_size=20, cell_size=1.0, ripple_amplitude=1.2, ripple_frequency=2.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
