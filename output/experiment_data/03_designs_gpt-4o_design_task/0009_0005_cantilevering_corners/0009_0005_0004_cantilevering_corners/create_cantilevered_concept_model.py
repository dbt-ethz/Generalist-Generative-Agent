# Created for 0009_0005_cantilevering_corners.json

""" Summary:
The provided function generates an architectural concept model reflecting the metaphor of "Cantilevering corners." It starts by defining a central core, serving as the structural anchor. From this core, multiple cantilevered sections are extended outwards at varied angles and lengths, embodying a sense of dynamic motion and tension. The function incorporates randomness in the dimensions and positioning of these cantilevers to create a visually engaging and balanced composition. By allowing varying levels of transparency, it further emphasizes the interaction between solid and void, enhancing light and shadow dynamics. This approach successfully captures the essence of stability and movement."""

#! python 3
function_code = """def create_cantilevered_concept_model(core_size, num_cantilevers, max_cantilever_length, max_cantilever_angle, transparency):
    \"""
    Generates an architectural Concept Model based on the metaphor of 'Cantilevering corners'.
    
    Parameters:
    - core_size: Tuple of three floats (width, depth, height) defining the dimensions of the central core.
    - num_cantilevers: Integer specifying the number of cantilevered sections to be generated.
    - max_cantilever_length: Float specifying the maximum length a cantilever can extend from the core.
    - max_cantilever_angle: Float specifying the maximum angle in degrees that a cantilever can deviate from the horizontal plane.
    - transparency: Float between 0 and 1 representing the transparency level of the cantilevered sections (0 is fully opaque, 1 is fully transparent).
    
    Returns:
    - List of Rhino.Geometry.Brep objects representing the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensuring replicability
    
    # Create the central core
    core_width, core_depth, core_height = core_size
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_depth), rg.Interval(0, core_height))
    core_brep = core_box.ToBrep()

    geometries = [core_brep]

    # Generate cantilevered sections
    for _ in range(num_cantilevers):
        # Randomly determine size, angle, and position for each cantilever
        length = random.uniform(0.5 * max_cantilever_length, max_cantilever_length)
        angle = random.uniform(-max_cantilever_angle, max_cantilever_angle)
        base_point_x = random.uniform(0, core_width)
        base_point_y = random.uniform(0, core_depth)
        base_point = rg.Point3d(base_point_x, base_point_y, core_height)

        # Define the cantilever plane and direction
        cantilever_plane = rg.Plane(base_point, rg.Vector3d(0, 0, 1))
        cantilever_direction = rg.Vector3d(math.cos(math.radians(angle)), math.sin(math.radians(angle)), 0)
        
        # Create the cantilever volume
        cantilever_box = rg.Box(cantilever_plane, rg.Interval(0, length), rg.Interval(0, core_depth * 0.5), rg.Interval(-core_height * 0.5, 0))
        cantilever_brep = cantilever_box.ToBrep()
        
        # Apply transparency (as a placeholder for material properties)
        # Here, transparency can be considered in the visualization context, which is not directly applicable in pure geometry
        # But this can be used in the context of applying materials in the rendering environment
        
        geometries.append(cantilever_brep)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_concept_model((5.0, 3.0, 10.0), 4, 6.0, 45.0, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_concept_model((10.0, 5.0, 15.0), 6, 8.0, 30.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_concept_model((7.0, 4.0, 12.0), 3, 5.0, 60.0, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_concept_model((8.0, 6.0, 20.0), 5, 10.0, 50.0, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_concept_model((4.0, 2.0, 8.0), 2, 7.0, 40.0, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
