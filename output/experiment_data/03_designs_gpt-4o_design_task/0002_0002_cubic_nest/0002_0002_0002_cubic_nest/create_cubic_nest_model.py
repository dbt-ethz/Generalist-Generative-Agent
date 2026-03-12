# Created for 0002_0002_cubic_nest.json

""" Summary:
The provided function, `create_cubic_nest_model`, generates an architectural concept model based on the "Cubic nest" metaphor by creating a series of overlapping cubic volumes. It defines a base cube size, the number of cubes, and an overlap ratio to simulate the interlocking nature of the design. The function utilizes randomness for positioning and material variation, enhancing the perception of complexity and shelter. Each cube's placement is determined by a direction and offset, allowing for unexpected pathways and spatial interactions. This results in a dynamic model that embodies the metaphor's protective and interconnected qualities, inviting exploration."""

#! python 3
function_code = """def create_cubic_nest_model(base_cube_size, number_of_cubes, overlap_ratio, material_variation_seed):
    \"""
    Creates an architectural Concept Model based on the 'Cubic nest' metaphor.
    
    This function generates a cluster of nested and interlocking cubic volumes representing
    a protective and complex architectural form. The cubes overlap and vary in material to
    transition from solid to void, enhancing the perception of shelter and complexity.

    Parameters:
    - base_cube_size (float): The size of the base cube in meters.
    - number_of_cubes (int): The total number of cubes to be created.
    - overlap_ratio (float): The ratio of overlap between adjacent cubes (0 to 1).
    - material_variation_seed (int): Seed for randomizing material variation.

    Returns:
    - List of RhinoCommon.Brep: A list of Brep objects representing the cubic volumes.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for material variation
    random.seed(material_variation_seed)

    # Initialize a list to store the resulting breps
    cubes = []

    # Define the initial position of the base cube
    current_position = rg.Point3d(0, 0, 0)

    for i in range(number_of_cubes):
        # Create a cube centered at the current position
        half_size = base_cube_size / 2
        corner1 = rg.Point3d(current_position.X - half_size, 
                             current_position.Y - half_size, 
                             current_position.Z - half_size)
        corner2 = rg.Point3d(current_position.X + half_size, 
                             current_position.Y + half_size, 
                             current_position.Z + half_size)
        
        cube = rg.Box(rg.BoundingBox(corner1, corner2)).ToBrep()
        cubes.append(cube)

        # Determine the next position with overlap
        offset = base_cube_size * (1 - overlap_ratio)
        direction = rg.Vector3d(random.choice([-1, 1]), random.choice([-1, 1]), random.choice([-1, 1]))
        direction.Unitize()
        direction *= offset

        # Update current position
        current_position += direction

    return cubes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_model(2.0, 10, 0.3, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_model(1.5, 5, 0.2, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_model(3.0, 15, 0.4, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_model(2.5, 8, 0.5, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_model(1.0, 12, 0.1, 33)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
