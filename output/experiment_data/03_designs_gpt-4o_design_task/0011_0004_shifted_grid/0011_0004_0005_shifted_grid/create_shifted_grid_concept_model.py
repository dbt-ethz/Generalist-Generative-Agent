# Created for 0011_0004_shifted_grid.json

""" Summary:
The function `create_shifted_grid_concept_model` generates an architectural concept model by implementing the "Shifted Grid" metaphor. It starts with a conventional grid, then applies strategic shifts and rotations to create dynamic, non-linear spatial configurations. The function constructs multiple layers of interconnected 3D volumes, resulting in a playful silhouette with diverse angles and projections. By emphasizing fluid circulation paths and varying scales of space, it fosters adaptability and encourages exploration. Additionally, the model incorporates elements that manipulate light and shadow, enhancing the sense of movement and discovery, aligning with the metaphor's core traits of fluidity and innovation."""

#! python 3
function_code = """def create_shifted_grid_concept_model(base_grid_size, shift_amount, rotation_angle, grid_layers, height_per_layer):
    \"""
    Creates an architectural Concept Model based on the "Shifted Grid" metaphor.
    
    This function generates a series of interconnected 3D volumes based on a shifted and rotated grid system.
    The model features dynamic angles and projections, emphasizing a playful and intricate silhouette with 
    non-linear circulation paths and varying spaces. It focuses on the interaction of light and shadow and 
    allows for adaptability by creating reconfigurable spaces.

    Parameters:
    - base_grid_size (float): The size of the base grid cells in meters.
    - shift_amount (float): The amount by which each subsequent layer of the grid shifts, in meters.
    - rotation_angle (float): The angle by which each layer is rotated in degrees.
    - grid_layers (int): The number of vertical grid layers to create.
    - height_per_layer (float): The height of each grid layer in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import math
    
    # Seed for randomness to ensure replicability
    import random
    random.seed(42)
    
    geometries = []

    # Base grid points
    base_points = []
    for x in range(4):
        for y in range(4):
            base_points.append(rg.Point3d(x * base_grid_size, y * base_grid_size, 0))
    
    # Create layers with shifts and rotations
    for layer in range(grid_layers):
        # Calculate shift and rotation for the current layer
        shift_vector = rg.Vector3d(shift_amount * layer, shift_amount * layer, 0)
        rotation = rg.Transform.Rotation(math.radians(rotation_angle * layer), rg.Point3d.Origin)
        
        # Create grid for current layer
        for pt in base_points:
            # Shift and rotate the point
            shifted_pt = pt + shift_vector
            shifted_pt.Transform(rotation)
            
            # Define a box at this point
            box_corners = [rg.Point3d(shifted_pt.X + dx * base_grid_size, shifted_pt.Y + dy * base_grid_size, layer * height_per_layer)
                           for dx in (0, 1) for dy in (0, 1)]
            box = rg.Brep.CreateFromBox(box_corners)
            
            if box is not None:
                geometries.append(box)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(5.0, 2.0, 30, 3, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(4.0, 1.5, 45, 5, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(6.0, 3.0, 60, 4, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(7.0, 2.5, 15, 6, 3.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(8.0, 1.0, 90, 2, 5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
