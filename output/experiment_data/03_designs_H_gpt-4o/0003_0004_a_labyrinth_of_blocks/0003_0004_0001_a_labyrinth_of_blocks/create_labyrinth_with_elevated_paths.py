# Created for 0003_0004_a_labyrinth_of_blocks.json

""" Summary:
The function `create_labyrinth_with_elevated_paths` generates an architectural concept model inspired by the metaphor "A labyrinth of blocks." It creates a collection of block-like structures with varying dimensions, orientations, and heights, forming a complex, non-linear spatial arrangement. The design intentionally avoids regular patterns, mimicking the unpredictability of a labyrinth. Elevated paths connect the blocks, enhancing exploration and mystery, while varying heights allow light to cast dynamic shadows. This interplay of geometries and circulation routes fosters a sense of discovery, aligning the architectural model with the metaphors emphasis on engagement and experience within the built environment."""

#! python 3
function_code = """def create_labyrinth_with_elevated_paths(base_size, height_range, num_blocks, path_width, seed=None):
    \"""
    Generates an architectural Concept Model based on the metaphor 'A labyrinth of blocks'.

    This function creates an intricate assemblage of block-like structures with differing shapes,
    orientations, and heights to form a complex spatial arrangement. The design includes elevated
    paths that connect different areas, enhancing the sense of mystery and exploration.

    Parameters:
    - base_size: float, the base size for each block in meters.
    - height_range: tuple(float, float), the range of heights for the blocks.
    - num_blocks: int, the number of blocks to generate.
    - path_width: float, the width of the elevated paths.
    - seed: int, optional, a seed for random number generation to ensure replicability.

    Returns:
    - list of Rhino.Geometry.Brep: A list of 3D geometries representing the blocks and paths.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    if seed is not None:
        random.seed(seed)

    geometries = []

    # Create blocks with random sizes and positions
    for _ in range(num_blocks):
        # Randomize block dimensions
        length = random.uniform(base_size * 0.5, base_size * 2)
        width = random.uniform(base_size * 0.5, base_size * 2)
        height = random.uniform(height_range[0], height_range[1])

        # Randomize block position and orientation
        x = random.uniform(-base_size * 5, base_size * 5)
        y = random.uniform(-base_size * 5, base_size * 5)
        z = 0  # Start blocks at the base level
        angle = random.uniform(0, 360)

        # Create a block at the randomized location and orientation
        base_plane = rg.Plane.WorldXY
        block_plane = rg.Plane(base_plane)
        block_plane.Translate(rg.Vector3d(x, y, z))
        block_plane.Rotate(math.radians(angle), base_plane.ZAxis)

        # Create a box geometry for the block
        block = rg.Box(block_plane, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))
        geometries.append(block.ToBrep())

    # Generate elevated paths
    for i in range(num_blocks - 1):
        start_point = geometries[i].GetBoundingBox(True).Center
        end_point = geometries[i + 1].GetBoundingBox(True).Center
        start_point.Z += random.uniform(2, 4)  # Elevate path
        end_point.Z += random.uniform(2, 4)    # Elevate path

        # Create path as a loft between elevated points
        path_curve = rg.Line(start_point, end_point).ToNurbsCurve()
        offset_curves = path_curve.Offset(rg.Plane.WorldXY, path_width / 2, 0.01, rg.CurveOffsetCornerStyle.Sharp)

        # Extrude the offset curves to create 3D paths
        for offset_curve in offset_curves:
            path_brep = rg.Brep.CreateFromSurface(rg.Extrusion.Create(offset_curve, 0.1, True))
            geometries.append(path_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_with_elevated_paths(base_size=3.0, height_range=(1.0, 5.0), num_blocks=10, path_width=0.5, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_with_elevated_paths(base_size=2.0, height_range=(0.5, 3.0), num_blocks=15, path_width=0.3, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_with_elevated_paths(base_size=4.0, height_range=(2.0, 6.0), num_blocks=20, path_width=0.7, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_with_elevated_paths(base_size=5.0, height_range=(3.0, 8.0), num_blocks=12, path_width=0.4, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_with_elevated_paths(base_size=1.5, height_range=(0.5, 2.5), num_blocks=8, path_width=0.6, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
