# Created for 0002_0002_cubic_nest.json

""" Summary:
The provided function generates an architectural concept model based on the 'Cubic nest' metaphor by creating a series of nested cubic volumes that interlock and overlap. It defines parameters for cube size, overlap, and cantilevering, allowing for dynamic spatial arrangements. Each cube's position is randomized to enhance complexity and mimic the protective nature of a nest. The function constructs 3D geometries using Rhino's geometry library, producing intricate silhouettes that evoke exploration and shelter. By varying the cube sizes and their arrangements, the model reflects the metaphor's essence, emphasizing interconnectedness and the playful interaction of solid and void."""

#! python 3
function_code = """def generate_cubic_nest_with_dynamic_layers(base_cube_size, num_cubes, overlap_factor, cantilever_ratio, randomness_seed):
    \"""
    Generate an architectural Concept Model based on the 'Cubic nest' metaphor,
    with dynamic layering and cantilevered cubes to enhance exploration and spatial complexity.

    Parameters:
    - base_cube_size (float): The size of the base cube in meters.
    - num_cubes (int): The number of cubes to generate.
    - overlap_factor (float): A factor that determines the extent of overlap between cubes.
    - cantilever_ratio (float): A factor to control the degree of cantilevering.
    - randomness_seed (int): Seed for the random number generator to ensure reproducible results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometries of the nested cubic volumes.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(randomness_seed)

    # Initialize a list to store the Breps
    breps = []

    # Define the initial base cube
    base_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(-base_cube_size / 2, base_cube_size / 2),
                       rg.Interval(-base_cube_size / 2, base_cube_size / 2),
                       rg.Interval(-base_cube_size / 2, base_cube_size / 2)).ToBrep()
    breps.append(base_cube)

    for i in range(1, num_cubes):
        # Calculate the size of the new cube
        cube_size = base_cube_size * (1 + overlap_factor * i)
        
        # Determine random translation for overlap and cantilevering
        dx = random.uniform(-cube_size * overlap_factor, cube_size * overlap_factor)
        dy = random.uniform(-cube_size * overlap_factor, cube_size * overlap_factor)
        dz = random.uniform(-cube_size * cantilever_ratio, cube_size * cantilever_ratio)

        # Create a new cube
        new_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(-cube_size / 2, cube_size / 2),
                          rg.Interval(-cube_size / 2, cube_size / 2),
                          rg.Interval(-cube_size / 2, cube_size / 2)).ToBrep()
        
        # Apply translation to simulate cantilevered effect
        translation = rg.Transform.Translation(rg.Vector3d(dx, dy, dz))
        new_cube.Transform(translation)

        # Add the new cube to the breps list
        breps.append(new_cube)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cubic_nest_with_dynamic_layers(1.0, 5, 0.2, 0.5, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cubic_nest_with_dynamic_layers(2.0, 10, 0.3, 0.7, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cubic_nest_with_dynamic_layers(0.5, 3, 0.1, 0.4, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cubic_nest_with_dynamic_layers(1.5, 8, 0.25, 0.6, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cubic_nest_with_dynamic_layers(3.0, 6, 0.15, 0.3, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
