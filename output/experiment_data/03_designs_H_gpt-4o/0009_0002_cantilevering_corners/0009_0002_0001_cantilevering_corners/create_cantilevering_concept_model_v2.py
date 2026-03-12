# Created for 0009_0002_cantilevering_corners.json

""" Summary:
The function `create_cantilevering_concept_model_v2` generates an architectural concept model based on the metaphor of "Cantilevering corners." It creates a central core volume (a cube) from which multiple cantilevered sections extend outward at varying angles and lengths. This design emphasizes a dynamic balance between stability (the core) and motion (the cantilevers), reflecting the metaphor's essence. By varying the size, orientation, and position of the cantilevered elements, the function captures the interplay of light and shadow, creating intriguing spatial relationships that invite exploration and interaction with the surrounding environment."""

#! python 3
function_code = """def create_cantilevering_concept_model_v2(base_size=10, cantilever_count=6, max_extension=8, max_angle_variation=30):
    \"""
    Generates an architectural Concept Model inspired by the 'Cantilevering corners' metaphor.

    This function creates a base volume and multiple cantilevered sections that extend outward,
    emphasizing dynamic balance and spatial interaction. The cantilevered sections project at
    varying angles and distances, creating an interplay of stability and motion.

    Parameters:
    - base_size (float): The dimension of the central core cube in meters.
    - cantilever_count (int): The number of cantilevered volumes to generate.
    - max_extension (float): The maximum extension of cantilevered volumes from the core in meters.
    - max_angle_variation (float): The maximum angular variation for cantilever projection in degrees.

    Returns:
    - list: A list of RhinoCommon Breps representing the concept model geometries.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set a seed for reproducibility
    random.seed(42)

    # Create the central core as a cube
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-base_size/2, base_size/2), rg.Interval(-base_size/2, base_size/2), rg.Interval(0, base_size))
    core_brep = core_box.ToBrep()
    geometries = [core_brep]

    # Function to create a cantilevered volume
    def create_cantilever(length, angle):
        # Create a cantilever box
        cantilever_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_size/2), rg.Interval(0, base_size/4), rg.Interval(0, base_size/4))

        # Randomly choose a direction for the cantilever
        direction = rg.Vector3d(random.choice([-1, 1]), random.choice([-1, 1]), 0)
        direction.Unitize()
        direction *= length

        # Apply rotation to the cantilever
        rotation = rg.Transform.Rotation(math.radians(angle), rg.Vector3d.ZAxis, rg.Point3d.Origin)
        cantilever_box.Transform(rotation)

        # Apply translation to position the cantilever
        translation = rg.Transform.Translation(direction)
        cantilever_box.Transform(translation)

        # Convert the box to a Brep
        cantilever_brep = cantilever_box.ToBrep()
        return cantilever_brep

    # Generate cantilevered volumes
    for _ in range(cantilever_count):
        length = random.uniform(base_size/2, max_extension)
        angle = random.uniform(-max_angle_variation, max_angle_variation)

        cantilever = create_cantilever(length, angle)
        geometries.append(cantilever)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevering_concept_model_v2(base_size=12, cantilever_count=8, max_extension=10, max_angle_variation=45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevering_concept_model_v2(base_size=15, cantilever_count=5, max_extension=12, max_angle_variation=60)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevering_concept_model_v2(base_size=8, cantilever_count=10, max_extension=6, max_angle_variation=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevering_concept_model_v2(base_size=20, cantilever_count=4, max_extension=5, max_angle_variation=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevering_concept_model_v2(base_size=11, cantilever_count=7, max_extension=9, max_angle_variation=35)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
