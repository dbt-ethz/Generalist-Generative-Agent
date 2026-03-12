# Created for 0002_0002_cubic_nest.json

""" Summary:
The function `create_cubic_nest_concept` generates an architectural concept model based on the "Cubic Nest" metaphor by creating a series of nested cubic volumes. It begins with a base cube and iteratively generates additional cubes, varying their size and applying random transformations to create overlaps and interlocking arrangements. This process emphasizes the protective and interconnected nature of the design, reflecting the metaphor's essence. The cubes' dynamic orientations and overlapping positions enhance spatial complexity, inviting exploration and interaction, while the randomness introduces unique variations in each model, capturing the intricate and layered experience suggested by the metaphor."""

#! python 3
function_code = """def create_cubic_nest_concept(base_cube_size, layer_count, size_variation, overlap_factor, seed_value):
    \"""
    Generate an architectural Concept Model based on the 'Cubic Nest' metaphor,
    utilizing a hierarchy of nested and interlocking cubic volumes.

    Parameters:
    base_cube_size (float): The size of the largest cube in meters.
    layer_count (int): The number of nested cube layers.
    size_variation (float): The factor by which the cube size can vary between layers.
    overlap_factor (float): The factor determining the overlap of cubes.
    seed_value (int): Seed for random number generation to ensure replicability.

    Returns:
    list: A list of RhinoCommon Breps representing the nested cubic volumes.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Setting the random seed for reproducibility
    random.seed(seed_value)

    # List to store the resulting Breps
    breps = []

    # Define the base cube
    current_size = base_cube_size
    base_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(-current_size / 2, current_size / 2),
                       rg.Interval(-current_size / 2, current_size / 2), rg.Interval(-current_size / 2, current_size / 2))
    
    # Add the base cube to the breps list
    breps.append(base_cube.ToBrep())

    # Generate nested cubes
    for layer in range(1, layer_count):
        # Randomize size variation
        size_variation_factor = 1 + size_variation * (random.random() - 0.5)
        cube_size = current_size * size_variation_factor

        # Calculate random overlap offsets
        max_offset = overlap_factor * current_size / 2
        offset_x = random.uniform(-max_offset, max_offset)
        offset_y = random.uniform(-max_offset, max_offset)
        offset_z = random.uniform(-max_offset, max_offset)

        # Create transformation for overlap and rotation
        translation_vector = rg.Vector3d(offset_x, offset_y, offset_z)
        rotation_angle = random.uniform(0, math.pi / 4)
        rotation_axis = rg.Vector3d(random.choice([-1, 1]), random.choice([-1, 1]), random.choice([-1, 1]))
        rotation_axis.Unitize()

        # Create a new cube and apply transformations
        new_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(-cube_size / 2, cube_size / 2),
                          rg.Interval(-cube_size / 2, cube_size / 2), rg.Interval(-cube_size / 2, cube_size / 2))
        new_cube.Transform(rg.Transform.Translation(translation_vector))
        new_cube.Transform(rg.Transform.Rotation(rotation_angle, rotation_axis, rg.Point3d.Origin))

        # Add the transformed cube to the breps list
        breps.append(new_cube.ToBrep())

        # Update the size for the next layer
        current_size = cube_size

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_concept(5.0, 10, 0.2, 0.3, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_concept(3.0, 8, 0.1, 0.5, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_concept(4.0, 6, 0.15, 0.4, 27)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_concept(6.0, 5, 0.25, 0.2, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_concept(2.5, 12, 0.3, 0.1, 73)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
