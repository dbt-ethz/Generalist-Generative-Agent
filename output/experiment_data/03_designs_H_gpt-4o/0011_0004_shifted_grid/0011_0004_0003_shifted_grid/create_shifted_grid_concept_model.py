# Created for 0011_0004_shifted_grid.json

""" Summary:
The provided function generates an architectural concept model based on the 'Shifted Grid' metaphor by manipulating a conventional grid structure. It starts by defining a grid of points and applies random shifts and rotations to create dynamic, irregular volumes that deviate from traditional orthogonal layouts. Each volume's height varies, contributing to an intricate silhouette. The function emphasizes non-linear circulation paths, enabling fluid movement through interconnected spaces. This approach enhances interactions with light and shadow, fostering a sense of discovery and engagement. The result is a playful architectural model that embodies the metaphor's principles of movement and adaptability."""

#! python 3
function_code = """def create_shifted_grid_concept_model(base_grid_size=6, shift_variation=1.5, rotation_variation=20, height_variation=3, layers=4):
    \"""
    Creates an architectural Concept Model based on the 'Shifted Grid' metaphor. This function generates a series of 
    interconnected, dynamically shifted, and rotated volumes, producing a playful silhouette with non-linear circulation paths.

    Parameters:
        base_grid_size (float): The base size of grid cells in meters.
        shift_variation (float): Maximum shift variation for grid cells in meters.
        rotation_variation (float): Maximum rotation angle variation for grid elements in degrees.
        height_variation (float): Height variation for each volume in meters.
        layers (int): Number of vertical layers to generate.

    Returns:
        List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometry of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    # Set random seed for replicability
    random.seed(42)
    
    geometries = []

    # Define base grid points
    grid_points = []
    grid_count = 5  # Number of grid points along one axis
    for x in range(grid_count):
        for y in range(grid_count):
            grid_points.append(rg.Point3d(x * base_grid_size, y * base_grid_size, 0))
    
    # Iterate through layers
    for layer in range(layers):
        z_offset = layer * height_variation
        
        # Create volumes based on grid points
        for pt in grid_points:
            # Apply random shift
            shift_x = random.uniform(-shift_variation, shift_variation)
            shift_y = random.uniform(-shift_variation, shift_variation)
            shifted_pt = rg.Point3d(pt.X + shift_x, pt.Y + shift_y, z_offset)
            
            # Define box corners with varied height
            box_corners = [
                shifted_pt,
                rg.Point3d(shifted_pt.X + base_grid_size, shifted_pt.Y, z_offset),
                rg.Point3d(shifted_pt.X + base_grid_size, shifted_pt.Y + base_grid_size, z_offset + random.uniform(height_variation, height_variation + 2)),
                rg.Point3d(shifted_pt.X, shifted_pt.Y + base_grid_size, z_offset + random.uniform(height_variation, height_variation + 2))
            ]
            
            box = rg.Brep.CreateFromCornerPoints(box_corners[0], box_corners[1], box_corners[2], box_corners[3], 0.01)
            if box:
                # Apply random rotation
                rotation_angle = math.radians(random.uniform(-rotation_variation, rotation_variation))
                rotation_center = rg.Point3d(shifted_pt.X + base_grid_size / 2, shifted_pt.Y + base_grid_size / 2, z_offset)
                rotation = rg.Transform.Rotation(rotation_angle, rotation_center)
                box.Transform(rotation)
                
                geometries.append(box)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(base_grid_size=10, shift_variation=2.0, rotation_variation=30, height_variation=5, layers=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(base_grid_size=8, shift_variation=1.0, rotation_variation=15, height_variation=4, layers=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(base_grid_size=12, shift_variation=2.5, rotation_variation=25, height_variation=6, layers=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(base_grid_size=7, shift_variation=1.2, rotation_variation=10, height_variation=2, layers=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(base_grid_size=9, shift_variation=1.8, rotation_variation=22, height_variation=3.5, layers=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
