# Created for 0009_0001_cantilevering_corners.json

""" Summary:
The function `create_concept_model` generates an architectural concept model inspired by the metaphor of "Cantilevering corners." It constructs a stable base and adds cantilevered sections at each corner, reflecting a dynamic balance between stability and motion, as described in the metaphor. Each cantilever is designed to project outward, featuring dramatic overhangs that challenge conventional support structures. The function incorporates randomness in angle variations for a unique aesthetic, resulting in a diverse range of architectural forms. This approach effectively embodies the metaphor's essence, allowing for innovative and visually striking architectural concepts."""

#! python 3
function_code = """def create_concept_model(base_width, base_depth, base_height, cantilever_length, cantilever_height, random_seed):
    \"""
    Create an architectural Concept Model based on the metaphor of 'Cantilevering corners'.
    
    This function generates a conceptual architectural model featuring dynamic interactions between 
    stability and motion. The model includes a stable base with cantilevered sections that project outward 
    in a balanced manner, creating dramatic overhangs.

    Parameters:
    base_width (float): The width of the stable base of the structure in meters.
    base_depth (float): The depth of the stable base of the structure in meters.
    base_height (float): The height of the stable base of the structure in meters.
    cantilever_length (float): The length of the cantilevering sections in meters.
    cantilever_height (float): The height of the cantilevering sections in meters.
    random_seed (int): Seed for the random number generator to ensure replicability.

    Returns:
    list: A list of Breps representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for replicability
    random.seed(random_seed)

    # Create the base of the structure
    base_origin = rg.Point3d(0, 0, 0)
    base = rg.Box(rg.Plane(base_origin, rg.Vector3d.ZAxis), rg.Interval(0, base_width), rg.Interval(0, base_depth), rg.Interval(0, base_height))
    
    # Create cantilevering sections
    cantilevers = []
    for i in range(4):  # Create cantilevers at each corner of the base
        offset_x = base_width if i % 2 == 0 else 0
        offset_y = base_depth if i < 2 else 0
        cantilever_origin = rg.Point3d(offset_x, offset_y, base_height)
        
        angle_variation = random.uniform(-15, 15)  # Random angle variation for dynamic effect
        rotation_axis = rg.Vector3d.ZAxis
        rotation_angle = math.radians(angle_variation)
        
        cantilever = rg.Box(rg.Plane(cantilever_origin, rg.Vector3d.ZAxis), rg.Interval(0, cantilever_length), rg.Interval(0, cantilever_length), rg.Interval(0, cantilever_height))
        # Rotate the cantilever for a dynamic effect
        cantilever_brep = cantilever.ToBrep()
        rotation_transform = rg.Transform.Rotation(rotation_angle, rotation_axis, cantilever_origin)
        cantilever_brep.Transform(rotation_transform)
        cantilevers.append(cantilever_brep)

    # Combine base and cantilevers into a list of geometries
    geometries = [base.ToBrep()] + cantilevers

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(10.0, 5.0, 3.0, 4.0, 2.0, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(12.0, 6.0, 4.0, 5.0, 3.0, 100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(15.0, 7.0, 5.0, 6.0, 4.0, 23)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(8.0, 4.0, 2.5, 3.0, 1.5, 55)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(14.0, 8.0, 6.0, 7.0, 3.5, 78)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
