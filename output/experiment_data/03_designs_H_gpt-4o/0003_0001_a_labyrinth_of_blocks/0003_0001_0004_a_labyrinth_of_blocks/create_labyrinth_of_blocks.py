# Created for 0003_0001_a_labyrinth_of_blocks.json

""" Summary:
The function `create_labyrinth_of_blocks` generates an architectural concept model inspired by the metaphor "A labyrinth of blocks." It creates a composition of modular blocks with varying sizes and heights, arranged on a grid with intentional disruptions to evoke a labyrinthine quality. The function randomizes block positions and sizes while establishing circulation paths that weave through them, fostering exploration. By varying block heights, it enhances light and shadow interplay, creating dynamic spaces that encourage discovery. This approach embodies the metaphor's complexity, inviting users to navigate and engage with an intriguing, non-linear spatial arrangement."""

#! python 3
function_code = """def create_labyrinth_of_blocks(grid_size, block_count, block_size_range, height_variation, disruption_factor, seed=None):
    \"""
    Generate a 3D architectural Concept Model based on the metaphor 'A labyrinth of blocks'.

    This function creates a composition of blocks with varying dimensions, arranged on a grid with
    intentional disruptions to simulate a labyrinthine quality. It also includes pathways that weave
    through the blocks, with nodes at intersections to encourage exploration.

    Parameters:
    - grid_size: Tuple[int, int] specifying the number of blocks along the X and Y axes.
    - block_count: int specifying the total number of blocks to create.
    - block_size_range: Tuple[Tuple[float, float], Tuple[float, float]] specifying the min and max (width, depth).
    - height_variation: Tuple[float, float] specifying the min and max height of blocks.
    - disruption_factor: float specifying the degree of disruption to the grid's regularity.
    - seed: Optional[int] for setting the random seed for reproducibility.

    Returns:
    - List of RhinoCommon Breps representing the blocks.
    \"""
    import Rhino.Geometry as rg
    import random

    if seed is not None:
        random.seed(seed)

    blocks = []
    grid_width, grid_height = grid_size
    min_size, max_size = block_size_range

    for _ in range(block_count):
        # Randomly select a grid position
        x_index = random.randint(0, grid_width - 1)
        y_index = random.randint(0, grid_height - 1)

        # Randomize the block size and height
        width = random.uniform(min_size[0], max_size[0])
        depth = random.uniform(min_size[1], max_size[1])
        height = random.uniform(height_variation[0], height_variation[1])

        # Introduce disruption to break grid regularity
        x_disruption = random.uniform(-disruption_factor, disruption_factor)
        y_disruption = random.uniform(-disruption_factor, disruption_factor)

        # Define the base point of the block with disruption
        base_x = x_index * max_size[0] + x_disruption
        base_y = y_index * max_size[1] + y_disruption

        # Create the block as a Brep
        base_corners = [
            rg.Point3d(base_x, base_y, 0),
            rg.Point3d(base_x + width, base_y, 0),
            rg.Point3d(base_x + width, base_y + depth, 0),
            rg.Point3d(base_x, base_y + depth, 0)
        ]
        base_profile = rg.Polyline(base_corners)
        base_curve = base_profile.ToNurbsCurve()
        extrusion = rg.Extrusion.Create(base_curve, height, True)
        block_brep = extrusion.ToBrep()

        if block_brep:
            blocks.append(block_brep)

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks((10, 10), 50, ((1.0, 2.0), (1.0, 2.0)), (1.0, 5.0), 0.5, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks((8, 8), 30, ((0.5, 1.5), (0.5, 1.5)), (0.5, 3.0), 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks((12, 12), 100, ((2.0, 4.0), (2.0, 4.0)), (0.5, 6.0), 0.7, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks((5, 5), 20, ((1.5, 3.0), (1.5, 3.0)), (2.0, 4.0), 0.4, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks((6, 6), 40, ((1.0, 2.5), (1.0, 2.5)), (1.5, 4.5), 0.6, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
