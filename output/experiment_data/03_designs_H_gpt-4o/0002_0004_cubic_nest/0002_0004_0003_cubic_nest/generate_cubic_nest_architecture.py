# Created for 0002_0004_cubic_nest.json

""" Summary:
The `generate_cubic_nest_architecture` function creates an architectural concept model inspired by the "Cubic nest" metaphor. It generates multiple clusters of cubic volumes, varying in size and orientation, to embody interconnectedness and individuality. Each cluster's random positioning promotes a layered, protective structure that encourages movement and interaction. The function utilizes parameters like the number of clusters and size variation to replicate diverse spatial experiences. The resulting 3D geometries, represented as Rhino `Brep` objects, reflect the metaphor's essence by fostering a dynamic composition that invites exploration, showcasing the interplay of solid and void within the architectural design."""

#! python 3
function_code = """def generate_cubic_nest_architecture(num_clusters, cluster_size, cube_base_size, size_variation, seed):
    \"""
    Creates an architectural Concept Model based on the 'Cubic nest' metaphor, 
    emphasizing a layered, protective spatial organization with a matrix of interlocking cubes.

    This function constructs a series of cubic clusters, where each cluster consists of cubes that vary in size 
    and orientation. The clusters are interconnected, suggesting both individuality and collective harmony, 
    and promoting movement and interaction within the composition.

    Parameters:
    - num_clusters (int): The number of clusters to generate.
    - cluster_size (int): Number of cubes in each cluster.
    - cube_base_size (float): The base size for the cubes in meters.
    - size_variation (float): Maximum variation in cube size from the base size.
    - seed (int): Seed for the random number generator to ensure replicability.

    Returns:
    - list: A list of Rhino.Geometry.Brep objects representing the Concept Model's 3D geometry.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set random seed for consistency
    random.seed(seed)

    geometries = []

    for cluster_index in range(num_clusters):
        # Define a random position for the cluster
        cluster_x = random.uniform(-10, 10)
        cluster_y = random.uniform(-10, 10)
        cluster_z = random.uniform(0, 5)

        for _ in range(cluster_size):
            # Randomize the size and offset of each cube within the cluster
            size = cube_base_size + random.uniform(-size_variation, size_variation)
            x_offset = random.uniform(-1, 1)
            y_offset = random.uniform(-1, 1)
            z_offset = random.uniform(-1, 1)

            # Define the base point for the cube
            base_point = rg.Point3d(cluster_x + x_offset, cluster_y + y_offset, cluster_z + z_offset)

            # Create the cube as a Box and convert it to a Brep
            box = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), rg.Interval(0, size), rg.Interval(0, size), rg.Interval(0, size))
            cube_brep = box.ToBrep()

            # Append the Brep to the list
            geometries.append(cube_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cubic_nest_architecture(5, 10, 2.0, 0.5, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cubic_nest_architecture(3, 8, 1.5, 0.2, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cubic_nest_architecture(4, 6, 3.0, 1.0, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cubic_nest_architecture(6, 12, 2.5, 0.8, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cubic_nest_architecture(2, 5, 1.0, 0.3, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
