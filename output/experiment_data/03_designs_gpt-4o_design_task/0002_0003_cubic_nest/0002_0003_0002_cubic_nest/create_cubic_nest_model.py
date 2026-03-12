# Created for 0002_0003_cubic_nest.json

""" Summary:
The provided function generates an architectural concept model based on the "Cubic nest" metaphor by creating a series of interlinked cubic forms. Each cube's size and height vary randomly within specified parameters, fostering a dynamic and multi-dimensional structure. The function arranges these cubes with minimal gaps between them, reflecting the interconnectedness and protective qualities of a "nest." By manipulating the position and orientation of the cubes, the model achieves a balance of enclosure and openness. This design encourages exploration through its layered geometry, allowing users to experience unique spatial encounters within the architectural composition."""

#! python 3
function_code = """def create_cubic_nest_model(base_size, num_cubes, height_variation, min_gap, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Cubic nest' metaphor using a sequence of interwoven cubic forms.
    
    Parameters:
    - base_size: float - The base size of each cube in meters.
    - num_cubes: int - The number of cubic modules to generate.
    - height_variation: float - The maximum height variation for cubes in meters.
    - min_gap: float - The minimum gap between adjacent cubes in meters.
    - seed: int - Seed for random number generator to ensure replicability.
    
    Returns:
    - List of Brep: A list of Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    cubes = []

    # Define the initial starting point
    current_pos = rg.Point3d(0, 0, 0)

    for i in range(num_cubes):
        # Randomize the cube size slightly for variation
        size = base_size + random.uniform(-0.2, 0.2) * base_size

        # Create a base cube
        box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(current_pos.X, current_pos.X + size),
            rg.Interval(current_pos.Y, current_pos.Y + size),
            rg.Interval(current_pos.Z, current_pos.Z + size + random.uniform(0, height_variation))
        )
        cubes.append(box.ToBrep())

        # Calculate next position with a gap
        direction = random.choice([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
        move_vector = rg.Vector3d(
            direction[0] * (size + min_gap),
            direction[1] * (size + min_gap),
            direction[2] * (size + min_gap)
        )
        current_pos = rg.Point3d.Add(current_pos, move_vector)

    return cubes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_model(2.0, 10, 3.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_model(1.5, 5, 2.0, 0.3, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_model(3.0, 15, 1.5, 0.2, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_model(2.5, 8, 4.0, 0.4, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_model(1.0, 12, 2.5, 0.6, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
