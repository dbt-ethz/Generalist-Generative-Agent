# Created for 0003_0004_a_labyrinth_of_blocks.json

""" Summary:
The function `generate_labyrinth_of_blocks` creates an architectural concept model inspired by the metaphor "A labyrinth of blocks." It generates a collection of block-like structures with varying sizes, orientations, and heights, forming a complex and intriguing spatial arrangement. The function incorporates meandering pathways that reflect the unpredictable nature of a labyrinth, enhancing exploration and engagement. By randomizing positions, angles, and dimensions, it avoids regular patterns, fostering a sense of mystery. Additionally, the inclusion of vertical elements and dynamic circulation routes intensifies the interplay of light and shadow, inviting users to discover hidden spaces within the design."""

#! python 3
function_code = """def generate_labyrinth_of_blocks(num_blocks, block_size_range, height_range, path_width, seed):
    \"""
    Generates an architectural Concept Model based on the metaphor 'A labyrinth of blocks'.
    
    This function creates an intricate assemblage of block-like structures with differing shapes,
    orientations, and heights to form a complex spatial arrangement. The design includes meandering 
    circulation paths and varying block heights to enhance the sense of mystery and exploration.

    Parameters:
    - num_blocks: int, the number of blocks to generate.
    - block_size_range: tuple(float, float), the range of sizes for the blocks (length and width).
    - height_range: tuple(float, float), the range of heights for the blocks.
    - path_width: float, the width of the paths that meander through the blocks.
    - seed: int, the seed for random number generation to ensure replicability.

    Returns:
    - list of Rhino.Geometry.Brep: A list of 3D geometries representing the blocks and paths.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed
    random.seed(seed)

    # Initialize a list to hold the generated geometries
    geometries = []

    # Define a base plane for layout
    base_plane = rg.Plane.WorldXY

    # Create blocks with random sizes and positions
    for _ in range(num_blocks):
        # Randomize block dimensions
        length = random.uniform(*block_size_range)
        width = random.uniform(*block_size_range)
        height = random.uniform(*height_range)

        # Randomize block position and orientation
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        z = 0  # Start blocks at the base level
        angle = random.uniform(0, 360)

        # Create a block at the randomized location and orientation
        block_plane = rg.Plane(base_plane)
        block_plane.Translate(rg.Vector3d(x, y, z))
        block_plane.Rotate(math.radians(angle), base_plane.ZAxis)

        # Create a box geometry for the block
        block = rg.Box(block_plane, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))
        geometries.append(block.ToBrep())

    # Generate circulation paths
    path_points = []
    for _ in range(num_blocks):
        # Create random points for path generation
        path_x = random.uniform(-10, 10)
        path_y = random.uniform(-10, 10)
        path_points.append(rg.Point3d(path_x, path_y, 0))

    # Create a polyline to represent the path
    path_polyline = rg.Polyline(path_points)

    # Offset the path to create a passageway
    path_curve = path_polyline.ToNurbsCurve()
    offset_curves = path_curve.Offset(rg.Plane.WorldXY, path_width, 0.01, rg.CurveOffsetCornerStyle.Sharp)

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
    geometry = generate_labyrinth_of_blocks(num_blocks=20, block_size_range=(1.0, 3.0), height_range=(2.0, 5.0), path_width=0.5, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_labyrinth_of_blocks(num_blocks=15, block_size_range=(0.5, 2.0), height_range=(1.0, 4.0), path_width=0.3, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_labyrinth_of_blocks(num_blocks=25, block_size_range=(2.0, 4.0), height_range=(1.5, 6.0), path_width=0.4, seed=101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_labyrinth_of_blocks(num_blocks=30, block_size_range=(0.8, 2.5), height_range=(1.0, 3.5), path_width=0.6, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_labyrinth_of_blocks(num_blocks=10, block_size_range=(1.5, 3.5), height_range=(2.5, 7.0), path_width=0.2, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
