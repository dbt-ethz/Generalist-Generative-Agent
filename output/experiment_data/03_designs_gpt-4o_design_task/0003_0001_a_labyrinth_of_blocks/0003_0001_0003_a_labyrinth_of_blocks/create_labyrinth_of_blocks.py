# Created for 0003_0001_a_labyrinth_of_blocks.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor "A labyrinth of blocks." It creates a grid of modular blocks with varying sizes and heights, simulating a chaotic yet intentional layout. By introducing disruptions in the grid alignment, it mimics the non-linear pathways characteristic of a labyrinth. The function randomly determines the dimensions and positions of each block, ensuring a fragmented silhouette that fosters exploration. Additionally, the varying heights enhance light and shadow play, creating dynamic spatial experiences. This approach encourages discovery and engagement, aligning perfectly with the metaphor's implications of mystery and exploration."""

#! python 3
function_code = """def create_labyrinth_of_blocks(grid_size, block_min_size, block_max_size, height_variation, disruption_chance, seed=None):
    \"""
    Creates an architectural Concept Model based on the metaphor 'A labyrinth of blocks'.
    
    Parameters:
    - grid_size: Tuple[int, int] representing the number of blocks in the x and y directions.
    - block_min_size: Tuple[float, float] representing the minimum width and depth of each block.
    - block_max_size: Tuple[float, float] representing the maximum width and depth of each block.
    - height_variation: Tuple[float, float] representing the minimum and maximum height of blocks.
    - disruption_chance: float representing the probability of a block disrupting the grid alignment.
    - seed: Optional[int] seed for random number generation to ensure replicable results.
    
    Returns:
    - List of RhinoCommon Brep objects representing the blocks in the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    if seed is not None:
        random.seed(seed)

    blocks = []
    grid_spacing_x = (block_max_size[0] + block_min_size[0]) / 2
    grid_spacing_y = (block_max_size[1] + block_min_size[1]) / 2

    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            # Determine block position, applying grid disruption
            x = i * grid_spacing_x + (random.uniform(-grid_spacing_x / 4, grid_spacing_x / 4) if random.random() < disruption_chance else 0)
            y = j * grid_spacing_y + (random.uniform(-grid_spacing_y / 4, grid_spacing_y / 4) if random.random() < disruption_chance else 0)

            # Determine block dimensions
            width = random.uniform(block_min_size[0], block_max_size[0])
            depth = random.uniform(block_min_size[1], block_max_size[1])
            height = random.uniform(height_variation[0], height_variation[1])

            # Create block
            block_corners = [
                rg.Point3d(x, y, 0),
                rg.Point3d(x + width, y, 0),
                rg.Point3d(x + width, y + depth, 0),
                rg.Point3d(x, y + depth, 0)
            ]
            base_profile = rg.Polyline(block_corners)
            base_curve = base_profile.ToNurbsCurve()
            block_brep = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(base_curve, rg.Vector3d(0, 0, height)))
            
            if block_brep:
                blocks.append(block_brep)
    
    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks((5, 5), (1.0, 1.0), (2.0, 2.0), (3.0, 5.0), 0.2, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks((3, 4), (0.5, 0.5), (1.5, 1.5), (2.0, 4.0), 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks((6, 6), (0.8, 1.2), (1.5, 2.5), (2.5, 6.0), 0.3, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks((4, 3), (2.0, 2.0), (3.0, 3.5), (1.0, 2.0), 0.15, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks((7, 7), (1.5, 1.5), (3.0, 3.0), (2.0, 5.0), 0.25, seed=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
