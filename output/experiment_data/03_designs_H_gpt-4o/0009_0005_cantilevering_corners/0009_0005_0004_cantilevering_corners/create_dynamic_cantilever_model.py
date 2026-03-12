# Created for 0009_0005_cantilevering_corners.json

""" Summary:
The provided function, `create_dynamic_cantilever_model`, generates an architectural concept model embodying the metaphor of "Cantilevering corners." It establishes a central core as the structural anchor and extends various cantilevered sections outward at specified angles and lengths. This approach emphasizes the contrast between stability and motion, creating a dynamic interplay of solid and void spaces. The cantilevers are designed to appear as if they defy gravity, enhancing the building's visual tension and balance. By manipulating dimensions, angles, and material properties, the function fosters engaging, exploratory spaces that challenge traditional architectural norms."""

#! python 3
function_code = """def create_dynamic_cantilever_model(core_dimensions=(4, 4, 8), cantilever_specs=[(5, 2, 45), (6, 3, -30), (4, 2, 60)]):
    \"""
    Generates a conceptual architectural model embodying 'Cantilevering corners'.

    The model features a central core with dynamically arranged cantilevered sections extending outward.
    The design emphasizes the contrast between stability and motion, creating a dynamic interplay
    between solid and void, with a focus on varying angles and lengths.

    Parameters:
    - core_dimensions (tuple): Dimensions of the central core (width, depth, height) in meters.
    - cantilever_specs (list): A list of tuples, each specifying (length, width, angle) for a cantilever.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the model.
    \"""
    import Rhino.Geometry as rg
    import math

    core_width, core_depth, core_height = core_dimensions

    # Create the central core as a box
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_depth), rg.Interval(0, core_height))
    geometries = [core_box.ToBrep()]

    # Calculate the top center of the core for placing cantilevers
    top_center = rg.Point3d(core_width / 2, core_depth / 2, core_height)

    # Create cantilevered sections based on specifications
    for length, width, angle in cantilever_specs:
        # Define the cantilever plane and direction
        direction = rg.Vector3d(math.cos(math.radians(angle)), math.sin(math.radians(angle)), 0)
        direction.Unitize()

        # Create a cantilevered box
        cantilever_origin = top_center + (direction * length * 0.5)
        cantilever_plane = rg.Plane(cantilever_origin, direction)
        cantilever_box = rg.Box(cantilever_plane,
                                rg.Interval(-length / 2, length / 2),
                                rg.Interval(-width / 2, width / 2),
                                rg.Interval(-core_height * 0.1, core_height * 0.1))
        cantilever_brep = cantilever_box.ToBrep()

        # Add the cantilever to the list of geometries
        geometries.append(cantilever_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dynamic_cantilever_model((5, 5, 10), [(7, 3, 30), (8, 2, -45), (5, 4, 60)])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dynamic_cantilever_model((3, 3, 6), [(4, 1, 15), (5, 2, 75), (6, 1, -60)])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dynamic_cantilever_model((6, 4, 12), [(9, 3, 0), (10, 2, 45), (8, 3, -30)])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dynamic_cantilever_model((4, 4, 8), [(5, 2, 15), (6, 3, 90), (4, 2, -45)])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dynamic_cantilever_model((7, 5, 15), [(10, 4, 30), (3, 2, -60), (8, 3, 75)])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
