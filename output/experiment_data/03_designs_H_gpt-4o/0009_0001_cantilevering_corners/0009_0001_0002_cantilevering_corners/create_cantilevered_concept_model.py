# Created for 0009_0001_cantilevering_corners.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "Cantilevering corners." By defining a central core with specified dimensions, the function creates a series of cantilevered extensions that project outward in various directions and heights. This design emphasizes the dynamic tension between solid support and void spaces, reflecting the metaphor's theme of balance and instability. Randomization of extension properties, such as length and height, introduces variability, allowing the model to visually challenge gravity. The result is a collection of geometries that captures the interplay of light, shadow, and movement, fulfilling the design task."""

#! python 3
function_code = """def create_cantilevered_concept_model(core_dimensions, num_extensions, max_extension_length, max_extension_height, seed=42):
    \"""
    Creates an architectural Concept Model emphasizing the dynamic tension of cantilevered elements.

    The model features a central core with extensions that project outward in various directions and heights,
    creating a sense of balance and instability. It explores the interaction between solid and void spaces.

    Parameters:
    - core_dimensions: tuple of floats (width, depth, height) representing the dimensions of the central core in meters.
    - num_extensions: int, the number of cantilevered extensions to create.
    - max_extension_length: float, the maximum length an extension can reach outwards in meters.
    - max_extension_height: float, the maximum height variation for the extensions in meters.
    - seed: int, optional, seed for the random number generator to ensure replicability (default is 42).

    Returns:
    - list of Rhino.Geometry.Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Initialize random seed
    random.seed(seed)

    # Unpack core dimensions
    core_width, core_depth, core_height = core_dimensions

    # Create the central core
    core = rg.Box(rg.Plane.WorldXY, rg.Interval(-core_width/2, core_width/2), rg.Interval(-core_depth/2, core_depth/2), rg.Interval(0, core_height))
    geometries = [core.ToBrep()]

    # Define potential directions for extensions
    directions = [rg.Vector3d(1, 0, 0), rg.Vector3d(-1, 0, 0), rg.Vector3d(0, 1, 0), rg.Vector3d(0, -1, 0)]

    for _ in range(num_extensions):
        # Randomize extension properties
        direction = random.choice(directions)
        extension_length = random.uniform(core_width/4, max_extension_length)
        extension_height = random.uniform(core_height/4, max_extension_height)

        # Determine base point for the extension
        base_point = rg.Point3d(core_width * direction.X / 2, core_depth * direction.Y / 2, core_height)

        # Create a plane for the extension
        extension_plane = rg.Plane(base_point, rg.Vector3d.ZAxis)

        # Create the extension box
        extension_box = rg.Box(extension_plane, rg.Interval(0, extension_length), rg.Interval(-core_depth/4, core_depth/4), rg.Interval(0, extension_height))

        # Translate extension box outward
        translation_vector = direction * extension_length
        extension_box.Transform(rg.Transform.Translation(translation_vector))

        # Convert the box to a Brep and add to the list
        geometries.append(extension_box.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_concept_model((5.0, 3.0, 4.0), 6, 10.0, 8.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_concept_model((3.0, 2.0, 5.0), 4, 7.0, 6.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_concept_model((6.0, 4.0, 3.0), 5, 9.0, 7.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_concept_model((4.0, 2.5, 6.0), 8, 12.0, 10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_concept_model((2.0, 1.5, 3.0), 3, 5.0, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
