# Created for 0002_0001_cubic_nest.json

""" Summary:
The function `create_cubic_nest_model` generates an architectural concept model based on the "Cubic nest" metaphor by creating a collection of interlocking cubic volumes. Each cube's size and position are randomized within specified parameters, allowing for overlapping and dynamic spatial relationships that reflect the metaphor's essence of shelter and interconnectedness. The interplay of solid and void is emphasized through varying cube sizes and orientations, while the overlap factor enhances the protective qualities of the structure. Ultimately, this algorithm generates a cohesive model that invites exploration and discovery, fulfilling the design task's requirements."""

#! python 3
function_code = """def create_cubic_nest_model(base_cube_size, cube_count, overlap_factor, random_seed):
    \"""
    Creates a 3D architectural Concept Model based on the 'Cubic nest' metaphor using interlocking and overlapping cubic volumes.
    
    Parameters:
    base_cube_size (float): The side length of the base cube in meters.
    cube_count (int): The number of cubes to generate.
    overlap_factor (float): A factor to determine the degree of overlap between cubes (0.0 to 1.0).
    random_seed (int): Seed for random number generation to ensure replicability.
    
    Returns:
    list: A list of Brep geometries representing the interlocking and overlapping cubic volumes.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(random_seed)

    # Initialize an empty list to hold the Brep geometries
    cubes = []

    # Start with a base cube
    base_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_cube_size), rg.Interval(0, base_cube_size), rg.Interval(0, base_cube_size))
    cubes.append(base_cube.ToBrep())

    for _ in range(cube_count - 1):
        # Randomly determine the size of the new cube
        size_factor = random.uniform(0.5, 1.5)
        cube_size = base_cube_size * size_factor

        # Randomly determine the position for the new cube
        x_offset = random.uniform(-cube_size * overlap_factor, cube_size * overlap_factor)
        y_offset = random.uniform(-cube_size * overlap_factor, cube_size * overlap_factor)
        z_offset = random.uniform(-cube_size * overlap_factor, cube_size * overlap_factor)

        # Create a transformation matrix
        translation = rg.Transform.Translation(x_offset, y_offset, z_offset)

        # Create the new cube and transform it
        new_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(0, cube_size), rg.Interval(0, cube_size), rg.Interval(0, cube_size))
        new_cube.Transform(translation)
        
        # Add the transformed cube to the list
        cubes.append(new_cube.ToBrep())

    return cubes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_model(1.0, 10, 0.2, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_model(2.0, 5, 0.3, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_model(0.5, 15, 0.1, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_model(1.5, 20, 0.4, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_model(3.0, 8, 0.5, 33)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
