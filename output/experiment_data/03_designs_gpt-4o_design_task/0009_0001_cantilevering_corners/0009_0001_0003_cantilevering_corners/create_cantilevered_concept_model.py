# Created for 0009_0001_cantilevering_corners.json

""" Summary:
The provided function, `create_cantilevered_concept_model`, generates an architectural concept model inspired by the metaphor of "Cantilevering corners." It constructs a central core that symbolizes stability and from which multiple cantilevered extensions project outward, creating dynamic tension and balance. The function allows for customizable dimensions of the core and extensions, emphasizing the interplay of solid and void. By randomly orienting the extensions in different directions, it captures the sense of motion and defiance of gravity inherent in the metaphor. The model is created as 3D geometries that visually represent the architectural concept, enhancing spatial relationships through light and shadow."""

#! python 3
function_code = """def create_cantilevered_concept_model(core_width, core_height, core_depth, extension_length, extension_height, extension_width, num_extensions, seed=42):
    \"""
    Creates an architectural Concept Model based on the metaphor of "Cantilevering corners".
    
    This function constructs a central core and appends cantilevered extensions that project outward
    to emphasize dynamic tension and balance in the design.

    Inputs:
        core_width (float): Width of the central core in meters.
        core_height (float): Height of the central core in meters.
        core_depth (float): Depth of the central core in meters.
        extension_length (float): Maximum length of the cantilevered extensions in meters.
        extension_height (float): Height of the cantilevered extensions in meters.
        extension_width (float): Width of the cantilevered extensions in meters.
        num_extensions (int): Number of cantilevered extensions.
        seed (int, optional): Seed for random number generation to ensure replicability.

    Outputs:
        List of RhinoCommon Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed
    random.seed(seed)

    # Create the central core as a Brep box
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_depth), rg.Interval(0, core_height))
    core_brep = core_box.ToBrep()

    geometries = [core_brep]

    # Function to create a cantilevered extension
    def create_extension(core_box, direction_vector, length, width, height):
        # Create a bounding box for the extension
        extension_origin = core_box.Center + direction_vector * (core_box.X.Length / 2.0 + length / 2.0)
        extension_box = rg.Box(rg.Plane(extension_origin, direction_vector), rg.Interval(-width / 2.0, width / 2.0), rg.Interval(0, height), rg.Interval(-length / 2.0, length / 2.0))
        return extension_box.ToBrep()

    # Generate cantilevered extensions
    directions = [rg.Vector3d.XAxis, rg.Vector3d.YAxis, -rg.Vector3d.XAxis, -rg.Vector3d.YAxis]
    for _ in range(num_extensions):
        direction = random.choice(directions)
        extension_brep = create_extension(core_box, direction, extension_length, extension_width, extension_height)
        geometries.append(extension_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_concept_model(5.0, 10.0, 3.0, 4.0, 2.0, 1.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_concept_model(6.0, 12.0, 4.0, 5.0, 3.0, 2.0, 3, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_concept_model(7.0, 15.0, 5.0, 6.0, 4.0, 3.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_concept_model(4.0, 8.0, 2.0, 3.0, 1.5, 0.5, 2, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_concept_model(8.0, 20.0, 6.0, 7.0, 5.0, 4.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
