# Created for 0002_0004_cubic_nest.json

""" Summary:
The function `create_cubic_nest_model` generates an architectural concept model inspired by the "Cubic nest" metaphor by creating a matrix of cubic forms that vary in size and orientation. It utilizes parameters like base size, height variation, and cube count to produce a diverse arrangement of cubic volumes, reflecting interconnectedness and individuality. Each cube's random placement fosters a layered, protective quality, embodying the essence of a nest. The function employs randomness for reproducibility, ensuring distinct yet cohesive structures. The resulting geometries articulate a dynamic interplay of light and shadow, inviting exploration through their intricate spatial relationships."""

#! python 3
function_code = """def create_cubic_nest_model(base_size, height_variation, cube_count, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Cubic nest' metaphor, using a matrix-like arrangement of cubic volumes.
    
    Parameters:
    - base_size (float): The base size of the cubes in meters.
    - height_variation (float): The maximum variance in cube height to create diversity in vertical arrangement.
    - cube_count (int): The number of cubes to generate in the model.
    - seed (int, optional): The seed for randomness to ensure replicable results. Default is 42.
    
    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(seed)

    # List to store the generated Breps
    geometries = []

    # Create a matrix of cubes
    for i in range(cube_count):
        # Randomly determine the position and height variation of each cube
        x_offset = random.uniform(-base_size, base_size)
        y_offset = random.uniform(-base_size, base_size)
        z_offset = random.uniform(0, height_variation)

        # Define the base point of the cube
        base_point = rg.Point3d(i * base_size + x_offset, i * base_size + y_offset, z_offset)

        # Create the cube as a Brep
        cube = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), rg.Interval(0, base_size), rg.Interval(0, base_size), rg.Interval(0, base_size + random.uniform(-height_variation, height_variation)))

        # Convert the box to a Brep and add to the list
        geometries.append(cube.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_model(5.0, 10.0, 20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_model(3.0, 15.0, 10, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_model(4.0, 8.0, 15, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_model(6.0, 12.0, 25, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_model(2.5, 5.0, 30, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
