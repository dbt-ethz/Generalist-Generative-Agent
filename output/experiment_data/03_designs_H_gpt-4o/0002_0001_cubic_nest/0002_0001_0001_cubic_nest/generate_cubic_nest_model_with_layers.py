# Created for 0002_0001_cubic_nest.json

""" Summary:
The provided function generates an architectural concept model based on the "Cubic nest" metaphor by creating a series of interlocking and overlapping cubic volumes. Each cube is scaled randomly and arranged in layers, emphasizing the dynamic interplay of solid and void spaces. The function allows for variations in size and height, contributing to a layered silhouette that evokes a sense of shelter and interconnectedness. By incorporating random rotations, the cubes enhance their interlocking quality, further encouraging exploration and discovery within the structure. The output is a collection of Brep objects that visually represent the metaphor-driven design task."""

#! python 3
function_code = """def generate_cubic_nest_model_with_layers(base_cube_size, num_cubes, layer_height, seed=42):
    \"""
    Generate an architectural Concept Model based on the 'Cubic nest' metaphor with distinct layered heights.

    This function creates a series of modular cubic volumes that interlock and overlap, emphasizing
    the spatial interplay of solid and void. Cubes are arranged vertically in layers, each with a unique
    height, forming a protective and layered structure.

    Parameters:
    - base_cube_size: float, the size of the base cube in meters.
    - num_cubes: int, the number of cubes to generate.
    - layer_height: float, the height of each layer in meters.
    - seed: int, seed for randomness to ensure replicability.

    Returns:
    - List of Rhino.Geometry.Brep objects representing the cubic nest model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    breps = []
    current_height = 0

    for i in range(num_cubes):
        # Determine scale factors for each cube
        scale_factor_x = random.uniform(0.5, 1.5)
        scale_factor_y = random.uniform(0.5, 1.5)
        scale_factor_z = random.uniform(0.5, 1.5)
        
        # Calculate scaled cube size
        cube_size_x = base_cube_size * scale_factor_x
        cube_size_y = base_cube_size * scale_factor_y
        cube_size_z = base_cube_size * scale_factor_z
        
        # Create a base cube
        base_cube = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(0, cube_size_x),
            rg.Interval(0, cube_size_y),
            rg.Interval(current_height, current_height + cube_size_z)
        )
        
        # Adjust height for the next layer, incrementally
        current_height += layer_height
        
        # Rotate each cube randomly to enhance the interlocking effect
        rotation_axis = rg.Vector3d(0, 0, 1)  # Rotate around Z-axis
        rotation_angle = random.uniform(-0.2, 0.2)  # Small rotation for subtlety
        rotation_center = base_cube.Center
        rotation_transform = rg.Transform.Rotation(rotation_angle, rotation_axis, rotation_center)
        base_cube.Transform(rotation_transform)
        
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
    geometry = generate_cubic_nest_model_with_layers(1.0, 10, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cubic_nest_model_with_layers(2.0, 5, 1.0, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cubic_nest_model_with_layers(1.5, 8, 0.3, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cubic_nest_model_with_layers(0.8, 15, 0.4, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cubic_nest_model_with_layers(1.2, 12, 0.6, seed=55)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
