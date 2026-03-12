# Created for 0007_0005_rippled_grid.json

""" Summary:
The provided function generates an architectural concept model based on the "rippled grid" metaphor by creating a series of undulating surfaces that overlay a structured grid. It defines a grid using specified dimensions and calculates the height of each point in the grid according to a sinusoidal wave function, simulating the ripple effect. The function then constructs 3D surface patches from these calculated points, embodying the dynamic interplay of fluidity and order. By adjusting parameters like ripple amplitude and frequency, the model emphasizes the rhythmic quality suggested by the metaphor while maintaining a coherent grid structure."""

#! python 3
function_code = """def create_rippled_grid_model(grid_size, ripple_amplitude, ripple_frequency, grid_spacing, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'rippled grid' metaphor. 
    The model consists of undulating surfaces overlaying a regular grid structure.

    Parameters:
    - grid_size: Tuple (int, int) representing the number of grid cells in the x and y directions.
    - ripple_amplitude: Float indicating the maximum height of the ripple effect.
    - ripple_frequency: Float determining the frequency of the ripple pattern.
    - grid_spacing: Float representing the distance between adjacent grid points in meters.
    - seed: Integer to seed the random number generator for reproducibility.

    Returns:
    - List of Breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Seed the random number generator
    random.seed(seed)

    # Extract grid dimensions
    grid_x, grid_y = grid_size

    # List to store the generated Breps
    breps = []

    # Create the grid points
    for i in range(grid_x):
        for j in range(grid_y):
            # Calculate the position of the grid point
            x = i * grid_spacing
            y = j * grid_spacing
            # Calculate the ripple height using a sinusoidal wave function
            z = ripple_amplitude * math.sin(ripple_frequency * (x + y))

            # Create a point in 3D space
            point = rg.Point3d(x, y, z)

            # Create a surface patch for each grid cell
            if i < grid_x - 1 and j < grid_y - 1:
                # Get the four corners of the grid cell
                p0 = point
                p1 = rg.Point3d(x + grid_spacing, y, ripple_amplitude * math.sin(ripple_frequency * (x + grid_spacing + y)))
                p2 = rg.Point3d(x + grid_spacing, y + grid_spacing, ripple_amplitude * math.sin(ripple_frequency * (x + grid_spacing + y + grid_spacing)))
                p3 = rg.Point3d(x, y + grid_spacing, ripple_amplitude * math.sin(ripple_frequency * (x + y + grid_spacing)))

                # Create a nurbs surface from the corners
                corners = [p0, p1, p2, p3]
                nurbs_surface = rg.NurbsSurface.CreateFromCorners(corners[0], corners[1], corners[2], corners[3])

                # Add the surface to the breps list
                if nurbs_surface:
                    breps.append(nurbs_surface)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_model((10, 10), 5.0, 2.0, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_model((8, 12), 3.0, 1.5, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_model((15, 15), 4.0, 3.0, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_model((20, 5), 6.0, 1.0, 0.75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_model((12, 8), 2.5, 2.5, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
