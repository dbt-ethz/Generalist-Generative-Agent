# Created for 0003_0001_a_labyrinth_of_blocks.json

""" Summary:
The function `create_labyrinth_of_blocks` generates an architectural concept model by creating a series of randomly sized and positioned blocks on a grid, simulating the metaphor "A labyrinth of blocks." It incorporates deliberate disruptions in the grid to establish a non-linear, labyrinthine layout that encourages exploration. The blocks vary in height and size, enhancing the spatial complexity and creating dynamic circulation paths that weave through them. This interplay of solid and void facilitates unexpected discoveries, while the varying heights allow light to penetrate deeper into the structure, casting intriguing shadows and enhancing the overall sense of mystery and engagement within the space."""

#! python 3
function_code = """def create_labyrinth_of_blocks(grid_size, num_blocks, max_block_size, seed=42):
    \"""
    Create an architectural Concept Model embodying the metaphor 'A labyrinth of blocks'.

    This function generates a series of interconnected blocks of varying sizes and heights, arranged
    on a grid system with deliberate disruptions to simulate a labyrinthine quality. The design
    incorporates circulation paths that weave through the blocks, with nodes where paths intersect,
    and employs a play of solid and void to enhance the sense of mystery and exploration.

    Parameters:
    - grid_size: tuple of two integers (rows, columns) defining the size of the grid.
    - num_blocks: integer, the number of blocks to generate.
    - max_block_size: tuple of three floats (width, depth, height) representing the maximum dimensions of any block.
    - seed: integer, seed for the random number generator to ensure replicability.

    Returns:
    - list of Rhino.Geometry.Brep objects representing the blocks in the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    blocks = []

    grid_rows, grid_cols = grid_size
    max_width, max_depth, max_height = max_block_size

    # Calculate the spacing between grid points
    grid_spacing_x = max_width * 1.5
    grid_spacing_y = max_depth * 1.5

    # Generate random blocks
    for _ in range(num_blocks):
        # Choose a random grid position
        grid_x = random.randint(0, grid_cols - 1)
        grid_y = random.randint(0, grid_rows - 1)

        # Randomize block size within the maximum limit
        width = random.uniform(max_width * 0.3, max_width)
        depth = random.uniform(max_depth * 0.3, max_depth)
        height = random.uniform(max_height * 0.5, max_height)

        # Calculate the block's position
        base_x = grid_x * grid_spacing_x
        base_y = grid_y * grid_spacing_y
        base_z = 0  # All blocks start from the ground level

        # Define the base of the block
        base_corners = [
            rg.Point3d(base_x, base_y, base_z),
            rg.Point3d(base_x + width, base_y, base_z),
            rg.Point3d(base_x + width, base_y + depth, base_z),
            rg.Point3d(base_x, base_y + depth, base_z)
        ]
        
        # Create a planar surface for the base
        base_surface = rg.Brep.CreateFromCornerPoints(base_corners[0], base_corners[1], base_corners[2], base_corners[3], 0.01)

        # Create a rectangle curve from the base corners
        base_curve = rg.PolylineCurve(base_corners + [base_corners[0]])

        # Extrude the base curve to create a block
        extrusion = rg.Extrusion.Create(base_curve, height, True)
        block = extrusion.ToBrep()

        blocks.append(block)

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks((10, 10), 20, (5.0, 5.0, 10.0), seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks((15, 15), 30, (6.0, 6.0, 12.0), seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks((8, 12), 25, (4.0, 4.0, 8.0), seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks((12, 12), 15, (3.0, 3.0, 15.0), seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks((20, 20), 50, (7.0, 7.0, 20.0), seed=11)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
