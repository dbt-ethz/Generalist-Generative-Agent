# Created for 0003_0001_a_labyrinth_of_blocks.json

""" Summary:
The function `create_labyrinth_of_blocks` generates an architectural concept model based on the metaphor "A labyrinth of blocks." It constructs a grid of modular blocks with varying sizes and heights, introducing intentional disruptions to create a non-linear, labyrinthine arrangement. This arrangement encourages exploration, with winding pathways and intersecting nodes that invite users to engage with the space. The design also emphasizes the interplay of light and shadow by varying block heights, allowing natural light to penetrate and create dynamic visual experiences throughout the structure, embodying the metaphor's essence of curiosity and discovery."""

#! python 3
function_code = """def create_labyrinth_of_blocks(grid_size, min_block_size, max_block_size, height_variation, disruption_factor, path_nodes, seed=None):
    \"""
    Generate a 3D architectural Concept Model based on the metaphor 'A labyrinth of blocks'.

    This function arranges a series of modular blocks in a grid with deliberate disruptions to create a labyrinthine quality.
    It introduces non-linear pathways and nodes for exploration, with blocks varying in height and size to encourage
    dynamic light and shadow play.

    Parameters:
    - grid_size: Tuple[int, int] specifying the number of blocks along the X and Y axes.
    - min_block_size: Tuple[float, float, float] specifying the minimum size of each block in meters (width, depth, height).
    - max_block_size: Tuple[float, float, float] specifying the maximum size of each block in meters (width, depth, height).
    - height_variation: float specifying the maximum variation in block heights to allow light penetration.
    - disruption_factor: float specifying the degree of disruption in grid alignment (0 to 1).
    - path_nodes: int specifying the number of nodes for pathways within the labyrinth.
    - seed: Optional[int] for setting the random seed for reproducibility.

    Returns:
    - List of RhinoCommon Breps representing the blocks and pathways.
    \"""
    import Rhino.Geometry as rg
    import random
    
    if seed is not None:
        random.seed(seed)
    
    blocks = []
    paths = []
    grid_spacing_x = (max_block_size[0] + min_block_size[0]) / 2
    grid_spacing_y = (max_block_size[1] + min_block_size[1]) / 2
    
    # Create blocks with disruptions
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            # Calculate block position with potential disruption
            x = i * grid_spacing_x + random.uniform(-grid_spacing_x * disruption_factor, grid_spacing_x * disruption_factor)
            y = j * grid_spacing_y + random.uniform(-grid_spacing_y * disruption_factor, grid_spacing_y * disruption_factor)
            
            # Randomize block size within provided limits
            width = random.uniform(min_block_size[0], max_block_size[0])
            depth = random.uniform(min_block_size[1], max_block_size[1])
            height = random.uniform(min_block_size[2], max_block_size[2] + height_variation)
            
            # Create block
            block_corners = [
                rg.Point3d(x, y, 0),
                rg.Point3d(x + width, y, 0),
                rg.Point3d(x + width, y + depth, 0),
                rg.Point3d(x, y + depth, 0)
            ]
            base_curve = rg.Polyline(block_corners + [block_corners[0]]).ToNurbsCurve()
            block_brep = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(base_curve, rg.Vector3d(0, 0, height)))
            
            if block_brep:
                blocks.append(block_brep)
    
    # Create paths through specified nodes
    node_positions = []
    for _ in range(path_nodes):
        x = random.uniform(0, grid_size[0] * grid_spacing_x)
        y = random.uniform(0, grid_size[1] * grid_spacing_y)
        node_positions.append(rg.Point3d(x, y, 0))
    
    for index in range(1, len(node_positions)):
        start_point = node_positions[index - 1]
        end_point = node_positions[index]
        path_curve = rg.Line(start_point, end_point).ToNurbsCurve()
        paths.append(path_curve)
    
    return blocks + paths"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks((5, 5), (1.0, 1.0, 1.0), (2.0, 2.0, 3.0), 1.5, 0.3, 10, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks((4, 6), (0.5, 0.5, 0.5), (1.5, 1.5, 2.5), 2.0, 0.5, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks((6, 4), (1.5, 1.5, 0.5), (3.0, 3.0, 2.0), 1.0, 0.2, 15, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks((3, 3), (0.8, 0.8, 0.8), (2.5, 2.5, 4.0), 1.0, 0.4, 5, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks((7, 7), (0.6, 0.6, 0.6), (2.2, 2.2, 3.5), 1.2, 0.6, 12, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
