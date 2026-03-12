# Created for 0005_0002_distorted_puzzle.json

""" Summary:
The `generate_distorted_puzzle_model` function creates an architectural concept model inspired by the "Distorted puzzle" metaphor. It generates a series of fragmented modules, each randomly rotated and translated to form a cohesive yet complex structure. By varying module sizes, rotations, and translations, the function produces a labyrinthine spatial arrangement that encourages exploration and challenges traditional notions of order and symmetry. The resulting geometry features interconnected elements that evoke tension and curiosity, capturing the unpredictable yet unified essence of a distorted puzzle. This approach aligns with the metaphor's implications of fragmentation and cohesion in architectural design."""

#! python 3
function_code = """def generate_distorted_puzzle_model(module_base_size, num_modules, rotation_variation, translation_variation):
    \"""
    Creates an architectural Concept Model inspired by the 'Distorted puzzle' metaphor.
    
    This function generates a series of fragmented and interconnected modules that are rotated and translated 
    to form a cohesive whole. The model emphasizes labyrinthine spatial arrangements with varied alignments 
    that challenge traditional notions of order and symmetry.

    Parameters:
    - module_base_size: float, the base size of each module (in meters).
    - num_modules: int, the number of modules to generate.
    - rotation_variation: float, maximum rotation angle in degrees for each module.
    - translation_variation: float, maximum translation variation for module positioning (in meters).

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set seed for reproducibility
    random.seed(42)

    geometries = []

    # Create each module with random transformations
    for i in range(num_modules):
        # Define module as a box
        module = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(0, module_base_size),
            rg.Interval(0, module_base_size),
            rg.Interval(0, module_base_size)
        ).ToBrep()

        # Random rotation
        angle = math.radians(random.uniform(-rotation_variation, rotation_variation))
        rotation_axis = rg.Vector3d(0, 0, 1)  # Rotate around the Z-axis
        center_point = rg.Point3d(module_base_size / 2, module_base_size / 2, module_base_size / 2)
        rotation_transform = rg.Transform.Rotation(angle, rotation_axis, center_point)

        # Random translation
        x_translation = random.uniform(-translation_variation, translation_variation)
        y_translation = random.uniform(-translation_variation, translation_variation)
        z_translation = random.uniform(-translation_variation, translation_variation)
        translation_transform = rg.Transform.Translation(x_translation, y_translation, z_translation)

        # Apply transformations
        module.Transform(rotation_transform)
        module.Transform(translation_transform)

        # Add to list of geometries
        geometries.append(module)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_distorted_puzzle_model(5.0, 10, 45, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_distorted_puzzle_model(3.0, 15, 30, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_distorted_puzzle_model(4.0, 20, 60, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_distorted_puzzle_model(6.0, 8, 90, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_distorted_puzzle_model(2.5, 12, 75, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
