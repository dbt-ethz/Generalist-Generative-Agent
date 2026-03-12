# Created for 0002_0001_cubic_nest.json

""" Summary:
The provided function generates an architectural concept model based on the 'Cubic nest' metaphor by creating a three-dimensional structure composed of interlocking and overlapping cubic volumes. It organizes these cubes in multiple vertical layers, each defined by varying scales that emphasize the interplay of solid and void, echoing the protective qualities of a nest. By randomly positioning cubes within each layer while adhering to specific parameters, the model fosters exploration and discovery. The result is a complex yet cohesive architectural form that highlights interconnectedness while allowing individual cube identities to persist, effectively embodying the metaphor's essence."""

#! python 3
function_code = """def create_cubic_nest_structure(base_cube_size, num_layers, layer_height, cube_scale_range, seed=42):
    \"""
    Generate an architectural Concept Model inspired by the 'Cubic nest' metaphor.
    
    This function creates a vertically layered structure of modular cubic volumes 
    that interlock and overlap, forming a protective, layered 'nest'. Each layer 
    consists of cubes with varying scales that contribute to the dynamic spatial 
    relationships of solid and void spaces.

    Parameters:
    - base_cube_size: float, the size of the base cube in meters.
    - num_layers: int, the number of vertical layers in the structure.
    - layer_height: float, the height of each layer in meters.
    - cube_scale_range: tuple(float, float), the min and max scale factors for the cubes.
    - seed: int, seed for randomness to ensure replicability.

    Returns:
    - List of Rhino.Geometry.Brep objects representing the cubic nest structure.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    breps = []
    
    for layer in range(num_layers):
        layer_base_z = layer * layer_height
        num_cubes_per_layer = random.randint(3, 6)  # Random number of cubes per layer
        
        for _ in range(num_cubes_per_layer):
            # Randomly choose a scale for each cube
            scale_factor = random.uniform(cube_scale_range[0], cube_scale_range[1])
            cube_size = base_cube_size * scale_factor

            # Create a cube at a random position within the layer
            offset_x = random.uniform(-base_cube_size, base_cube_size)
            offset_y = random.uniform(-base_cube_size, base_cube_size)
            offset_z = layer_base_z

            base_point = rg.Point3d(offset_x, offset_y, offset_z)
            cube = rg.Box(
                rg.Plane(base_point, rg.Vector3d(1, 0, 0), rg.Vector3d(0, 1, 0)),
                rg.Interval(0, cube_size),
                rg.Interval(0, cube_size),
                rg.Interval(0, cube_size)
            ).ToBrep()

            # Store the cube
            breps.append(cube)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_structure(base_cube_size=2.0, num_layers=5, layer_height=3.0, cube_scale_range=(0.5, 1.5), seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_structure(base_cube_size=1.5, num_layers=4, layer_height=2.5, cube_scale_range=(0.3, 2.0), seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_structure(base_cube_size=3.0, num_layers=6, layer_height=2.0, cube_scale_range=(0.4, 1.2), seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_structure(base_cube_size=1.0, num_layers=3, layer_height=4.0, cube_scale_range=(0.2, 0.8), seed=12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_structure(base_cube_size=2.5, num_layers=7, layer_height=3.5, cube_scale_range=(0.6, 1.8), seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
