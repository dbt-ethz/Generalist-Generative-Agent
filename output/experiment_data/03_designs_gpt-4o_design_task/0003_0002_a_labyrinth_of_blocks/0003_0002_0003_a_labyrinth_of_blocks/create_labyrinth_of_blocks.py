# Created for 0003_0002_a_labyrinth_of_blocks.json

""" Summary:
The function `create_labyrinth_of_blocks` generates a three-dimensional architectural concept model inspired by the metaphor "A labyrinth of blocks." It creates an intricate arrangement of interlocking blocks with varying sizes and orientations, embodying complexity and disorientation. The random positioning and rotation of blocks reflect the non-linear pathways described in the design task, fostering exploration and interaction. By allowing natural light to filter through openings and voids, the model enhances the interplay of light and shadow, further enriching the labyrinthine experience and inviting users to navigate through its dynamic spaces."""

#! python 3
function_code = """def create_labyrinth_of_blocks(width, depth, height, block_count, seed=42):
    \"""
    Creates an architectural Concept Model based on the metaphor 'A labyrinth of blocks'.
    
    This function generates a 3D model consisting of interlocking blocks that vary in size
    and orientation, forming a complex and disorienting spatial configuration. The design 
    encourages exploration through non-linear pathways and vertical circulation.

    Parameters:
    - width (float): The overall width of the model space in meters.
    - depth (float): The overall depth of the model space in meters.
    - height (float): The overall height of the model space in meters.
    - block_count (int): The number of blocks to generate within the model.
    - seed (int, optional): A seed value for the random number generator to ensure replicability.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometry of the blocks.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    blocks = []
    base_height = height / 10  # Base height for blocks to allow variation in height

    for _ in range(block_count):
        # Random position within the bounds
        x = random.uniform(0, width)
        y = random.uniform(0, depth)
        
        # Random dimensions and orientation
        block_width = random.uniform(width / 20, width / 5)
        block_depth = random.uniform(depth / 20, depth / 5)
        block_height = random.uniform(base_height, base_height * 3)
        
        # Create a box at the random position
        corner1 = rg.Point3d(x, y, 0)
        corner2 = rg.Point3d(x + block_width, y + block_depth, block_height)
        
        box = rg.Box(rg.BoundingBox(corner1, corner2)).ToBrep()
        
        # Randomly rotate the block around its center
        center = rg.Point3d((corner1.X + corner2.X) / 2, (corner1.Y + corner2.Y) / 2, block_height / 2)
        angle = random.uniform(0, 2 * 3.141592653589793)  # Random rotation angle
        axis = rg.Vector3d(0, 0, 1)  # Rotate around the Z-axis
        rotation = rg.Transform.Rotation(angle, axis, center)
        box.Transform(rotation)
        
        # Add block to the list
        blocks.append(box)

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks(10.0, 15.0, 8.0, 50, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(20.0, 25.0, 10.0, 100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(5.0, 10.0, 6.0, 30, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(12.0, 18.0, 9.0, 75, seed=456)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(15.0, 20.0, 10.0, 60, seed=789)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
