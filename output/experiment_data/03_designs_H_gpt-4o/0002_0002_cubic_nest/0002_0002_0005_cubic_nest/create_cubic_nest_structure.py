# Created for 0002_0002_cubic_nest.json

""" Summary:
The provided function `create_cubic_nest_structure` generates an architectural concept model based on the "Cubic nest" metaphor by creating a series of nested cubic volumes. It accepts parameters like base size, layer count, and cube variation to determine the dimensions and arrangement of the cubes. By introducing overlap and random offsets, the function simulates the interconnectedness and complexity of the design, reflecting the protective nature of a "nest." This results in a multi-layered structure that invites exploration while varying materials and orientations enhance the transition between solid and void, embodying the metaphor's essence."""

#! python 3
function_code = """def create_cubic_nest_structure(base_size, layer_count, cube_variation, overlap_ratio, random_seed):
    \"""
    Generate an architectural Concept Model based on the 'Cubic nest' metaphor using a dynamic assembly of nested cubes.

    Parameters:
    - base_size (float): The size of the initial cube in meters.
    - layer_count (int): The number of layers or levels of cubes.
    - cube_variation (float): A factor determining the variation in cube sizes.
    - overlap_ratio (float): The overlap ratio between cubes (0 to 1).
    - random_seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D cubic volumes.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(random_seed)

    # List to store Breps
    breps = []

    # Initial cube centered at the origin
    origin_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(-base_size/2, base_size/2),
                         rg.Interval(-base_size/2, base_size/2), rg.Interval(-base_size/2, base_size/2))
    breps.append(origin_cube.ToBrep())

    # Generate layers of cubes with variation and overlap
    for layer in range(1, layer_count + 1):
        # Determine size variation for this layer
        size_variation = base_size * (1 + cube_variation * (random.random() - 0.5))

        # Calculate overlap offset
        overlap_offset = base_size * overlap_ratio * layer

        # Randomly determine position offsets for the cube
        offset_x = random.uniform(-overlap_offset, overlap_offset)
        offset_y = random.uniform(-overlap_offset, overlap_offset)
        offset_z = random.uniform(-overlap_offset, overlap_offset)

        # Create a new cube with the varied size
        varied_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(-size_variation/2, size_variation/2),
                             rg.Interval(-size_variation/2, size_variation/2), rg.Interval(-size_variation/2, size_variation/2))

        # Translate the cube to the new position
        translation = rg.Transform.Translation(offset_x, offset_y, offset_z)
        varied_cube.Transform(translation)

        # Add the new cube to the list of Breps
        breps.append(varied_cube.ToBrep())

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_structure(2.0, 5, 0.3, 0.2, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_structure(1.5, 4, 0.4, 0.1, 100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_structure(3.0, 6, 0.2, 0.3, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_structure(2.5, 3, 0.5, 0.15, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_structure(4.0, 7, 0.25, 0.4, 13)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
