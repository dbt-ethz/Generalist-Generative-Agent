# Created for 0007_0003_rippled_grid.json

""" Summary:
The function `create_rippled_grid_concept_model` generates an architectural concept model based on the "rippled grid" metaphor by creating a series of layered, undulating surfaces across a defined grid. It takes parameters for grid size, ripple amplitude, frequency, and the number of layers. Using sine functions, it simulates the ripple effects, producing dynamic heights that reflect the metaphor's essence of fluidity and rhythm. Each layer is constructed as a Nurbs surface, maintaining the underlying grid structure while capturing the interplay between order and movement. The resulting geometries embody the concept of peaks and troughs, emphasizing spatial transitions."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size, ripple_amplitude, ripple_frequency, layer_count):
    \"""
    Creates an architectural Concept Model embodying the 'rippled grid' metaphor.

    This function generates a series of layered, undulating surfaces across a grid, capturing the 
    rhythmic movement of ripple effects while maintaining the underlying grid structure.

    Inputs:
    - grid_size: Tuple (int, int) representing the number of grid units in the x and y directions.
    - ripple_amplitude: Float representing the maximum height of the ripple effect.
    - ripple_frequency: Float representing the frequency of the ripple effect.
    - layer_count: Integer representing the number of layers or planes to generate.

    Outputs:
    - A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    random.seed(42)  # Ensure replicable randomness

    # Unpack grid dimensions
    x_count, y_count = grid_size

    # Calculate grid spacing
    grid_spacing = 10.0  # in meters, can be adjusted based on design needs

    # List to store generated Breps
    breps = []

    # Create layered planes with ripple effect
    for layer in range(layer_count):
        # Calculate vertical offset for each layer
        z_offset = layer * (ripple_amplitude / layer_count)

        # Create a surface for each layer
        points = []
        for i in range(x_count + 1):
            for j in range(y_count + 1):
                # Calculate the ripple effect height
                ripple_height = ripple_amplitude * math.sin((i + j) * ripple_frequency + layer)
                # Create points with ripple effect
                point = rg.Point3d(i * grid_spacing, j * grid_spacing, z_offset + ripple_height)
                points.append(point)

        # Create a nurbs surface from the grid of points
        nurbs_surface = rg.NurbsSurface.CreateFromPoints(points, x_count + 1, y_count + 1, 3, 3)
        breps.append(nurbs_surface.ToBrep())

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model((5, 5), 2.0, 0.5, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model((8, 6), 1.5, 0.8, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((10, 10), 3.0, 1.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((7, 4), 1.0, 0.3, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((4, 4), 2.5, 0.9, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
