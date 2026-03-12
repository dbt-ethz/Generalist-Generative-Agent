# Created for 0009_0001_cantilevering_corners.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "Cantilevering corners." It creates a central core, from which various cantilevered extensions project outward, mimicking the dynamic tension and balance suggested by the metaphor. The function takes parameters for the core dimensions and the characteristics (lengths, heights, and directions) of the cantilevers. By incorporating random elements, such as rotation, it enhances the illusion of movement and instability. The resulting geometries highlight the interplay of solid and void, showcasing dramatic overhangs and unexpected spatial relationships that challenge conventional architectural forms."""

#! python 3
function_code = """def create_cantilever_concept_model(core_size, extension_lengths, extension_heights, extension_directions, seed=42):
    \"""
    Creates an architectural Concept Model emphasizing the dynamic tension of cantilevered elements.
    
    Parameters:
        core_size (tuple): Dimensions of the central core as (width, depth, height) in meters.
        extension_lengths (list): List of lengths for each cantilevered extension.
        extension_heights (list): List of heights for each cantilevered extension.
        extension_directions (list): List of directions (in degrees) for each cantilevered extension.
        seed (int): Seed for random generation to ensure replicability.
    
    Returns:
        list: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    # Set random seed for replicability
    random.seed(seed)
    
    # Create the central core
    core_width, core_depth, core_height = core_size
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_depth), rg.Interval(0, core_height))
    geometries = [core_box.ToBrep()]

    # Create cantilevered extensions
    for length, height, direction in zip(extension_lengths, extension_heights, extension_directions):
        # Calculate the translation vector for the cantilever based on direction and length
        angle_rad = math.radians(direction)
        translation_vector = rg.Vector3d(math.cos(angle_rad) * length, math.sin(angle_rad) * length, 0)

        # Define the base plane for the cantilever
        base_plane = rg.Plane(rg.Point3d(core_width / 2, core_depth / 2, core_height), rg.Vector3d.ZAxis)
        base_plane.Translate(translation_vector)

        # Create the cantilever box
        cantilever_box = rg.Box(base_plane, rg.Interval(0, core_width / 2), rg.Interval(0, core_depth / 2), rg.Interval(0, height))
        
        # Randomly decide whether to rotate the cantilever to add dynamic tension
        if random.choice([True, False]):
            rotation_angle = random.uniform(-15, 15)  # Rotate by a random angle between -15 and 15 degrees
            cantilever_box.Transform(rg.Transform.Rotation(math.radians(rotation_angle), base_plane.ZAxis, base_plane.Origin))

        # Add the cantilever to the list of geometries
        geometries.append(cantilever_box.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilever_concept_model((5, 3, 2), [4, 6, 5], [1, 2, 3], [30, 60, 90])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilever_concept_model((10, 5, 3), [7, 8], [2, 4], [45, 135])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilever_concept_model((6, 4, 3), [5, 7, 3, 8], [2, 3, 1, 4], [0, 90, 180, 270])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilever_concept_model((4, 2, 2), [3, 5, 2], [1, 3, 2], [15, 75, 120])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilever_concept_model((8, 6, 4), [5, 10, 6], [3, 5, 2], [0, 45, 90])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
