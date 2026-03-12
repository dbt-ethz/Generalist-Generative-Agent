# Created for 0002_0001_cubic_nest.json

""" Summary:
The provided function, `create_cubic_nest`, generates an architectural concept model inspired by the "Cubic nest" metaphor by creating interlocking and overlapping cubic volumes. The function takes parameters to define the base cube size, the number of cubes, and the degree of overlap. It uses random offsets to position each new cube relative to an existing one, fostering a dynamic arrangement that reflects shelter and interconnectedness. The resulting 3D models emphasize the interplay of solid and void, encouraging exploration through varied spatial experiences. This approach maintains distinct identities for cubes while contributing to an overall cohesive structure."""

#! python 3
function_code = """def create_cubic_nest(base_cube_size, cube_count, overlap_factor, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Cubic nest' metaphor,
    using a series of interlocking and overlapping cubic volumes to form a complex,
    layered structure. The model emphasizes spatial interplay of solid and void,
    and experiments with different orientations and alignments to highlight the
    interconnectedness of the volumes.

    Parameters:
    - base_cube_size (float): The size of the base cube in meters.
    - cube_count (int): The number of cubic volumes to generate.
    - overlap_factor (float): A factor that determines the degree of overlap
                              between cubes (0 to 1).
    - seed (int, optional): Seed for randomness to ensure replicability (default is 42).

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Breps representing the cubic volumes.
    \"""

    import Rhino.Geometry as rg
    import random

    # Set the seed for reproducibility
    random.seed(seed)

    # List to store the resulting Breps
    cubes = []

    # Create the initial base cube
    base_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_cube_size),
                       rg.Interval(0, base_cube_size), rg.Interval(0, base_cube_size))
    cubes.append(base_cube.ToBrep())

    # Generate additional cubes
    for _ in range(1, cube_count):
        # Randomly select a cube from the list to overlap with
        reference_cube = random.choice(cubes)
        bbox = reference_cube.GetBoundingBox(True)

        # Determine a random overlap offset
        offset_x = random.uniform(-overlap_factor, overlap_factor) * base_cube_size
        offset_y = random.uniform(-overlap_factor, overlap_factor) * base_cube_size
        offset_z = random.uniform(-overlap_factor, overlap_factor) * base_cube_size

        # Create a new cube with the calculated offset
        new_origin = rg.Point3d(bbox.Min.X + offset_x, bbox.Min.Y + offset_y, bbox.Min.Z + offset_z)
        new_cube = rg.Box(rg.Plane(new_origin, rg.Vector3d.XAxis, rg.Vector3d.YAxis),
                          rg.Interval(0, base_cube_size), rg.Interval(0, base_cube_size), rg.Interval(0, base_cube_size))

        # Add the new cube to the list
        cubes.append(new_cube.ToBrep())

    return cubes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest(5.0, 10, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest(3.0, 15, 0.5, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest(4.0, 8, 0.2, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest(6.0, 5, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest(2.5, 20, 0.4, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
