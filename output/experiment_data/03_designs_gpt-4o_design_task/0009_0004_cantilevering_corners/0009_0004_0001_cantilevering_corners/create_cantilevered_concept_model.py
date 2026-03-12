# Created for 0009_0004_cantilevering_corners.json

""" Summary:
The provided function, `create_cantilevered_concept_model`, generates an architectural concept model inspired by the metaphor of "Cantilevering corners." It constructs a central core structure, from which asymmetrical extensions project outward, creating dynamic cantilevered volumes. The design emphasizes the interplay between the grounded core and floating elements, reflecting the tension between stability and motion inherent in the metaphor. By incorporating random variations in direction and height, the function produces diverse geometric forms that challenge conventional support structures. This approach not only captures the essence of the metaphor but also invites exploration of unique spatial relationships and light interactions within the model."""

#! python 3
function_code = """def create_cantilevered_concept_model(core_height, core_width, core_depth, extension_length, extension_height, extension_width, seed=42):
    \"""
    Create an architectural Concept Model that captures the essence of 'Cantilevering corners'.
    
    This function generates a central core structure with angular, interlocking volumes extending
    asymmetrically from it, forming cantilevered corners. The design emphasizes the contrast between
    grounded and suspended elements, creating dynamic spaces and dramatic overhangs.

    Parameters:
    - core_height (float): The height of the central core structure in meters.
    - core_width (float): The width of the central core structure in meters.
    - core_depth (float): The depth of the central core structure in meters.
    - extension_length (float): The length of the extending cantilever sections in meters.
    - extension_height (float): The height of the extending cantilever sections in meters.
    - extension_width (float): The width of the extending cantilever sections in meters.
    - seed (int): Seed for random number generator to ensure replicable results. Default is 42.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries (breps) representing the concept model.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Point3d, Box, Plane, Vector3d

    random.seed(seed)
    
    geometries = []

    # Create the core structure
    core_base = Point3d(0, 0, 0)
    core_plane = Plane(core_base, Vector3d.ZAxis)
    core_box = Box(core_plane, Rhino.Geometry.Interval(0, core_width), Rhino.Geometry.Interval(0, core_depth), Rhino.Geometry.Interval(0, core_height))
    core_brep = core_box.ToBrep()
    geometries.append(core_brep)

    # Create cantilever extensions
    directions = [Vector3d(1, 0, 0), Vector3d(-1, 0, 0), Vector3d(0, 1, 0), Vector3d(0, -1, 0)]
    for direction in directions:
        if random.choice([True, False]):
            # Randomly decide to mirror along Z for additional asymmetry
            direction *= random.choice([1, -1])
        extension_base = core_base + direction * core_width / 2
        if direction.Y == 0:  # Extend along X direction
            extension_base += Vector3d(0, random.uniform(-core_depth / 2, core_depth / 2), core_height)
        else:  # Extend along Y direction
            extension_base += Vector3d(random.uniform(-core_width / 2, core_width / 2), 0, core_height)
        
        extension_plane = Plane(extension_base, Vector3d.ZAxis)
        extension_box = Box(extension_plane, Rhino.Geometry.Interval(0, extension_length), Rhino.Geometry.Interval(0, extension_width), Rhino.Geometry.Interval(0, extension_height))
        extension_brep = extension_box.ToBrep()
        geometries.append(extension_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_concept_model(10, 5, 5, 7, 3, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_concept_model(8, 4, 4, 6, 2, 1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_concept_model(12, 6, 6, 5, 4, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_concept_model(15, 7, 7, 10, 5, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_concept_model(9, 4.5, 4.5, 8, 3.5, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
