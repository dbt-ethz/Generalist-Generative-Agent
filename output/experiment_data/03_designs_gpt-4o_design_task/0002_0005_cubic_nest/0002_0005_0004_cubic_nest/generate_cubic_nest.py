# Created for 0002_0005_cubic_nest.json

""" Summary:
The provided function `generate_cubic_nest` translates the 'Cubic nest' metaphor into a tangible architectural concept model by generating a 3D lattice of cubic volumes. Utilizing parameters like cube size, grid size, and height levels, it creates a randomized arrangement of cubes that interlace and stack, reflecting the metaphor's emphasis on complexity and interconnectedness. Each cube is treated as a modular component within a cohesive structure, fostering dynamic spatial experiences. The function ensures variability in design while maintaining the protective and engaging qualities of the 'Cubic nest' framework, inviting exploration through its rhythmic and layered configuration."""

#! python 3
function_code = """def generate_cubic_nest(seed: int, cube_size: float, grid_size: int, height_levels: int) -> list:
    \"""
    Creates an architectural Concept Model based on the 'Cubic nest' metaphor. This model consists of a lattice framework
    of interlaced cubic volumes that emphasize rhythmic arrangement and spatial layering.

    Parameters:
    - seed (int): A seed value for random generation to ensure replicability.
    - cube_size (float): The size of each individual cube in meters.
    - grid_size (int): The number of cubes along one edge of the grid.
    - height_levels (int): The number of vertical stacking levels of cubes.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the seed for randomness
    random.seed(seed)

    # Initialize a list to store the resulting Brep objects
    breps = []

    # Iterate through a 3D grid defined by grid_size and height_levels
    for x in range(grid_size):
        for y in range(grid_size):
            for z in range(height_levels):
                # Determine whether to create a cube at this position
                if random.random() > 0.2:  # 80% chance to create a cube
                    # Define the base point of the cube
                    base_point = rg.Point3d(x * cube_size, y * cube_size, z * cube_size)
                    # Create the cube (as a Brep box)
                    box = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), rg.Interval(0, cube_size), rg.Interval(0, cube_size), rg.Interval(0, cube_size))
                    brep = box.ToBrep()
                    breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cubic_nest(seed=42, cube_size=1.0, grid_size=5, height_levels=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cubic_nest(seed=7, cube_size=0.5, grid_size=4, height_levels=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cubic_nest(seed=21, cube_size=2.0, grid_size=6, height_levels=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cubic_nest(seed=15, cube_size=1.5, grid_size=3, height_levels=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cubic_nest(seed=10, cube_size=0.8, grid_size=7, height_levels=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
