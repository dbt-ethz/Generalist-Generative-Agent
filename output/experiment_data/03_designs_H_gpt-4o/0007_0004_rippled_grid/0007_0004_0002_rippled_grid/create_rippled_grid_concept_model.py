# Created for 0007_0004_rippled_grid.json

""" Summary:
The provided function generates an architectural concept model inspired by the "rippled grid" metaphor by creating a structured grid with undulating elements. It takes parameters such as grid size, cell dimensions, and ripple characteristics to define the building's geometry. Within nested loops, the function calculates the ripple effect using sine functions, creating dynamic elevations on the grid's vertical walls. This results in a series of curved surfaces that evoke movement while maintaining an organized underlying structure. The output is a list of 3D geometries that embody the interaction between fluidity and order, reflecting the metaphor's essence."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size, cell_size, ripple_amplitude, ripple_frequency, height):
    \"""
    Creates an architectural Concept Model based on the 'rippled grid' metaphor.
    
    This function generates a series of undulating walls that ripple across a grid, 
    maintaining a balance between fluidity and order. The model is constructed 
    using RhinoCommon geometries, focusing on creating a dynamic facade and 
    spatial transition.

    Parameters:
    grid_size (tuple): A tuple of two integers (rows, columns) representing the number of cells in the grid.
    cell_size (float): The size of each grid cell in meters.
    ripple_amplitude (float): The maximum height of the ripple effect in meters.
    ripple_frequency (float): The frequency of the ripple effect, determining the number of undulations.
    height (float): The height of the grid walls in meters.

    Returns:
    List[Rhino.Geometry.Brep]: A list of breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    rows, columns = grid_size
    breps = []

    # Create the base grid structure
    for i in range(rows):
        for j in range(columns):
            x = j * cell_size
            y = i * cell_size
            
            # Calculate the ripple effect
            ripple_effect = ripple_amplitude * math.sin(ripple_frequency * (x + y))

            # Define the corners of the vertical walls with ripple effect
            corner1 = rg.Point3d(x, y, 0)
            corner2 = rg.Point3d(x + cell_size, y, 0)
            corner3 = rg.Point3d(x + cell_size, y, height + ripple_effect)
            corner4 = rg.Point3d(x, y, height + ripple_effect)

            # Create a wall as a surface from the corners
            wall_surface = rg.NurbsSurface.CreateFromCorners(corner1, corner2, corner3, corner4)

            if wall_surface:
                breps.append(wall_surface.ToBrep())

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model((5, 5), 2.0, 1.0, 0.5, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model((10, 10), 1.5, 0.8, 1.0, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((3, 7), 1.0, 0.5, 2.0, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((8, 4), 3.0, 1.5, 0.75, 5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((6, 6), 2.5, 1.2, 1.5, 3.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
