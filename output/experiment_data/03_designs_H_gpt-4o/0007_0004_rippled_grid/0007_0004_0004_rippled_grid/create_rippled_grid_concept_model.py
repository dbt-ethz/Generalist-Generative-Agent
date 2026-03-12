# Created for 0007_0004_rippled_grid.json

""" Summary:
The provided function, `create_rippled_grid_concept_model`, generates an architectural concept model inspired by the "rippled grid" metaphor. It creates a structured grid using specified dimensions and spacing while introducing undulating surfaces that mimic the fluidity and movement of ripples. By applying sine functions, the function generates wave-like deformations either along the x or y-axis, resulting in curved geometries that maintain an underlying order. The output is a collection of Brep geometries that visually embody the rhythmic dynamics of the metaphor, effectively balancing the structured grid with flowing forms to enhance spatial transitions and overall aesthetic impact."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size, grid_spacing, ripple_amplitude, ripple_frequency, wave_direction='x'):
    \"""
    Creates an architectural Concept Model based on the 'rippled grid' metaphor.
    
    This function generates a model using a base grid structure with undulating elements
    that ripple across the grid. The model maintains an ordered grid while introducing
    fluidity through wave-like surfaces.

    Parameters:
        grid_size (tuple): A tuple of two integers (rows, columns) representing the number of cells in the grid.
        grid_spacing (float): The distance between adjacent grid nodes in meters.
        ripple_amplitude (float): The maximum height of the ripple effect in meters.
        ripple_frequency (float): The frequency of the ripple effect.
        wave_direction (str): Direction of the wave ('x' or 'y'). Determines along which axis the ripple primarily propagates.

    Returns:
        List[Rhino.Geometry.Brep]: A list of brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    rows, columns = grid_size
    breps = []

    # Generate grid points
    grid_points = []
    for i in range(rows + 1):
        row_points = []
        for j in range(columns + 1):
            x = j * grid_spacing
            y = i * grid_spacing
            z = 0
            if wave_direction == 'x':
                z = ripple_amplitude * math.sin(ripple_frequency * x)
            elif wave_direction == 'y':
                z = ripple_amplitude * math.sin(ripple_frequency * y)
            row_points.append(rg.Point3d(x, y, z))
        grid_points.append(row_points)

    # Create surfaces with the ripple effect
    for i in range(rows):
        for j in range(columns):
            p1 = grid_points[i][j]
            p2 = grid_points[i][j + 1]
            p3 = grid_points[i + 1][j + 1]
            p4 = grid_points[i + 1][j]

            # Create a surface patch
            try:
                surface = rg.Brep.CreateFromCornerPoints(p1, p2, p3, p4, 0.01)
                if surface:
                    breps.append(surface)
            except:
                continue

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model((10, 10), 1.0, 0.5, 2.0, wave_direction='x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model((5, 8), 0.5, 0.3, 1.5, wave_direction='y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((6, 6), 0.8, 0.4, 3.0, wave_direction='x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((7, 9), 0.75, 0.6, 1.0, wave_direction='y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((12, 15), 0.6, 0.7, 2.5, wave_direction='x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
