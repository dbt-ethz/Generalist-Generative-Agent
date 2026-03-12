# Created for 0011_0001_shifted_grid.json

""" Summary:
The provided function generates an architectural concept model based on the "Shifted Grid" metaphor by dynamically altering a regular grid pattern. It creates a series of 3D box geometries with randomized positions and heights, introducing movement and fluidity. The function allows for variations in grid size, shift amount, cell size, and height, reflecting the metaphor's emphasis on unexpected alignments and adaptability. As a result, the model facilitates diverse spatial experiences and circulation paths, encouraging playful interactions with light and shadow, ultimately fostering a sense of discovery within the architectural space."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size=5, shift_amount=2, cell_size=4, height_variation=3, random_seed=42):
    \"""
    Creates an architectural Concept Model using a 'Shifted Grid' metaphor. This model features a dynamic
    reconfiguration of a regular grid pattern to introduce movement and fluidity with varied alignments.

    Parameters:
    - grid_size (int): The number of cells along one dimension of the grid.
    - shift_amount (float): The maximum distance a grid cell can be shifted from its regular position.
    - cell_size (float): The base size of each cell in the grid (in meters).
    - height_variation (float): The maximum variation in height for each cell volume.
    - random_seed (int): Seed value for randomness to ensure replicability.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(random_seed)
    breps = []

    for i in range(grid_size):
        for j in range(grid_size):
            # Calculate the base position of the current grid cell
            base_x = i * cell_size
            base_y = j * cell_size

            # Randomly shift the cell within the allowable range
            shift_x = random.uniform(-shift_amount, shift_amount)
            shift_y = random.uniform(-shift_amount, shift_amount)

            # Determine the height of the block based on a random variation
            height = cell_size + random.uniform(0, height_variation)

            # Create a box representing the cell with a potential height variation
            corner1 = rg.Point3d(base_x + shift_x, base_y + shift_y, 0)
            corner2 = rg.Point3d(base_x + shift_x + cell_size, base_y + shift_y + cell_size, height)
            box = rg.Box(rg.BoundingBox(corner1, corner2))
            brep = box.ToBrep()

            breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(grid_size=6, shift_amount=3, cell_size=5, height_variation=2, random_seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(grid_size=4, shift_amount=1.5, cell_size=3, height_variation=4, random_seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(grid_size=7, shift_amount=2.5, cell_size=6, height_variation=5, random_seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(grid_size=3, shift_amount=4, cell_size=2, height_variation=1, random_seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(grid_size=5, shift_amount=2.5, cell_size=4, height_variation=3, random_seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
