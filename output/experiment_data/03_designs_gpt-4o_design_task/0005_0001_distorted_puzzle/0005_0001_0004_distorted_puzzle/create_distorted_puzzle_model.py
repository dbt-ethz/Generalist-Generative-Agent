# Created for 0005_0001_distorted_puzzle.json

""" Summary:
The provided function generates an architectural concept model based on the "Distorted puzzle" metaphor by creating a series of interlocking geometric volumes with intentional misalignments. It starts with a base volume defined by specified dimensions, then produces multiple additional volumes, each offset randomly within a defined range. This results in a dynamic arrangement that reflects the metaphor's emphasis on complexity, movement, and spatial discovery. The function ensures that despite the irregularities, the overall structure maintains coherence, mirroring the interconnected nature of a puzzle. Each generated volume contributes to a visually intriguing and explorative architectural model."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_volume, num_volumes, max_offset, seed=None):
    \"""
    Create an architectural Concept Model embodying the 'Distorted puzzle' metaphor by assembling a series of interlocking geometric volumes with slight misalignments.

    Parameters:
    - base_volume: A tuple representing the dimensions (length, width, height) of the base volume from which the model will be derived.
    - num_volumes: An integer specifying the number of interlocking volumes to generate.
    - max_offset: A float representing the maximum offset distance in meters for misalignments between interlocking volumes.
    - seed: An optional integer to set the random seed for reproducibility.

    Returns:
    - A list of RhinoCommon Brep objects representing the interlocking geometric volumes of the Concept Model.
    \"""

    import Rhino.Geometry as rg
    import random

    if seed is not None:
        random.seed(seed)

    length, width, height = base_volume
    volumes = []

    # Generate the initial base volume
    initial_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))
    volumes.append(initial_box.ToBrep())

    for _ in range(1, num_volumes):
        # Generate a random offset within the given maximum offset
        offset_x = random.uniform(-max_offset, max_offset)
        offset_y = random.uniform(-max_offset, max_offset)
        offset_z = random.uniform(-max_offset, max_offset)

        # Create a new volume with random misalignment
        new_box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(offset_x, length + offset_x),
            rg.Interval(offset_y, width + offset_y),
            rg.Interval(offset_z, height + offset_z)
        )
        volumes.append(new_box.ToBrep())

    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model((10, 5, 3), 8, 1.5, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model((15, 10, 5), 5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model((8, 4, 2), 10, 1.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model((12, 6, 4), 6, 2.5, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model((20, 15, 7), 12, 3.0, seed=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
