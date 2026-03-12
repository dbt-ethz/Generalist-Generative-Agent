# Created for 0009_0004_cantilevering_corners.json

""" Summary:
The function `generate_cantilevered_architecture` creates an architectural concept model based on the metaphor of "Cantilevering corners." It constructs a central core structure from specified dimensions, then generates a series of angular, projecting extensions that simulate dynamic cantilevers. Each extension is randomized in direction and rotation, embodying the tension between stability and motion inherent in the metaphor. By utilizing contrasting geometries and materials, the model captures the playful balance of solid and void, fostering unique spatial experiences. The function also considers light and shadow interactions, enhancing the visual impact of the cantilevered design."""

#! python 3
function_code = """def generate_cantilevered_architecture(core_dim, extension_dims, num_extensions, seed=42):
    \"""
    Generate a conceptual architectural model based on the 'Cantilevering corners' metaphor.

    This function creates a central core structure with several angular extensions
    that project outward, forming dynamic cantilevered volumes that reflect a balance
    between stability and motion.

    Parameters:
    - core_dim (tuple of floats): Dimensions of the core structure (width, depth, height) in meters.
    - extension_dims (tuple of floats): Maximum dimensions of the cantilevered extensions 
      (length, height) in meters.
    - num_extensions (int): Number of cantilevered extensions.
    - seed (int): Seed for randomness to ensure replicability. Default is 42.

    Returns:
    - List: A list of Rhino.Geometry.Brep objects representing the 3D geometries of the model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set random seed
    random.seed(seed)

    # Unpack core dimensions
    core_width, core_depth, core_height = core_dim

    # Create the central core structure
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_depth), rg.Interval(0, core_height))
    core_brep = core_box.ToBrep()

    # Prepare list for geometries
    geometries = [core_brep]

    # Define possible directions for cantilevering
    directions = [
        rg.Vector3d(1, 0, 0), rg.Vector3d(-1, 0, 0), 
        rg.Vector3d(0, 1, 0), rg.Vector3d(0, -1, 0),
        rg.Vector3d(1, 1, 0), rg.Vector3d(-1, -1, 0)
    ]

    # Create cantilevered extensions
    for _ in range(num_extensions):
        # Choose random direction and scale
        dir_vector = random.choice(directions)
        dir_vector.Unitize()
        dir_vector *= extension_dims[0]

        # Random angle for rotation
        angle = math.radians(random.uniform(-30, 30))

        # Create base plane for the extension
        base_point = rg.Point3d(core_width / 2, core_depth / 2, core_height)
        base_plane = rg.Plane(base_point, rg.Vector3d.ZAxis)

        # Create a box for the cantilevered extension
        ext_box = rg.Box(base_plane, rg.Interval(0, extension_dims[0]), rg.Interval(0, core_width / 4), rg.Interval(0, extension_dims[1]))

        # Rotate and translate the box to form a cantilever
        rotation = rg.Transform.Rotation(angle, rg.Vector3d.ZAxis, base_point)
        translation = rg.Transform.Translation(dir_vector)
        ext_box.Transform(rotation)
        ext_box.Transform(translation)

        # Add the transformed box to the list of geometries
        geometries.append(ext_box.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cantilevered_architecture((10, 5, 8), (3, 2), 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cantilevered_architecture((12, 6, 10), (4, 3), 5, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cantilevered_architecture((15, 7, 12), (5, 4), 3, seed=200)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cantilevered_architecture((8, 4, 6), (2, 1), 6, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cantilevered_architecture((9, 4, 7), (3.5, 2.5), 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
