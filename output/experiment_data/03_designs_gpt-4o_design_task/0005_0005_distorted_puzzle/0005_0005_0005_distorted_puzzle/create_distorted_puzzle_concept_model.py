# Created for 0005_0005_distorted_puzzle.json

""" Summary:
The provided function, `create_distorted_puzzle_concept_model`, generates an architectural concept model embodying the "Distorted Puzzle" metaphor. It creates a series of interlocking, asymmetric volumes that vary in height and form, simulating a fragmented yet cohesive structure. By incorporating random transformations, such as translation and rotation, the function ensures that each volume appears distinct while contributing to an interconnected whole. This design promotes a dynamic play of light and shadow, enhancing the spatial experience by transitioning between open and enclosed areas. Overall, the model reflects the metaphor's essence of visual complexity and unity through its varied geometries."""

#! python 3
function_code = """def create_distorted_puzzle_concept_model(base_size, volume_count, height_variation, randomness_seed):
    \"""
    Creates an architectural Concept Model based on the 'Distorted Puzzle' metaphor.
    
    This function generates a series of interlocking, asymmetric volumes that vary in height and form. 
    The design aims to create a dynamic play of light and shadow, with each volume being distinct yet 
    part of a larger interconnected system. The spatial arrangement promotes a balance between open 
    and enclosed spaces, enhancing the sense of tension and discovery.

    Parameters:
    - base_size: A tuple (width, depth) defining the base dimensions for the volumes.
    - volume_count: An integer specifying the number of volumes to generate.
    - height_variation: A float indicating the range of height variation for the volumes.
    - randomness_seed: An integer seed for the random number generator to ensure replicability.

    Returns:
    - A list of RhinoCommon Breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(randomness_seed)
    
    # Initialize list to store the resulting Breps
    geometries = []
    
    # Define base parameters
    base_width, base_depth = base_size
    base_height = 3.0  # Default base height in meters
    
    for i in range(volume_count):
        # Randomly perturb dimensions to create asymmetry and variation
        width_variation = random.uniform(-0.5, 0.5)
        depth_variation = random.uniform(-0.5, 0.5)
        height = base_height + random.uniform(-height_variation, height_variation)
        
        # Create a base box with the perturbed dimensions
        box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(0, base_width + width_variation),
            rg.Interval(0, base_depth + depth_variation),
            rg.Interval(0, height)
        )
        
        # Apply a random transformation for the distorted effect
        translation_vector = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), 0)
        rotation_angle = random.uniform(-0.1, 0.1)  # Small rotation in radians
        rotation_axis = rg.Vector3d(0, 0, 1)  # Rotate around Z-axis
        
        transform = rg.Transform.Translation(translation_vector)
        box.Transform(transform)
        transform = rg.Transform.Rotation(rotation_angle, rotation_axis, box.BoundingBox.Center)
        box.Transform(transform)
        
        # Convert Box to Brep and add to the list
        brep = box.ToBrep()
        geometries.append(brep)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_concept_model((10, 10), 5, 2.0, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_concept_model((8, 12), 7, 1.5, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_concept_model((6, 8), 4, 3.0, 27)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_concept_model((15, 15), 10, 4.0, 13)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_concept_model((12, 10), 6, 2.5, 56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
