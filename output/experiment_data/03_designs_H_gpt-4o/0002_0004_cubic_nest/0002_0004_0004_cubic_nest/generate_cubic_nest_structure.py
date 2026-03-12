# Created for 0002_0004_cubic_nest.json

""" Summary:
The function `generate_cubic_nest_structure` creates a 3D architectural concept model inspired by the 'Cubic nest' metaphor. It generates clusters of cubic volumes, varying their size, orientation, and position to embody interconnectedness and shelter. Each cluster is positioned randomly within a defined space, simulating the layered qualities of a nest. The use of parameters allows for customization, promoting dynamic spatial relationships that encourage exploration. By incorporating variations in size and height, the function articulates depth and complexity, reflecting the essence of a 'Cubic nest' where each cube maintains its individuality while contributing to a unified composition."""

#! python 3
function_code = """def generate_cubic_nest_structure(base_size=5.0, cluster_count=3, cubes_per_cluster=5, size_variation=2.0, height_variation=3.0, seed=24):
    \"""
    Generates a 3D architectural Concept Model inspired by the 'Cubic nest' metaphor.

    This function creates a structure composed of clusters of cubic volumes, each cluster representing
    a node of interconnected cubes. The cubes vary in size, orientation, and placement to create a
    dynamic and cohesive model that embodies the metaphor's essence of interconnectedness and shelter.

    Parameters:
    - base_size (float): The average base size for the cubes in meters.
    - cluster_count (int): The number of clusters of cubes to generate.
    - cubes_per_cluster (int): The number of cubes within each cluster.
    - size_variation (float): Maximum variation in cube size.
    - height_variation (float): Maximum vertical displacement of cubes.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - list of Rhino.Geometry.Brep: A list of Breps representing the cubic volumes.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for consistency
    random.seed(seed)

    # List to store the Brep geometries
    cubic_nest = []

    for cluster_index in range(cluster_count):
        # Determine a random center point for the cluster
        cluster_center = rg.Point3d(
            random.uniform(-10, 10),
            random.uniform(-10, 10),
            random.uniform(0, 5)
        )

        for _ in range(cubes_per_cluster):
            # Randomize cube size and position
            size = base_size + random.uniform(-size_variation, size_variation)
            x_offset = random.uniform(-size_variation, size_variation)
            y_offset = random.uniform(-size_variation, size_variation)
            z_offset = random.uniform(-height_variation, height_variation)
            
            # Create the base point for the cube relative to the cluster center
            base_point = rg.Point3d(
                cluster_center.X + x_offset,
                cluster_center.Y + y_offset,
                cluster_center.Z + z_offset
            )

            # Define the cube as a Box (convertible to Brep)
            box = rg.Box(
                rg.Plane(base_point, rg.Vector3d.ZAxis),
                rg.Interval(0, size),
                rg.Interval(0, size),
                rg.Interval(0, size)
            )

            # Convert the Box to a Brep for output
            cube_brep = box.ToBrep()

            # Append the cube Brep to the list
            cubic_nest.append(cube_brep)

    return cubic_nest"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cubic_nest_structure(base_size=6.0, cluster_count=4, cubes_per_cluster=3, size_variation=1.5, height_variation=2.0, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cubic_nest_structure(base_size=4.0, cluster_count=5, cubes_per_cluster=7, size_variation=3.0, height_variation=4.0, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cubic_nest_structure(base_size=5.0, cluster_count=2, cubes_per_cluster=6, size_variation=2.5, height_variation=3.5, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cubic_nest_structure(base_size=7.0, cluster_count=3, cubes_per_cluster=4, size_variation=2.0, height_variation=1.0, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cubic_nest_structure(base_size=5.0, cluster_count=6, cubes_per_cluster=5, size_variation=1.0, height_variation=2.0, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
