# Created for 0002_0001_cubic_nest.json

""" Summary:
The provided function, `generate_cubic_nest_model`, generates an architectural concept model inspired by the "Cubic nest" metaphor. It creates a series of modular cubic volumes that interlock and overlap, reflecting the metaphor's emphasis on shelter and interconnectedness. By varying the sizes and positions of the cubes, the function explores the spatial interplay of solid and void, allowing for dynamic movement within the structure. Each cube maintains its identity while contributing to a cohesive whole, embodying the protective, layered quality of the metaphor. The result is a diverse spatial experience that encourages exploration and discovery."""

#! python 3
function_code = """def generate_cubic_nest_model(base_cube_size, num_cubes, overlap_factor, seed=42):
    \"""
    Generate an architectural Concept Model based on the 'Cubic nest' metaphor.

    This function creates a series of modular cubic volumes that interlock and overlap,
    emphasizing the spatial interplay of solid and void. The cubes are arranged to form 
    a protective and layered structure, allowing for exploration and discovery.

    Parameters:
    - base_cube_size: float, the size of the base cube in meters.
    - num_cubes: int, the number of cubes to generate.
    - overlap_factor: float, a factor determining how much cubes overlap each other (0 to 1).
    - seed: int, seed for randomness to ensure replicability.

    Returns:
    - List of Rhino.Geometry.Brep objects representing the cubic nest model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    breps = []
    base_vector = rg.Vector3d(base_cube_size, base_cube_size, base_cube_size)

    for i in range(num_cubes):
        # Randomly choose a scale for each cube
        scale_factor = random.uniform(0.5, 1.5)
        cube_size = base_cube_size * scale_factor

        # Create a base cube
        base_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(0, cube_size), rg.Interval(0, cube_size), rg.Interval(0, cube_size))
        
        # Randomly offset the cube to overlap with others
        offset_x = random.uniform(-overlap_factor, overlap_factor) * base_cube_size
        offset_y = random.uniform(-overlap_factor, overlap_factor) * base_cube_size
        offset_z = random.uniform(-overlap_factor, overlap_factor) * base_cube_size

        # Move the cube
        translation = rg.Transform.Translation(offset_x, offset_y, offset_z)
        base_cube.Transform(translation)

        # Convert the box to a Brep and add to the list
        brep_cube = base_cube.ToBrep()
        breps.append(brep_cube)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cubic_nest_model(2.0, 10, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cubic_nest_model(1.5, 5, 0.5, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cubic_nest_model(3.0, 15, 0.2, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cubic_nest_model(2.5, 8, 0.4, seed=200)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cubic_nest_model(1.0, 20, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
