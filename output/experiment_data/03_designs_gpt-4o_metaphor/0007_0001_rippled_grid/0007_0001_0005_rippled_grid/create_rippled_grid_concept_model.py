# Created for 0007_0001_rippled_grid.json

""" Summary:
The function `create_rippled_grid_concept_model` translates the "rippled grid" metaphor into a 3D architectural model by generating a structured grid with undulating surfaces. It uses sine wave functions to create height variations (ripples) across a specified grid size, cell size, amplitude, and frequency. Each grid cell is represented by a box whose height fluctuates based on the sine wave, embodying the metaphor's dynamic and rhythmic qualities while maintaining an organized structure. This results in a visually engaging model that reflects movement and flow, suitable for architectural design exploration."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size, cell_size, amplitude, frequency):
    \"""
    Creates an architectural Concept Model based on the metaphor 'rippled grid'.
    
    The model consists of a structured grid with undulating surfaces that simulate the effect of ripples.
    The ripples are generated using a sine wave function applied across the grid.

    Parameters:
    - grid_size: Tuple of two integers (rows, columns) representing the number of cells in the grid.
    - cell_size: Float representing the size of each grid cell in meters.
    - amplitude: Float representing the maximum height variation of the ripple in meters.
    - frequency: Float representing the number of wave cycles across a single dimension of the grid.

    Returns:
    - List of RhinoCommon Breps representing the 3D geometry of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import math

    rows, cols = grid_size
    geometries = []

    # Loop through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # Calculate the center of the current cell
            x = j * cell_size
            y = i * cell_size

            # Calculate the z-coordinate using a sine wave function
            z = amplitude * math.sin(frequency * (x + y))

            # Create a box at this location with a ripple effect
            base_plane = rg.Plane(rg.Point3d(x, y, z), rg.Vector3d.ZAxis)
            box = rg.Box(base_plane, rg.Interval(0, cell_size), rg.Interval(0, cell_size), rg.Interval(0, amplitude))

            # Convert the box to a Brep and add to the list
            geometries.append(box.ToBrep())

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
    geometry = create_rippled_grid_concept_model((5, 8), 0.75, 1.0, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((15, 15), 0.5, 0.3, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((7, 12), 0.6, 0.8, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((6, 9), 0.9, 0.4, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
