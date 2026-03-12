# Created for 0011_0003_shifted_grid.json

""" Summary:
The provided function generates an architectural concept model based on the "Shifted Grid" metaphor by creating a non-linear grid structure with dynamically shifted and rotated elements. It begins with a conventional grid, introducing variations in alignment and height to each cell, producing unexpected intersections and a layered silhouette. As a result, the model emphasizes fluidity and complexity, fostering unique circulation paths and distinct spatial experiences. By manipulating light and shadow through angled surfaces, the design reflects adaptability and flexibility, allowing for diverse functions and playful interactions, ultimately inviting exploration and discovery within the space."""

#! python 3
function_code = """def create_shifted_grid_concept_model(alignment_variation=0.3, height_variation=2.0, grid_dim=5, grid_cell_size=5.0):
    \"""
    Creates an architectural Concept Model based on the 'Shifted Grid' metaphor.
    This function generates a non-linear grid structure with shifted and rotated elements
    to produce dynamic interwoven spaces that manipulate light and shadow.

    Parameters:
    alignment_variation (float): The maximum variation in grid alignment, in meters.
    height_variation (float): The maximum variation in height for different grid elements, in meters.
    grid_dim (int): The number of cells along each grid axis (x and y).
    grid_cell_size (float): The size of each grid cell in meters.

    Returns:
    list: A list of RhinoCommon.Brep objects representing the 3D geometries of the model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set a random seed for reproducibility
    random.seed(42)

    # List to store the resulting Breps
    breps = []

    # Create a grid of surfaces with varying heights and shifts
    for i in range(grid_dim):
        for j in range(grid_dim):
            # Base coordinates for the grid cell
            base_x = i * grid_cell_size
            base_y = j * grid_cell_size

            # Random shift for each cell
            shift_x = random.uniform(-alignment_variation, alignment_variation)
            shift_y = random.uniform(-alignment_variation, alignment_variation)

            # Random height for each cell
            cell_height = grid_cell_size + random.uniform(-height_variation, height_variation)

            # Create a base plane for the cell
            plane = rg.Plane(rg.Point3d(base_x + shift_x, base_y + shift_y, 0), rg.Vector3d.ZAxis)

            # Create a rectangle and extrude it to form a Brep
            rect = rg.Rectangle3d(plane, grid_cell_size, grid_cell_size)
            extrusion = rg.Extrusion.Create(rect.ToNurbsCurve(), cell_height, True)
            brep = extrusion.ToBrep()

            # Add the Brep to the list
            breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(alignment_variation=0.5, height_variation=3.0, grid_dim=4, grid_cell_size=6.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(alignment_variation=0.2, height_variation=1.5, grid_dim=6, grid_cell_size=4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(alignment_variation=0.4, height_variation=2.5, grid_dim=3, grid_cell_size=7.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(alignment_variation=0.1, height_variation=1.0, grid_dim=7, grid_cell_size=3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(alignment_variation=0.6, height_variation=2.0, grid_dim=5, grid_cell_size=5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
