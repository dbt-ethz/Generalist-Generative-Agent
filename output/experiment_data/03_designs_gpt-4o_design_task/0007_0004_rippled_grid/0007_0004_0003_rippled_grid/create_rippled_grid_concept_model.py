# Created for 0007_0004_rippled_grid.json

""" Summary:
The provided function, `create_rippled_grid_concept_model`, generates an architectural concept model embodying the 'rippled grid' metaphor by creating a grid structure with rhythmic undulations. It defines a grid of points, adjusting their vertical positions to introduce ripple effects based on sine functions, which simulate movement and fluidity. The function constructs surfaces between these modified grid points, maintaining a structured layout while showcasing dynamic forms. This approach effectively balances the metaphor's implications of order and fluidity, resulting in a model that reflects the desired spatial relationships and visual impact, aligning with the design task's requirements."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size, grid_spacing, ripple_amplitude, ripple_frequency, basis_height):
    \"""
    Creates an architectural Concept Model based on the 'rippled grid' metaphor.
    The model consists of a grid structure with undulating surfaces that suggest
    movement across a regular grid layout.

    Parameters:
        grid_size (int): The number of grid cells along one dimension of the base grid.
        grid_spacing (float): The distance between adjacent grid lines in meters.
        ripple_amplitude (float): The maximum height of the ripples in meters.
        ripple_frequency (float): The frequency of the ripples.
        basis_height (float): The base height of the grid structure in meters.

    Returns:
        List[Rhino.Geometry.Brep]: A list of brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    # List to store the final brep geometries
    breps = []

    # Create base grid points
    grid_points = []
    for i in range(grid_size + 1):
        row = []
        for j in range(grid_size + 1):
            x = i * grid_spacing
            y = j * grid_spacing
            z = basis_height
            row.append(rg.Point3d(x, y, z))
        grid_points.append(row)

    # Create ripple effect by modifying the z-coordinate of grid points
    for i in range(grid_size + 1):
        for j in range(grid_size + 1):
            point = grid_points[i][j]
            ripple_effect = ripple_amplitude * math.sin(ripple_frequency * (i + j))
            grid_points[i][j] = rg.Point3d(point.X, point.Y, point.Z + ripple_effect)

    # Create surfaces between grid points
    for i in range(grid_size):
        for j in range(grid_size):
            p1 = grid_points[i][j]
            p2 = grid_points[i+1][j]
            p3 = grid_points[i+1][j+1]
            p4 = grid_points[i][j+1]

            # Create a surface patch
            surface = rg.Brep.CreateFromCornerPoints(p1, p2, p3, p4, 0.01)

            # Add created surface to the breps list
            if surface:
                breps.append(surface)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model(10, 1.0, 0.5, 2.0, 0.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model(5, 0.5, 1.0, 3.0, 0.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model(8, 0.75, 0.3, 1.5, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model(6, 2.0, 0.4, 1.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model(12, 1.5, 0.6, 2.5, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
