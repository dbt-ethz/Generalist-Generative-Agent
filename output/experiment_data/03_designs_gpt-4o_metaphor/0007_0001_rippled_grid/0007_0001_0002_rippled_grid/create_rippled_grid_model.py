# Created for 0007_0001_rippled_grid.json

""" Summary:
The function `create_rippled_grid_model` generates a 3D architectural concept model inspired by the metaphor of a "rippled grid." By manipulating grid parameters such as size, cell dimensions, amplitude, and frequency, the code creates a series of undulating surfaces that reflect the dynamic, rhythmic quality of waves. Each surface is defined by its corner points, which are calculated using sine functions to simulate a ripple effect, thus producing a structured yet fluid design. This results in visually compelling geometry that embodies the metaphor's essence, creating a harmonious blend of order and movement in architectural form."""

#! python 3
function_code = """def create_rippled_grid_model(grid_size, cell_size, amplitude, frequency):
    \"""
    Creates a 3D architectural Concept Model based on the 'rippled grid' metaphor.
    
    This function generates a series of undulating surfaces on a regular grid, 
    mimicking the effect of ripples propagating across the grid. The ripples 
    introduce a dynamic and rhythmic spatial quality to the model.

    Parameters:
    grid_size (tuple): The number of cells in the grid as (rows, columns).
    cell_size (float): The size of each cell in meters.
    amplitude (float): The maximum height of the ripple effect.
    frequency (float): The number of ripples across the grid.

    Returns:
    list: A list of RhinoCommon Brep objects representing the 3D geometry.
    \"""
    import Rhino.Geometry as rg
    import math

    rows, cols = grid_size
    geometries = []

    for i in range(rows):
        for j in range(cols):
            # Calculate the center of the current cell
            x = j * cell_size
            y = i * cell_size

            # Create a grid point with a ripple effect
            z = amplitude * math.sin(frequency * (x + y))

            # Define the corners of the cell as a rectangle
            start_point = rg.Point3d(x, y, z)
            end_point = rg.Point3d(x + cell_size, y + cell_size, z)
            rectangle = rg.Rectangle3d(rg.Plane.WorldXY, start_point, end_point)

            # Convert the rectangle to a surface
            surface = rg.Brep.CreateFromCornerPoints(
                rg.Point3d(rectangle.Corner(0).X, rectangle.Corner(0).Y, amplitude * math.sin(frequency * (rectangle.Corner(0).X + rectangle.Corner(0).Y))),
                rg.Point3d(rectangle.Corner(1).X, rectangle.Corner(1).Y, amplitude * math.sin(frequency * (rectangle.Corner(1).X + rectangle.Corner(1).Y))),
                rg.Point3d(rectangle.Corner(2).X, rectangle.Corner(2).Y, amplitude * math.sin(frequency * (rectangle.Corner(2).X + rectangle.Corner(2).Y))),
                rg.Point3d(rectangle.Corner(3).X, rectangle.Corner(3).Y, amplitude * math.sin(frequency * (rectangle.Corner(3).X + rectangle.Corner(3).Y))),
                0.01
            )

            if surface:
                geometries.append(surface)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_model((10, 10), 1.0, 0.5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_model((5, 8), 2.0, 1.0, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_model((4, 6), 1.5, 0.7, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_model((6, 12), 0.5, 0.3, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_model((8, 8), 1.2, 0.8, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
