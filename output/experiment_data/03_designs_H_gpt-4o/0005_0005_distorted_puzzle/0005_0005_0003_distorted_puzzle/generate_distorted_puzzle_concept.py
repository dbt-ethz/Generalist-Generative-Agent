# Created for 0005_0005_distorted_puzzle.json

""" Summary:
The function `generate_distorted_puzzle_concept` creates an architectural concept model inspired by the "Distorted Puzzle" metaphor. It generates fragmented, interlocking volumes of varying heights and shapes, simulating a dynamic interplay of light and shadow. By randomly positioning and transforming these blocks, the function ensures asymmetry, reflecting the metaphor's theme of complexity and interconnectedness. The spatial arrangement allows for individual experiences within a cohesive whole, embodying tension and equilibrium. Ultimately, the model captures the essence of a distorted puzzle, where each unique element contributes to a visually engaging and cohesive architectural expression."""

#! python 3
function_code = """def generate_distorted_puzzle_concept(base_area, height_range, num_blocks, random_seed=0):
    \"""
    Create an architectural Concept Model for the 'Distorted Puzzle' metaphor.

    This function assembles fragmented, interlocking volumes with varying heights and asymmetrical forms.
    The design emphasizes a play of light and shadow, ensuring each volume is distinct yet part of a cohesive whole.

    Parameters:
    - base_area (tuple): Dimensions of the base footprint (length, width) in meters.
    - height_range (tuple): Min and max height (min_height, max_height) for the volumes in meters.
    - num_blocks (int): Number of interlocking volumes to generate.
    - random_seed (int, optional): Seed for random number generation to ensure replicability. Default is 0.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(random_seed)
    blocks = []
    base_length, base_width = base_area
    min_height, max_height = height_range

    for _ in range(num_blocks):
        # Randomly determine the position and size of each block
        x = random.uniform(0, base_length)
        y = random.uniform(0, base_width)
        width = random.uniform(0.1 * base_width, 0.25 * base_width)
        length = random.uniform(0.1 * base_length, 0.25 * base_length)
        height = random.uniform(min_height, max_height)

        # Create a base plane and box for the block
        base_plane = rg.Plane(rg.Point3d(x, y, 0), rg.Vector3d.ZAxis)
        box = rg.Box(base_plane, rg.Interval(0, width), rg.Interval(0, length), rg.Interval(0, height))
        block_brep = box.ToBrep()

        # Apply random transformations for asymmetry
        angle = random.uniform(-0.15, 0.15) # in radians
        axis = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        axis.Unitize()
        rotation = rg.Transform.Rotation(angle, axis, box.Center)
        block_brep.Transform(rotation)

        blocks.append(block_brep)

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_distorted_puzzle_concept((10, 5), (2, 4), 15, random_seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_distorted_puzzle_concept((8, 6), (1, 3), 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_distorted_puzzle_concept((12, 8), (3, 7), 20, random_seed=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_distorted_puzzle_concept((15, 10), (4, 8), 12, random_seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_distorted_puzzle_concept((5, 10), (1, 5), 8, random_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
