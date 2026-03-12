# Created for 0005_0002_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_model` generates an architectural concept model inspired by the 'Distorted puzzle' metaphor by creating a series of interconnected, skewed modules. Each module is a 3D shape that is distorted through skew transformations, reflecting the metaphor's themes of fragmentation and cohesion. The modules are randomly positioned and stacked, forming a labyrinthine spatial arrangement that invites exploration. By varying the size and skew factor, the model embodies complexity and movement, challenging traditional notions of symmetry and order. Ultimately, the design evokes curiosity and interaction, encapsulating the playful yet deliberate nature of a distorted puzzle."""

#! python 3
function_code = """def create_distorted_puzzle_model(module_base, module_count, random_seed, skew_factor):
    \"""
    Creates an architectural Concept Model based on the 'Distorted puzzle' metaphor.
    
    The function generates a series of skewed and interconnected modules that are stacked
    and arranged to form a cohesive yet fragmented spatial composition. The design focuses 
    on creating a labyrinthine arrangement with varied alignments and perspectives, 
    challenging traditional order and symmetry.

    Parameters:
    - module_base: float, the base size of each module in meters.
    - module_count: int, the number of modules to create and arrange.
    - random_seed: int, the seed for randomness to ensure replicable results.
    - skew_factor: float, the amount by which modules are skewed, influencing their distortion.

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set the random seed for reproducibility
    random.seed(random_seed)
    
    # Initialize list to store the generated geometries
    geometries = []
    
    # Define a helper function to create a skewed module
    def create_skewed_module(base_size, skew):
        # Create a base box
        base_plane = rg.Plane.WorldXY
        box = rg.Box(base_plane, rg.Interval(0, base_size), rg.Interval(0, base_size), rg.Interval(0, base_size))
        
        # Apply a skew transformation
        skew_transform = rg.Transform.Identity
        skew_transform.M03 = skew  # Skew in the x-direction
        skew_transform.M13 = skew  # Skew in the y-direction
        box.Transform(skew_transform)
        
        return box.ToBrep()
    
    # Generate modules with skew and random positioning
    for i in range(module_count):
        # Create a skewed module
        skew_amount = random.uniform(-skew_factor, skew_factor)
        module = create_skewed_module(module_base, skew_amount)
        
        # Randomly position the module within a certain range
        x_offset = random.uniform(-module_base / 2, module_base / 2)
        y_offset = random.uniform(-module_base / 2, module_base / 2)
        z_offset = random.uniform(0, module_base * module_count * 0.1)  # Stacking effect
        
        # Apply translation
        translation = rg.Transform.Translation(x_offset, y_offset, z_offset)
        module.Transform(translation)
        
        # Add the module to the list of geometries
        geometries.append(module)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(2.0, 10, 42, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(1.5, 15, 7, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(3.0, 20, 99, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(2.5, 5, 123, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(4.0, 8, 56, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
