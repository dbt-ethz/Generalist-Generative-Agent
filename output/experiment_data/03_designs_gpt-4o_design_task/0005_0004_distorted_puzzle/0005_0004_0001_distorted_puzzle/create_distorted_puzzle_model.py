# Created for 0005_0004_distorted_puzzle.json

""" Summary:
The provided function, `create_distorted_puzzle_model`, generates an architectural concept model based on the "Distorted puzzle" metaphor by creating a series of irregularly shaped units that interconnect through perceived tension. It achieves this by generating tilted boxes with random orientations and positions, ensuring non-linear spatial arrangements that form niches and alcoves. The function allows for dynamic visual complexity while maintaining coherence through key visual axes. By manipulating parameters like base size, unit count, and tilt angles, the model captures the essence of a distorted yet cohesive structure, inviting exploration and discovery through its intricate massing and unexpected spatial relationships."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_size, unit_count, angle_range, seed):
    \"""
    Create an architectural Concept Model based on the 'Distorted puzzle' metaphor.
    
    This function generates a series of interconnected yet irregularly shaped units that fit together
    through perceived tension and dynamic alignment, creating an intricate massing with tilted planes
    and skewed edges. The spatial arrangement promotes a non-linear flow, with interlocking spaces
    forming niches and alcoves, inviting exploration and highlighting key visual axes.

    Parameters:
    - base_size (float): The base size of each unit in meters.
    - unit_count (int): The number of units to generate.
    - angle_range (tuple): A tuple of two floats representing the minimum and maximum angles (in degrees)
      for tilting planes and skewed edges.
    - seed (int): The seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino
    import System
    import random
    import math

    # Set the seed for replicability
    random.seed(seed)

    # Helper function to create a tilted box
    def create_tilted_box(origin, size, angle):
        # Create a base box
        base_box = Rhino.Geometry.Box(
            Rhino.Geometry.Plane(origin, Rhino.Geometry.Vector3d.ZAxis),
            Rhino.Geometry.Interval(0, size),
            Rhino.Geometry.Interval(0, size),
            Rhino.Geometry.Interval(0, size)
        )
        # Tilt the box by rotating around a random axis
        rotation_axis = Rhino.Geometry.Vector3d(
            random.uniform(-1, 1),
            random.uniform(-1, 1),
            random.uniform(-1, 1)
        )
        rotation_axis.Unitize()
        rotation_angle = math.radians(random.uniform(angle[0], angle[1]))
        transform = Rhino.Geometry.Transform.Rotation(rotation_angle, rotation_axis, origin)
        base_box.Transform(transform)
        return base_box.ToBrep()

    # List to store the generated units
    units = []

    # Generate units with random placement and orientation
    for _ in range(unit_count):
        # Randomly position each unit
        x = random.uniform(-base_size * unit_count / 2, base_size * unit_count / 2)
        y = random.uniform(-base_size * unit_count / 2, base_size * unit_count / 2)
        z = random.uniform(0, base_size * unit_count / 2)
        origin = Rhino.Geometry.Point3d(x, y, z)

        # Create a tilted box unit
        unit = create_tilted_box(origin, base_size, angle_range)
        units.append(unit)

    return units"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(5.0, 10, (15, 45), 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(3.5, 15, (10, 30), 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(4.0, 20, (20, 60), 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(6.0, 12, (5, 25), 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(2.5, 8, (30, 75), 101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
