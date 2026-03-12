# Created for 0002_0004_cubic_nest.json

""" Summary:
The provided function, `generate_cubic_nest_pattern`, creates a 3D architectural concept model inspired by the "Cubic nest" metaphor. It generates clusters of cubic volumes, varying in size and orientation, to embody the layered, interconnected essence of a nest. By utilizing parameters like `base_size`, `cluster_count`, and `cube_variation`, the function ensures diverse spatial arrangements. The randomization of cube positions and orientations fosters a dynamic interaction between solid and void, enhancing light and shadow interplay. This design invites exploration and interaction, reflecting both individuality and collective harmony, thus fulfilling the architectural design task effectively."""

#! python 3
function_code = """def generate_cubic_nest_pattern(base_size=5.0, cluster_count=3, cube_variation=2.0, grid_spacing=10.0, seed=24):
    \"""
    Generates a 3D architectural Concept Model based on the 'Cubic nest' metaphor.

    This function creates a pattern of interconnected cubic volumes organized into clusters. 
    Each cluster consists of cubes that vary in size and orientation, creating a dynamic 
    spatial arrangement that emphasizes the protective and intertwined qualities of a 'nest'.

    Parameters:
    - base_size (float): The base size for the cubes in meters.
    - cluster_count (int): The number of clusters to generate in the model.
    - cube_variation (float): The maximum variation in cube size.
    - grid_spacing (float): The spacing between clusters in meters.
    - seed (int): The seed for random number generation to ensure replicability.

    Returns:
    - list: A list of Rhino.Geometry.Brep objects representing the 3D geometries.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for consistency
    random.seed(seed)

    geometries = []

    for cluster_index in range(cluster_count):
        # Calculate the base position for each cluster
        cluster_offset_x = cluster_index * grid_spacing
        cluster_offset_y = cluster_index * grid_spacing

        # Create a number of cubes within each cluster
        for _ in range(random.randint(3, 5)):  # Each cluster has 3 to 5 cubes
            # Randomize the size and orientation of the cubes
            size = base_size + random.uniform(-cube_variation, cube_variation)
            orientation_angle = random.uniform(0, 360)
            
            # Create a rotation transformation
            rotation = rg.Transform.Rotation(math.radians(orientation_angle), rg.Vector3d.ZAxis, rg.Point3d(0, 0, 0))
            
            # Random position within the cluster
            x_offset = cluster_offset_x + random.uniform(-grid_spacing / 2, grid_spacing / 2)
            y_offset = cluster_offset_y + random.uniform(-grid_spacing / 2, grid_spacing / 2)
            z_offset = random.uniform(0, base_size)

            # Create the base point for the cube
            base_point = rg.Point3d(x_offset, y_offset, z_offset)

            # Define the cube as a Box
            box = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), rg.Interval(0, size), rg.Interval(0, size), rg.Interval(0, size))
            
            # Apply the rotation transformation to the box
            box.Transform(rotation)

            # Convert the Box to a Brep for output
            cube_brep = box.ToBrep()

            # Append the cube Brep to the list
            geometries.append(cube_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cubic_nest_pattern(base_size=6.0, cluster_count=4, cube_variation=1.5, grid_spacing=12.0, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cubic_nest_pattern(base_size=7.0, cluster_count=5, cube_variation=3.0, grid_spacing=15.0, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cubic_nest_pattern(base_size=5.5, cluster_count=2, cube_variation=2.5, grid_spacing=8.0, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cubic_nest_pattern(base_size=4.0, cluster_count=6, cube_variation=1.0, grid_spacing=20.0, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cubic_nest_pattern(base_size=8.0, cluster_count=3, cube_variation=2.0, grid_spacing=10.0, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
