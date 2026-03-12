# Created for 0002_0004_cubic_nest.json

""" Summary:
The function `generate_cubic_nest_structure` creates an architectural concept model representing the "Cubic nest" metaphor by generating a layered arrangement of cubic volumes. It varies cube sizes, positions, and translucency to emphasize protective and interconnected qualities. By utilizing randomization within specified parameters (e.g., base size, layer count), the function produces diverse geometries that reflect the metaphor's themes of shelter and harmony. Each cube's distinct characteristics contribute to a cohesive whole, fostering exploration and interaction. The result is a dynamic architectural composition that embodies the essence of a nested structure, inviting discovery within its complex spatial organization."""

#! python 3
function_code = """def generate_cubic_nest_structure(base_size=5.0, layer_count=4, seed=123, translucency_variation=0.5):
    \"""
    Creates an architectural Concept Model based on the 'Cubic nest' metaphor, using a layered arrangement
    of cubic volumes that vary in size, orientation, and translucency. This emphasizes the protective and 
    interconnected qualities of the design.

    Parameters:
    - base_size (float): The base size of the cubes in meters.
    - layer_count (int): The number of vertical layers of cubes.
    - seed (int): A seed for the random number generator to ensure replicability.
    - translucency_variation (float): The variation in translucency for the cubes.

    Returns:
    - list: A list of Rhino.Geometry.Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set the random seed for replicability
    random.seed(seed)
    
    # List to store the generated Breps
    geometries = []
    
    # Create layers of cubes
    for layer in range(layer_count):
        # Determine the number of cubes in this layer
        cube_count = random.randint(3, 6)
        
        for _ in range(cube_count):
            # Randomly vary the size of the cube
            size_variation = random.uniform(-0.3, 0.3) * base_size
            cube_size = base_size + size_variation
            
            # Randomly vary the position within the layer
            x_offset = random.uniform(-0.5, 0.5) * base_size
            y_offset = random.uniform(-0.5, 0.5) * base_size
            z_offset = layer * (base_size * 0.8)  # Slight overlap between layers
            
            # Create the base point of the cube
            base_point = rg.Point3d(x_offset, y_offset, z_offset)
            
            # Define the cube as a Box (which can be converted to Brep)
            box = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), rg.Interval(0, cube_size), rg.Interval(0, cube_size), rg.Interval(0, cube_size))
            
            # Convert the Box to a Brep for output
            cube_brep = box.ToBrep()
            
            # Add translucency variation (as a placeholder for visual properties)
            translucency = random.uniform(0.0, translucency_variation)
            # Normally, you would apply this translucency to a material in Rhino, not directly in geometry
            
            # Append the cube Brep to the list
            geometries.append(cube_brep)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cubic_nest_structure(base_size=6.0, layer_count=5, seed=42, translucency_variation=0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cubic_nest_structure(base_size=4.0, layer_count=3, seed=99, translucency_variation=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cubic_nest_structure(base_size=7.0, layer_count=6, seed=10, translucency_variation=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cubic_nest_structure(base_size=5.5, layer_count=2, seed=2023, translucency_variation=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cubic_nest_structure(base_size=8.0, layer_count=7, seed=15, translucency_variation=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
