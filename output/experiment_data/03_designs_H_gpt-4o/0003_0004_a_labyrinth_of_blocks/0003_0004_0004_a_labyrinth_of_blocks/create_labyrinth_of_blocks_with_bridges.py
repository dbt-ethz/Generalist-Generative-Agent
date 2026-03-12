# Created for 0003_0004_a_labyrinth_of_blocks.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor "A labyrinth of blocks." It creates a series of interconnected, uniquely shaped blocks with varied heights and orientations, embodying the complexity and unpredictability of a labyrinth. The function allows for the inclusion of bridges that connect different blocks, enhancing spatial interaction and exploration. By randomizing block dimensions and positions, it fosters an organic configuration, avoiding regular patterns. The design prioritizes dynamic circulation paths and varying elevations that facilitate light penetration, fostering an engaging environment that encourages curiosity and discovery throughout the architectural space."""

#! python 3
function_code = """def create_labyrinth_of_blocks_with_bridges(base_size, height_variation, num_blocks, bridge_chance, seed=None):
    \"""
    Generates an architectural Concept Model based on the metaphor 'A labyrinth of blocks' with potential bridge connections.
    
    Parameters:
    - base_size (float): The base size for each block in meters.
    - height_variation (tuple): A tuple (min_height, max_height) specifying the range of block heights.
    - num_blocks (int): The number of blocks to generate.
    - bridge_chance (float): The probability (0 to 1) of a bridge being added between blocks.
    - seed (int, optional): A seed for the random number generator to ensure reproducibility.
    
    Returns:
    - list: A list of RhinoCommon Brep objects representing the blocks and bridges.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    if seed is not None:
        random.seed(seed)
    
    blocks = []
    block_centers = []  # To store centers for potential bridge connections

    for _ in range(num_blocks):
        # Randomly generate the position of the block
        x = random.uniform(-base_size * 5, base_size * 5)
        y = random.uniform(-base_size * 5, base_size * 5)
        z = 0  # Keeping this zero for ground-based blocks

        # Randomize the size and height of each block
        width = random.uniform(base_size * 0.5, base_size * 2)
        depth = random.uniform(base_size * 0.5, base_size * 2)
        height = random.uniform(height_variation[0], height_variation[1])

        # Create the base plane for each block
        base_plane = rg.Plane(rg.Point3d(x, y, z), rg.Vector3d.ZAxis)

        # Create the box as a Brep
        block = rg.Box(base_plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height)).ToBrep()
        
        # Store block center for bridges
        block_centers.append(rg.Point3d(x + width/2, y + depth/2, height))

        # Add the block to the list
        blocks.append(block)

    # Attempt to create bridges between blocks
    for i in range(len(block_centers) - 1):
        for j in range(i + 1, len(block_centers)):
            if random.random() < bridge_chance:
                # Create a bridge between two block centers
                start = block_centers[i]
                end = block_centers[j]
                
                # Create a bridge only if it spans a reasonable distance
                if start.DistanceTo(end) < base_size * 3:
                    # Create a simple rectangular bridge
                    bridge_curve = rg.Line(start, end).ToNurbsCurve()
                    bridge = rg.Brep.CreateFromSurface(rg.Extrusion.Create(bridge_curve, 0.5, True))
                    
                    # Add the bridge to the list
                    blocks.append(bridge)

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks_with_bridges(2.0, (1.0, 5.0), 10, 0.3, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks_with_bridges(3.0, (2.0, 6.0), 15, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks_with_bridges(1.5, (0.5, 4.0), 20, 0.2, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks_with_bridges(4.0, (1.5, 7.0), 12, 0.4, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks_with_bridges(2.5, (1.0, 3.0), 8, 0.6, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
