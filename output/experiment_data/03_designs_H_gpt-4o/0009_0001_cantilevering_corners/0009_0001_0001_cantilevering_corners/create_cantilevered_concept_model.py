# Created for 0009_0001_cantilevering_corners.json

""" Summary:
The function `create_cantilevered_concept_model` generates an architectural concept model based on the metaphor of "Cantilevering corners" by creating a central core from which multiple cantilevered extensions project outward. It employs parameters such as core dimensions and extension characteristics to define the model's proportions and dynamics. Each extension is designed to appear as if it is defying gravity, enhancing the sense of tension and balance. The interplay between solid and void is emphasized through varying lengths and angles of the extensions, which, along with contrasting materials, create a visually intriguing representation of stability intermingled with motion."""

#! python 3
function_code = """def create_cantilevered_concept_model(core_dimensions, num_extensions, max_extension_length, max_extension_angle, seed=42):
    \"""
    Generates an architectural Concept Model featuring cantilevered elements extending from a central core.

    The model emphasizes the dynamic tension between stability and motion, with extensions projecting outward
    in a visually intriguing manner that suggests balance and defiance of gravity.

    Parameters:
    - core_dimensions: tuple of floats (width, depth, height) representing the dimensions of the core in meters.
    - num_extensions: int, the number of cantilevered extensions.
    - max_extension_length: float, the maximum length of any cantilevered extension in meters.
    - max_extension_angle: float, the maximum angle (in degrees) from the horizontal plane for any extension.
    - seed: int, optional, seed for random number generator to ensure replicability (default is 42).

    Returns:
    - list of Rhino.Geometry.Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    random.seed(seed)

    # Create the central core as a Brep box
    core_width, core_depth, core_height = core_dimensions
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_depth), rg.Interval(0, core_height))
    core_brep = core_box.ToBrep()

    geometries = [core_brep]

    # Function to create a cantilevered extension
    def create_extension(core_center, max_length, max_angle):
        # Randomly choose the length and angle for the extension
        length = random.uniform(max_length / 2, max_length)
        angle = random.uniform(-max_angle, max_angle)
        angle_rad = math.radians(angle)

        # Determine the vector direction for the extension
        direction = rg.Vector3d(math.cos(angle_rad), math.sin(angle_rad), random.uniform(-0.2, 0.2))
        direction.Unitize()

        # Create the base plane for the extension
        extension_origin = core_center + direction * (core_width / 2)
        extension_plane = rg.Plane(extension_origin, direction)

        # Create the extension box
        extension_box = rg.Box(extension_plane, rg.Interval(0, length), rg.Interval(-core_depth / 4, core_depth / 4),
                               rg.Interval(-core_height / 4, core_height / 4))

        return extension_box.ToBrep()

    # Generate extensions
    core_center = core_box.Center
    for _ in range(num_extensions):
        extension = create_extension(core_center, max_extension_length, max_extension_angle)
        geometries.append(extension)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_concept_model((5.0, 3.0, 2.0), 4, 6.0, 30.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_concept_model((10.0, 5.0, 3.0), 6, 8.0, 45.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_concept_model((4.0, 2.0, 1.5), 3, 5.0, 60.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_concept_model((8.0, 4.0, 3.0), 5, 7.0, 50.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_concept_model((6.0, 3.5, 2.5), 5, 10.0, 40.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
