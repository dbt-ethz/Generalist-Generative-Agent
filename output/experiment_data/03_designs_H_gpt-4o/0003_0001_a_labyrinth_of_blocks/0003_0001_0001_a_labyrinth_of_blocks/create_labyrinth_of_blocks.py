# Created for 0003_0001_a_labyrinth_of_blocks.json

""" Summary:
The provided function, `create_labyrinth_of_blocks`, generates an architectural concept model that embodies the metaphor "A labyrinth of blocks." It creates a 3D arrangement of modular blocks with varying sizes and heights, strategically disrupted from a standard grid to evoke a labyrinthine quality. Circulation paths are designed to weave through these blocks, incorporating nodes for moments of pause and reflection. By manipulating block heights, the function allows light to penetrate and cast dynamic shadows, enhancing the sense of exploration and mystery within the space. This approach fosters user engagement with the architecture's intricate, non-linear spatial relationships."""

#! python 3
function_code = """def create_labyrinth_of_blocks(grid_size, block_size_range, height_variation_range, path_width, seed=None):
    \"""
    Generate a 3D architectural Concept Model based on the metaphor 'A labyrinth of blocks'.

    This function creates a composition of modular blocks with varying dimensions and orientations,
    arranged in a grid-like pattern with deliberate disruptions to achieve a labyrinthine quality.
    It includes circulation paths that weave through the blocks, with nodes at intersections.

    Parameters:
    - grid_size: Tuple[int, int] specifying the number of blocks along the X and Y axes.
    - block_size_range: Tuple[Tuple[float, float], Tuple[float, float]] specifying the min and max size of each block (width, depth) in meters.
    - height_variation_range: Tuple[float, float] specifying the minimum and maximum height variation of blocks to create light penetration.
    - path_width: float specifying the width of the circulation paths in meters.
    - seed: Optional[int] for setting the random seed for reproducibility.

    Returns:
    - List of RhinoCommon Breps representing the blocks and circulation paths.
    \"""
    import Rhino.Geometry as rg
    import random

    if seed is not None:
        random.seed(seed)

    blocks = []
    paths = []

    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            # Calculate base point with random offset for disruption
            base_x = i * block_size_range[1][0] + random.uniform(-block_size_range[1][0] * 0.5, block_size_range[1][0] * 0.5)
            base_y = j * block_size_range[1][1] + random.uniform(-block_size_range[1][1] * 0.5, block_size_range[1][1] * 0.5)

            # Determine block size within the specified range
            width = random.uniform(block_size_range[0][0], block_size_range[1][0])
            depth = random.uniform(block_size_range[0][1], block_size_range[1][1])
            height = random.uniform(height_variation_range[0], height_variation_range[1])

            # Create a block as a Brep
            corners = [
                rg.Point3d(base_x, base_y, 0),
                rg.Point3d(base_x + width, base_y, 0),
                rg.Point3d(base_x + width, base_y + depth, 0),
                rg.Point3d(base_x, base_y + depth, 0)
            ]
            block = rg.Brep.CreateFromBox([corners[0], corners[1], corners[2], corners[3],
                                           rg.Point3d(corners[0].X, corners[0].Y, height),
                                           rg.Point3d(corners[1].X, corners[1].Y, height),
                                           rg.Point3d(corners[2].X, corners[2].Y, height),
                                           rg.Point3d(corners[3].X, corners[3].Y, height)])
            blocks.append(block)

            # Create circulation path by connecting to adjacent block centers
            if i > 0 and j > 0:
                path_start = rg.Point3d(base_x + width / 2, base_y + depth / 2, 0)
                path_end_x = (base_x - block_size_range[1][0] / 2) if i > 0 else path_start.X
                path_end_y = (base_y - block_size_range[1][1] / 2) if j > 0 else path_start.Y
                path_end = rg.Point3d(path_end_x, path_end_y, 0)
                path_line = rg.LineCurve(path_start, path_end)
                path_offset = path_line.Offset(rg.Plane.WorldXY, path_width / 2, 0.01, rg.CurveOffsetCornerStyle.Sharp)
                if path_offset:
                    for offset_curve in path_offset:
                        path_surface = rg.Brep.CreatePlanarBreps(offset_curve)
                        if path_surface:
                            paths.extend(path_surface)

    return blocks + paths"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks((5, 5), ((1, 1), (3, 3)), (2, 5), 0.5, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks((4, 6), ((0.5, 0.5), (2, 2)), (1, 4), 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks((3, 7), ((2, 2), (4, 4)), (1, 3), 0.6, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks((6, 4), ((1, 2), (2, 5)), (1, 6), 0.4, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks((7, 3), ((1.5, 1.5), (2.5, 2.5)), (3, 7), 0.2, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
