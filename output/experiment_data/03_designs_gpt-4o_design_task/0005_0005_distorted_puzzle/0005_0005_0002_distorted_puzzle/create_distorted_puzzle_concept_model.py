# Created for 0005_0005_distorted_puzzle.json

""" Summary:
The provided function, `create_distorted_puzzle_concept_model`, generates an architectural concept model inspired by the "Distorted puzzle" metaphor. It creates a series of interlocking, fragmented volumes that vary in height and form, embodying the metaphor's themes of asymmetry and interconnectedness. By randomly positioning and transforming these volumes, the function ensures a dynamic play of light and shadow, enhancing visual complexity. Each volume appears distinct yet contributes to a cohesive whole, allowing for diverse spatial experiences. This approach not only reflects the metaphor's essence but also invites exploration and discovery within the architectural space."""

#! python 3
function_code = """def create_distorted_puzzle_concept_model(base_length, base_width, max_height, min_height, num_volumes, seed=42):
    \"""
    Generate a Concept Model based on the 'Distorted puzzle' metaphor. The model consists of fragmented, interlocking volumes
    with asymmetric forms and varying heights. The design aims to create a dynamic interplay of light and shadow, promoting a 
    balance between individuality and unity among the volumes.

    Parameters:
    - base_length (float): The base length of the bounding area for the concept model in meters.
    - base_width (float): The base width of the bounding area for the concept model in meters.
    - max_height (float): The maximum height of any volume in the model in meters.
    - min_height (float): The minimum height of any volume in the model in meters.
    - num_volumes (int): The number of interlocking volumes to generate.
    - seed (int, optional): Seed for random number generator to ensure replicable results. Default is 42.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    volumes = []

    for _ in range(num_volumes):
        # Generate random dimensions for each volume
        length = random.uniform(base_length * 0.1, base_length * 0.3)
        width = random.uniform(base_width * 0.1, base_width * 0.3)
        height = random.uniform(min_height, max_height)

        # Create a random position within the base area
        x = random.uniform(0, base_length - length)
        y = random.uniform(0, base_width - width)
        z = 0  # All volumes start from the base plane

        # Create a base point for the volume
        base_point = rg.Point3d(x, y, z)

        # Create a box (volume) with the generated dimensions at the base point
        box = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))
        brep = box.ToBrep()

        # Apply a random transformation to create asymmetry
        center = box.Center
        angle = random.uniform(-0.2, 0.2)  # Radians
        axis = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        axis.Unitize()
        rotation = rg.Transform.Rotation(angle, axis, center)
        brep.Transform(rotation)

        volumes.append(brep)

    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_concept_model(10.0, 5.0, 3.0, 1.0, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_concept_model(8.0, 4.0, 2.5, 0.5, 10, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_concept_model(12.0, 6.0, 4.0, 2.0, 20, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_concept_model(15.0, 7.0, 5.0, 2.0, 12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_concept_model(9.0, 4.5, 3.5, 1.5, 18, seed=75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
