# Created for 0005_0002_distorted_puzzle.json

""" Summary:
The provided function generates an architectural concept model inspired by the 'Distorted puzzle' metaphor by creating a series of fragmented, interconnected modules. Each module is designed as a tilted and rotated box, incorporating random variations in height, tilt, and rotation to enhance the sense of tension and complexity. The function allows for overlapping and stacking of modules, creating a labyrinthine spatial arrangement that challenges traditional notions of order and symmetry. This design approach encourages exploration and interaction, embodying the playful, yet cohesive characteristics of the metaphor, resulting in a visually engaging and dynamic architectural model."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_size, num_modules, height_variation, overlap_factor, seed=42):
    \"""
    Generate an architectural Concept Model based on the 'Distorted puzzle' metaphor.

    Parameters:
    - base_size: A float representing the base dimension of each module in meters.
    - num_modules: An integer representing the number of modules to be created.
    - height_variation: A float indicating the maximum height variation between stacked modules.
    - overlap_factor: A float between 0 and 1 indicating the degree of overlap between modules.
    - seed: An integer seed for random number generation to ensure replicability.

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

    # Define the base module as a simple tilted and rotated box
    def create_base_module(x, y, z, size, height, tilt_angle, rotation_angle):
        base_plane = rg.Plane(rg.Point3d(x, y, z), rg.Vector3d.ZAxis)
        box = rg.Box(base_plane, rg.Interval(0, size), rg.Interval(0, size), rg.Interval(0, height))
        
        # Create a transformation for tilting
        tilt_axis = rg.Vector3d(size / 2, size / 2, 0)
        tilt_transform = rg.Transform.Rotation(math.radians(tilt_angle), tilt_axis, base_plane.Origin)
        
        # Create a transformation for rotating
        rotation_transform = rg.Transform.Rotation(math.radians(rotation_angle), rg.Vector3d.ZAxis, base_plane.Origin)
        
        # Apply transformations
        box.Transform(tilt_transform)
        box.Transform(rotation_transform)
        
        return box.ToBrep()

    current_x, current_y, current_z = 0, 0, 0

    for i in range(num_modules):
        # Calculate the module's height with a variation
        module_height = base_size + random.uniform(-height_variation, height_variation)
        
        # Randomly decide tilt and rotation angles
        tilt_angle = random.uniform(-15, 15)  # degrees
        rotation_angle = random.uniform(-30, 30)  # degrees

        # Create a new module and add it to the list
        module = create_base_module(current_x, current_y, current_z, base_size, module_height, tilt_angle, rotation_angle)
        geometries.append(module)

        # Randomly decide the next module's position with overlap
        offset_x = base_size * (1 - random.uniform(0, overlap_factor))
        offset_y = base_size * (1 - random.uniform(0, overlap_factor))
        
        # Randomly select if the module should move in x or y direction
        if random.uniform(0, 1) > 0.5:
            current_x += offset_x
        else:
            current_y += offset_y

        # Randomly decide if the module should be stacked (add to z)
        if random.uniform(0, 1) > 0.3:
            current_z += module_height * (1 - overlap_factor)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(3.0, 10, 1.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(2.5, 15, 0.5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(4.0, 8, 2.0, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(5.0, 12, 1.5, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(1.5, 20, 0.8, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
