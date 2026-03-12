# Created for 0005_0001_distorted_puzzle.json

""" Summary:
The provided function, `create_distorted_puzzle_model`, generates an architectural concept model based on the "Distorted puzzle" metaphor by creating interlocking geometric volumes with slight misalignments. It accepts parameters for base dimensions and the number of volumes, utilizing randomness to introduce distortion and variation in size and position. Each volume is represented as a 3D box, with random offsets ensuring that they connect in unexpected yet coherent ways, mimicking a puzzle's interlocking nature. The result is a dynamic and visually intriguing model that embodies movement and tension while promoting exploration within its irregularly shaped spaces."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_length, base_width, base_height, num_volumes, seed=None):
    \"""
    Create an architectural Concept Model embodying the 'Distorted puzzle' metaphor by assembling a series of interlocking 
    geometric volumes with slight misalignments. The model emphasizes the spatial logic of interlocking and overlapping forms to 
    generate dynamic pathways and spaces that invite exploration.

    Args:
    - base_length (float): The base length of the initial volume in meters.
    - base_width (float): The base width of the initial volume in meters.
    - base_height (float): The base height of the initial volume in meters.
    - num_volumes (int): The number of interlocking volumes to create.
    - seed (int, optional): Seed for random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    if seed is not None:
        random.seed(seed)

    volumes = []
    current_position = rg.Point3d(0, 0, 0)

    for i in range(num_volumes):
        # Create a box with a base size and randomize dimensions slightly
        length = base_length * (1 + random.uniform(-0.1, 0.1))
        width = base_width * (1 + random.uniform(-0.1, 0.1))
        height = base_height * (1 + random.uniform(-0.1, 0.1))
        
        # Create a box at the current position
        box = rg.Box(rg.Plane(current_position, rg.Vector3d.ZAxis), rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))
        brep = box.ToBrep()
        volumes.append(brep)
        
        # Determine the next position with random offset for distortion
        offset_vector = rg.Vector3d(random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0))
        offset_vector *= random.uniform(0.5, 1.5)
        current_position += offset_vector

    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(5.0, 3.0, 2.0, 10, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(4.0, 2.0, 3.0, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(6.0, 4.0, 5.0, 12, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(7.0, 5.0, 4.0, 15, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(3.5, 2.5, 1.5, 6, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
