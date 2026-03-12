# Created for 0011_0002_shifted_grid.json

""" Summary:
The function `create_shifted_grid_concept_model` generates an architectural concept model by transforming a standard grid framework into a dynamic structure that embodies the 'Shifted Grid' metaphor. It achieves this by randomly shifting grid points within specified parameters, creating irregular alignments and staggered volumes. Each volume's height varies, adding vertical dynamism and enhancing the sense of movement. The resulting interconnected spaces encourage exploration and diverse circulation paths, while the interplay of light and shadow is emphasized through the varied orientations and projections of the volumes, fostering unexpected and adaptable spatial experiences."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size, grid_spacing, shift_amount, height_variation):
    \"""
    Creates an architectural Concept Model based on the 'Shifted Grid' metaphor.
    
    Parameters:
    - grid_size (int): The number of cells along one side of the square grid.
    - grid_spacing (float): The distance between grid lines in meters.
    - shift_amount (float): The maximum amount by which grid lines can be shifted.
    - height_variation (float): The range of height variation for the volumes.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Point3d, Line, Brep, Box, Vector3d, Plane, Interval

    # Set a random seed for replicability
    random.seed(42)

    breps = []

    # Create a grid of points
    points = []
    for i in range(grid_size):
        for j in range(grid_size):
            x = i * grid_spacing + random.uniform(-shift_amount, shift_amount)
            y = j * grid_spacing + random.uniform(-shift_amount, shift_amount)
            points.append(Point3d(x, y, 0))

    # Create volumes based on shifted grid points
    for pt in points:
        # Randomly vary the height of each box to create dynamic vertical variation
        height = grid_spacing + random.uniform(-height_variation, height_variation)
        base_plane = Plane(pt, Vector3d.ZAxis)
        x_interval = Interval(0, grid_spacing * 0.9)
        y_interval = Interval(0, grid_spacing * 0.9)
        z_interval = Interval(0, height)
        base = Box(base_plane, x_interval, y_interval, z_interval)

        # Convert the Box to a Brep and add to the list
        brep = base.ToBrep()
        breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(10, 2.0, 1.0, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(8, 1.5, 0.5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(12, 3.0, 1.5, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(6, 2.5, 2.0, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(15, 2.0, 0.8, 5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
