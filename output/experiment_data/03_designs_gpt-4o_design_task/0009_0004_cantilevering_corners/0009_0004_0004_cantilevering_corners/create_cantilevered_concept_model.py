# Created for 0009_0004_cantilevering_corners.json

""" Summary:
The provided function `create_cantilevered_concept_model` generates an architectural concept model inspired by the metaphor of "Cantilevering corners." It constructs a central core structure and extends multiple cantilevered volumes in various directions. By allowing these sections to project outward from the core, the model embodies the tension between stability and motion, reflecting the metaphor's implications. The function utilizes randomization to determine the location and orientation of each cantilever, resulting in a dynamic and visually engaging composition. This approach creates unique spatial relationships, emphasizing the interplay of solid and void while capturing light and shadow to enhance the model's aesthetic appeal."""

#! python 3
function_code = """def create_cantilevered_concept_model(base_length, base_width, base_height, cantilever_length, cantilever_height, num_cantilevers, seed):
    \"""
    Generate an architectural Concept Model capturing the essence of 'Cantilevering corners' using angular, interlocking volumes.
    
    Parameters:
    - base_length (float): Length of the grounded core structure.
    - base_width (float): Width of the grounded core structure.
    - base_height (float): Height of the grounded core structure.
    - cantilever_length (float): Maximum extension length of cantilevered corners.
    - cantilever_height (float): Height of the cantilevered sections.
    - num_cantilevers (int): Number of cantilevered sections to create.
    - seed (int): Seed for random number generator to ensure replicability.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the architectural Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    geometries = []

    # Create the base core structure
    base_core = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    geometries.append(base_core.ToBrep())

    # Create cantilevered elements projecting from the core
    for _ in range(num_cantilevers):
        # Randomly choose a side of the core to attach the cantilever
        side = random.choice(['left', 'right', 'front', 'back', 'top'])
        
        if side == 'left':
            origin = rg.Point3d(-cantilever_length, random.uniform(0, base_width), random.uniform(0, base_height))
            vector = rg.Vector3d(cantilever_length, 0, 0)
        elif side == 'right':
            origin = rg.Point3d(base_length, random.uniform(0, base_width), random.uniform(0, base_height))
            vector = rg.Vector3d(cantilever_length, 0, 0)
        elif side == 'front':
            origin = rg.Point3d(random.uniform(0, base_length), -cantilever_length, random.uniform(0, base_height))
            vector = rg.Vector3d(0, cantilever_length, 0)
        elif side == 'back':
            origin = rg.Point3d(random.uniform(0, base_length), base_width, random.uniform(0, base_height))
            vector = rg.Vector3d(0, cantilever_length, 0)
        elif side == 'top':
            origin = rg.Point3d(random.uniform(0, base_length), random.uniform(0, base_width), base_height)
            vector = rg.Vector3d(0, 0, cantilever_length)

        # Create the cantilevered box
        cantilever_box = rg.Box(rg.Plane(origin, rg.Vector3d.XAxis, rg.Vector3d.YAxis), rg.Interval(0, vector.X), rg.Interval(0, vector.Y), rg.Interval(0, cantilever_height))
        geometries.append(cantilever_box.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_concept_model(10.0, 5.0, 3.0, 2.0, 1.5, 4, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_concept_model(15.0, 8.0, 4.0, 3.0, 2.0, 5, 101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_concept_model(12.0, 6.0, 3.5, 2.5, 2.0, 3, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_concept_model(8.0, 4.0, 2.5, 1.0, 1.0, 2, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_concept_model(20.0, 10.0, 5.0, 4.0, 3.0, 6, 123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
