# Created for 0011_0004_shifted_grid.json

""" Summary:
The provided function generates an architectural concept model inspired by the "Shifted Grid" metaphor. It begins with a conventional grid and applies strategic shifts and rotations to each grid cell, resulting in a dynamic and playful architectural form. By iterating through layers and modifying positions and orientations, the function creates varied volumes that enhance spatial relationships and circulation paths. The model emphasizes fluid movement and interaction with light and shadow, fostering a sense of discovery. Ultimately, the function produces a series of interconnected Breps, representing a flexible design that accommodates diverse functions and experiences within the space."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size=5, shift_amount=2, rotation_angle=15, layer_height=4, num_layers=3):
    \"""
    Creates an architectural Concept Model based on the 'Shifted Grid' metaphor. This function generates a series of 
    interconnected volumes with strategic shifts and rotations applied to a conventional grid, resulting in a dynamic 
    and fluid architectural form. It emphasizes non-linear circulation paths and the interaction of light and shadow.

    Args:
        grid_size (int): The size of the grid defining the number of divisions.
        shift_amount (float): The amount by which each grid cell is shifted.
        rotation_angle (float): The angle by which each grid cell is rotated to create a dynamic form.
        layer_height (float): The height of each layer in the model.
        num_layers (int): The number of vertical layers in the model.

    Returns:
        List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometry of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Seed for randomness to ensure replicability
    random.seed(42)

    breps = []

    # Define the base size of each grid cell
    cell_size = 10  # meters

    # Loop through the grid for each layer
    for layer in range(num_layers):
        layer_offset = layer * layer_height
        for i in range(grid_size):
            for j in range(grid_size):
                # Calculate the base position of the cell
                base_x = i * cell_size
                base_y = j * cell_size

                # Apply a shift to the base position
                shift_x = base_x + (layer * shift_amount)
                shift_y = base_y + (layer * shift_amount)

                # Create the base volume as a box
                base_box = rg.Box(
                    rg.Plane.WorldXY, 
                    rg.Interval(0, cell_size), 
                    rg.Interval(0, cell_size), 
                    rg.Interval(layer_offset, layer_offset + layer_height)
                )

                # Move the box to the shifted position
                translation = rg.Transform.Translation(shift_x, shift_y, 0)
                base_box.Transform(translation)

                # Rotate the box around its center
                rotation_center = base_box.Center
                rotation = rg.Transform.Rotation(math.radians(rotation_angle * layer), rotation_center)
                base_box.Transform(rotation)

                # Convert the box to a Brep and add to the list
                brep_box = base_box.ToBrep()
                breps.append(brep_box)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(grid_size=6, shift_amount=3, rotation_angle=20, layer_height=5, num_layers=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(grid_size=8, shift_amount=4, rotation_angle=30, layer_height=3, num_layers=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(grid_size=7, shift_amount=1.5, rotation_angle=10, layer_height=6, num_layers=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(grid_size=4, shift_amount=2.5, rotation_angle=45, layer_height=2, num_layers=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(grid_size=5, shift_amount=1, rotation_angle=25, layer_height=3, num_layers=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
