# Created for 0007_0003_rippled_grid.json

""" Summary:
The provided function generates an architectural concept model inspired by the "rippled grid" metaphor. It creates a series of layered surfaces that undulate across a structured grid, capturing the rhythmic movement of ripples while maintaining visible grid patterns. Each layer is calculated based on parameters such as ripple amplitude and wave frequency to create variations in height, resulting in a dynamic facade or roofline. The model emphasizes the interplay of order and fluidity, with spaces arranged to reflect the expansion and contraction suggested by the ripples, showcasing a harmonious blend of peaks and troughs that evoke movement and cohesion."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size, cell_size, ripple_amplitude, wave_frequency, wave_phase, layer_count):
    \"""
    Creates an architectural Concept Model embodying the 'rippled grid' metaphor by generating a series of layered surfaces
    that undulate across a grid, capturing rhythmic movement while maintaining a visible grid structure.

    Parameters:
    - grid_size (tuple): The number of subdivisions in the grid (rows, columns).
    - cell_size (float): The size of each grid cell in meters.
    - ripple_amplitude (float): The maximum height variation of the ripple effect in meters.
    - wave_frequency (float): The frequency of the ripple effect.
    - wave_phase (float): The phase shift applied to the ripple effect.
    - layer_count (int): The number of layered planes to generate.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    from math import cos

    # Initialize the list to store the generated Breps
    breps = []

    # Generate layered planes with ripple effect
    for layer in range(layer_count):
        # Calculate vertical offset for each layer
        z_offset = layer * (ripple_amplitude / layer_count)

        # Create a surface for each layer
        points = []
        for i in range(grid_size[0] + 1):
            for j in range(grid_size[1] + 1):
                # Calculate the ripple effect height using a cosine wave
                ripple_height = ripple_amplitude * cos(wave_frequency * (i * cell_size + j * cell_size) + wave_phase)
                # Create points with ripple effect and vertical offset
                point = rg.Point3d(i * cell_size, j * cell_size, z_offset + ripple_height)
                points.append(point)

        # Create a Nurbs surface from the grid of points
        nurbs_surface = rg.NurbsSurface.CreateFromPoints(points, grid_size[0] + 1, grid_size[1] + 1, 3, 3)
        if nurbs_surface:
            breps.append(nurbs_surface.ToBrep())

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model((10, 10), 1.0, 0.5, 2.0, 0.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model((8, 12), 0.75, 0.3, 1.5, 1.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((5, 5), 2.0, 0.7, 3.0, 0.5, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((15, 15), 1.5, 0.4, 2.5, 0.2, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((6, 8), 1.2, 0.6, 2.8, 0.1, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
