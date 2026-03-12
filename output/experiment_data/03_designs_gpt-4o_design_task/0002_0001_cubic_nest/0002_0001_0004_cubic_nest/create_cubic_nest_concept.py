# Created for 0002_0001_cubic_nest.json

""" Summary:
The provided function generates an architectural concept model inspired by the "Cubic nest" metaphor through a systematic approach to creating interlocking cubic volumes. It takes parameters that dictate the size, number, and scaling of cubes while allowing for controlled overlaps. By employing random positioning and scaling, the function ensures a dynamic interplay of solid and void spaces, reflecting the metaphor's themes of shelter and interconnectedness. The resulting geometries form a layered and cohesive structure, inviting exploration and discovery, while each cube retains its distinct identity, thus embodying the essence of the "Cubic nest" concept."""

#! python 3
function_code = """def create_cubic_nest_concept(base_cube_size, num_cubes, max_overlap, min_cube_scale, max_cube_scale, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Cubic nest' metaphor using interlocking and overlapping cubes.

    Parameters:
    - base_cube_size (float): The size of the base cube edge in meters.
    - num_cubes (int): The number of cubes to generate in the concept model.
    - max_overlap (float): The maximum allowable overlap between cubes as a percentage of the base cube size.
    - min_cube_scale (float): The minimum scale factor for resizing cubes.
    - max_cube_scale (float): The maximum scale factor for resizing cubes.
    - seed (int): The seed for randomness to ensure replicability. Default is 42.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the interlocking and overlapping cubes.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for replicability
    random.seed(seed)

    cubes = []
    for i in range(num_cubes):
        # Randomly scale the cube within the specified range
        scale_factor = random.uniform(min_cube_scale, max_cube_scale)
        cube_size = base_cube_size * scale_factor
        
        # Create a base cube
        base_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(0, cube_size), rg.Interval(0, cube_size), rg.Interval(0, cube_size))
        
        # Randomly position the cube within the maximum overlap range
        max_translation = base_cube_size * max_overlap
        translation_vector = rg.Vector3d(
            random.uniform(-max_translation, max_translation),
            random.uniform(-max_translation, max_translation),
            random.uniform(-max_translation, max_translation)
        )
        
        # Translate the cube's base plane
        translated_plane = rg.Plane(base_cube.Plane)  # Corrected this line
        translated_plane.Translate(translation_vector)
        
        # Create a new cube with the translated plane
        new_cube = rg.Box(translated_plane, base_cube.X, base_cube.Y, base_cube.Z).ToBrep()
        
        cubes.append(new_cube)

    return cubes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_concept(1.0, 10, 0.5, 0.5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_concept(0.5, 5, 0.3, 0.8, 1.5, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_concept(2.0, 15, 0.4, 0.6, 1.8, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_concept(1.5, 8, 0.6, 0.7, 1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_concept(3.0, 20, 0.2, 0.4, 1.0, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
