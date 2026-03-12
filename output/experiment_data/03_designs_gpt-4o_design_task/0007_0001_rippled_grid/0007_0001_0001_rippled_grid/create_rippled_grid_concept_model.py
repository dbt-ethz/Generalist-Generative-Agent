# Created for 0007_0001_rippled_grid.json

""" Summary:
The function `create_rippled_grid_concept_model` generates an architectural concept model inspired by the "rippled grid" metaphor. It utilizes a grid framework to define spatial organization while introducing wave-like variations in height through sine wave calculations. Parameters such as grid size, cell dimensions, ripple amplitude, and frequency allow for customization of the model's undulating surfaces. The function constructs 3D geometries by creating points based on these calculations and forming Nurbs surfaces between them. This approach captures the metaphor's essence by achieving a balance between structured order and dynamic fluidity, enhancing both exterior aesthetics and interior spatial flow."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size, cell_size, ripple_amplitude, ripple_frequency, seed=42):
    \"""
    Creates an architectural Concept Model embodying the "rippled grid" metaphor. This model uses a grid system as an underlying framework
    and introduces wave-like patterns to the facade or roof, suggesting movement and dynamic qualities while maintaining order.

    Parameters:
    - grid_size: Tuple of two integers (rows, columns), defining the size of the grid.
    - cell_size: Float, size of each grid cell in meters.
    - ripple_amplitude: Float, the maximum height variation in the ripple effect.
    - ripple_frequency: Float, the frequency of the ripples across the grid.
    - seed: Integer, seed for random number generator to ensure replicable results.

    Returns:
    - List of RhinoCommon Breps representing the 3D geometries of the concept model.
    \"""

    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    rows, cols = grid_size
    geometries = []

    # Create the base grid of points
    points = []
    for i in range(rows):
        row = []
        for j in range(cols):
            x = j * cell_size
            y = i * cell_size
            # Calculate the z-value based on a sine wave pattern to create ripples
            z = ripple_amplitude * math.sin(ripple_frequency * (x + y))
            point = rg.Point3d(x, y, z)
            row.append(point)
        points.append(row)

    # Create surfaces between points
    for i in range(rows - 1):
        for j in range(cols - 1):
            # Create a surface using 4 corner points
            pt1 = points[i][j]
            pt2 = points[i][j + 1]
            pt3 = points[i + 1][j + 1]
            pt4 = points[i + 1][j]
            corner_pts = [pt1, pt2, pt3, pt4]
            try:
                # Create a nurbs surface from corner points (assuming they form a valid planar region)
                surface = rg.NurbsSurface.CreateFromCorners(corner_pts[0], corner_pts[1], corner_pts[2], corner_pts[3])
                geometries.append(surface)
            except:
                continue

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model((10, 10), 1.0, 2.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model((5, 8), 2.0, 1.5, 3.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((6, 6), 0.5, 1.0, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((8, 12), 1.5, 3.0, 1.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((4, 4), 1.0, 0.5, 2.0, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
