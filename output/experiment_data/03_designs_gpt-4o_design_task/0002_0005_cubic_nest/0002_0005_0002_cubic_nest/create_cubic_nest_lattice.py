# Created for 0002_0005_cubic_nest.json

""" Summary:
The function `create_cubic_nest_lattice` generates an architectural concept model based on the "Cubic nest" metaphor by creating a lattice framework of interlaced cubic volumes. It employs a specified base cube size and number of layers to stack and arrange cubes rhythmically. Random offsets introduce variability in cube positions, enhancing the model's complexity while maintaining modular identities. Each cube interacts with its neighbors, forming dynamic spaces that promote exploration within a protective network. Ultimately, the function outputs a list of Brep objects that represent the intricate and layered cubic structure, encapsulating the metaphor's essence."""

#! python 3
function_code = """def create_cubic_nest_lattice(base_cube_size, num_layers, randomness_seed=None):
    \"""
    Creates an architectural Concept Model emulating the 'Cubic nest' metaphor. This model features a lattice framework
    of interlaced cubic volumes. The design explores the rhythmic arrangement and spatial layering of cubes to form a 
    dynamic and protective network, enhancing depth and intricacy through varied materials and cube interconnection.

    Parameters:
    base_cube_size (float): The edge length of the base cube in meters.
    num_layers (int): The number of layers of cubes to be stacked.
    randomness_seed (int, optional): Seed for random number generator to ensure replicable randomness in cube positions.

    Returns:
    List[Rhino.Geometry.Brep]: A list of Brep objects representing the cubic lattice framework.
    \"""
    import Rhino.Geometry as rg
    import random

    if randomness_seed is not None:
        random.seed(randomness_seed)

    cubes = []

    # Define offsets for cube positioning
    offset_range = base_cube_size * 0.5
    layers_z_offset = base_cube_size * 0.8

    for layer in range(num_layers):
        # Determine the number of cubes per layer based on the layer index
        num_cubes_per_layer = 3 + layer

        for i in range(num_cubes_per_layer):
            # Create random offsets to position cubes
            x_offset = random.uniform(-offset_range, offset_range)
            y_offset = random.uniform(-offset_range, offset_range)

            # Calculate the center point of the cube
            cube_center = rg.Point3d(
                i * base_cube_size + x_offset,
                (layer % 2) * base_cube_size + y_offset,
                layer * layers_z_offset
            )

            # Create the cube as a Brep
            cube = rg.Box(rg.Plane(cube_center, rg.Vector3d.ZAxis), rg.Interval(-base_cube_size / 2, base_cube_size / 2), rg.Interval(-base_cube_size / 2, base_cube_size / 2), rg.Interval(-base_cube_size / 2, base_cube_size / 2)).ToBrep()

            # Append the cube to the list
            cubes.append(cube)

    return cubes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_lattice(1.0, 5, randomness_seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_lattice(0.5, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_lattice(2.0, 4, randomness_seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_lattice(1.5, 6, randomness_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_lattice(3.0, 2, randomness_seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
