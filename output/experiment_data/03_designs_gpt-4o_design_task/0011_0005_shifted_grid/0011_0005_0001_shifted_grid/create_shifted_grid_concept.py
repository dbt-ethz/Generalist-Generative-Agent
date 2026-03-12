# Created for 0011_0005_shifted_grid.json

""" Summary:
The function `create_shifted_grid_concept` generates an architectural concept model based on the 'Shifted Grid' metaphor by manipulating a standard grid framework. It creates a series of staggered, skewed, and rotated volumes to embody movement and fluidity. Each grid cell undergoes random shifts and optional rotations, resulting in dynamic forms that reflect the metaphor's essence. The function emphasizes innovative spatial arrangements, encouraging varied circulation paths and unique experiences. Additionally, it captures light and shadow interactions through these misalignments, fostering adaptability and discovery within the structure. The output is a collection of Breps representing the transformed architectural model."""

#! python 3
function_code = """def create_shifted_grid_concept(width, depth, height, grid_size, shift_factor, rotation_angle):
    \"""
    Create an architectural Concept Model based on the 'Shifted Grid' metaphor.
    
    This function generates a structure with staggered, skewed, and rotated volumes
    to represent the dynamic and interactive form described by the metaphor. It 
    begins with a standard grid framework and applies shifts, rotations, and misalignments
    to create a sense of movement and fluidity in the model.

    Parameters:
    - width (float): The overall width of the building in meters.
    - depth (float): The overall depth of the building in meters.
    - height (float): The overall height of the building in meters.
    - grid_size (float): The size of the grid cells in meters.
    - shift_factor (float): The maximum shift distance for the grid points in meters.
    - rotation_angle (float): The maximum rotation angle in degrees for grid elements.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the generated volumes.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set seed for reproducibility in randomness
    random.seed(42)

    # Create a list to hold the resulting geometries
    geometries = []

    # Calculate the number of cells in each dimension
    x_cells = int(width / grid_size)
    y_cells = int(depth / grid_size)
    z_cells = int(height / grid_size)

    # Loop through the grid cells
    for i in range(x_cells):
        for j in range(y_cells):
            for k in range(z_cells):
                # Base point for the current cell
                base_point = rg.Point3d(i * grid_size, j * grid_size, k * grid_size)

                # Apply a random shift to the base point
                shift_x = random.uniform(-shift_factor, shift_factor)
                shift_y = random.uniform(-shift_factor, shift_factor)
                shift_z = random.uniform(-shift_factor, shift_factor)
                shifted_point = rg.Point3d(base_point.X + shift_x, base_point.Y + shift_y, base_point.Z + shift_z)

                # Create a box at the shifted point
                box_corner1 = shifted_point
                box_corner2 = rg.Point3d(shifted_point.X + grid_size, shifted_point.Y + grid_size, shifted_point.Z + grid_size)
                box = rg.Box(rg.BoundingBox(box_corner1, box_corner2))

                # Randomly decide if the box should be rotated
                if random.random() > 0.5:
                    # Find the center of the box
                    center = box.Center
                    # Define a vertical axis for rotation
                    axis = rg.Line(center, rg.Point3d(center.X, center.Y, center.Z + 1)).Direction
                    # Create a rotation transform
                    angle_rad = math.radians(random.uniform(-rotation_angle, rotation_angle))
                    rotation = rg.Transform.Rotation(angle_rad, axis, center)
                    # Apply the rotation to the box
                    box.Transform(rotation)

                # Add the box to the list of geometries
                geometries.append(box.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept(20.0, 30.0, 10.0, 2.0, 1.0, 45.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept(15.0, 25.0, 12.0, 3.0, 0.5, 30.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept(25.0, 35.0, 15.0, 2.5, 2.0, 60.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept(18.0, 22.0, 14.0, 4.0, 1.5, 90.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept(10.0, 15.0, 8.0, 1.0, 0.8, 75.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
