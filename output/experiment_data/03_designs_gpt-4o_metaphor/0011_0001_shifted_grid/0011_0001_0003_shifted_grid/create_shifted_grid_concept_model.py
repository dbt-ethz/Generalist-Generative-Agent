# Created for 0011_0001_shifted_grid.json

""" Summary:
The provided function generates an architectural concept model based on the "shifted grid" metaphor, which emphasizes dynamic reconfiguration of traditional layouts. It creates a series of vertical and horizontal grid lines that are randomly shifted within defined limits, establishing an innovative and fluid spatial arrangement. By adjusting parameters such as grid size, base size, and shift amount, the function produces varied geometric outputs that embody movement, adaptability, and interaction with light and shadow. The resulting 3D geometries foster diverse spatial experiences and circulation paths, thus embodying the metaphor's key traits in the architectural design."""

#! python 3
function_code = """def create_shifted_grid_concept_model(base_size, grid_size, shift_amount, height, random_seed):
    \"""
    Creates an architectural Concept Model based on a shifted grid metaphor.

    Args:
    - base_size (float): The size of the base square grid in meters.
    - grid_size (int): The number of grid units along one edge of the base grid.
    - shift_amount (float): The maximum distance in meters that grid lines can be shifted.
    - height (float): The height of the vertical elements in the model.
    - random_seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(random_seed)

    # Initialize list to store the breps
    breps = []

    # Calculate the spacing of the grid lines
    spacing = base_size / grid_size

    # Create vertical shifted grid walls
    for i in range(grid_size + 1):
        for j in range(grid_size + 1):
            # Calculate the base position of the grid line
            base_x = i * spacing
            base_y = j * spacing

            # Apply a random shift within the specified range
            shift_x = random.uniform(-shift_amount, shift_amount)
            shift_y = random.uniform(-shift_amount, shift_amount)

            # Create the start and end points of the shifted grid line
            start_point = rg.Point3d(base_x + shift_x, 0, 0)
            end_point = rg.Point3d(base_x + shift_x, base_size, 0)

            # Create a vertical plane surface for the grid line
            plane = rg.Plane(start_point, rg.Vector3d(0, 1, 0))
            rect = rg.Rectangle3d(plane, rg.Interval(-0.1, 0.1), rg.Interval(0, height))
            vertical_surface = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(rect.ToNurbsCurve(), rg.Vector3d(0, 0, 1)))

            breps.append(vertical_surface)

            # Create horizontal shifted grid walls
            start_point = rg.Point3d(0, base_y + shift_y, 0)
            end_point = rg.Point3d(base_size, base_y + shift_y, 0)

            # Create a vertical plane surface for the grid line
            plane = rg.Plane(start_point, rg.Vector3d(1, 0, 0))
            rect = rg.Rectangle3d(plane, rg.Interval(-0.1, 0.1), rg.Interval(0, height))
            horizontal_surface = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(rect.ToNurbsCurve(), rg.Vector3d(0, 0, 1)))

            breps.append(horizontal_surface)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(10.0, 5, 2.0, 3.0, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(15.0, 4, 1.5, 5.0, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(12.0, 6, 3.0, 4.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(8.0, 3, 1.0, 2.5, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(20.0, 7, 3.5, 6.0, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
