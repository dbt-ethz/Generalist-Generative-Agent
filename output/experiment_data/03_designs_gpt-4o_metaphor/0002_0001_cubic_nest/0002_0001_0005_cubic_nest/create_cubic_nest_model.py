# Created for 0002_0001_cubic_nest.json

""" Summary:
The provided function `create_cubic_nest_model` generates an architectural concept model based on the metaphor "Cubic nest," which emphasizes interlocking cubic volumes. It uses parameters like base cube size, number of layers, and layer offset to create a layered structure that reflects complexity and shelter. The function employs randomness for positioning, ensuring each layer overlaps differently, enhancing the dynamic spatial experience. Each generated cube is defined in a 3D coordinate system, resulting in a collective geometry that embodies the metaphor's essence of interconnectedness and exploration, ultimately producing a unique architectural composition."""

#! python 3
function_code = """def create_cubic_nest_model(base_cube_size=5, num_layers=3, layer_offset=2, randomness_seed=42):
    \"""
    Creates a conceptual architectural model based on the metaphor 'Cubic nest'. This model consists
    of interlocking or overlapping cubic volumes, evoking a layered and protective spatial organization.

    Parameters:
    - base_cube_size (float): The size of the base cube in meters. Represents the baseline dimension for cubes.
    - num_layers (int): The number of layers of cubes to create. More layers increase complexity.
    - layer_offset (float): The distance offset for each new layer of cubes. Affects the degree of overlap.
    - randomness_seed (int): Seed for random number generator to ensure replicability of the model.

    Returns:
    - List of RhinoCommon Brep: The list of 3D geometries representing the conceptual model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(randomness_seed)
    geometries = []

    for i in range(num_layers):
        # Calculate the size and position offset of the current layer
        current_size = base_cube_size + i * layer_offset
        offset_x = random.uniform(-layer_offset, layer_offset)
        offset_y = random.uniform(-layer_offset, layer_offset)
        offset_z = random.uniform(-layer_offset, layer_offset)

        # Define the base point for the cube
        base_point = rg.Point3d(offset_x, offset_y, offset_z)

        # Create a cube as a Brep
        cube = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), 
                      rg.Interval(0, current_size), 
                      rg.Interval(0, current_size), 
                      rg.Interval(0, current_size)).ToBrep()

        # Add the cube to the list of geometries
        geometries.append(cube)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_model(base_cube_size=4, num_layers=5, layer_offset=1.5, randomness_seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_model(base_cube_size=6, num_layers=4, layer_offset=3, randomness_seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_model(base_cube_size=3, num_layers=6, layer_offset=2.5, randomness_seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_model(base_cube_size=7, num_layers=2, layer_offset=4, randomness_seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_model(base_cube_size=5, num_layers=3, layer_offset=2, randomness_seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
