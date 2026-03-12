# Created for 0002_0002_cubic_nest.json

""" Summary:
The provided function generates an architectural concept model based on the "Cubic Nest" metaphor by creating a series of nested cubic volumes. It defines parameters such as base size, number of cubes, and overlap factor, which guide the design's complexity and protection. The function uses random variation in cube sizes and positions to create a dynamic arrangement that reflects the metaphor's emphasis on interconnectedness and distinctiveness. By adjusting the overlap and layering of the cubes, the output results in a model that invites exploration and interaction, embodying the protective and intricate qualities of a "cubic nest.""""

#! python 3
function_code = """def create_cubic_nest_concept_model_advanced(base_size, num_cubes, overlap_factor, random_seed):
    \"""
    Generate an architectural Concept Model based on the 'Cubic Nest' metaphor using an advanced composition of nested cubic volumes.

    Parameters:
    - base_size (float): The size of the initial cube in meters.
    - num_cubes (int): The number of cubes to generate.
    - overlap_factor (float): The factor determining the overlap between cubes.
    - random_seed (int): Seed for random number generation to ensure replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometries of the nested cubic volumes.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set random seed for consistency
    random.seed(random_seed)

    # List to hold the resulting geometries
    breps = []

    # Define a helper function to create a cube Brep
    def create_cube(center, size):
        half_size = size / 2
        min_corner = rg.Point3d(center.X - half_size, center.Y - half_size, center.Z - half_size)
        max_corner = rg.Point3d(center.X + half_size, center.Y + half_size, center.Z + half_size)
        return rg.Box(rg.BoundingBox(min_corner, max_corner)).ToBrep()

    # Initial base position
    current_position = rg.Point3d(0, 0, 0)

    for i in range(num_cubes):
        # Randomly adjust size to create variation
        size_variation = base_size * (1 + random.uniform(-0.2, 0.2))
        
        # Create a cube at the current position
        cube = create_cube(current_position, size_variation)
        breps.append(cube)

        # Calculate offset for the next cube
        offset_distance = base_size * (1 - overlap_factor)
        offset_direction = rg.Vector3d(
            random.choice([-1, 1]),
            random.choice([-1, 1]),
            random.choice([-1, 1])
        )
        offset_direction.Unitize()
        offset_vector = offset_direction * offset_distance

        # Update position for the next cube
        current_position += offset_vector

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_concept_model_advanced(5.0, 10, 0.3, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_concept_model_advanced(3.0, 15, 0.5, 100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_concept_model_advanced(4.0, 8, 0.2, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_concept_model_advanced(6.0, 12, 0.4, 2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_concept_model_advanced(2.5, 20, 0.1, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
