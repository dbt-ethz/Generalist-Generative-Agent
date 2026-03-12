# Created for 0009_0002_cantilevering_corners.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "Cantilevering corners." It establishes a central core structure from which multiple cantilevered volumes extend at varying angles and lengths, embodying dynamic balance and tension. By employing randomness in the length and angle of these projections, the model results in a diverse interplay of volumes that emphasizes the contrast between stability and motion. The method highlights the relationship between the core and the cantilevers through distinct transformations in form and material, while also considering interactions with light and shadow, ultimately capturing the essence of the metaphor."""

#! python 3
function_code = """def create_cantilevered_concept_model(core_size=10, cantilever_count=4, max_length=15, max_angle=45):
    \"""
    Creates an architectural Concept Model based on the metaphor of 'Cantilevering corners'.
    
    The model consists of a central core from which a series of cantilevered volumes project outward at various angles and lengths.
    These volumes create a dynamic play of balance and counterbalance, emphasizing the relationship between the stable core and the cantilevered sections.

    Parameters:
    - core_size: The size of the central core cube in meters.
    - cantilever_count: The number of cantilevered volumes to create.
    - max_length: The maximum length of the cantilevered volumes in meters.
    - max_angle: The maximum angle in degrees at which the cantilevers can project from the core.

    Returns:
    - List of 3D geometries (breps) representing the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set a seed for randomness to ensure replicability
    random.seed(42)

    # Create the central core as a cube
    core = rg.Box(rg.Plane.WorldXY, rg.Interval(-core_size/2, core_size/2), rg.Interval(-core_size/2, core_size/2), rg.Interval(-core_size/2, core_size/2))
    geometries = [core.ToBrep()]

    # Generate cantilevered volumes
    for _ in range(cantilever_count):
        length = random.uniform(core_size / 2, max_length)
        angle = random.uniform(-max_angle, max_angle)
        
        # Create a transformation matrix for rotation and translation
        rotation_axis = rg.Vector3d(random.choice([1,-1]), random.choice([1,-1]), 0)
        rotation = rg.Transform.Rotation(math.radians(angle), rotation_axis, core.Center)
        
        # Determine the direction of the cantilever
        direction = rg.Vector3d(random.choice([-1, 1]), random.choice([-1, 1]), 0)
        translation = rg.Transform.Translation(direction * length)

        # Create cantilevered volume as a box
        cantilever_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_size), rg.Interval(0, core_size), rg.Interval(0, core_size/3))
        cantilever_brep = cantilever_box.ToBrep()
        
        # Apply transformations
        cantilever_brep.Transform(rotation)
        cantilever_brep.Transform(translation)
        
        # Add cantilever to geometries
        geometries.append(cantilever_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_concept_model(core_size=12, cantilever_count=5, max_length=20, max_angle=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_concept_model(core_size=8, cantilever_count=3, max_length=10, max_angle=60)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_concept_model(core_size=15, cantilever_count=6, max_length=25, max_angle=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_concept_model(core_size=14, cantilever_count=2, max_length=18, max_angle=35)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_concept_model(core_size=9, cantilever_count=4, max_length=12, max_angle=40)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
