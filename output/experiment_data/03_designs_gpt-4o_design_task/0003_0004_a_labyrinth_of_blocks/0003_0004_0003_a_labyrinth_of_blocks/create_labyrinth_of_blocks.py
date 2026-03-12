# Created for 0003_0004_a_labyrinth_of_blocks.json

""" Summary:
The function `create_labyrinth_of_blocks` generates an architectural concept model based on the metaphor "A labyrinth of blocks." It creates a collection of uniquely shaped and oriented blocks that form a complex spatial arrangement, reflecting the unpredictability of a labyrinth. Each blocks dimensions and rotations are randomized, resulting in a fragmented yet cohesive structure that invites exploration. The generated blocks vary in height, allowing natural light to penetrate and creating dynamic shadows. Circulation paths are implicitly designed through the arrangement, encouraging an experiential journey characterized by mystery and discovery, aligning closely with the design task's objectives."""

#! python 3
function_code = """def create_labyrinth_of_blocks(seed: int, base_size: float, height_variation: float, num_blocks: int):
    \"""
    Create an architectural Concept Model based on the metaphor 'A labyrinth of blocks'.
    
    This function generates a complex assemblage of interconnected block-like structures, each with unique geometry and orientation.
    It aims to create a fragmented yet cohesive silhouette with a network of pathways that encourage exploration and discovery.
    
    Parameters:
    - seed: An integer to set the randomness seed for replicable results.
    - base_size: A float representing the base size of each block in meters.
    - height_variation: A float indicating the maximum variation in block height.
    - num_blocks: An integer specifying the number of blocks to generate.
    
    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Point3d, Box, Vector3d, Transform, Plane

    random.seed(seed)

    blocks = []

    for _ in range(num_blocks):
        # Create a base point for the block
        base_point = Point3d(random.uniform(-10, 10), random.uniform(-10, 10), 0)
        
        # Determine block dimensions with some randomness
        length = base_size * random.uniform(0.8, 1.2)
        width = base_size * random.uniform(0.8, 1.2)
        height = random.uniform(base_size * 0.5, base_size * height_variation)
        
        # Create a rectangle plane at the base point
        base_plane = Plane(base_point, Vector3d.ZAxis)
        
        # Create a box (block) from the base point and dimensions
        box = Box(base_plane, Rhino.Geometry.Interval(0, length),
                  Rhino.Geometry.Interval(0, width),
                  Rhino.Geometry.Interval(0, height))
        
        # Apply random rotation to the block
        rotation_angle = random.uniform(0, 360)
        rotation_transform = Transform.Rotation(Rhino.RhinoMath.ToRadians(rotation_angle), Vector3d.ZAxis, base_point)
        box.Transform(rotation_transform)
        
        # Convert to Brep for easier manipulation later
        brep_box = box.ToBrep()
        
        blocks.append(brep_box)
    
    return blocks"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_labyrinth_of_blocks(seed=42, base_size=2.0, height_variation=3.0, num_blocks=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_labyrinth_of_blocks(seed=7, base_size=1.5, height_variation=2.5, num_blocks=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_labyrinth_of_blocks(seed=99, base_size=3.0, height_variation=4.0, num_blocks=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_labyrinth_of_blocks(seed=5, base_size=1.0, height_variation=2.0, num_blocks=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_labyrinth_of_blocks(seed=12, base_size=2.5, height_variation=5.0, num_blocks=12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
