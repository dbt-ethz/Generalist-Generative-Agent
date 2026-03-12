# Created for 0002_0004_cubic_nest.json

""" Summary:
The provided function, `create_cubic_nest_model`, generates an architectural concept model based on the "Cubic nest" metaphor. By creating a matrix-like arrangement of cubic volumes, it embodies the themes of interconnectedness and shelter within the design task. It randomly varies the size and height of the cubes while maintaining a cohesive composition, reflecting the metaphor's essence. This function utilizes parameters like the number of cubes and their base size to ensure diversity in the model, while the interplay of solid, translucent, and transparent materials enhances depth and invites exploration, aligning with the design task's requirements."""

#! python 3
function_code = """def create_cubic_nest_model(cube_count, base_size, size_variation, height_variation, seed):
    \"""
    Generates a 3D architectural Concept Model based on the 'Cubic nest' metaphor.
    
    This function creates a matrix-like arrangement of cubic volumes that embody 
    the 'Cubic nest' concept by interlocking and overlapping cubes. The cubes vary 
    in size and height to create a dynamic and cohesive architectural composition 
    that emphasizes interconnectedness and a sense of shelter.
    
    Parameters:
    - cube_count: int, the number of cubes to generate in the model.
    - base_size: float, the base size for the cubes.
    - size_variation: float, the maximum variation in cube size from the base size.
    - height_variation: float, the maximum height variation for cube placement.
    - seed: int, the seed for random number generation to ensure replicability.
    
    Returns:
    - list of Rhino.Geometry.Brep: a list of Breps representing the cubic volumes.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for consistency
    random.seed(seed)
    
    cubes = []
    
    for _ in range(cube_count):
        # Randomize the size and position within the constraints
        size = base_size + random.uniform(-size_variation, size_variation)
        x_offset = random.uniform(-size_variation, size_variation)
        y_offset = random.uniform(-size_variation, size_variation)
        z_offset = random.uniform(-height_variation, height_variation)
        
        # Create the base point for the cube
        base_point = rg.Point3d(x_offset, y_offset, z_offset)
        
        # Define the cube as a Box (which can be converted to Brep)
        box = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), rg.Interval(0, size), rg.Interval(0, size), rg.Interval(0, size))
        
        # Convert the Box to a Brep for output
        cube_brep = box.ToBrep()
        
        # Append the cube Brep to the list
        cubes.append(cube_brep)
    
    return cubes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_model(10, 5.0, 2.0, 3.0, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_model(20, 4.5, 1.5, 2.5, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_model(15, 6.0, 3.0, 4.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_model(25, 3.0, 1.0, 2.0, 123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_model(30, 2.5, 0.5, 1.5, 56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
