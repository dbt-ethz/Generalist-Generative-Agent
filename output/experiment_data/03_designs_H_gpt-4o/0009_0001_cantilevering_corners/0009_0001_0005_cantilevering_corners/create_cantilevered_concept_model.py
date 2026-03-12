# Created for 0009_0001_cantilevering_corners.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "Cantilevering corners." It creates a central core structure, from which multiple extensions project outward, embodying dynamic tension and balance. By randomly selecting orientations and lengths for these cantilevered elements, the model visually represents the interplay between solid (the core) and void (the extensions), suggesting movement and defiance of gravity. The use of varied dimensions and potential contrasting materials enhances the spatial experience, while the overall form reflects the metaphor's implications of balance and instability, ultimately resulting in a visually compelling architectural narrative."""

#! python 3
function_code = """def create_cantilevered_concept_model(core_size, num_extensions, max_extension_length, max_extension_height, seed=42):
    \"""
    Generates an architectural Concept Model emphasizing the dynamic tension of cantilevered elements.

    This function creates a central core from which extensions project outward in varying directions and lengths,
    creating a sense of balance and instability. The design focuses on the interplay between solid and void.

    Parameters:
    - core_size: tuple of floats (width, depth, height) representing the dimensions of the core in meters.
    - num_extensions: int, the number of cantilevered extensions.
    - max_extension_length: float, the maximum length of the cantilevered extensions in meters.
    - max_extension_height: float, the maximum height of the cantilevered extensions in meters.
    - seed: int, optional, seed for random number generator to ensure replicability (default is 42).

    Returns:
    - list of Rhino.Geometry.Brep objects representing the solid and void geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)

    # Create the central core
    core_width, core_depth, core_height = core_size
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_depth), rg.Interval(0, core_height))
    geometries = [core_box.ToBrep()]

    # Create cantilevered extensions
    def create_cantilever(core_box, length, height):
        # Randomly select a face of the core for the extension
        face_index = random.randint(0, 3)
        if face_index == 0:
            direction = rg.Vector3d(1, 0, 0)
            base_origin = rg.Point3d(core_width, random.uniform(0, core_depth), random.uniform(0, core_height))
        elif face_index == 1:
            direction = rg.Vector3d(-1, 0, 0)
            base_origin = rg.Point3d(0, random.uniform(0, core_depth), random.uniform(0, core_height))
        elif face_index == 2:
            direction = rg.Vector3d(0, 1, 0)
            base_origin = rg.Point3d(random.uniform(0, core_width), core_depth, random.uniform(0, core_height))
        else:
            direction = rg.Vector3d(0, -1, 0)
            base_origin = rg.Point3d(random.uniform(0, core_width), 0, random.uniform(0, core_height))
        
        # Create the extension box
        extension_box = rg.Box(rg.Plane(base_origin, direction), rg.Interval(0, length), rg.Interval(-core_depth * 0.2, core_depth * 0.2), rg.Interval(0, height))
        
        # Return the extension Brep
        return extension_box.ToBrep()

    for _ in range(num_extensions):
        length = random.uniform(0.5 * max_extension_length, max_extension_length)
        height = random.uniform(0.5 * max_extension_height, max_extension_height)
        extension_brep = create_cantilever(core_box, length, height)
        geometries.append(extension_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_concept_model((2.0, 1.0, 3.0), 5, 2.0, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_concept_model((1.5, 1.5, 2.0), 3, 1.0, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_concept_model((3.0, 2.0, 4.0), 7, 3.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_concept_model((2.5, 1.2, 3.5), 4, 2.5, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_concept_model((4.0, 2.5, 5.0), 6, 3.5, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
