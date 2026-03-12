# Created for 0005_0002_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_model` generates an architectural concept model inspired by the 'Distorted puzzle' metaphor. It creates a series of interconnected modules that are fragmented yet cohesive, reflecting the metaphor's emphasis on tension and complexity. By manipulating parameters such as height, rotation, and translation, the function introduces variability in each module's form, resulting in a labyrinthine arrangement that encourages exploration. The random transformations ensure that the modules fit together in unexpected ways, evoking curiosity and challenging traditional notions of order. The final output is a collection of 3D geometries that embody the metaphor's playful yet structured essence."""

#! python 3
function_code = """def create_distorted_puzzle_model(module_size, num_modules, height_variation, rotation_variation, translation_variation):
    \"""
    Generate an architectural Concept Model based on the 'Distorted puzzle' metaphor.

    Parameters:
    - module_size: A float representing the base dimension of each module in meters.
    - num_modules: An integer representing the number of modules to be created.
    - height_variation: A float indicating the maximum height variation for each module.
    - rotation_variation: A float representing the maximum angle in degrees for rotating modules.
    - translation_variation: A float indicating the maximum translation allowed in meters for each module.

    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    # Set the random seed for reproducibility
    random.seed(42)
    
    # Initialize empty list to store geometries
    geometries = []
    
    # Define a base module (e.g., a box)
    base_module = rg.Box(rg.Plane.WorldXY, rg.Interval(0, module_size), rg.Interval(0, module_size), rg.Interval(0, module_size))
    
    for _ in range(num_modules):
        # Create a new module by duplicating the base
        module = base_module.ToBrep().Duplicate()
        
        # Apply random scaling for height variation
        height_scale = 1 + random.uniform(-height_variation, height_variation)
        scaling = rg.Transform.Scale(rg.Plane.WorldXY, 1, 1, height_scale)
        module.Transform(scaling)
        
        # Apply random rotation
        angle = random.uniform(-rotation_variation, rotation_variation)
        rotation = rg.Transform.Rotation(math.radians(angle), rg.Vector3d.ZAxis, rg.Point3d.Origin)
        module.Transform(rotation)
        
        # Apply random translation
        x_trans = random.uniform(-translation_variation, translation_variation)
        y_trans = random.uniform(-translation_variation, translation_variation)
        z_trans = random.uniform(0, translation_variation)  # Encourage upward stacking
        translation = rg.Transform.Translation(x_trans, y_trans, z_trans)
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
    geometry = create_distorted_puzzle_model(2.0, 10, 0.5, 30, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(1.5, 15, 0.3, 45, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(3.0, 8, 0.4, 60, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(2.5, 12, 0.6, 15, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(1.0, 20, 0.2, 75, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
