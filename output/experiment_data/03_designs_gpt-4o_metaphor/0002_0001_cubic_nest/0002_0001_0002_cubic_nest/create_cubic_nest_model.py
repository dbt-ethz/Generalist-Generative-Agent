# Created for 0002_0001_cubic_nest.json

""" Summary:
The function `create_cubic_nest_model` generates an architectural concept model inspired by the metaphor "Cubic nest." It creates a series of interlocking cubic volumes that embody a layered and protective spatial organization. By defining parameters such as base size, number of cubes, and maximum offset, the function produces unique arrangements of cubes, reflecting complexity and interconnectedness. Each cube maintains its identity while contributing to the overall design, promoting dynamic spatial experiences. This approach evokes a sense of shelter and encourages exploration, aligning with the metaphor's essence of a cohesive yet diverse architectural structure."""

#! python 3
function_code = """def create_cubic_nest_model(base_size, num_cubes, max_offset, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Cubic Nest' metaphor.
    
    This function generates a series of interlocking or overlapping cubic volumes, creating a layered and protective spatial organization. 
    The design suggests complexity and interconnectedness, with each cubic form maintaining its distinct identity while contributing to the whole.

    Parameters:
    - base_size (float): The base size for the cubes in meters.
    - num_cubes (int): The number of cubes to generate.
    - max_offset (float): The maximum offset to apply to the cubes' positions in meters.
    - seed (int, optional): Seed for randomness to ensure replicability.

    Returns:
    - List of Rhino.Geometry.Brep: A list of 3D Brep geometries representing the cubes.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    cubes = []
    base_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_size), rg.Interval(0, base_size), rg.Interval(0, base_size))
    cubes.append(base_cube.ToBrep())
    
    for _ in range(num_cubes - 1):
        offset_x = random.uniform(-max_offset, max_offset)
        offset_y = random.uniform(-max_offset, max_offset)
        offset_z = random.uniform(-max_offset, max_offset)
        
        translation = rg.Vector3d(offset_x, offset_y, offset_z)
        new_cube = rg.Box(base_cube)
        new_cube.Transform(rg.Transform.Translation(translation))
        
        cubes.append(new_cube.ToBrep())
    
    return cubes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_model(5.0, 10, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_model(3.0, 20, 1.5, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_model(4.0, 15, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_model(6.0, 8, 4.0, seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_model(2.5, 12, 1.0, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
