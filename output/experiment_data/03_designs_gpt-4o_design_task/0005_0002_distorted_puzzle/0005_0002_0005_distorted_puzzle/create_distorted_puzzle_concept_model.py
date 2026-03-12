# Created for 0005_0002_distorted_puzzle.json

""" Summary:
The provided function generates an architectural concept model based on the "Distorted puzzle" metaphor by creating a series of interconnected, fragmented modules. It employs random transformations to simulate the metaphor's essence, where each module is slightly misaligned, reflecting a dynamic interplay of parts. By adjusting vertical and horizontal variations, the function creates a labyrinthine spatial arrangement that invites exploration and challenges traditional notions of order. The result is a cohesive whole that maintains complexity through overlapping forms, evoking curiosity and engagement, embodying the playful yet structured nature of a "distorted puzzle."""

#! python 3
function_code = """def create_distorted_puzzle_concept_model(base_module_size, num_modules, vertical_variation, horizontal_variation, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Distorted puzzle' metaphor using a series of fragmented yet 
    interconnected modules. The function generates a labyrinthine spatial arrangement with a cohesive whole that suggests 
    movement and tension. It features varied perspectives and alignments challenging perceptions of order and symmetry.

    Parameters:
    - base_module_size: float, the base size of each module (in meters).
    - num_modules: int, the number of modules to generate.
    - vertical_variation: float, the maximum vertical offset for stacking modules (in meters).
    - horizontal_variation: float, the maximum horizontal offset for positioning modules (in meters).
    - seed: int, the seed for randomness to ensure replicable results.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(seed)

    # Initialize a list to store the generated geometries
    geometries = []

    # Create a base module shape (e.g., a cube) using the base_module_size
    base_module = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_module_size), rg.Interval(0, base_module_size), rg.Interval(0, base_module_size))

    # Iterate to create the specified number of modules
    for i in range(num_modules):
        # Apply random transformations to simulate the 'distorted puzzle' concept
        x_offset = random.uniform(-horizontal_variation, horizontal_variation)
        y_offset = random.uniform(-horizontal_variation, horizontal_variation)
        z_offset = random.uniform(-vertical_variation, vertical_variation)

        # Create a transformation matrix
        translation = rg.Transform.Translation(x_offset, y_offset, z_offset)

        # Apply the transformation to the base module
        transformed_module = base_module.ToBrep().Duplicate()  # Duplicate to avoid modifying the original
        transformed_module.Transform(translation)

        # Add the transformed module to the list of geometries
        geometries.append(transformed_module)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_concept_model(2.0, 10, 1.0, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_concept_model(3.0, 15, 2.0, 2.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_concept_model(1.5, 8, 0.5, 0.5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_concept_model(4.0, 20, 3.0, 3.0, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_concept_model(5.0, 12, 2.5, 2.5, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
