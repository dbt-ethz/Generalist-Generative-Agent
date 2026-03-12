# Created for 0009_0005_cantilevering_corners.json

""" Summary:
The function `create_cantilevered_concept_model` generates an architectural concept model inspired by the metaphor of "Cantilevering corners." It begins with a central core, representing stability, from which multiple cantilevered sections extend outward at varying angles. These projections create a dynamic interplay of tension and balance, embodying the contrast between solid and void. The parameters allow for customization of the cantilever dimensions, enhancing the visual impact. By utilizing varied angles and incorporating negative spaces, the model invites exploration and interaction, effectively translating the metaphor into a tangible architectural representation that challenges conventional design notions."""

#! python 3
function_code = """def create_cantilevered_concept_model(core_dimensions=(4, 4, 10), cantilever_params=[(6, 2, 1), (5, 3, 2)], angle_variation=15):
    \"""
    Generates a conceptual architectural model embodying 'Cantilevering corners'.

    This model features a central core with multiple cantilevered sections extending outward.
    It emphasizes dynamic interaction between stability and motion. Each cantilever is
    defined by its length, width, and height, and they are positioned at varied angles
    to create a sense of tension and balance.

    Parameters:
    - core_dimensions (tuple): Dimensions (width, depth, height) of the central core.
    - cantilever_params (list of tuples): Each tuple contains (length, width, height) of a cantilever.
    - angle_variation (float): Maximum angular variation for cantilevers in degrees.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the model.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    # Set random seed for reproducibility
    random.seed(42)

    # Unpack core dimensions
    core_width, core_depth, core_height = core_dimensions

    # Create the central core as a box
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_depth), rg.Interval(0, core_height))
    geometries = [core_box.ToBrep()]

    # Calculate the center of the top face of the core
    top_center = rg.Point3d(core_width / 2, core_depth / 2, core_height)

    # Create cantilevered sections
    for length, width, height in cantilever_params:
        angle = random.uniform(-angle_variation, angle_variation)
        direction = rg.Vector3d(math.cos(math.radians(angle)), math.sin(math.radians(angle)), 0)
        direction.Unitize()

        # Calculate cantilever base point and orientation
        base_point = top_center + direction * (core_width / 2)
        cantilever_plane = rg.Plane(base_point, direction)

        # Define cantilever box
        cantilever_box = rg.Box(cantilever_plane, rg.Interval(0, length), rg.Interval(-width / 2, width / 2), rg.Interval(0, height))
        cantilever_brep = cantilever_box.ToBrep()
        
        geometries.append(cantilever_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_concept_model(core_dimensions=(5, 5, 12), cantilever_params=[(7, 2, 3), (4, 2, 1)], angle_variation=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_concept_model(core_dimensions=(6, 4, 8), cantilever_params=[(5, 3, 2), (8, 1, 4)], angle_variation=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_concept_model(core_dimensions=(3, 3, 9), cantilever_params=[(4, 2, 2), (6, 3, 1)], angle_variation=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_concept_model(core_dimensions=(4, 6, 10), cantilever_params=[(5, 4, 3), (7, 2, 5)], angle_variation=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_concept_model(core_dimensions=(8, 4, 10), cantilever_params=[(10, 5, 3), (6, 3, 2)], angle_variation=18)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
