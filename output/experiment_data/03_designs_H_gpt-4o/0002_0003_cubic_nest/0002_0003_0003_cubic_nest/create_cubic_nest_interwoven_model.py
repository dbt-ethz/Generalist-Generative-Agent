# Created for 0002_0003_cubic_nest.json

""" Summary:
The function `create_cubic_nest_interwoven_model` generates an architectural concept model based on the "Cubic nest" metaphor by creating a series of interwoven cubic forms. It defines a base cube and generates additional cubes positioned at varying layers, applying random rotations to enhance the sense of complexity and interconnectedness. The cubes are arranged to foster dynamic spatial experiences, embodying both enclosure and openness. By manipulating the arrangement and orientation of the cubes and allowing for movement through the structure, the model visually represents the metaphor's implications of refuge and curiosity, while each cubic module retains its distinct identity within the cohesive whole."""

#! python 3
function_code = """def create_cubic_nest_interwoven_model(base_size=10.0, layer_count=5, rotation_variation=15, seed=42):
    \"""
    Create an architectural Concept Model that represents a 'Cubic nest' metaphor using interwoven cubic forms.
    
    Parameters:
    - base_size (float): The base size of each cubic module in meters.
    - layer_count (int): The number of layers of cubes to create.
    - rotation_variation (float): Maximum angle variation for cube rotations in degrees.
    - seed (int): Seed for random number generator to ensure replicability.
    
    Returns:
    - List of Brep: A list of Brep objects representing the 3D geometry of the model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    
    breps = []

    # Create base cube
    base_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_size), rg.Interval(0, base_size), rg.Interval(0, base_size))
    breps.append(base_cube.ToBrep())

    # Generate additional cubes with interwoven rotations
    for layer in range(1, layer_count):
        # Calculate rotation angles
        angle_x = math.radians(random.uniform(-rotation_variation, rotation_variation))
        angle_y = math.radians(random.uniform(-rotation_variation, rotation_variation))
        angle_z = math.radians(random.uniform(-rotation_variation, rotation_variation))

        # Create transformation for rotation
        center_point = rg.Point3d(base_size / 2, base_size / 2, base_size / 2)
        rotation_x = rg.Transform.Rotation(angle_x, rg.Vector3d(1, 0, 0), center_point)
        rotation_y = rg.Transform.Rotation(angle_y, rg.Vector3d(0, 1, 0), center_point)
        rotation_z = rg.Transform.Rotation(angle_z, rg.Vector3d(0, 0, 1), center_point)

        # Create translation to offset cubes
        offset_distance = base_size * 0.3 * layer
        translation = rg.Transform.Translation(layer * offset_distance, 0, 0)

        # Apply transformations to a new cube
        new_cube = rg.Box(base_cube)
        new_cube.Transform(rotation_x)
        new_cube.Transform(rotation_y)
        new_cube.Transform(rotation_z)
        new_cube.Transform(translation)

        # Add the new cube to the list of Breps
        breps.append(new_cube.ToBrep())

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_interwoven_model(base_size=15.0, layer_count=7, rotation_variation=20, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_interwoven_model(base_size=12.0, layer_count=4, rotation_variation=10, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_interwoven_model(base_size=8.0, layer_count=6, rotation_variation=25, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_interwoven_model(base_size=20.0, layer_count=3, rotation_variation=30, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_interwoven_model(base_size=5.0, layer_count=8, rotation_variation=5, seed=200)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
