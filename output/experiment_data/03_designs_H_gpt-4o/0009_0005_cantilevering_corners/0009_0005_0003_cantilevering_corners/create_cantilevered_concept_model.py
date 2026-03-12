# Created for 0009_0005_cantilevering_corners.json

""" Summary:
The provided function, `create_cantilevered_concept_model`, generates an architectural concept model based on the metaphor of "Cantilevering corners." It establishes a central core as the structural anchor and projects cantilevered sections outward, embodying the contrast between stability and motion. By varying the dimensions, angles, and positions of these cantilevers, the model creates a dynamic form that appears to defy gravity, enhancing the sense of tension and balance. The function also emphasizes spatial relationships and the interplay of light and shadow, inviting exploration and interaction within the resulting architectural spaces, thus fulfilling the design task effectively."""

#! python 3
function_code = """def create_cantilevered_concept_model(core_dimensions=(4, 4, 6), cantilever_dims=(2, 2, 2), cantilever_count=4, offset=3):
    \"""
    Generates a conceptual architectural model embodying 'Cantilevering corners'.

    This model features a central core with cantilevered sections extending outward,
    creating a dynamic interplay between stability and motion. The design emphasizes
    the contrast between solid and void, and highlights the interaction of light and shadow.

    Parameters:
    - core_dimensions (tuple): Dimensions (width, depth, height) of the central core.
    - cantilever_dims (tuple): Dimensions (width, depth, height) of each cantilever.
    - cantilever_count (int): Number of cantilevered sections.
    - offset (float): Distance from the core where cantilevers start.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the model.
    \"""
    import Rhino.Geometry as rg

    # Create the central core as a box
    core_width, core_depth, core_height = core_dimensions
    core_origin = rg.Point3d(0, 0, 0)
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_depth), rg.Interval(0, core_height))
    geometries = [core_box.ToBrep()]

    # Define the cantilevered sections
    cantilever_width, cantilever_depth, cantilever_height = cantilever_dims
    cantilever_positions = [
        rg.Point3d(core_width + offset, core_depth / 2, core_height / 2),
        rg.Point3d(-cantilever_width - offset, core_depth / 2, core_height / 2),
        rg.Point3d(core_width / 2, core_depth + offset, core_height / 2),
        rg.Point3d(core_width / 2, -cantilever_depth - offset, core_height / 2)
    ]

    for i in range(min(cantilever_count, len(cantilever_positions))):
        position = cantilever_positions[i]
        cantilever_plane = rg.Plane(position, rg.Vector3d.ZAxis)
        cantilever_box = rg.Box(cantilever_plane, rg.Interval(0, cantilever_width), rg.Interval(0, cantilever_depth), rg.Interval(0, cantilever_height))
        geometries.append(cantilever_box.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_concept_model(core_dimensions=(5, 5, 10), cantilever_dims=(3, 3, 3), cantilever_count=4, offset=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_concept_model(core_dimensions=(6, 6, 12), cantilever_dims=(2, 2, 5), cantilever_count=3, offset=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_concept_model(core_dimensions=(8, 4, 7), cantilever_dims=(2, 1, 2), cantilever_count=2, offset=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_concept_model(core_dimensions=(3, 3, 5), cantilever_dims=(1, 1, 1), cantilever_count=5, offset=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_concept_model(core_dimensions=(7, 3, 8), cantilever_dims=(2, 3, 2), cantilever_count=3, offset=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
