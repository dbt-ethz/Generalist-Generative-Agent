# Created for 0002_0004_cubic_nest.json

""" Summary:
The function `create_cubic_nest_concept_model` generates an architectural concept model that embodies the "Cubic nest" metaphor by creating a matrix-like arrangement of cubic volumes. It utilizes randomization to determine the size and position of cubes within a defined grid, allowing for a diverse yet cohesive composition. Each cube represents individuality while contributing to the overall interconnectedness, mimicking the layered quality of a nest. The use of varying cube sizes and placements promotes exploration and dynamic spatial experiences, while the interplay of solid and void enhances the perception of depth, aligning with the metaphor's essence."""

#! python 3
function_code = """def create_cubic_nest_concept_model(base_size=10, cube_count=5, min_cube_size=2, max_cube_size=4, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Cubic nest' metaphor. The function generates a matrix-like
    arrangement of interwoven cubic volumes that suggest a sense of shelter and interconnectedness.

    Parameters:
    - base_size: The size of the base grid in meters (default is 10).
    - cube_count: The number of cubic volumes to generate (default is 5).
    - min_cube_size: The minimum size of each cube (default is 2 meters).
    - max_cube_size: The maximum size of each cube (default is 4 meters).
    - seed: Random seed for reproducibility (default is 42).

    Returns:
    - A list of RhinoCommon Brep geometries representing the cubic volumes.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(seed)

    # Initialize list to store the resulting Breps
    breps = []

    # Define the base grid as a list of points
    grid_points = [(x, y, z) for x in range(0, base_size, min_cube_size)
                             for y in range(0, base_size, min_cube_size)
                             for z in range(0, base_size, min_cube_size)]

    # Randomly select points from the grid to place cubes
    selected_points = random.sample(grid_points, cube_count)

    for point in selected_points:
        # Randomize the size of the cube within the specified range
        cube_size = random.uniform(min_cube_size, max_cube_size)

        # Create a box (cube) at the given point with the randomized size
        base_plane = rg.Plane(rg.Point3d(*point), rg.Vector3d.ZAxis)
        cube_box = rg.Box(base_plane, rg.Interval(0, cube_size), rg.Interval(0, cube_size), rg.Interval(0, cube_size))
        brep = cube_box.ToBrep()

        # Add the cube to the list of breps
        breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_concept_model(base_size=15, cube_count=10, min_cube_size=3, max_cube_size=6, seed=101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_concept_model(base_size=12, cube_count=8, min_cube_size=1, max_cube_size=5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_concept_model(base_size=20, cube_count=6, min_cube_size=2, max_cube_size=5, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_concept_model(base_size=8, cube_count=4, min_cube_size=1, max_cube_size=3, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_concept_model(base_size=25, cube_count=7, min_cube_size=2, max_cube_size=3, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
