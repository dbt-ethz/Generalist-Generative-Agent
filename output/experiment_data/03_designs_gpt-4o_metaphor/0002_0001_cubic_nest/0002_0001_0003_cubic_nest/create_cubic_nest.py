# Created for 0002_0001_cubic_nest.json

""" Summary:
The provided function, `create_cubic_nest`, generates an architectural concept model based on the metaphor "Cubic nest." It creates interlocking cubic volumes that embody the key traits of shelter, complexity, and interconnectedness. The function uses parameters like base size, layers, layer height, and overlap factor to define the geometry of each cube. By randomizing the positions and sizes of the cubes within specified constraints, it produces a dynamic structure that reflects a nest-like organization. The resulting models encourage exploration and interaction, aligning with the metaphor's themes of distinct yet cohesive spatial experiences."""

#! python 3
function_code = """def create_cubic_nest(base_size, layers, layer_height, overlap_factor, seed=42):
    \"""
    Generates a 'Cubic Nest' architectural concept model consisting of interlocking cubic volumes.

    Args:
        base_size (float): The size of the base cube in meters.
        layers (int): The number of layers of cubes.
        layer_height (float): The height of each layer in meters.
        overlap_factor (float): The factor by which cubes overlap in each layer, ranging from 0 to 1.
        seed (int, optional): The seed for randomization. Defaults to 42.

    Returns:
        list: A list of Breps representing the cubic nest structure.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set random seed for reproducibility
    random.seed(seed)

    geometries = []

    # Iterate over the number of layers
    for i in range(layers):
        # Calculate the size and position of the cubes in the current layer
        cube_size = base_size * (1 - overlap_factor * i / layers)
        layer_offset = i * layer_height

        # Calculate the number of cubes in the layer
        num_cubes = max(1, int((1 + overlap_factor) * (layers - i)))

        for j in range(num_cubes):
            # Randomize the position of each cube within a constrained range
            x_offset = random.uniform(-overlap_factor * base_size, overlap_factor * base_size)
            y_offset = random.uniform(-overlap_factor * base_size, overlap_factor * base_size)

            # Create the cube as a Brep
            cube = rg.Box(
                rg.Plane(rg.Point3d(x_offset, y_offset, layer_offset), rg.Vector3d.ZAxis),
                rg.Interval(0, cube_size),
                rg.Interval(0, cube_size),
                rg.Interval(0, layer_height)
            )
            
            geometries.append(cube.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest(2.0, 5, 1.0, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest(1.5, 3, 0.5, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest(3.0, 4, 1.5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest(2.5, 6, 0.8, 0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest(1.0, 8, 0.7, 0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
