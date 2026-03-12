# Created for 0003_0001_a_labyrinth_of_blocks.json

""" Summary:
The function `create_labyrinth_of_blocks` generates an architectural concept model that embodies the metaphor of "a labyrinth of blocks." It creates a complex spatial arrangement by randomly generating blocks of varying sizes and positions within defined boundaries. The randomization fosters intricate configurations that challenge navigation and orientation, aligning with the metaphor's essence of mystery and exploration. Each block's height, size, and orientation contribute to diverse perspectives and dynamic circulation routes, enhancing the interplay of light and shadow. The resulting 3D geometries encourage engagement with the architecture, reflecting the complexity implied by the metaphor."""

#! python 3
function_code = """def create_labyrinth_of_blocks(seed: int, num_blocks: int, min_size: float, max_size: float) -> list:
    \"""
    Creates a labyrinth-like architectural Concept Model composed of randomly sized and positioned blocks.
    
    The model is designed to evoke the metaphor of a labyrinth of blocks, characterized by complex and intricate
    spatial configurations that challenge navigation and orientation. The design emphasizes the interplay of light
    and shadow, varying perspectives, and dynamic circulation routes.

    Parameters:
    - seed (int): A seed for the random number generator to ensure replicable results.
    - num_blocks (int): The number of blocks to create in the labyrinth.
    - min_size (float): The minimum size of the blocks.
    - max_size (float): The maximum size of the blocks.

    Returns:
    - list: A list of Breps representing the 3D geometries of the blocks.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(seed)

    blocks = []

    # Define a spatial boundary for the labyrinth
    boundary_x = 50.0  # meters
    boundary_y = 50.0  # meters
    boundary_z = 20.0  # meters

    for _ in range(num_blocks):
        # Randomize size and position of each block
        size_x = random.uniform(min_size, max_size)
        size_y = random.uniform(min_size, max_size)
        size_z = random.uniform(min_size, max_size)

        pos_x = random.uniform(0, boundary_x - size_x)
        pos_y = random.uniform(0, boundary_y - size_y)
        pos_z = random.uniform(0, boundary_z - size_z)

        # Create a block (box) as a Brep
        base_point = rg.Point3d(pos_x, pos_y, pos_z)
        block_corners = [
            base_point,
            rg.Point3d(pos_x + size_x, pos_y, pos_z),
            rg.Point3d(pos_x + size_x, pos_y + size_y, pos_z),
            rg.Point3d(pos_x, pos_y + size_y, pos_z),
            rg.Point3d(pos_x, pos_y, pos_z + size_z),
            rg.Point3d(pos_x + size_x, pos_y, pos_z + size_z),
            rg.Point3d(pos_x + size_x, pos_y + size_y, pos_z + size_z),
            rg.Point3d(pos_x, pos_y + size_y, pos_z + size_z)
        ]
        block_box = rg.Box(rg.BoundingBox(block_corners))
        block_brep = block_box.ToBrep()
        
        blocks.append(block_brep)

    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks(seed=42, num_blocks=10, min_size=1.0, max_size=5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(seed=7, num_blocks=15, min_size=0.5, max_size=3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(seed=123, num_blocks=20, min_size=2.0, max_size=6.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(seed=99, num_blocks=12, min_size=0.8, max_size=4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(seed=2023, num_blocks=25, min_size=1.5, max_size=7.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
