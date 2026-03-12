# Created for 0002_0002_cubic_nest.json

""" Summary:
The function `create_cubic_nest_model_v2` generates an architectural concept model inspired by the "Cubic nest" metaphor by creating a series of interlocking cubic volumes. It establishes a base cube and adds layers of cubes, each with a variable size and random offsets, enhancing the design's complexity and interconnectedness. The overlap factor allows cubes to nest and intertwine, fostering a sense of protection and inviting exploration. By varying cube dimensions and orientations, the function embodies the metaphor's themes of shelter and dynamic spatial relationships, resulting in a visually intricate model that reflects the essence of the design task provided."""

#! python 3
function_code = """def create_cubic_nest_model_v2(base_size, layers, overlap_factor, randomness_seed):
    \"""
    Create an architectural Concept Model using the 'Cubic Nest' metaphor
    with nested and interlocking cubic volumes.

    Parameters:
    - base_size (float): The size of the base cube in meters.
    - layers (int): Number of layers of interlocking cubes.
    - overlap_factor (float): Factor determining overlap between cubes (0 to 1).
    - randomness_seed (int): Seed for random number generator to ensure reproducibility.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the cubic volumes.
    \"""
    import Rhino.Geometry as rg
    import random

    # Seed the random number generator for reproducibility
    random.seed(randomness_seed)

    # List to store resulting Breps
    breps = []

    # Define initial cube
    initial_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(-base_size/2, base_size/2),
                          rg.Interval(-base_size/2, base_size/2), rg.Interval(-base_size/2, base_size/2))
    breps.append(initial_cube.ToBrep())

    # Iterate to create layers of cubes
    for layer in range(1, layers + 1):
        # Calculate size and offset for current layer
        cube_size = base_size + base_size * overlap_factor * layer
        offset = cube_size * 0.1

        # Randomize offset for dynamic overlapping
        dx = random.uniform(-offset, offset)
        dy = random.uniform(-offset, offset)
        dz = random.uniform(-offset, offset)

        # Create transform for the current cube
        translation = rg.Transform.Translation(dx, dy, dz)

        # Create a new cube and apply the transformation
        new_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(-cube_size/2, cube_size/2),
                          rg.Interval(-cube_size/2, cube_size/2), rg.Interval(-cube_size/2, cube_size/2))
        new_cube.Transform(translation)

        # Convert to Brep and add to list
        breps.append(new_cube.ToBrep())

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_model_v2(1.0, 5, 0.2, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_model_v2(0.5, 3, 0.1, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_model_v2(2.0, 4, 0.3, 100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_model_v2(1.5, 6, 0.15, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_model_v2(1.2, 7, 0.25, 55)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
