# Created for 0007_0001_rippled_grid.json

""" Summary:
The function `create_rippled_grid_concept_model` generates an architectural concept model based on the "rippled grid" metaphor by creating modular elements that form a dynamically undulating facade. It utilizes a grid framework, manipulating it with a cosine wave function to produce wave-like patterns in the z-axis, which suggests movement and rhythm while maintaining structural order. The parameters allow customization of grid size, module dimensions, and wave characteristics. By generating 3D geometries that embody this concept, the model explores how these ripples influence both the exterior form and interior spatial relationships, enhancing the dynamic quality of the design."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size, module_size, wave_amplitude, wave_length):
    \"""
    Create an architectural Concept Model that embodies the 'rippled grid' metaphor.

    This function generates modular elements forming a rippled surface by employing a grid system
    as the underlying framework. The grid is manipulated to create wave-like patterns, suggesting 
    movement and dynamic qualities while maintaining structural order.

    Parameters:
    - grid_size: Tuple (int, int), defining the number of modules in the grid (rows, columns).
    - module_size: Float, the size of each grid module in meters.
    - wave_amplitude: Float, the amplitude of the wave effect.
    - wave_length: Float, the wave length, affecting the spacing of the ripples.

    Returns:
    - List of RhinoCommon Breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    rows, cols = grid_size
    geometries = []

    # Create the grid and apply ripple effect
    for i in range(rows):
        for j in range(cols):
            # Calculate the base point of the module
            x = i * module_size
            y = j * module_size

            # Calculate the z offset using a cosine wave for ripple effect
            z_offset = wave_amplitude * math.cos((x + y) / wave_length * 2 * math.pi)

            # Define the corners of the module
            corners = [
                rg.Point3d(x, y, z_offset),
                rg.Point3d(x + module_size, y, z_offset),
                rg.Point3d(x + module_size, y + module_size, z_offset),
                rg.Point3d(x, y + module_size, z_offset)
            ]

            # Create a surface from the corners
            surface = rg.NurbsSurface.CreateFromCorners(corners[0], corners[1], corners[2], corners[3])
            if surface:
                geometries.append(surface)

    return geometries"""

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
    geometry = create_rippled_grid_concept_model((5, 8), 0.75, 0.3, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((6, 12), 1.2, 0.4, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((8, 8), 1.5, 0.6, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((4, 6), 2.0, 0.8, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
