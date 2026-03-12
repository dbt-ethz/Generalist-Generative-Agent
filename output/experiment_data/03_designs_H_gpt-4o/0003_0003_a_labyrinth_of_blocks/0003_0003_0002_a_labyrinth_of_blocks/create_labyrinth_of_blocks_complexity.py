# Created for 0003_0003_a_labyrinth_of_blocks.json

""" Summary:
The function `create_labyrinth_of_blocks_complexity` generates an architectural concept model that embodies the metaphor "A labyrinth of blocks." It creates a complex arrangement of interlocking blocks with varied dimensions, orientations, and heights, simulating a non-linear, maze-like structure. By incorporating winding pathways and elevated elements, the design emphasizes exploration and engagement. The inclusion of voids and openings allows natural light to filter through, creating dynamic shadows that enhance the sense of mystery. This approach aligns with the design task's focus on intricate spatial configurations, encouraging users to navigate and discover the architecture in an interactive manner."""

#! python 3
function_code = """def create_labyrinth_of_blocks_complexity(base_point, num_blocks, min_dim, max_dim, height_variation, seed):
    \"""
    Generates an architectural Concept Model embodying the metaphor 'A labyrinth of blocks' with increased complexity.
    
    This function creates a series of interlocking blocks with varying dimensions, orientations, and stacked layers 
    to form a multi-tiered and intricate massing. The arrangement is non-linear, simulating a labyrinthine quality 
    with diverse pathways and elevations. The design integrates voids and openings to allow natural light to 
    filter through, creating dynamic shadows.

    Parameters:
    - base_point: A tuple of (x, y, z) representing the starting point of the model.
    - num_blocks: An integer specifying the number of blocks to generate.
    - min_dim: A float indicating the minimum dimension for any side of a block.
    - max_dim: A float indicating the maximum dimension for any side of a block.
    - height_variation: A float representing the maximum variation in height for the blocks.
    - seed: An integer used to seed the random number generator for replicable results.

    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometries of the blocks.
    \"""

    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for reproducibility
    random.seed(seed)
    
    # List to store the block geometries
    blocks = []

    # Variable to track layers
    current_layer = 0

    for i in range(num_blocks):
        # Randomly determine dimensions for the block
        length = random.uniform(min_dim, max_dim)
        width = random.uniform(min_dim, max_dim)
        height = random.uniform(min_dim, height_variation)

        # Create a base point for the block
        x_offset = random.uniform(-max_dim, max_dim)
        y_offset = random.uniform(-max_dim, max_dim)
        
        # Increment layer after certain number of blocks
        if i % (num_blocks // 3) == 0:
            current_layer += 1
        
        z_offset = current_layer * height_variation + random.uniform(0, height_variation / 2)

        block_base_point = rg.Point3d(base_point[0] + x_offset, base_point[1] + y_offset, base_point[2] + z_offset)

        # Create the block as a box
        block = rg.Box(rg.Plane(block_base_point, rg.Vector3d.ZAxis), rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))

        # Introduce a random rotation
        rotation_angle = random.uniform(0, 360)
        rotation_transform = rg.Transform.Rotation(math.radians(rotation_angle), rg.Vector3d.ZAxis, block_base_point)
        block.Transform(rotation_transform)

        # Create random openings by subtracting smaller boxes
        if random.choice([True, False]):
            opening_length = random.uniform(min_dim / 2, length / 2)
            opening_width = random.uniform(min_dim / 2, width / 2)
            opening_height = random.uniform(min_dim / 2, height / 2)
            opening_offset = rg.Point3d(block_base_point.X + random.uniform(0, length - opening_length),
                                        block_base_point.Y + random.uniform(0, width - opening_width),
                                        block_base_point.Z + random.uniform(0, height - opening_height))
            opening_box = rg.Box(rg.Plane(opening_offset, rg.Vector3d.ZAxis), rg.Interval(0, opening_length), rg.Interval(0, opening_width), rg.Interval(0, opening_height))
            block_brep = block.ToBrep()
            opening_brep = opening_box.ToBrep()
            block_brep = rg.Brep.CreateBooleanDifference([block_brep], [opening_brep], 0.01)
            if block_brep:
                blocks.extend(block_brep)
        else:
            # Add the block to the list
            blocks.append(block.ToBrep())
        
    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks_complexity((0, 0, 0), 50, 1.0, 5.0, 10.0, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks_complexity((10, 10, 0), 75, 0.5, 3.0, 8.0, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks_complexity((-5, -5, 0), 100, 2.0, 6.0, 12.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks_complexity((20, 15, 0), 60, 1.5, 4.5, 9.0, 12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks_complexity((5, 5, 0), 80, 0.8, 4.0, 15.0, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
