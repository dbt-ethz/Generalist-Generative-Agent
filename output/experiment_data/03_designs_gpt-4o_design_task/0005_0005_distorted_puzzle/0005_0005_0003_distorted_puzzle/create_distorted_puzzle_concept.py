# Created for 0005_0005_distorted_puzzle.json

""" Summary:
The provided function, `create_distorted_puzzle_concept`, generates an architectural concept model that embodies the "Distorted puzzle" metaphor by creating a series of fragmented and interlocking volumes. Each volume varies in height and form, promoting a dynamic interplay of light and shadow through asymmetric shapes. The function applies random transformations to distort these volumes, reflecting the metaphor's themes of tension and interconnectedness. By adjusting parameters like base size, height variation, and the number of volumes, the function produces diverse geometries that evoke a complex, visually intriguing structure, simulating the experience of navigating a distorted puzzle in space."""

#! python 3
function_code = """def create_distorted_puzzle_concept(seed, base_size, height_variation, num_volumes):
    \"""
    Generates an architectural Concept Model based on the 'Distorted Puzzle' metaphor. This function creates
    an array of fragmented, interlocking volumes that vary in height and form, emphasizing a play of light 
    and shadow through asymmetric shapes and openings.

    Parameters:
    - seed (int): Seed for random number generation to ensure replicability.
    - base_size (float): The base size of each volume in meters.
    - height_variation (float): The range of height variation for the volumes.
    - num_volumes (int): The number of volumes in the concept model.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # List to store the resulting Brep objects
    volumes = []
    
    # Generate each volume
    for _ in range(num_volumes):
        # Randomly distort the base size
        dx = base_size * (0.5 + random.random())
        dy = base_size * (0.5 + random.random())
        dz = base_size + random.uniform(-height_variation, height_variation)
        
        # Create a box representing the volume
        box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(0, dx),
            rg.Interval(0, dy),
            rg.Interval(0, dz)
        )
        
        # Convert the box to a Brep
        brep = box.ToBrep()
        
        # Apply a random transformation to distort the volume
        xform = rg.Transform.Rotation(random.uniform(-0.1, 0.1), rg.Vector3d.ZAxis, box.Center)
        brep.Transform(xform)
        
        # Add the transformed Brep to the volumes list
        volumes.append(brep)
    
    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_concept(seed=42, base_size=2.0, height_variation=1.5, num_volumes=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_concept(seed=7, base_size=3.0, height_variation=2.0, num_volumes=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_concept(seed=21, base_size=1.5, height_variation=0.8, num_volumes=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_concept(seed=15, base_size=4.0, height_variation=3.0, num_volumes=12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_concept(seed=99, base_size=2.5, height_variation=2.5, num_volumes=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
