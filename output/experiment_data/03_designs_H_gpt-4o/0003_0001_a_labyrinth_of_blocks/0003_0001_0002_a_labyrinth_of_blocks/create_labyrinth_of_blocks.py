# Created for 0003_0001_a_labyrinth_of_blocks.json

""" Summary:
The function `create_labyrinth_of_blocks` generates an architectural concept model based on the metaphor 'A labyrinth of blocks' by creating a grid of modular blocks with varying sizes and heights. It intentionally disrupts the grid layout to simulate a labyrinthine structure, enhancing exploration and curiosity. The function incorporates circulation pathways that weave through the blocks, forming nodes for reflection. By manipulating block dimensions and heights, it fosters a dynamic interplay of solid and void, allowing light to penetrate and cast shadows. This design encourages users to navigate through unexpected pathways and discover hidden spaces, embodying the metaphor effectively."""

#! python 3
function_code = """def create_labyrinth_of_blocks(grid_size, max_block_size, height_variation, pathway_width, disruption_factor, seed=None):
    \"""
    Create an architectural Concept Model embodying the metaphor 'A labyrinth of blocks'.

    This function generates a series of blocks of varying sizes and heights, arranged in a grid system
    with intentional disruptions to simulate a labyrinthine quality. It includes circulation pathways that weave
    through the blocks, emphasizing the interplay of solid and void to enhance the sense of exploration.

    Parameters:
    - grid_size: Tuple[int, int] specifying the grid dimensions (rows, columns).
    - max_block_size: Tuple[float, float, float] specifying the maximum block dimensions (width, depth, height).
    - height_variation: float specifying the maximum variation in block heights.
    - pathway_width: float specifying the width of circulation pathways.
    - disruption_factor: float (0 to 1) indicating the likelihood of a block's position being disrupted.
    - seed: Optional[int] for setting the random seed for reproducibility.

    Returns:
    - List of Rhino.Geometry.Brep objects representing the blocks and pathways in the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    if seed is not None:
        random.seed(seed)

    blocks = []
    pathways = []
    grid_spacing_x = max_block_size[0] * 1.5
    grid_spacing_y = max_block_size[1] * 1.5

    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            # Determine if the block position should be disrupted
            x_offset = random.uniform(-grid_spacing_x / 4, grid_spacing_x / 4) if random.random() < disruption_factor else 0
            y_offset = random.uniform(-grid_spacing_y / 4, grid_spacing_y / 4) if random.random() < disruption_factor else 0

            # Base position of the block
            base_x = i * grid_spacing_x + x_offset
            base_y = j * grid_spacing_y + y_offset

            # Randomize block dimensions
            width = random.uniform(max_block_size[0] * 0.4, max_block_size[0])
            depth = random.uniform(max_block_size[1] * 0.4, max_block_size[1])
            height = random.uniform(max_block_size[2] * 0.5, max_block_size[2] + height_variation)

            # Create block
            base_corners = [
                rg.Point3d(base_x, base_y, 0),
                rg.Point3d(base_x + width, base_y, 0),
                rg.Point3d(base_x + width, base_y + depth, 0),
                rg.Point3d(base_x, base_y + depth, 0)
            ]
            base_curve = rg.Polyline(base_corners + [base_corners[0]]).ToNurbsCurve()
            extrusion = rg.Extrusion.Create(base_curve, height, True)
            block = extrusion.ToBrep()
            blocks.append(block)

            # Establish pathways
            if i > 0 and j > 0:
                # Connect to previous block pathways
                prev_base_x = (i - 1) * grid_spacing_x
                prev_base_y = (j - 1) * grid_spacing_y
                path_start = rg.Point3d(prev_base_x, prev_base_y, 0)
                path_end = rg.Point3d(base_x, base_y, 0)
                path_line = rg.Line(path_start, path_end)
                path_curve = path_line.ToNurbsCurve()
                offset_curves = path_curve.Offset(rg.Plane.WorldXY, pathway_width / 2, 0.01, rg.CurveOffsetCornerStyle.Sharp)
                if offset_curves:
                    for offset_curve in offset_curves:
                        path_surface = rg.Brep.CreatePlanarBreps(offset_curve)
                        if path_surface:
                            pathways.extend(path_surface)

    return blocks + pathways"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks((5, 5), (2.0, 2.0, 3.0), 1.0, 0.5, 0.3, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks((3, 4), (1.5, 1.5, 2.0), 0.5, 0.3, 0.2, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks((6, 6), (2.5, 2.5, 4.0), 2.0, 0.4, 0.5, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks((4, 3), (3.0, 1.0, 2.5), 1.5, 0.6, 0.4, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks((7, 2), (1.0, 3.0, 2.0), 0.8, 0.2, 0.1, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
