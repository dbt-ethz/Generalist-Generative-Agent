# Created for 0003_0001_a_labyrinth_of_blocks.json

""" Summary:
The function `create_labyrinth_of_blocks` generates an architectural concept model embodying the metaphor "A labyrinth of blocks" by creating a series of modular blocks with varying dimensions and heights, arranged in a disrupted grid pattern. This configuration simulates a labyrinthine structure, encouraging exploration through non-linear pathways that twist and turn. The function also incorporates circulation paths that connect intersections, serving as focal points for reflection. By manipulating block heights and introducing openings, the design emphasizes dynamic light and shadow play, enhancing the atmosphere of mystery and discovery, aligning perfectly with the metaphor's implications."""

#! python 3
function_code = """def create_labyrinth_of_blocks(grid_size, block_min_size, block_max_size, height_variation, path_width, seed=None):
    \"""
    Generate a 3D architectural Concept Model based on the metaphor 'A labyrinth of blocks'.
    
    This function creates a composition of modular blocks of varying dimensions and orientations, arranged in a grid system 
    with deliberate disruptions to achieve a labyrinthine quality. It also includes circulation paths that weave through the 
    blocks, with nodes or focal points at intersections.

    Parameters:
    - grid_size: Tuple[int, int] specifying the number of blocks along the X and Y axes.
    - block_min_size: Tuple[float, float, float] specifying the minimum size of each block in meters (width, depth, height).
    - block_max_size: Tuple[float, float, float] specifying the maximum size of each block in meters (width, depth, height).
    - height_variation: float specifying the maximum variation in block heights to create light penetration.
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
    path_points = []
    
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            # Determine block size within the specified range
            width = random.uniform(block_min_size[0], block_max_size[0])
            depth = random.uniform(block_min_size[1], block_max_size[1])
            base_height = random.uniform(block_min_size[2], block_max_size[2])
            height = base_height + random.uniform(0, height_variation)
            
            # Create a base point for the block
            base_point = rg.Point3d(i * block_max_size[0], j * block_max_size[1], 0)
            
            # Create a block as a Brep
            block_corners = [
                base_point,
                rg.Point3d(base_point.X + width, base_point.Y, base_point.Z),
                rg.Point3d(base_point.X + width, base_point.Y + depth, base_point.Z),
                rg.Point3d(base_point.X, base_point.Y + depth, base_point.Z)
            ]
            block = rg.Brep.CreateFromBox([block_corners[0], block_corners[1], block_corners[2], block_corners[3],
                                           rg.Point3d(block_corners[0].X, block_corners[0].Y, block_corners[0].Z + height),
                                           rg.Point3d(block_corners[1].X, block_corners[1].Y, block_corners[1].Z + height),
                                           rg.Point3d(block_corners[2].X, block_corners[2].Y, block_corners[2].Z + height),
                                           rg.Point3d(block_corners[3].X, block_corners[3].Y, block_corners[3].Z + height)])
            blocks.append(block)
            
            # Add path points at random positions within the grid
            if random.random() < 0.3:  # 30% chance to add a path point
                path_point = rg.Point3d(base_point.X + random.uniform(0, width), 
                                        base_point.Y + random.uniform(0, depth), 
                                        0)
                path_points.append(path_point)
    
    # Create paths through the labyrinth
    paths = []
    for index in range(1, len(path_points)):
        start_point = path_points[index - 1]
        end_point = path_points[index]
        line = rg.Line(start_point, end_point)
        path_curve = line.ToNurbsCurve()
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
    geometry = create_labyrinth_of_blocks((10, 10), (0.5, 0.5, 0.5), (2.0, 2.0, 2.0), 1.5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks((7, 4), (0.8, 0.8, 0.8), (2.5, 2.5, 2.5), 1.0, 0.4, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks((6, 6), (0.6, 0.6, 0.6), (2.2, 2.2, 2.2), 1.8, 0.2, seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks((8, 3), (1.5, 1.5, 1.5), (4.0, 4.0, 4.0), 3.0, 0.6, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
