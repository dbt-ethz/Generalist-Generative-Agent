# Created for 0005_0002_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_model` generates an architectural concept model inspired by the 'Distorted puzzle' metaphor by creating a series of fragmented, interconnected modules. Each module is a box with randomized dimensions, twisted around a vertical axis to enhance the sense of movement and tension. The modules are positioned with random offsets, creating a labyrinthine arrangement that encourages exploration. The stacking and overlapping of these forms embody the metaphors complexity, while the overall layout challenges perceptions of order and symmetry, evoking curiosity and engagement in users as they navigate through the dynamic space."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_size, num_modules, max_twist_angle, max_offset, seed=42):
    \"""
    Generate an architectural Concept Model based on the 'Distorted puzzle' metaphor.

    Parameters:
    - base_size: A float representing the base dimension of each module in meters.
    - num_modules: An integer representing the number of modules to be created.
    - max_twist_angle: A float indicating the maximum angle in degrees to twist each module.
    - max_offset: A float indicating the maximum offset distance for positioning modules.
    - seed: An integer for random number generation to ensure replicable results.

    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the randomness seed for reproducibility
    random.seed(seed)

    # Initialize a list to store the resulting geometries
    geometries = []

    # Starting point for module placement
    current_x, current_y, current_z = 0, 0, 0

    # Define the base module as a simple box with random dimensions
    def create_module(x, y, z, size):
        width = size + random.uniform(-0.2, 0.2) * size
        depth = size + random.uniform(-0.2, 0.2) * size
        height = size + random.uniform(-0.2, 0.2) * size
        base_plane = rg.Plane(rg.Point3d(x, y, z), rg.Vector3d.ZAxis)
        box = rg.Box(base_plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))
        return box.ToBrep()

    for i in range(num_modules):
        # Create a new module
        module = create_module(current_x, current_y, current_z, base_size)

        # Twist the module around its vertical axis
        twist_angle = random.uniform(-max_twist_angle, max_twist_angle)
        twist_axis = rg.Line(rg.Point3d(current_x, current_y, current_z), rg.Point3d(current_x, current_y, current_z + base_size))
        twist = rg.Transform.Rotation(math.radians(twist_angle), twist_axis.Direction, twist_axis.From)
        module.Transform(twist)

        # Add the module to the list of geometries
        geometries.append(module)

        # Determine the offset for the next module
        offset_x = random.uniform(-max_offset, max_offset)
        offset_y = random.uniform(-max_offset, max_offset)
        offset_z = random.uniform(0, base_size * 0.5)

        # Update the current position
        current_x += offset_x
        current_y += offset_y
        current_z += offset_z

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(1.0, 10, 45, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(2.0, 15, 30, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(1.5, 20, 60, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(3.0, 5, 90, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(0.8, 12, 75, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
