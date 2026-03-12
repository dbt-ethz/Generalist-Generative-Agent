# Created for 0002_0002_cubic_nest.json

""" Summary:
The function `create_cubic_nest_model` generates an architectural concept model based on the 'Cubic nest' metaphor by creating a series of nested, overlapping cubic volumes. It takes parameters such as base size, number of cubes, size range, and overlap factor to define the models structure. Each cube is randomly sized and positioned, allowing for complex interactions between them, which reflects the protective and interconnected nature of a nest. The resulting geometries represent a visually intricate silhouette, enhancing the perception of shelter and inviting exploration, while embodying the metaphor's emphasis on complexity and spatial relationships."""

#! python 3
function_code = """def create_cubic_nest_model(base_size, num_cubes, cube_size_range, overlap_factor, seed):
    \"""
    Create a Concept Model based on the 'Cubic Nest' metaphor using nested and overlapping cubes.

    Parameters:
    - base_size (float): The dimension of the base cubic volume in meters.
    - num_cubes (int): The number of nested cubes to generate.
    - cube_size_range (tuple of float): The range (min, max) of sizes for the nested cubes.
    - overlap_factor (float): A factor to determine the extent of overlap between cubes (0 to 1).
    - seed (int): A seed value for randomness to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set random seed for replicability
    random.seed(seed)

    # List to store generated geometries
    geometries = []

    # Create the base cube
    base_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(-base_size/2, base_size/2), rg.Interval(-base_size/2, base_size/2), rg.Interval(-base_size/2, base_size/2))
    geometries.append(base_cube.ToBrep())

    # Generate nested cubes
    for _ in range(num_cubes):
        # Randomly determine the size of the cube within the specified range
        size = random.uniform(cube_size_range[0], cube_size_range[1])
        
        # Calculate random position offsets for the cube, within the overlap range
        offset_x = random.uniform(-overlap_factor * base_size, overlap_factor * base_size)
        offset_y = random.uniform(-overlap_factor * base_size, overlap_factor * base_size)
        offset_z = random.uniform(-overlap_factor * base_size, overlap_factor * base_size)

        # Create a cube oriented along the world coordinates
        nested_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(-size/2, size/2), rg.Interval(-size/2, size/2), rg.Interval(-size/2, size/2))
        
        # Move the nested cube to the calculated offset position
        translation_vector = rg.Vector3d(offset_x, offset_y, offset_z)
        nested_cube.Transform(rg.Transform.Translation(translation_vector))
        
        # Add the transformed cube to the list of geometries
        geometries.append(nested_cube.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_model(10.0, 5, (2.0, 4.0), 0.5, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_model(15.0, 3, (1.0, 3.0), 0.3, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_model(12.0, 4, (3.0, 6.0), 0.2, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_model(20.0, 6, (1.5, 5.0), 0.4, 11)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_model(8.0, 7, (2.5, 5.5), 0.6, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
