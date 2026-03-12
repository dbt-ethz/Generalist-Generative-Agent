# Created for 0002_0003_cubic_nest.json

""" Summary:
The function `create_cubic_nest_concept_model` generates an architectural concept model inspired by the "Cubic nest" metaphor. It creates layers of interwoven cubic volumes that balance enclosure and openness, fostering a sense of refuge and interconnectedness. By manipulating the size, number of layers, and offsets of the cubes, the function produces diverse spatial arrangements. Each cube is transformed through random translations and rotations, emphasizing individuality while contributing to the overall nested structure. This approach highlights the interplay of solid and void, encouraging exploration and dynamic experiences within the architectural composition."""

#! python 3
function_code = """def create_cubic_nest_concept_model(base_cube_size, num_layers, offset_factor):
    \"""
    Creates an architectural Concept Model based on the 'Cubic nest' metaphor.
    
    This function generates a sequence of interwoven cubic forms expressing the 'Cubic nest' design task, 
    with a balance of enclosure and openness, using a series of overlapping cubes. Each cube is a distinct 
    module contributing to the overall structure, embodying a sense of refuge and interconnectedness.

    Inputs:
    - base_cube_size (float): The size of the cubes in meters.
    - num_layers (int): The number of layers of cubes to create.
    - offset_factor (float): A factor to determine the offset between cubes in different layers.
    
    Outputs:
    - List of Rhino.Geometry.Brep: A list of breps representing the cubic volumes in the concept model.

    \"""
    import Rhino.Geometry as rg
    import random
    import math  # Import the math module

    random.seed(42)  # Ensuring replicable randomness

    cubes = []

    # Create a base cube as the starting point
    base_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_cube_size), rg.Interval(0, base_cube_size), rg.Interval(0, base_cube_size))
    
    # Add the base cube to the list of cubes
    cubes.append(base_cube.ToBrep())

    # Generate additional cubes in layers
    for layer in range(1, num_layers):
        # Calculate the offset distance for this layer
        offset_distance = base_cube_size * offset_factor * layer

        # Randomly decide the position and rotation for the new cube
        offset_x = random.choice([-1, 1]) * offset_distance
        offset_y = random.choice([-1, 1]) * offset_distance
        offset_z = random.choice([-1, 1]) * offset_distance
        
        # Create a transformation matrix for the new cube
        translation = rg.Transform.Translation(offset_x, offset_y, offset_z)
        rotation_angle = random.uniform(0, math.pi / 4)  # Use math.pi instead of rg.Math.PI
        rotation_axis = rg.Vector3d(random.choice([1, 0, 0]), random.choice([0, 1, 0]), random.choice([0, 0, 1]))
        rotation = rg.Transform.Rotation(rotation_angle, rotation_axis, rg.Point3d(0, 0, 0))
        
        # Create a new cube from the base cube
        transformed_box = rg.Box(base_cube)  # Duplicate the box
        transformed_box.Transform(translation)
        transformed_box.Transform(rotation)
        
        # Add the new cube to the list of cubes
        cubes.append(transformed_box.ToBrep())

    return cubes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_concept_model(2.0, 5, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_concept_model(1.5, 3, 0.75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_concept_model(3.0, 4, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_concept_model(1.0, 6, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_concept_model(2.5, 7, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
