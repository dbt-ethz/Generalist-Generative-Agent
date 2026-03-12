# Created for 0003_0002_a_labyrinth_of_blocks.json

""" Summary:
The provided function, `create_labyrinth_of_blocks`, generates a three-dimensional architectural concept model inspired by the metaphor "A labyrinth of blocks." It creates an array of interlocking blocks with varying sizes and orientations, arranged in an organic, non-linear pattern that reflects complexity and encourages exploration. The function incorporates randomness to introduce unexpected pathways and hidden spaces, enhancing the sense of mystery. Additionally, it strategically includes voids within the blocks to manipulate light and shadow, thereby enriching the spatial experience. This design approach aligns with the metaphor's implications of disorientation and interaction, resulting in a dynamic architectural model."""

#! python 3
function_code = """def create_labyrinth_of_blocks(seed: int, num_blocks: int, base_size: float, height_variation: float, max_offset: float):
    \"""
    Creates an architectural Concept Model based on the metaphor 'A labyrinth of blocks'.
    
    This function generates an array of interlocking blocks with varying dimensions and orientations.
    The blocks are arranged in a non-linear, organic pattern to form a complex spatial configuration,
    encouraging exploration and interaction. The design emphasizes light and shadow interplay through
    varying block heights and strategically placed voids.
    
    Inputs:
    - seed: An integer to set the randomness seed for reproducibility.
    - num_blocks: The number of blocks to generate in the labyrinth.
    - base_size: The base size of each block, influencing its initial width and depth.
    - height_variation: The maximum variation in height for the blocks.
    - max_offset: The maximum offset for block placement to create a more organic arrangement.
    
    Outputs:
    - A list of RhinoCommon Brep objects representing the 3D geometries of the blocks.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    blocks = []
    
    for _ in range(num_blocks):
        # Random position with some offset to create organic arrangement
        x_offset = random.uniform(-max_offset, max_offset)
        y_offset = random.uniform(-max_offset, max_offset)
        
        # Random size and height
        width = base_size * random.uniform(0.5, 1.5)
        depth = base_size * random.uniform(0.5, 1.5)
        height = base_size * random.uniform(0.5, 1.0) + height_variation * random.random()

        # Create a base box for the block
        base_plane = rg.Plane.WorldXY
        base_plane.Origin += rg.Vector3d(x_offset, y_offset, 0)
        box = rg.Box(base_plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))
        
        # Convert the box to a Brep
        block_brep = box.ToBrep()
        
        # Optionally create a void within the block
        if random.random() > 0.7:  # 30% chance to create a void
            void_width = width * random.uniform(0.2, 0.6)
            void_depth = depth * random.uniform(0.2, 0.6)
            void_height = height * random.uniform(0.3, 0.7)
            void_box = rg.Box(base_plane, rg.Interval(0, void_width), rg.Interval(0, void_depth), rg.Interval(height * 0.3, height))
            void_brep = void_box.ToBrep()
            block_brep = rg.Brep.CreateBooleanDifference([block_brep], [void_brep], 0.01)[0]
        
        blocks.append(block_brep)
    
    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks(seed=42, num_blocks=10, base_size=2.0, height_variation=1.5, max_offset=3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(seed=7, num_blocks=20, base_size=1.5, height_variation=2.0, max_offset=5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(seed=99, num_blocks=15, base_size=3.0, height_variation=2.5, max_offset=4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(seed=12, num_blocks=25, base_size=1.0, height_variation=0.5, max_offset=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(seed=100, num_blocks=30, base_size=2.5, height_variation=3.0, max_offset=6.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
