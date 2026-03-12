# Created for 0003_0005_a_labyrinth_of_blocks.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor "A labyrinth of blocks." It constructs a series of randomly sized and positioned block-like structures, ensuring a non-linear arrangement to create intriguing pathways and intersections. By incorporating variations in height and adding voids for light wells, the design emphasizes exploration and dynamic spatial relationships, fostering unexpected encounters. The interplay of light and shadow is achieved through the varying orientations of blocks, enhancing the labyrinthine experience. This approach aligns with the metaphor's implications, promoting a complex, multifaceted architectural journey that invites user engagement and discovery."""

#! python 3
function_code = """def create_labyrinth_of_blocks(base_size, height_variation, block_count, seed=None):
    \"""
    Creates an architectural Concept Model embodying the metaphor 'A labyrinth of blocks'.
    
    Parameters:
    - base_size (float): The average base size of each block in meters.
    - height_variation (float): The range of variation in block heights in meters.
    - block_count (int): The number of blocks to create.
    - seed (int, optional): A seed for the random number generator to ensure replicability.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of breps representing the blocks in the labyrinth.
    \"""
    import Rhino.Geometry as rg
    import random

    if seed is not None:
        random.seed(seed)
    
    blocks = []
    for _ in range(block_count):
        # Randomize block size
        dx = base_size * random.uniform(0.5, 1.5)
        dy = base_size * random.uniform(0.5, 1.5)
        dz = height_variation * random.uniform(0.5, 2.0)
        
        # Randomize block position
        x = random.uniform(-base_size * block_count / 2, base_size * block_count / 2)
        y = random.uniform(-base_size * block_count / 2, base_size * block_count / 2)
        z = 0  # Base level of blocks
        
        # Create a box for each block
        base_point = rg.Point3d(x, y, z)
        box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, dx), rg.Interval(0, dy), rg.Interval(0, dz))
        block_brep = box.ToBrep()
        
        blocks.append(block_brep)
    
    # Introduce light wells or voids
    void_count = block_count // 4
    for _ in range(void_count):
        # Create a smaller void block
        void_dx = base_size * random.uniform(0.2, 0.5)
        void_dy = base_size * random.uniform(0.2, 0.5)
        void_dz = height_variation * random.uniform(0.5, 1.5)
        
        # Randomize void position
        void_x = random.uniform(-base_size * block_count / 2, base_size * block_count / 2)
        void_y = random.uniform(-base_size * block_count / 2, base_size * block_count / 2)
        void_z = random.uniform(0, height_variation)
        
        # Create a box for the void
        void_base_point = rg.Point3d(void_x, void_y, void_z)
        void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, void_dx), rg.Interval(0, void_dy), rg.Interval(0, void_dz))
        void_brep = void_box.ToBrep()
        
        blocks.append(void_brep)
    
    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks(2.0, 5.0, 20, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(1.5, 3.0, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(3.0, 4.0, 30, seed=101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(2.5, 6.0, 25, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(4.0, 8.0, 10, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
