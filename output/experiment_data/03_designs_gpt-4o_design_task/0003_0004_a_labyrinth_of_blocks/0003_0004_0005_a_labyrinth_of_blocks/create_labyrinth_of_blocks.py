# Created for 0003_0004_a_labyrinth_of_blocks.json

""" Summary:
The function `create_labyrinth_of_blocks` generates an architectural concept model by creating a series of unique block-like structures that embody the metaphor "A labyrinth of blocks." It achieves this by using random dimensions, orientations, and positions for each block within defined spatial parameters. The resulting configuration is intentionally non-linear and complex, mimicking the unpredictability of a labyrinth, with varied heights and multi-dimensional circulation paths that foster exploration. By incorporating vertical elements and varying textures, the design emphasizes light, shadow, and dynamic perspectives, enhancing the experiential journey through the space and inviting curiosity and discovery."""

#! python 3
function_code = """def create_labyrinth_of_blocks(width, depth, height, num_blocks, seed=None):
    \"""
    Creates an architectural Concept Model based on the metaphor 'A labyrinth of blocks'.
    
    This function generates a series of interconnected block-like structures with varying shapes, orientations, and heights.
    The configuration is intentionally non-linear and complex, creating a spatial arrangement that invites exploration 
    and discovery. Vertical elements such as elevated platforms are also included to add layers of complexity.

    Parameters:
    - width: float. The total width of the space to fill with blocks in meters.
    - depth: float. The total depth of the space to fill with blocks in meters.
    - height: float. The maximum height of the blocks in meters.
    - num_blocks: int. The number of blocks to generate.
    - seed: int, optional. A seed value for random number generation to ensure replicable results.

    Returns:
    - List of RhinoCommon Brep objects representing the blocks.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    if seed is not None:
        random.seed(seed)

    blocks = []

    for _ in range(num_blocks):
        # Random dimensions for each block
        block_width = random.uniform(2, width / 4)
        block_depth = random.uniform(2, depth / 4)
        block_height = random.uniform(2, height)

        # Random position for each block
        x = random.uniform(0, width - block_width)
        y = random.uniform(0, depth - block_depth)
        z = 0  # Start from the base level

        # Random orientation angle
        angle = random.uniform(0, 360)

        # Create a base rectangle
        base_rect = rg.Rectangle3d(
            rg.Plane.WorldXY, rg.Point3d(x, y, z), rg.Point3d(x + block_width, y + block_depth, z)
        )

        # Create a block as a Brep
        box_corners = [
            base_rect.Corner(0),
            base_rect.Corner(1),
            base_rect.Corner(2),
            base_rect.Corner(3),
            rg.Point3d(x, y, z + block_height),
            rg.Point3d(x + block_width, y, z + block_height),
            rg.Point3d(x + block_width, y + block_depth, z + block_height),
            rg.Point3d(x, y + block_depth, z + block_height)
        ]
        block_brep = rg.Brep.CreateFromBox(box_corners)

        # Rotate the block randomly
        rotation_axis = rg.Line(base_rect.Center, rg.Point3d(base_rect.Center.X, base_rect.Center.Y, block_height)).ToNurbsCurve()
        rotated_block_brep = block_brep.Duplicate()
        rotated_block_brep.Transform(rg.Transform.Rotation(math.radians(angle), base_rect.Center))

        blocks.append(rotated_block_brep)

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks(50, 30, 10, 20, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(100, 50, 15, 30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(75, 40, 12, 25, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(60, 20, 8, 15, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(80, 60, 20, 40, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
