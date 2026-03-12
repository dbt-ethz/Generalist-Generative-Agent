# Created for 0002_0001_cubic_nest.json

""" Summary:
The function `build_cubic_nest` generates an architectural concept model inspired by the "Cubic nest" metaphor by creating a collection of interlocking cubic volumes. It utilizes parameters such as base cube size, number of cubes, and overlap ratio to define the model's complexity and spatial dynamics. Each cube is randomly scaled and positioned, emphasizing the interplay of solid and void spaces, which fosters exploration and discovery. The resulting model maintains distinct cube identities while contributing to an overarching protective, layered structure. This approach effectively materializes the metaphor's themes of shelter and interconnectedness within the architectural design."""

#! python 3
function_code = """def build_cubic_nest(base_cube_size, num_cubes, overlap_ratio, min_scale, max_scale, seed=42):
    \"""
    Generate an architectural Concept Model based on the 'Cubic nest' metaphor.

    This function arranges a series of interlocking and overlapping cubic volumes
    in varying scales and orientations to explore the interplay of solid and void.
    The cubes are positioned in a way that reinforces the metaphor's themes of
    shelter and interconnectedness.

    Parameters:
    - base_cube_size: float, the size of the base cube in meters.
    - num_cubes: int, the number of cubes to generate.
    - overlap_ratio: float, a factor (0 to 1) determining maximum overlap extent.
    - min_scale: float, minimum scale factor for resizing the cubes.
    - max_scale: float, maximum scale factor for resizing the cubes.
    - seed: int, seed for randomness to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the cubic nest model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    breps = []

    for _ in range(num_cubes):
        # Randomly scale the cube
        scale_factor = random.uniform(min_scale, max_scale)
        cube_size = base_cube_size * scale_factor

        # Create a cube
        cube = rg.Box(rg.Plane.WorldXY, rg.Interval(0, cube_size), rg.Interval(0, cube_size), rg.Interval(0, cube_size))

        # Determine random position within the overlap bounds
        max_translation = base_cube_size * overlap_ratio
        translation_vector = rg.Vector3d(
            random.uniform(-max_translation, max_translation),
            random.uniform(-max_translation, max_translation),
            random.uniform(-max_translation, max_translation)
        )
        
        # Apply translation to the cube
        cube.Transform(rg.Transform.Translation(translation_vector))

        # Convert the box to a Brep and add it to the list
        breps.append(cube.ToBrep())

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = build_cubic_nest(base_cube_size=1.0, num_cubes=10, overlap_ratio=0.5, min_scale=0.5, max_scale=1.5, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = build_cubic_nest(base_cube_size=2.0, num_cubes=5, overlap_ratio=0.3, min_scale=0.8, max_scale=1.2, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = build_cubic_nest(base_cube_size=1.5, num_cubes=20, overlap_ratio=0.4, min_scale=0.6, max_scale=1.0, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = build_cubic_nest(base_cube_size=0.5, num_cubes=15, overlap_ratio=0.2, min_scale=0.3, max_scale=2.0, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = build_cubic_nest(base_cube_size=3.0, num_cubes=8, overlap_ratio=0.6, min_scale=0.4, max_scale=1.8, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
