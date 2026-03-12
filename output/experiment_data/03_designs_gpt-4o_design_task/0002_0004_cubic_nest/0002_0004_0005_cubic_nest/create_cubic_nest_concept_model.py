# Created for 0002_0004_cubic_nest.json

""" Summary:
The function `create_cubic_nest_concept_model` generates an architectural concept model inspired by the "Cubic nest" metaphor by creating a series of interconnected cubic volumes. Each cube's size, position, and height are randomly varied to create a dynamic arrangement that emphasizes both individuality and collective harmony. The model's design incorporates a layered and protective quality, allowing for open and enclosed spaces that encourage movement and interaction. By manipulating the geometry and materials, the function articulates light and shadow, fostering an exploratory environment that reflects the interconnected nature of the 'nest.'"""

#! python 3
function_code = """def create_cubic_nest_concept_model(base_size, height_variation, cube_count, seed):
    \"""
    Create an architectural Concept Model based on the 'Cubic nest' metaphor.

    This function generates a pattern of interconnected cubic volumes that vary in size and 
    orientation, emphasizing their protective and layered quality. The model is organized into 
    clusters that suggest both individuality and collective harmony, promoting movement and 
    interaction within and between the cubic forms.

    Parameters:
    - base_size (float): The base size for the cubes in meters.
    - height_variation (float): The maximum variation in height for the cubes.
    - cube_count (int): The number of cubes to generate in the model.
    - seed (int): A seed for the random number generator to ensure replicability.

    Returns:
    - list: A list of Rhino.Geometry.Brep objects representing the 3D geometry of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for replicability
    random.seed(seed)

    # Initialize the list to store cube geometries
    geometries = []

    for _ in range(cube_count):
        # Randomly vary the size of the cube
        size_variation = random.uniform(-0.5, 0.5) * base_size
        cube_size = base_size + size_variation

        # Randomly vary the position and height of the cube
        x_offset = random.uniform(-0.5, 0.5) * base_size
        y_offset = random.uniform(-0.5, 0.5) * base_size
        z_offset = random.uniform(0, height_variation)

        # Create the base point of the cube
        base_point = rg.Point3d(x_offset, y_offset, z_offset)

        # Create the cube as a Brep
        cube = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), rg.Interval(0, cube_size), rg.Interval(0, cube_size), rg.Interval(0, cube_size)).ToBrep()

        # Add the cube to the list of geometries
        geometries.append(cube)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_concept_model(2.0, 3.0, 10, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_concept_model(1.5, 2.0, 15, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_concept_model(3.0, 5.0, 20, 100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_concept_model(2.5, 4.0, 12, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_concept_model(1.0, 1.0, 8, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
