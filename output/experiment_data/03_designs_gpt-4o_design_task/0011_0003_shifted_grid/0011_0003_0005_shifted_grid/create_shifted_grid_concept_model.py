# Created for 0011_0003_shifted_grid.json

""" Summary:
The function `create_shifted_grid_concept_model` generates an architectural concept model inspired by the "Shifted Grid" metaphor. It begins with a conventional grid framework and introduces dynamic alterations through random shifts and rotations of grid elements. This creates a structure characterized by misaligned volumes, enabling unexpected intersections and varied silhouettes. The resulting model emphasizes fluidity and adaptability, with interwoven spaces fostering unique circulation paths and diverse experiences. By manipulating light and shadow through angled surfaces, the model embodies a sense of movement and discovery, aligning with the metaphor's core traits of flexibility and innovative spatial arrangements."""

#! python 3
function_code = """def create_shifted_grid_concept_model(base_size, grid_spacing, shift_amount, rotation_angle):
    \"""
    Creates an architectural Concept Model based on the 'Shifted Grid' metaphor. This model starts with a conventional
    grid structure and applies strategic shifts and rotations to selected elements, emphasizing dynamic reconfiguration
    through intersecting and overlapping planes.

    Parameters:
    - base_size (float): The size of the base grid structure in meters.
    - grid_spacing (float): The spacing between the grid lines in meters.
    - shift_amount (float): The maximum distance to shift grid elements in meters.
    - rotation_angle (float): The maximum angle in degrees to rotate grid elements.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the concept model.
    \"""
    import Rhino
    import random
    import math
    
    # Set random seed for reproducibility
    random.seed(42)
    
    # Create a list to hold the resulting geometries
    geometries = []
    
    # Calculate the number of grid lines based on the base size and grid spacing
    num_lines = int(base_size / grid_spacing)
    
    # Iterate over the grid positions
    for i in range(num_lines):
        for j in range(num_lines):
            # Define the grid point
            x = i * grid_spacing
            y = j * grid_spacing
            
            # Randomly decide whether to shift or rotate this grid point
            if random.choice([True, False]):
                # Apply shift
                shift_x = random.uniform(-shift_amount, shift_amount)
                shift_y = random.uniform(-shift_amount, shift_amount)
            else:
                shift_x = 0
                shift_y = 0
            
            # Apply rotation
            angle = random.uniform(-rotation_angle, rotation_angle)
            rotation_rad = math.radians(angle)
            
            # Define the base plane at the grid point
            plane = Rhino.Geometry.Plane(Rhino.Geometry.Point3d(x + shift_x, y + shift_y, 0), Rhino.Geometry.Vector3d.ZAxis)
            plane.Rotate(rotation_rad, Rhino.Geometry.Vector3d.ZAxis)
            
            # Create a rectangular surface at the grid point
            rect = Rhino.Geometry.Rectangle3d(plane, grid_spacing, grid_spacing)
            brep = Rhino.Geometry.Brep.CreateFromCornerPoints(rect.Corner(0), rect.Corner(1), rect.Corner(2), rect.Corner(3), 0.01)
            
            # Add the Brep to the geometries list
            if brep:
                geometries.append(brep)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(10.0, 1.0, 0.5, 30.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(15.0, 2.0, 1.0, 45.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(20.0, 0.5, 0.2, 60.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(12.0, 1.5, 0.75, 15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(25.0, 2.5, 1.5, 90.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
