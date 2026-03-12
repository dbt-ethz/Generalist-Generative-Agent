# Created for 0007_0003_rippled_grid.json

""" Summary:
The provided function generates an architectural concept model based on the "rippled grid" metaphor by creating a series of layered surfaces that undulate across a structured grid. It defines a grid size, plane distance, ripple amplitude, and frequency, allowing the model to reflect dynamic movement and fluidity. By employing mathematical sine functions, it calculates height offsets for each grid cell, creating a rhythmic ripple effect while maintaining the underlying grid structure. The resulting 3D geometries embody the interplay between order and fluidity, showcasing the concept's dynamic spatial qualities and enhancing the architectural narrative of movement and flow."""

#! python 3
function_code = """def create_rippled_grid_concept_model(grid_size, plane_distance, ripple_amplitude, ripple_frequency, random_seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'rippled grid' metaphor.
    
    Parameters:
    - grid_size (tuple): A tuple of two integers representing the number of grid cells (rows, columns).
    - plane_distance (float): The distance between each layer of planes in meters.
    - ripple_amplitude (float): The amplitude of the ripples in meters.
    - ripple_frequency (float): The frequency of the ripples.
    - random_seed (int): A seed for the random number generator to ensure replicable results.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    # Set the random seed
    random.seed(random_seed)
    
    # Initialize list for breps
    breps = []
    
    # Define the grid
    rows, cols = grid_size
    cell_size = 5.0  # Each cell is 5 meters wide for simplicity
    
    # Generate layered planes with ripple effect
    for layer in range(-2, 3):  # Create 5 layers for complexity
        for i in range(rows + 1):
            for j in range(cols + 1):
                # Calculate the height offset using a sine wave for the ripple effect
                height_offset = ripple_amplitude * math.sin(ripple_frequency * math.sqrt(i ** 2 + j ** 2) + layer)
                
                # Create points for the grid cell
                pt1 = rg.Point3d(i * cell_size, j * cell_size, layer * plane_distance + height_offset)
                pt2 = rg.Point3d((i + 1) * cell_size, j * cell_size, layer * plane_distance + height_offset)
                pt3 = rg.Point3d((i + 1) * cell_size, (j + 1) * cell_size, layer * plane_distance + height_offset)
                pt4 = rg.Point3d(i * cell_size, (j + 1) * cell_size, layer * plane_distance + height_offset)
                
                # Create a surface from the points
                corners = [pt1, pt2, pt3, pt4, pt1]
                polyline = rg.Polyline(corners)
                surface = rg.Brep.CreateFromCornerPoints(polyline[0], polyline[1], polyline[2], polyline[3], 0.01)
                
                if surface:
                    breps.append(surface)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_rippled_grid_concept_model((10, 10), 3.0, 0.5, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_rippled_grid_concept_model((5, 8), 2.0, 0.3, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_rippled_grid_concept_model((15, 15), 4.0, 0.7, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_rippled_grid_concept_model((7, 12), 2.5, 0.4, 1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_rippled_grid_concept_model((8, 10), 2.0, 0.6, 0.9)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
