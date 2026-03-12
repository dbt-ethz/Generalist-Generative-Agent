# Created for 0011_0002_shifted_grid.json

""" Summary:
The provided function, `create_shifted_grid_concept_alternative`, generates an architectural concept model based on the "Shifted Grid" metaphor. It starts with a regular grid framework and introduces random shifts and height variations to create interconnected volumes. This process results in a dynamic, fluid structure that embodies movement and unpredictability, as outlined in the metaphor. The function uses parameters like grid size, number of cells, shift intensity, and height variation to create irregular alignments and staggered layers. The resulting model showcases diverse spatial experiences, adaptability, and playful interactions with light and shadow, reflecting the essence of the design task."""

#! python 3
function_code = """def create_shifted_grid_concept_alternative(grid_size, num_cells, shift_intensity, height_variation, base_height=3.0):
    \"""
    Generates an architectural Concept Model based on the 'Shifted Grid' metaphor.

    This function creates a series of interconnected volumes by shifting a regular grid structure
    and varying the height of each volume. The model emphasizes movement and fluidity through
    staggered layers and varied orientations.

    Parameters:
    - grid_size (float): The size of each grid cell in meters.
    - num_cells (int): The number of cells along one axis of the grid.
    - shift_intensity (float): The maximum distance grid points can be shifted from their original positions.
    - height_variation (float): The maximum variation in height for each volume.
    - base_height (float): The base height of each volume in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a seed for reproducibility
    random.seed(42)

    geometries = []

    # Create the base grid with shifted and varied heights
    for i in range(num_cells):
        for j in range(num_cells):
            # Calculate the base position
            x_base = i * grid_size
            y_base = j * grid_size

            # Apply shifts to the base position
            x_shift = x_base + random.uniform(-shift_intensity, shift_intensity)
            y_shift = y_base + random.uniform(-shift_intensity, shift_intensity)

            # Determine the height variation for the current cell
            cell_height = base_height + random.uniform(-height_variation, height_variation)

            # Define the corners of the shifted volume
            corners = [
                rg.Point3d(x_shift, y_shift, 0),
                rg.Point3d(x_shift + grid_size, y_shift, 0),
                rg.Point3d(x_shift + grid_size, y_shift + grid_size, 0),
                rg.Point3d(x_shift, y_shift + grid_size, 0),
                rg.Point3d(x_shift, y_shift, cell_height),
                rg.Point3d(x_shift + grid_size, y_shift, cell_height),
                rg.Point3d(x_shift + grid_size, y_shift + grid_size, cell_height),
                rg.Point3d(x_shift, y_shift + grid_size, cell_height)
            ]

            # Create the Brep from the corners
            brep = rg.Brep.CreateFromBox(corners)
            if brep:
                geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_alternative(2.0, 5, 0.5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_alternative(1.5, 6, 0.3, 1.5, base_height=4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_alternative(3.0, 4, 0.7, 1.0, base_height=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_alternative(2.5, 3, 0.4, 1.2, base_height=5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_alternative(1.0, 8, 0.6, 3.0, base_height=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
