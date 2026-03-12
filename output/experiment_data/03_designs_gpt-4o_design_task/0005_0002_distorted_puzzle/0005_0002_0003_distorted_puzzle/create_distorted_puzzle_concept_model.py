# Created for 0005_0002_distorted_puzzle.json

""" Summary:
The provided function, `create_distorted_puzzle_concept_model`, generates an architectural concept model that embodies the 'Distorted puzzle' metaphor by creating a series of fragmented yet interconnected modules. Each module is randomly scaled and positioned to reflect the metaphors themes of tension and cohesion. The function employs random transformations and stacking to achieve a labyrinthine spatial arrangement with varied perspectives, encouraging exploration. By manipulating geometric forms, the model evokes curiosity and challenges traditional notions of order and symmetry, ultimately resulting in a cohesive structure that captures the essence of a distorted yet unified puzzle."""

#! python 3
function_code = """def create_distorted_puzzle_concept_model(base_length, base_width, base_height, num_modules, seed=None):
    \"""
    Creates an architectural Concept Model based on the 'Distorted puzzle' metaphor.
    
    Parameters:
    - base_length (float): Length of the base module in meters.
    - base_width (float): Width of the base module in meters.
    - base_height (float): Height of the base module in meters.
    - num_modules (int): Number of modules to generate and arrange.
    - seed (int, optional): Seed for randomness to ensure replicable results.
    
    Returns:
    - List of Rhino.Geometry.Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the seed for randomness
    if seed is not None:
        random.seed(seed)
    
    geometries = []

    # Iterate to create and place each module
    for i in range(num_modules):
        # Randomly scale each module to create a varied effect
        scale_x = random.uniform(0.8, 1.2)
        scale_y = random.uniform(0.8, 1.2)
        scale_z = random.uniform(0.8, 1.2)
        
        # Create a base box
        box_origin = rg.Point3d(0, 0, 0)
        box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length * scale_x), rg.Interval(0, base_width * scale_y), rg.Interval(0, base_height * scale_z))
        
        # Randomly position each module within a certain range to create the distorted puzzle look
        move_x = random.uniform(-base_length * 0.5, base_length * 0.5)
        move_y = random.uniform(-base_width * 0.5, base_width * 0.5)
        move_z = random.uniform(0, base_height * num_modules * 0.1)  # Stacked effect with some overlap
        translation = rg.Vector3d(move_x, move_y, move_z)

        # Apply translation to the box
        box.Transform(rg.Transform.Translation(translation))

        # Convert the box to a Brep (Boundary Representation)
        brep = box.ToBrep()

        # Add to the list of geometries
        geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_concept_model(5.0, 3.0, 2.0, 10, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_concept_model(4.0, 2.5, 3.0, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_concept_model(6.0, 4.0, 2.5, 12, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_concept_model(7.0, 5.0, 4.0, 15, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_concept_model(3.0, 2.0, 1.0, 5, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
