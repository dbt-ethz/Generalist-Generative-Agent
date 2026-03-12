# Created for 0007_0003_rippled_grid.json

""" Summary:
The provided function generates an architectural concept model by interpreting the 'rippled grid' metaphor through a structured series of undulating surfaces. It creates a grid-based layout, applying a cosine wave to determine the height variations, thus generating ripples that reflect dynamic movement. The parameters allow for customization of grid size, spacing, ripple height, and number of layers, ensuring a visual interplay between structured order and fluidity. This design captures the metaphor's essence by emphasizing transitions between areas of compression and openness, while maintaining an underlying grid structure that evokes a sense of rhythm and flow throughout the architectural model."""

#! python 3
function_code = """def create_rippled_grid_surface(grid_size, grid_spacing, ripple_height, wave_frequency, layer_thickness, num_layers):
    \"""
    Generates an architectural Concept Model based on the 'rippled grid' metaphor.

    This function creates a series of undulating surfaces that follow a ripple pattern 
    across a structured grid, generating a visual dynamic of peaks and troughs while 
    preserving the underlying grid structure.

    Parameters:
    - grid_size (tuple): Number of grid divisions as (rows, columns).
    - grid_spacing (float): The distance between each grid line in meters.
    - ripple_height (float): Maximum height variation of the ripple effect in meters.
    - wave_frequency (float): The frequency of the ripples across the grid.
    - layer_thickness (float): The vertical distance between each layer in meters.
    - num_layers (int): The number of layers to generate.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the rippled surfaces.
    \"""
    import Rhino.Geometry as rg
    import math

    rows, cols = grid_size
    surfaces = []

    for layer in range(num_layers):
        points = []
        for i in range(rows + 1):
            for j in range(cols + 1):
                # Create a ripple effect using a cosine wave
                x = i * grid_spacing
                y = j * grid_spacing
                z = ripple_height * math.cos(wave_frequency * (x + y)) + layer * layer_thickness
                points.append(rg.Point3d(x, y, z))
        
        # Create a nurbs surface from the grid of points
        if len(points) >= (rows + 1) * (cols + 1):
            nurbs_surface = rg.NurbsSurface.CreateFromPoints(points, rows + 1, cols + 1, 3, 3)
            if nurbs_surface:
                surfaces.append(nurbs_surface.ToBrep())

    return surfaces"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_surface((10, 10), 1.0, 2.0, 0.5, 0.1, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_surface((8, 12), 0.5, 1.5, 1.0, 0.2, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_surface((5, 15), 0.75, 3.0, 0.8, 0.15, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_surface((6, 6), 0.8, 2.5, 1.2, 0.3, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_surface((12, 8), 1.5, 4.0, 0.6, 0.25, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
