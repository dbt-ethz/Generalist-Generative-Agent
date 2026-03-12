# Created for 0003_0001_a_labyrinth_of_blocks.json

""" Summary:
The function `create_labyrinth_of_blocks` generates an architectural concept model inspired by the metaphor "A labyrinth of blocks." It creates a 3D arrangement of modular blocks with varying sizes, heights, and orientations, organized in a disrupted grid pattern to evoke a labyrinthine quality. The function simulates pathways that meander through these blocks, incorporating focal points where paths intersect, promoting exploration and curiosity. By varying block heights and dimensions, along with light penetration, the design fosters an interplay of solid and void, enhancing the sense of mystery and dynamic circulation essential to the architectural concept."""

#! python 3
function_code = """def create_labyrinth_of_blocks(grid_size, block_min_size, block_max_size, height_variation, path_width, seed=None):
    \"""
    Generate a 3D architectural Concept Model based on the metaphor 'A labyrinth of blocks'.

    This function creates a composition of modular blocks with varying dimensions, heights, and orientations, 
    arranged in a partially disrupted grid pattern to achieve a labyrinthine quality. It includes circulation 
    pathways that meander through the blocks, with nodes or focal points at intersections to enhance the sense of 
    discovery and exploration.

    Parameters:
    - grid_size: Tuple[int, int] specifying the number of blocks along the X and Y axes.
    - block_min_size: Tuple[float, float, float] specifying the minimum size of each block in meters (width, depth, height).
    - block_max_size: Tuple[float, float, float] specifying the maximum size of each block in meters (width, depth, height).
    - height_variation: float specifying the maximum variation in block heights to allow light penetration.
    - path_width: float specifying the width of the circulation paths in meters.
    - seed: Optional[int] for setting the random seed for reproducibility.

    Returns:
    - List of RhinoCommon Breps representing the blocks and circulation paths.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    if seed is not None:
        random.seed(seed)

    blocks = []
    paths = []

    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            # Randomize block dimensions and height variation
            width = random.uniform(block_min_size[0], block_max_size[0])
            depth = random.uniform(block_min_size[1], block_max_size[1])
            base_height = random.uniform(block_min_size[2], block_max_size[2])
            height = base_height + random.uniform(0, height_variation)

            # Apply random rotation and translation to disrupt the grid
            x_offset = random.uniform(-block_max_size[0] / 2, block_max_size[0] / 2)
            y_offset = random.uniform(-block_max_size[1] / 2, block_max_size[1] / 2)
            rotation_angle = random.uniform(0, math.pi / 4)

            # Define base point and rotation transformation
            base_point = rg.Point3d(i * block_max_size[0] + x_offset, j * block_max_size[1] + y_offset, 0)
            rotation_center = base_point
            rotation_axis = rg.Vector3d(0, 0, 1)
            rotation = rg.Transform.Rotation(rotation_angle, rotation_center)

            # Create block geometry
            block_corners = [
                base_point,
                rg.Point3d(base_point.X + width, base_point.Y, base_point.Z),
                rg.Point3d(base_point.X + width, base_point.Y + depth, base_point.Z),
                rg.Point3d(base_point.X, base_point.Y + depth, base_point.Z)
            ]
            for corner in block_corners:
                corner.Transform(rotation)

            block = rg.Brep.CreateFromBox([
                block_corners[0], block_corners[1], block_corners[2], block_corners[3],
                rg.Point3d(block_corners[0].X, block_corners[0].Y, block_corners[0].Z + height),
                rg.Point3d(block_corners[1].X, block_corners[1].Y, block_corners[1].Z + height),
                rg.Point3d(block_corners[2].X, block_corners[2].Y, block_corners[2].Z + height),
                rg.Point3d(block_corners[3].X, block_corners[3].Y, block_corners[3].Z + height)
            ])
            blocks.append(block)

            # Create circulation paths
            if random.random() < 0.4:  # 40% chance to create a path
                path_start = rg.Point3d(base_point.X + random.uniform(0, width), 
                                        base_point.Y + random.uniform(0, depth), 
                                        0)
                path_end = rg.Point3d(path_start.X + random.uniform(-path_width, path_width), 
                                      path_start.Y + random.uniform(-path_width, path_width), 
                                      0)
                path_line = rg.Line(path_start, path_end)
                path_curve = path_line.ToNurbsCurve()
                offset_curves = path_curve.Offset(rg.Plane.WorldXY, path_width / 2, 0.01, rg.CurveOffsetCornerStyle.Sharp)
                if offset_curves:
                    for offset_curve in offset_curves:
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
    geometry = create_labyrinth_of_blocks((5, 5), (1.0, 1.0, 1.0), (3.0, 3.0, 3.0), 2.0, 0.5, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks((10, 8), (0.5, 0.5, 0.5), (2.0, 2.0, 2.0), 1.5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks((7, 4), (1.5, 1.5, 1.5), (4.0, 4.0, 4.0), 3.0, 0.4, seed=101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks((6, 6), (2.0, 2.0, 2.0), (5.0, 5.0, 5.0), 1.0, 0.7, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks((4, 6), (0.8, 0.8, 0.8), (2.5, 2.5, 2.5), 2.5, 0.6, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
