# Created for 0009_0005_cantilevering_corners.json

""" Summary:
The provided function, `create_cantilevering_corners_model`, generates an architectural concept model based on the metaphor of "Cantilevering corners." It begins by establishing a central core that acts as a stable anchor, embodying the essence of balance. The function then creates multiple cantilevered sections that extend outward from this core, each varying in angle and height to enhance the sense of motion and tension. This design approach captures the interplay between solid and void, utilizing randomness to create unique spatial configurations that challenge traditional architectural forms. The resulting geometries invite exploration, embodying the dynamic relationship between stability and motion."""

#! python 3
function_code = """def create_cantilevering_corners_model(core_height, core_width, core_depth, cantilever_count, cantilever_length, cantilever_height_variation):
    \"""
    Creates an architectural Concept Model embodying the 'Cantilevering corners' metaphor. 
    The model consists of a central core with multiple cantilevered sections extending outward.
    
    Parameters:
    - core_height (float): The height of the central core in meters.
    - core_width (float): The width of the central core in meters.
    - core_depth (float): The depth of the central core in meters.
    - cantilever_count (int): The number of cantilevered sections extending from the core.
    - cantilever_length (float): The length of the cantilevers in meters.
    - cantilever_height_variation (float): Maximum variation in height for each cantilever in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the concept model.
    \"""
    import Rhino
    import Rhino.Geometry as rg
    import random
    import math

    # Set a seed for randomness to ensure replicable results
    random.seed(42)

    # Create the central core as a Brep
    core = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_depth), rg.Interval(0, core_height))
    breps = [core.ToBrep()]

    # Generate cantilevered sections
    for i in range(cantilever_count):
        angle = random.uniform(0, 360)  # Random angle for each cantilever
        height_variation = random.uniform(-cantilever_height_variation, cantilever_height_variation)
        
        # Create a vector for the cantilever direction
        direction = rg.Vector3d(cantilever_length, 0, 0)
        direction.Rotate(math.radians(angle), rg.Vector3d.ZAxis)
        
        # Define the base plane for the cantilever
        base_plane = rg.Plane(core.Center, rg.Vector3d.ZAxis)
        base_plane.OriginZ += height_variation
        
        # Create the cantilever as a Brep
        cantilever = rg.Box(base_plane, rg.Interval(0, cantilever_length), rg.Interval(0, core_width / 2), rg.Interval(0, core_height / 3))
        breps.append(cantilever.ToBrep())

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevering_corners_model(10.0, 5.0, 5.0, 4, 3.0, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevering_corners_model(15.0, 6.0, 4.0, 6, 2.5, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevering_corners_model(12.0, 7.0, 6.0, 5, 4.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevering_corners_model(8.0, 4.0, 3.0, 3, 2.0, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevering_corners_model(9.0, 5.5, 4.5, 2, 3.5, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
