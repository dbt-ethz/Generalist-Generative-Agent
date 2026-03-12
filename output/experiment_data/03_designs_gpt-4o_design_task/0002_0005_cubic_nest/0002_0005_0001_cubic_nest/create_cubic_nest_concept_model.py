# Created for 0002_0005_cubic_nest.json

""" Summary:
The provided function `create_cubic_nest_concept_model` generates an architectural concept model based on the "Cubic nest" metaphor by creating a dynamic lattice of interwoven cubic volumes. It utilizes parameters such as cube size, layers, and offsets to define the spatial arrangement and layering of cubes, effectively embodying the metaphor's emphasis on complexity and interconnectedness. The function randomly determines whether to create solid cubes or voids, enhancing depth and visual interest. This results in a protective framework that encourages exploration and diverse spatial experiences, aligning with the metaphor's notion of a multi-dimensional, sheltering network."""

#! python 3
function_code = """def create_cubic_nest_concept_model(base_cube_size, cube_layers, layer_offset, seed=42):
    \"""
    Create an architectural Concept Model based on the 'Cubic nest' metaphor. This function generates
    a lattice framework of interlaced cubic volumes, emphasizing a rhythmic arrangement and spatial layering
    to create a dynamic and protective network.

    Parameters:
    - base_cube_size (float): The edge length of the base cube in meters.
    - cube_layers (int): The number of layers of cubes to generate.
    - layer_offset (float): The offset distance between each layer in meters.
    - seed (int, optional): Random seed for replicable randomness in cube positioning.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Box, Point3d, Vector3d, Plane, Interval

    random.seed(seed)
    geometries = []

    # Create a base plane for cube layers
    base_plane = Plane(Point3d(0, 0, 0), Vector3d(0, 0, 1))

    for layer in range(cube_layers):
        # Calculate the height of the current layer
        z_offset = layer * layer_offset
        current_plane = base_plane.Clone()
        current_plane.Translate(Vector3d(0, 0, z_offset))

        # Define the base cube at this layer using intervals
        x_interval = Interval(-base_cube_size / 2, base_cube_size / 2)
        y_interval = Interval(-base_cube_size / 2, base_cube_size / 2)
        z_interval = Interval(0, base_cube_size)
        base_cube = Box(current_plane, x_interval, y_interval, z_interval)

        # Randomly decide to create a solid or a void
        if random.choice([True, False]):
            # Create a solid cube
            geometries.append(base_cube.ToBrep())
        else:
            # Create a void represented by a perforated or open cube
            # For simplicity, representing void as a cube with smaller dimensions
            void_size = base_cube_size * random.uniform(0.5, 0.8)
            void_x_interval = Interval(-void_size / 2, void_size / 2)
            void_y_interval = Interval(-void_size / 2, void_size / 2)
            void_z_interval = Interval(0, void_size)
            void_cube = Box(current_plane, void_x_interval, void_y_interval, void_z_interval)
            geometries.append(void_cube.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_concept_model(2.0, 5, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_concept_model(1.5, 3, 0.5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_concept_model(3.0, 4, 0.8, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_concept_model(2.5, 6, 1.5, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_concept_model(1.0, 2, 0.2, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
