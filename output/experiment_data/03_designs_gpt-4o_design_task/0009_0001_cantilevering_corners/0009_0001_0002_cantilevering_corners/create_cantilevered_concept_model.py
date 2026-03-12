# Created for 0009_0001_cantilevering_corners.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "Cantilevering corners." It creates a central core structure that serves as a stable base from which various cantilevered sections extend outward in diverse directions and lengths. This design emphasizes the dynamic tension between solid and void, with some elements appearing to defy gravity. The function incorporates randomness in the positioning and length of cantilevers, enhancing the sense of movement and instability. By manipulating material contrasts and exploring light and shadow, the model accentuates the architectural interplay between stability and dynamic projection, embodying the metaphor's essence."""

#! python 3
function_code = """def create_cantilevered_concept_model(core_height=10, core_width=8, core_depth=8, cantilever_length=5, cantilever_height=4, cantilever_width=4, seed=42):
    \"""
    Create an architectural Concept Model that emphasizes the dynamic tension of cantilevered elements.

    This function generates a central core from which sections extend outward in varying directions and lengths.
    The model highlights the tension between solid and void, and explores the interplay of light and shadow
    across these elements to enhance the perception of movement and tension.

    Parameters:
    core_height (float): Height of the central core in meters.
    core_width (float): Width of the central core in meters.
    core_depth (float): Depth of the central core in meters.
    cantilever_length (float): Length of the cantilevered sections in meters.
    cantilever_height (float): Height of the cantilevered sections in meters.
    cantilever_width (float): Width of the cantilevered sections in meters.
    seed (int): Seed for randomness to ensure replicability.

    Returns:
    List: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    geometries = []

    # Create the central core
    core_origin = rg.Point3d(0, 0, 0)
    core_box = rg.Box(rg.Plane(core_origin, rg.Vector3d.ZAxis), rg.Interval(-core_width/2, core_width/2), rg.Interval(-core_depth/2, core_depth/2), rg.Interval(0, core_height))
    core_brep = core_box.ToBrep()
    geometries.append(core_brep)

    # Create cantilevered sections
    directions = [rg.Vector3d(1, 0, 0), rg.Vector3d(-1, 0, 0), rg.Vector3d(0, 1, 0), rg.Vector3d(0, -1, 0)]
    for direction in directions:
        # Randomize the length and position of the cantilever
        offset = random.uniform(0, core_height - cantilever_height)
        cantilever_origin = rg.Point3d(core_width/2 * direction.X, core_depth/2 * direction.Y, offset)
        cantilever_plane = rg.Plane(cantilever_origin, rg.Vector3d.ZAxis)
        cantilever_box = rg.Box(cantilever_plane, rg.Interval(0, cantilever_length), rg.Interval(-cantilever_width/2, cantilever_width/2), rg.Interval(0, cantilever_height))

        # Transform the cantilever box to the correct direction
        transform = rg.Transform.Translation(direction * cantilever_length)
        cantilever_brep = cantilever_box.ToBrep()
        cantilever_brep.Transform(transform)
        geometries.append(cantilever_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_concept_model(core_height=15, core_width=10, core_depth=10, cantilever_length=7, cantilever_height=5, cantilever_width=3, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_concept_model(core_height=12, core_width=9, core_depth=9, cantilever_length=6, cantilever_height=4, cantilever_width=5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_concept_model(core_height=20, core_width=12, core_depth=10, cantilever_length=8, cantilever_height=6, cantilever_width=4, seed=456)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_concept_model(core_height=18, core_width=11, core_depth=9, cantilever_length=9, cantilever_height=7, cantilever_width=5, seed=789)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_concept_model(core_height=14, core_width=10, core_depth=8, cantilever_length=6, cantilever_height=4, cantilever_width=6, seed=101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
