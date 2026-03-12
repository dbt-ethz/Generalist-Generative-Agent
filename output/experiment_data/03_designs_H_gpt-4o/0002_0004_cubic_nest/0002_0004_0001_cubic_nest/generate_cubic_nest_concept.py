# Created for 0002_0004_cubic_nest.json

""" Summary:
The provided function, `generate_cubic_nest_concept`, creates an architectural concept model inspired by the "Cubic nest" metaphor. It arranges cubic volumes in a matrix-like grid, varying their sizes and orientations to enhance individuality while maintaining collective harmony. Through parameters like `cube_variation` and `overlap_factor`, the function generates a layered structure that suggests shelter and interconnectedness. By using random offsets, it promotes dynamic spatial relationships, encouraging exploration. The result is a cohesive architectural composition where each cube contributes to a complex interplay of solid and void, embodying the essence of a protective and inviting "nest.""""

#! python 3
function_code = """def generate_cubic_nest_concept(base_size, grid_size, cube_variation, overlap_factor, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Cubic nest' metaphor.

    This function generates a pattern of interconnected cubic volumes arranged in
    a grid. The cubes vary in size, orientation, and overlap to create a layered
    and protective quality, emphasizing individuality and collective harmony. The
    model invites exploration and interaction through its dynamic spatial composition.

    Parameters:
    - base_size (float): The base size for the cubes in meters.
    - grid_size (int): The number of cubes in one dimension of the grid (grid_size x grid_size).
    - cube_variation (float): The maximum variation in size for the cubes.
    - overlap_factor (float): The factor determining how much cubes can overlap.
    - seed (int): A seed for the random number generator to ensure replicability.

    Returns:
    - list: A list of Rhino.Geometry.Brep objects representing the 3D geometry of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set random seed for replicability
    random.seed(seed)

    # Initialize the list to store cube geometries
    geometries = []

    # Calculate the grid spacing
    grid_spacing = base_size * (1 - overlap_factor)

    for i in range(grid_size):
        for j in range(grid_size):
            # Randomly vary the size of the cube
            size_variation = random.uniform(-cube_variation, cube_variation)
            cube_size = base_size + size_variation

            # Calculate the base point with a random offset
            x_offset = i * grid_spacing + random.uniform(-cube_variation, cube_variation)
            y_offset = j * grid_spacing + random.uniform(-cube_variation, cube_variation)
            z_offset = random.uniform(-cube_variation, cube_variation)

            # Create the base point of the cube
            base_point = rg.Point3d(x_offset, y_offset, z_offset)
            
            # Define the cube as a Box (which can be converted to a Brep)
            box = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), 
                         rg.Interval(0, cube_size), 
                         rg.Interval(0, cube_size), 
                         rg.Interval(0, cube_size))

            # Convert the Box to a Brep for output
            cube_brep = box.ToBrep()

            # Append the cube Brep to the list
            geometries.append(cube_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cubic_nest_concept(base_size=2.0, grid_size=5, cube_variation=0.5, overlap_factor=0.2, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cubic_nest_concept(base_size=1.5, grid_size=4, cube_variation=0.3, overlap_factor=0.1, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cubic_nest_concept(base_size=3.0, grid_size=6, cube_variation=0.8, overlap_factor=0.3, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cubic_nest_concept(base_size=2.5, grid_size=3, cube_variation=0.4, overlap_factor=0.15, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cubic_nest_concept(base_size=1.0, grid_size=7, cube_variation=0.6, overlap_factor=0.25, seed=55)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
