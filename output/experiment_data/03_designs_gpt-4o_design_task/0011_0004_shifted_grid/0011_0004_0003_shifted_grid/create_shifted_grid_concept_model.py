# Created for 0011_0004_shifted_grid.json

""" Summary:
The function `create_shifted_grid_concept_model` translates the 'Shifted Grid' metaphor into an architectural concept model by manipulating a conventional grid framework. It uses parameters like grid size, shifts, rotations, and height variations to create dynamic, non-orthogonal structures. Each cell in the grid is adjusted with strategic shifts and rotations, resulting in varied angles and projections that generate a playful silhouette. The model emphasizes fluid circulation through interconnected spaces, enhancing the experience of light and shadow. This approach fosters adaptability, allowing for reconfigurable spaces that promote exploration and discovery within the architectural form."""

#! python 3
function_code = """def create_shifted_grid_concept_model(base_grid_size=3, grid_shift=1.5, grid_rotation=15, height_variation=0.5, levels=3):
    \"""
    Creates an architectural Concept Model based on the 'Shifted Grid' metaphor. The model features a dynamic silhouette
    with varied angles and projections, interconnected spaces, and intricate light and shadow interactions.

    Parameters:
        base_grid_size (float): The base size of the grid cells in meters.
        grid_shift (float): The amount by which the grid is shifted from its original alignment in meters.
        grid_rotation (float): The angle by which the grid is rotated in degrees.
        height_variation (float): The variation in height for different levels in meters.
        levels (int): The number of levels in the building.

    Returns:
        list: A list of 3D Brep geometries representing the architectural concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    random.seed(42)  # Ensure replicable results

    geometries = []
    base_grid_cells = 5  # Number of cells in the base grid

    for level in range(levels):
        level_height = level * height_variation
        for i in range(base_grid_cells):
            for j in range(base_grid_cells):
                # Create a base grid cell
                base_center = rg.Point3d(i * base_grid_size, j * base_grid_size, level_height)
                
                # Apply shifts and rotations
                shift_x = (i % 2) * grid_shift
                shift_y = (j % 2) * grid_shift
                rotation = rg.Transform.Rotation(
                    math.radians(grid_rotation * (random.random() - 0.5)), 
                    rg.Vector3d.ZAxis,
                    rg.Point3d(i * base_grid_size + shift_x, j * base_grid_size + shift_y, level_height)
                )
                
                # Create a box for each grid cell with a shifted and rotated center
                box_corners = [
                    rg.Point3d(base_center.X + shift_x - base_grid_size / 2, base_center.Y + shift_y - base_grid_size / 2, level_height),
                    rg.Point3d(base_center.X + shift_x + base_grid_size / 2, base_center.Y + shift_y - base_grid_size / 2, level_height),
                    rg.Point3d(base_center.X + shift_x + base_grid_size / 2, base_center.Y + shift_y + base_grid_size / 2, level_height + height_variation),
                    rg.Point3d(base_center.X + shift_x - base_grid_size / 2, base_center.Y + shift_y + base_grid_size / 2, level_height + height_variation)
                ]
                
                # Create a brep from box corners
                box = rg.Brep.CreateFromCornerPoints(box_corners[0], box_corners[1], box_corners[2], box_corners[3], 0.01)
                if box:
                    box.Transform(rotation)                
                    geometries.append(box)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(base_grid_size=4, grid_shift=2, grid_rotation=30, height_variation=1, levels=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(base_grid_size=2, grid_shift=1, grid_rotation=45, height_variation=0.3, levels=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(base_grid_size=5, grid_shift=2.5, grid_rotation=10, height_variation=0.7, levels=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(base_grid_size=3, grid_shift=1, grid_rotation=60, height_variation=0.4, levels=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(base_grid_size=6, grid_shift=3, grid_rotation=20, height_variation=0.8, levels=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
