# Created for 0002_0003_cubic_nest.json

""" Summary:
The `generate_cubic_nest_model` function creates an architectural concept model based on the 'Cubic nest' metaphor by generating a series of interwoven cubic volumes. Each cube is positioned using random offsets, creating a dynamic arrangement that embodies both enclosure and openness. The function takes parameters like base length, number of cubes, and spacing, allowing for varied configurations that reflect the protective yet interconnected nature of the design. The resulting list of 3D Brep objects represents the complex spatial relationships and individual identities of the cubes, fostering an engaging environment that encourages exploration within the nested structure."""

#! python 3
function_code = """def generate_cubic_nest_model(base_length, num_cubes, cube_spacing, randomness_seed=42):
    \"""
    Generates a 3D architectural concept model based on the 'Cubic nest' metaphor.
    This model consists of interwoven cubic volumes that create a protective and multi-dimensional enclosure.

    Parameters:
        base_length (float): The base length of each cubic module in meters.
        num_cubes (int): The number of cubes to generate in the model.
        cube_spacing (float): The distance between the centers of adjacent cubes.
        randomness_seed (int, optional): Seed for random number generator to ensure replicability. Default is 42.

    Returns:
        list: A list of RhinoCommon Brep objects representing the 3D geometry of the model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Initialize the random seed
    random.seed(randomness_seed)

    # Initialize the list to hold the resulting Breps
    model_breps = []

    # Create cubes and arrange them in a nested pattern
    for i in range(num_cubes):
        # Random offsets to create a sense of interweaving
        x_offset = random.uniform(-cube_spacing/2, cube_spacing/2)
        y_offset = random.uniform(-cube_spacing/2, cube_spacing/2)
        z_offset = random.uniform(-cube_spacing/2, cube_spacing/2)

        # Base point for the cube
        base_point = rg.Point3d(i * cube_spacing + x_offset, y_offset, z_offset)

        # Create a cube (as a Brep) at the base point
        cube_corners = [
            rg.Point3d(base_point.X, base_point.Y, base_point.Z),
            rg.Point3d(base_point.X + base_length, base_point.Y, base_point.Z),
            rg.Point3d(base_point.X + base_length, base_point.Y + base_length, base_point.Z),
            rg.Point3d(base_point.X, base_point.Y + base_length, base_point.Z),
            rg.Point3d(base_point.X, base_point.Y, base_point.Z + base_length),
            rg.Point3d(base_point.X + base_length, base_point.Y, base_point.Z + base_length),
            rg.Point3d(base_point.X + base_length, base_point.Y + base_length, base_point.Z + base_length),
            rg.Point3d(base_point.X, base_point.Y + base_length, base_point.Z + base_length)
        ]

        # Create a Brep from the cube corners
        cube_brep = rg.Brep.CreateFromBox(cube_corners)

        if cube_brep:
            model_breps.append(cube_brep)

    return model_breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cubic_nest_model(2.0, 10, 5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cubic_nest_model(1.5, 15, 3.0, randomness_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cubic_nest_model(3.0, 20, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cubic_nest_model(2.5, 8, 6.0, randomness_seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cubic_nest_model(2.0, 12, 4.0, randomness_seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
