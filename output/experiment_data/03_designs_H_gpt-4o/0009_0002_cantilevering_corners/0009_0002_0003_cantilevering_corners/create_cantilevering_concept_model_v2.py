# Created for 0009_0002_cantilevering_corners.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "Cantilevering corners." It constructs a central core structure and adds multiple cantilevered volumes that extend outward at varying angles and lengths. The design emphasizes the dynamic interplay between stability and motion, capturing the essence of the metaphor. By varying the scale, orientation, and attachment of each cantilevered element, the function creates a complex arrangement that fosters exploration of negative spaces and interactions with light and shadow. The resulting geometries represent a balance between anchored stability and daring projections, reflecting the architectural intent of the task."""

#! python 3
function_code = """def create_cantilevering_concept_model_v2(core_size=10, cantilever_count=5, max_extension=12, max_rotation=30):
    \"""
    Creates an architectural Concept Model based on the metaphor of 'Cantilevering corners'.
    
    This updated model comprises a central core with multiple cantilevered volumes extending outward
    at different angles and lengths. The design focuses on the interplay of balance and counterbalance,
    highlighting transitions between the stable core and dynamic projections by varying scale and orientation.

    Parameters:
    - core_size (float): The size of the core structure in meters.
    - cantilever_count (int): The number of cantilevered volumes to generate.
    - max_extension (float): The maximum extension length of cantilevered volumes in meters.
    - max_rotation (float): The maximum rotation angle in degrees of cantilevered volumes.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set a seed for randomness to ensure replicability
    random.seed(42)

    # Create the central core as a cube
    core = rg.Box(rg.Plane.WorldXY, rg.Interval(-core_size/2, core_size/2),
                  rg.Interval(-core_size/2, core_size/2), rg.Interval(-core_size/2, core_size/2))
    geometries = [core.ToBrep()]

    # Generate cantilevered volumes
    for _ in range(cantilever_count):
        length = random.uniform(core_size * 0.6, max_extension)
        width = random.uniform(core_size * 0.3, core_size * 0.5)
        height = random.uniform(core_size * 0.2, core_size * 0.4)

        angle = random.uniform(-max_rotation, max_rotation)
        rotation_axis = rg.Vector3d(random.choice([0, 1]), random.choice([0, 1]), random.choice([0, 1]))
        
        # Create a basic cantilever box
        cantilever_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))
        
        # Apply a rotation transformation
        rotation = rg.Transform.Rotation(math.radians(angle), rotation_axis, rg.Point3d.Origin)
        cantilever_box.Transform(rotation)

        # Randomly determine the attachment side and translation
        attach_side = random.choice(['left', 'right', 'front', 'back', 'top'])
        if attach_side == 'left':
            translation = rg.Transform.Translation(-core_size/2 - length/2, 0, 0)
        elif attach_side == 'right':
            translation = rg.Transform.Translation(core_size/2 + length/2, 0, 0)
        elif attach_side == 'front':
            translation = rg.Transform.Translation(0, -core_size/2 - width/2, 0)
        elif attach_side == 'back':
            translation = rg.Transform.Translation(0, core_size/2 + width/2, 0)
        else:  # top
            translation = rg.Transform.Translation(0, 0, core_size/2 + height/2)

        cantilever_box.Transform(translation)
        
        # Convert to Brep and add to geometries
        geometries.append(cantilever_box.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevering_concept_model_v2(core_size=15, cantilever_count=8, max_extension=10, max_rotation=45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevering_concept_model_v2(core_size=20, cantilever_count=10, max_extension=15, max_rotation=60)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevering_concept_model_v2(core_size=12, cantilever_count=6, max_extension=14, max_rotation=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevering_concept_model_v2(core_size=18, cantilever_count=4, max_extension=8, max_rotation=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevering_concept_model_v2(core_size=25, cantilever_count=3, max_extension=20, max_rotation=35)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
