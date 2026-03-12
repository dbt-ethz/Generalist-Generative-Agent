# Created for 0007_0003_rippled_grid.json

""" Summary:
The function `create_rippled_grid_model` generates an architectural concept model by translating the 'rippled grid' metaphor into a series of undulating surfaces across a structured grid. It takes parameters such as grid size, cell dimensions, ripple amplitude, and layer count to create a visually dynamic model. The function uses mathematical sine and cosine functions to simulate the ripple effect, producing a 3D geometry that maintains the underlying grid structure while showcasing fluidity and rhythm. This approach captures the essence of movement and flow, reflecting the interplay between order and dynamism in architectural design."""

#! python 3
function_code = """def create_rippled_grid_model(grid_size, cell_size, ripple_amplitude, layer_count):
    \"""
    Creates an architectural Concept Model based on the 'rippled grid' metaphor using a series of layered planes
    that undulate across a grid. The function captures the rhythmic movement of the ripple effect while maintaining
    the underlying grid structure.

    Parameters:
    grid_size (tuple): The size of the grid in terms of number of cells (rows, columns).
    cell_size (float): The size of each grid cell in meters.
    ripple_amplitude (float): The maximum height variation of the ripple effect in meters.
    layer_count (int): The number of layered planes to generate.

    Returns:
    list: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set a seed for randomness to ensure replicable results
    random.seed(42)

    rows, cols = grid_size
    breps = []

    for layer in range(layer_count):
        # Create a base surface for the current layer
        base_points = []
        for i in range(rows + 1):
            for j in range(cols + 1):
                # Calculate the ripple effect for each point
                ripple_effect = ripple_amplitude * (random.random() - 0.5)
                z = ripple_effect * math.sin(i * 0.5) * math.cos(j * 0.5)
                point = rg.Point3d(j * cell_size, i * cell_size, z + layer * ripple_amplitude / 2)
                base_points.append(point)

        # Create a surface from the point grid
        surface = rg.NurbsSurface.CreateFromPoints(base_points, rows + 1, cols + 1, 3, 3)
        
        # Convert the surface to a Brep
        brep = surface.ToBrep()
        breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_model((10, 10), 1.0, 0.5, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_model((8, 12), 0.75, 0.3, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_model((15, 15), 2.0, 0.8, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_model((12, 8), 1.5, 0.6, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_model((20, 5), 2.5, 1.0, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
