# Created for 0007_0001_rippled_grid.json

""" Summary:
The provided function, `create_rippled_grid_concept_model`, generates an architectural concept model based on the "rippled grid" metaphor by employing a grid framework that manipulates height to create undulating surfaces. It uses parameters for grid dimensions, cell sizes, and wave characteristics to calculate the z-axis height of each grid point, simulating ripple effects. The function constructs vertical lines at these points and then creates lofted surfaces between them, embodying fluidity and rhythm while adhering to an underlying grid structure. This approach allows for exploration of spatial dynamics and light interaction, aligning with the metaphor's principles of movement and order."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_dimensions, cell_dimensions, wave_parameters, seed=42):
    \"""
    Generates an architectural Concept Model embodying the "rippled grid" metaphor. This model uses an underlying grid 
    framework and creates an undulating surface effect by varying the height of the grid cells according to a ripple pattern.

    Parameters:
    - grid_dimensions: Tuple of two integers (rows, columns), defining the size of the grid.
    - cell_dimensions: Tuple of two floats (cell_width, cell_depth), defining the size of each grid cell in meters.
    - wave_parameters: Tuple of two floats (amplitude, frequency), defining the amplitude and frequency of the ripples.
    - seed: Integer, seed for random number generator to ensure replicable results.

    Returns:
    - List of RhinoCommon Breps representing the 3D geometries of the concept model.
    \"""

    import Rhino.Geometry as rg
    import math
    import random

    random.seed(seed)
    rows, cols = grid_dimensions
    cell_width, cell_depth = cell_dimensions
    amplitude, frequency = wave_parameters

    geometries = []

    # Create grid of base points
    for i in range(rows):
        for j in range(cols):
            x = j * cell_width
            y = i * cell_depth
            # Calculate the z-height using a ripple effect based on the distance from the grid's center
            distance_to_center = math.sqrt((x - (cols * cell_width) / 2) ** 2 + (y - (rows * cell_depth) / 2) ** 2)
            z = amplitude * math.sin(frequency * distance_to_center)

            # Create a base point
            base_point = rg.Point3d(x, y, z)

            # Create a vertical line at each grid point to represent the ripple height
            line = rg.Line(base_point, rg.Point3d(x, y, z + amplitude))
            geometry = line.ToNurbsCurve()
            geometries.append(geometry)

    # Create surfaces between lines using loft
    for i in range(rows - 1):
        for j in range(cols - 1):
            line1 = geometries[i * cols + j]
            line2 = geometries[i * cols + j + 1]
            line3 = geometries[(i + 1) * cols + j + 1]
            line4 = geometries[(i + 1) * cols + j]

            loft_surfaces = rg.Brep.CreateFromLoft([line1, line2, line3, line4], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
            if loft_surfaces:
                geometries.extend(loft_surfaces)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model((10, 10), (1.0, 1.0), (2.0, 0.5))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model((5, 8), (0.5, 0.5), (1.0, 1.0), seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((15, 15), (2.0, 2.0), (3.0, 0.75), seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((8, 12), (1.5, 1.5), (2.5, 1.0))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((6, 6), (1.0, 2.0), (1.5, 2.5), seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
