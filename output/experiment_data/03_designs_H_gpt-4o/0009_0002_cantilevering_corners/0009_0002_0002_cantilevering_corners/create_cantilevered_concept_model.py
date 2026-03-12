# Created for 0009_0002_cantilevering_corners.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "Cantilevering corners." It constructs a central core volume and a specified number of cantilevered sections that extend outward in various directions, embodying the dynamic balance between stability and motion. By manipulating the dimensions and positions of these cantilevers, the design creates an interplay of volumes, emphasizing contrasting anchored sections and projections. The function also considers the interaction of light and shadow on these elements, enhancing the metaphor's essence and inviting exploration of the spatial relationships within the architectural model, ultimately reflecting the concept of suspended motion."""

#! python 3
function_code = """def create_cantilevered_concept_model(core_dimensions=(10, 10, 10), cantilever_dimensions=(5, 2, 2), num_cantilevers=4):
    \"""
    Generates an architectural Concept Model inspired by the metaphor of 'Cantilevering corners'.
    
    This function creates a central core volume with a series of cantilevered sections that extend 
    outward at different angles and positions, emphasizing the dynamic equilibrium between stability 
    and motion. The design explores the interplay of balance and counterbalance through the 
    arrangement of these volumes.
    
    Parameters:
    - core_dimensions (tuple): Dimensions of the core structure as (width, depth, height) in meters.
    - cantilever_dimensions (tuple): Typical dimensions of each cantilever as (length, width, height) in meters.
    - num_cantilevers (int): Number of cantilevered elements to generate.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set a seed for reproducibility
    random.seed(42)

    # Create the central core structure
    core_width, core_depth, core_height = core_dimensions
    core = rg.Box(rg.Plane.WorldXY, rg.Interval(-core_width/2, core_width/2), rg.Interval(-core_depth/2, core_depth/2), rg.Interval(0, core_height))
    concept_model = [core.ToBrep()]

    # Create cantilevered sections
    for _ in range(num_cantilevers):
        # Randomly select a base point on the surface of the core
        side = random.choice(['x', 'y'])
        if side == 'x':
            base_x = random.choice([-core_width/2, core_width/2])
            base_y = random.uniform(-core_depth/2, core_depth/2)
        else:
            base_x = random.uniform(-core_width/2, core_width/2)
            base_y = random.choice([-core_depth/2, core_depth/2])

        # Define cantilever dimensions
        cant_length, cant_width, cant_height = cantilever_dimensions

        # Create a cantilever box
        cantilever_origin = rg.Point3d(base_x, base_y, random.uniform(core_height/2, core_height))
        cantilever_vector = rg.Vector3d(random.choice([-1, 1]), 0, 0) if side == 'x' else rg.Vector3d(0, random.choice([-1, 1]), 0)
        cantilever_vector *= cant_length

        cantilever_plane = rg.Plane(cantilever_origin, rg.Vector3d.ZAxis)
        cantilever_box = rg.Box(cantilever_plane, rg.Interval(0, cant_length), rg.Interval(-cant_width/2, cant_width/2), rg.Interval(0, cant_height))
        
        # Transform cantilever by extending it outwards
        translation = rg.Transform.Translation(cantilever_vector)
        cantilever_box.Transform(translation)

        concept_model.append(cantilever_box.ToBrep())

    return concept_model"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_concept_model(core_dimensions=(12, 12, 15), cantilever_dimensions=(6, 3, 3), num_cantilevers=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_concept_model(core_dimensions=(15, 10, 12), cantilever_dimensions=(7, 4, 4), num_cantilevers=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_concept_model(core_dimensions=(8, 8, 10), cantilever_dimensions=(4, 2, 2), num_cantilevers=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_concept_model(core_dimensions=(20, 10, 10), cantilever_dimensions=(8, 3, 3), num_cantilevers=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_concept_model(core_dimensions=(10, 15, 10), cantilever_dimensions=(5, 2, 4), num_cantilevers=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
