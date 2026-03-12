# Created for 0007_0004_rippled_grid.json

""" Summary:
The function `create_rippled_grid_concept_model` generates an architectural concept model that embodies the 'rippled grid' metaphor by creating a 3D grid structure with rhythmic undulations. It establishes an organized grid as the foundation, then applies a sine function to determine the ripple effect, which introduces dynamic, curved surfaces that suggest movement. Each cell's top surface is rippled while maintaining an underlying grid structure, ensuring spatial coherence. The result is a series of interconnected volumes that visually and spatially reflect the metaphor, highlighting the balance between structure and fluidity in the building's design."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size, cell_size, ripple_amplitude, ripple_frequency, ripple_depth):
    \"""
    Creates an architectural Concept Model based on the 'rippled grid' metaphor.

    The function generates a 3D grid structure with volumetric ripple elements that introduce 
    a dynamic and rhythmic quality to the grid. The model maintains an underlying grid organization,
    where the ripple effect creates a sense of movement and fluidity.

    Parameters:
    grid_size (tuple): A tuple of two integers (rows, columns) representing the number of cells in the grid.
    cell_size (float): The size of each grid cell in meters.
    ripple_amplitude (float): The maximum vertical extent of the ripple effect in meters.
    ripple_frequency (float): The frequency of the ripple effect, determining the number of undulations.
    ripple_depth (float): The depth of the ripple effect, extending below the grid plane.

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

            # Calculate the ripple effect using a sine function
            ripple_effect = ripple_amplitude * math.sin(ripple_frequency * (x + y))

            # Create a box with a rippled top surface
            base_point = rg.Point3d(x, y, -ripple_depth)
            box_corners = [
                base_point,
                rg.Point3d(x + cell_size, y, -ripple_depth),
                rg.Point3d(x + cell_size, y + cell_size, -ripple_depth),
                rg.Point3d(x, y + cell_size, -ripple_depth),
                rg.Point3d(x, y, ripple_effect),
                rg.Point3d(x + cell_size, y, ripple_effect),
                rg.Point3d(x + cell_size, y + cell_size, ripple_effect),
                rg.Point3d(x, y + cell_size, ripple_effect)
            ]

            # Create a box using the 8 corner points
            box = rg.Box(rg.BoundingBox(box_corners))
            breps.append(box.ToBrep())

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model((5, 5), 2.0, 1.0, 0.5, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model((10, 10), 1.0, 0.5, 1.0, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((8, 8), 1.5, 0.8, 0.3, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((6, 4), 3.0, 1.5, 0.7, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((7, 3), 1.2, 0.6, 1.5, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
