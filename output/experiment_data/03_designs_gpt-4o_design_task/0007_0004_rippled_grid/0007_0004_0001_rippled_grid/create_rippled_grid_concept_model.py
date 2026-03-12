# Created for 0007_0004_rippled_grid.json

""" Summary:
The provided function, `create_rippled_grid_concept_model`, generates an architectural concept model inspired by the 'rippled grid' metaphor. It constructs a 3D grid of rectangular cells, where each cell's corners are elevated based on a mathematical sine function to create undulating surfaces that mimic ripples. This design maintains an underlying grid structure, ensuring order while introducing fluidity through the ripple effect. By adjusting parameters like grid size, cell size, ripple amplitude, and frequency, the function creates diverse spatial configurations that embody the dynamic interplay of structured organization and visual movement, aligning with the design task's requirements."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size, cell_size, ripple_amplitude, ripple_frequency):
    \"""
    Creates an architectural Concept Model based on the 'rippled grid' metaphor.
    
    The function generates a 3D grid structure with undulating surfaces that ripple across the grid,
    creating a dynamic interplay of fluidity and structure. The model maintains an underlying grid
    organization, while the ripple effect introduces movement and spatial flow.

    Parameters:
    grid_size (tuple): A tuple of two integers (rows, columns) representing the number of cells in the grid.
    cell_size (float): The size of each grid cell in meters.
    ripple_amplitude (float): The maximum height of the ripple effect in meters.
    ripple_frequency (float): The frequency of the ripple effect, determining the number of undulations.

    Returns:
    List[Rhino.Geometry.Brep]: A list of breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math
    from random import seed, uniform

    seed(42)  # Ensure deterministic randomness

    rows, columns = grid_size
    breps = []

    # Create the base grid structure
    for i in range(rows):
        for j in range(columns):
            x = j * cell_size
            y = i * cell_size
            z = 0

            # Calculate the ripple effect
            ripple_effect = ripple_amplitude * math.sin(ripple_frequency * (x + y))

            # Create a rectangular cell with a rippled surface
            corners = [
                rg.Point3d(x, y, z),
                rg.Point3d(x + cell_size, y, z),
                rg.Point3d(x + cell_size, y + cell_size, z),
                rg.Point3d(x, y + cell_size, z)
            ]

            # Elevate corners based on ripple effect
            elevated_corners = [
                rg.Point3d(pt.X, pt.Y, pt.Z + ripple_effect) for pt in corners
            ]

            # Create a surface from the elevated corners
            rippled_surface = rg.NurbsSurface.CreateFromCorners(
                elevated_corners[0],
                elevated_corners[1],
                elevated_corners[2],
                elevated_corners[3]
            )

            if rippled_surface:
                breps.append(rippled_surface.ToBrep())

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model((10, 10), 1.0, 0.5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model((5, 8), 0.5, 1.0, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((7, 12), 0.75, 0.3, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((6, 6), 1.5, 1.0, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((8, 8), 0.8, 0.4, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
