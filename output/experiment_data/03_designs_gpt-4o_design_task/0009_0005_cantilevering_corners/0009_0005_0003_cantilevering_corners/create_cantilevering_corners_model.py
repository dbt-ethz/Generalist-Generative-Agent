# Created for 0009_0005_cantilevering_corners.json

""" Summary:
The provided function, `create_cantilevering_corners_model`, generates an architectural concept model based on the metaphor of "Cantilevering corners." It begins by establishing a central core that serves as a stable anchor. The function then creates multiple cantilevered sections that extend outward at varying angles, embodying a dynamic interplay between stability and motion. By adjusting the cantilever lengths and widths, along with their positions relative to the core, the model achieves a visually engaging silhouette. The integration of solid and void spaces enhances the sense of tension and balance, inviting exploration and interaction within the architectural design."""

#! python 3
function_code = """def create_cantilevering_corners_model(core_width, core_height, num_cantilevers, cantilever_length, cantilever_angle_range):
    \"""
    Creates an architectural Concept Model embodying the metaphor of 'Cantilevering corners'.
    
    Parameters:
    - core_width: The width of the central core in meters.
    - core_height: The height of the central core in meters.
    - num_cantilevers: The number of cantilevered sections extending from the core.
    - cantilever_length: The maximum length of the cantilevered sections in meters.
    - cantilever_angle_range: A tuple (min_angle, max_angle) defining the range of angles (in degrees) 
      for the cantilevered sections relative to the core.

    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometry of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for replicability
    random.seed(42)

    # Create the central core
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_width), rg.Interval(0, core_height))
    core_brep = core_box.ToBrep()

    # List to store all 3D geometries
    geometries = [core_brep]

    # Calculate the center point of the top face of the core
    top_center = rg.Point3d(core_width / 2, core_width / 2, core_height)

    # Create cantilevered sections
    for _ in range(num_cantilevers):
        # Randomly select an angle and direction for the cantilever
        angle = random.uniform(cantilever_angle_range[0], cantilever_angle_range[1])
        direction = rg.Vector3d(math.cos(math.radians(angle)), math.sin(math.radians(angle)), 0)
        direction.Unitize()

        # Create a cantilevered box
        cantilever_vector = direction * cantilever_length
        cantilever_width = core_width * 0.5  # Proportionally smaller than the core
        cantilever_height = core_height * 0.1  # Thin compared to the height for visual contrast
        cantilever_box = rg.Box(rg.Plane(top_center + cantilever_vector, direction),
                                rg.Interval(-cantilever_width / 2, cantilever_width / 2),
                                rg.Interval(-cantilever_width / 2, cantilever_width / 2),
                                rg.Interval(-cantilever_height, 0))
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
    geometry = create_cantilevering_corners_model(5, 10, 4, 3, (15, 75))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevering_corners_model(8, 12, 3, 4, (30, 60))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevering_corners_model(6, 15, 5, 2, (10, 80))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevering_corners_model(7, 14, 6, 5, (20, 70))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevering_corners_model(9, 11, 2, 6, (5, 90))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
