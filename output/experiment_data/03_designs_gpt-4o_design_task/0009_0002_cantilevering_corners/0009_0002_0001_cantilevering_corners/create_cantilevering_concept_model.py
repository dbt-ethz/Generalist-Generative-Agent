# Created for 0009_0002_cantilevering_corners.json

""" Summary:
The function `create_cantilevering_concept_model` generates an architectural concept model based on the metaphor of "Cantilevering corners" by creating a central core structure and attaching multiple cantilevered volumes that project outward. It emphasizes dynamic equilibrium, balancing stability and motion through varying lengths, angles, and orientations of these projections. The model's design incorporates randomness in the placement and direction of cantilevers, fostering intriguing negative spaces. This interaction invites exploration and highlights the relationship between the stable core and the cantilevered sections, effectively translating the metaphor into a physical representation that evokes a dialogue with its environment."""

#! python 3
function_code = """def create_cantilevering_concept_model(base_width, base_depth, base_height, cantilever_length, cantilever_height, num_cantilevers):
    \"""
    Creates an architectural Concept Model based on the metaphor of 'Cantilevering corners'. The model consists of a central core
    with multiple cantilevered volumes projecting outward at various angles and lengths, emphasizing the dynamic equilibrium
    and interplay of balance and counterbalance.

    Parameters:
    - base_width (float): The width of the core structure.
    - base_depth (float): The depth of the core structure.
    - base_height (float): The height of the core structure.
    - cantilever_length (float): The maximum length for the cantilevered volumes.
    - cantilever_height (float): The height of each cantilevered volume.
    - num_cantilevers (int): The number of cantilevered volumes to create.

    Returns:
    - list: A list of Breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a seed for randomness
    random.seed(42)

    # Create the core structure
    core = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_width), rg.Interval(0, base_depth), rg.Interval(0, base_height))
    geometries = [core.ToBrep()]

    # Calculate the positions and orientations for cantilevers
    for _ in range(num_cantilevers):
        # Randomly choose a side of the core for cantilever attachment
        side = random.choice(['left', 'right', 'front', 'back'])

        # Define the transformation for the cantilever
        if side == 'left':
            origin = rg.Point3d(0, random.uniform(0, base_depth), random.uniform(base_height / 3, base_height))
            direction = rg.Vector3d(-1, 0, random.uniform(-0.3, 0.3))
        elif side == 'right':
            origin = rg.Point3d(base_width, random.uniform(0, base_depth), random.uniform(base_height / 3, base_height))
            direction = rg.Vector3d(1, 0, random.uniform(-0.3, 0.3))
        elif side == 'front':
            origin = rg.Point3d(random.uniform(0, base_width), 0, random.uniform(base_height / 3, base_height))
            direction = rg.Vector3d(0, -1, random.uniform(-0.3, 0.3))
        else:  # back
            origin = rg.Point3d(random.uniform(0, base_width), base_depth, random.uniform(base_height / 3, base_height))
            direction = rg.Vector3d(0, 1, random.uniform(-0.3, 0.3))

        direction.Unitize()
        direction *= random.uniform(cantilever_length * 0.5, cantilever_length)

        # Create the cantilevered volume
        cantilever_box = rg.Box(rg.Plane(origin, rg.Vector3d.ZAxis), rg.Interval(0, cantilever_length), rg.Interval(0, base_depth / 3), rg.Interval(0, cantilever_height))
        cantilever_brep = cantilever_box.ToBrep()
        
        # Transform cantilever to its direction
        translation = rg.Transform.Translation(direction)
        cantilever_brep.Transform(translation)

        geometries.append(cantilever_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevering_concept_model(10.0, 15.0, 20.0, 5.0, 3.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevering_concept_model(12.0, 18.0, 25.0, 6.0, 4.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevering_concept_model(8.0, 10.0, 15.0, 4.0, 2.5, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevering_concept_model(14.0, 20.0, 30.0, 7.0, 5.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevering_concept_model(11.0, 14.0, 22.0, 4.5, 3.5, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
