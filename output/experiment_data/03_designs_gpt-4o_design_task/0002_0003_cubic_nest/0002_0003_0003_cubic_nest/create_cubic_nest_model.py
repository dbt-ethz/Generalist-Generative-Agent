# Created for 0002_0003_cubic_nest.json

""" Summary:
The provided function generates an architectural concept model based on the "Cubic nest" metaphor by creating a series of interwoven cubic forms. Each cube is defined with a base size and a height variation, resulting in dynamic vertical layering that enhances the sense of enclosure and openness. The function randomly positions cubes in three-dimensional space, simulating an intricate and protective spatial arrangement. By manipulating the orientation and arrangement of these cubes, the model embodies both individuality and interconnectedness, encouraging exploration. The contrasting materials can further accentuate the solid and void interplay, enhancing the overall architectural experience."""

#! python 3
function_code = """def create_cubic_nest_model(base_size=10, height_variation=3, cube_count=10, seed=42):
    \"""
    Create an architectural Concept Model that represents a 'Cubic nest' using a sequence of interwoven cubic forms.
    
    Parameters:
    - base_size (float): The base size of each cube in meters.
    - height_variation (float): The maximum variation in cube height to create dynamic vertical layering.
    - cube_count (int): The number of cubes to generate and arrange in the model.
    - seed (int): Seed for random number generator to ensure reproducibility.
    
    Returns:
    - list: A list of 3D Brep geometries representing the cubic forms.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Point3d, Box, Vector3d, Plane, Interval
    
    random.seed(seed)
    
    cubes = []
    current_position = Rhino.Geometry.Point3d(0, 0, 0)
    
    for i in range(cube_count):
        # Randomly determine the height variation
        height_offset = random.uniform(-height_variation, height_variation)
        
        # Create a cube with a base size and height variation
        corner1 = Point3d(current_position.X, current_position.Y, current_position.Z)
        corner2 = Point3d(current_position.X + base_size, 
                          current_position.Y + base_size, 
                          current_position.Z + base_size + height_offset)
        
        # Create the cube as a box
        x_interval = Interval(corner1.X, corner2.X)
        y_interval = Interval(corner1.Y, corner2.Y)
        z_interval = Interval(corner1.Z, corner2.Z)
        cube = Box(Plane.WorldXY, x_interval, y_interval, z_interval)
        cubes.append(cube.ToBrep())
        
        # Move to the next cube position, randomly choosing a direction
        direction = random.choice(['x', 'y', 'z'])
        if direction == 'x':
            current_position += Vector3d(base_size * 0.8, 0, 0)
        elif direction == 'y':
            current_position += Vector3d(0, base_size * 0.8, 0)
        else:
            current_position += Vector3d(0, 0, base_size * 0.8)
    
    return cubes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_model(base_size=5, height_variation=2, cube_count=15, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_model(base_size=12, height_variation=4, cube_count=8, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_model(base_size=7, height_variation=1, cube_count=20, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_model(base_size=15, height_variation=5, cube_count=12, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_model(base_size=10, height_variation=3, cube_count=25, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
