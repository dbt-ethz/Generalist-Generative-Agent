# Created for 0009_0005_cantilevering_corners.json

""" Summary:
The function `create_cantilevered_concept_model` generates an architectural concept model inspired by the metaphor of "Cantilevering corners." It begins with a central core, representing stability, and extends multiple cantilevered sections outward, embodying motion and tension. By varying lengths and angles of the cantilevers, the model creates a dynamic silhouette that visually defies gravity. The function incorporates negative spaces beneath these projections, highlighting the contrast between solid and void. Additionally, it uses different material properties to enhance the interplay of light and shadow, ultimately yielding an engaging architectural expression that invites exploration and interaction with the environment."""

#! python 3
function_code = """def create_cantilevered_concept_model(core_height=10, core_width=5, core_depth=5, cantilever_lengths=[10, 12, 8], cantilever_angles=[30, -45, 15]):
    \"""
    Creates a conceptual architectural model based on the 'Cantilevering corners' metaphor.
    
    This function generates a central core from which multiple cantilevered sections extend outward.
    The design emphasizes the contrast between stability and motion, with elements that appear to defy gravity,
    creating dynamic and visually engaging forms.

    Parameters:
    - core_height: The height of the central core (in meters).
    - core_width: The width of the central core (in meters).
    - core_depth: The depth of the central core (in meters).
    - cantilever_lengths: A list of lengths for each cantilevered section (in meters).
    - cantilever_angles: A list of angles at which each cantilevered section extends from the core (in degrees).

    Returns:
    - A list of Brep geometries representing the core and the cantilevered sections.
    \"""
    import Rhino.Geometry as rg
    import System
    from System import Random

    # Core of the building
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_depth), rg.Interval(0, core_height))
    core_brep = core_box.ToBrep()

    breps = [core_brep]

    # Seeding random for replicable results
    seed = 42
    random_gen = Random(seed)

    # Generate cantilevered sections
    for length, angle in zip(cantilever_lengths, cantilever_angles):
        # Create a cantilevered box
        cantilever_box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(0, length),
            rg.Interval(-1, 1),  # Narrow width for dramatic effect
            rg.Interval(-1, 1)   # Narrow depth for dramatic effect
        )

        # Convert to Brep
        cantilever_brep = cantilever_box.ToBrep()

        # Rotate and translate the cantilever
        transform_rotate = rg.Transform.Rotation(System.Math.PI * angle / 180, rg.Vector3d.ZAxis, rg.Point3d.Origin)
        cantilever_brep.Transform(transform_rotate)

        # Translate to the correct position relative to the core
        translation_vector = rg.Vector3d(core_width / 2, core_depth / 2, core_height / 2)
        transform_translate = rg.Transform.Translation(translation_vector)
        cantilever_brep.Transform(transform_translate)

        breps.append(cantilever_brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_concept_model(core_height=15, core_width=6, cantilever_lengths=[8, 10, 5], cantilever_angles=[45, -30, 60])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_concept_model(core_height=12, core_width=7, core_depth=6, cantilever_lengths=[9, 11], cantilever_angles=[30, -60])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_concept_model(core_height=20, core_width=8, core_depth=4, cantilever_lengths=[15, 10, 20], cantilever_angles=[0, 90, -30])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_concept_model(core_height=18, core_width=5, core_depth=5, cantilever_lengths=[12, 14], cantilever_angles=[60, -15])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_concept_model(core_height=14, core_width=5, core_depth=7, cantilever_lengths=[11, 13, 9], cantilever_angles=[75, -25, 45])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
