# Created for 0011_0005_shifted_grid.json

""" Summary:
The function `generate_shifted_grid_model` creates an architectural concept model based on the "Shifted Grid" metaphor by manipulating a standard grid framework. It introduces dynamic shifts and rotations to grid cells, resulting in staggered volumes that embody movement and fluidity. The function emphasizes non-linear spatial arrangements, which facilitate varied circulation paths and unique spatial experiences. Additionally, it considers the interaction of light and shadow through the misaligned elements, enhancing the model's visual complexity. Overall, this approach fosters adaptability in design, allowing spaces to transform for diverse functions while inviting exploration and discovery."""

#! python 3
function_code = """def generate_shifted_grid_model(width, depth, height, grid_size, max_shift, max_rotation, level_count):
    \"""
    Generates a 3D architectural Concept Model based on the 'Shifted Grid' metaphor.

    This function creates a dynamic structure by transforming a standard grid framework
    through shifts, rotations, and misalignments to embody movement and fluidity. It results
    in staggered volumes and intersecting planes, emphasizing non-linear spatial arrangements
    and creating varied light and shadow interactions.

    Parameters:
    - width (float): The overall width of the grid in meters.
    - depth (float): The overall depth of the grid in meters.
    - height (float): The overall height of the grid in meters.
    - grid_size (float): The size of each grid cell in meters.
    - max_shift (float): The maximum shift distance in meters for grid points.
    - max_rotation (float): The maximum rotation angle in degrees for grid elements.
    - level_count (int): The number of vertical levels in the model.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the generated 3D geometries.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Ensure replicable randomness
    random.seed(42)
    
    geometries = []

    # Calculate the number of cells in each dimension
    x_cells = int(width / grid_size)
    y_cells = int(depth / grid_size)

    # Loop through each level
    for level in range(level_count):
        for i in range(x_cells):
            for j in range(y_cells):
                # Base position for the current cell
                base_x = i * grid_size
                base_y = j * grid_size
                base_z = level * height / level_count

                # Apply random shift to the base position
                shift_x = random.uniform(-max_shift, max_shift)
                shift_y = random.uniform(-max_shift, max_shift)
                shifted_point = rg.Point3d(base_x + shift_x, base_y + shift_y, base_z)

                # Create a base box geometry
                box = rg.Box(
                    rg.Plane(shifted_point, rg.Vector3d.ZAxis),
                    rg.Interval(0, grid_size),
                    rg.Interval(0, grid_size),
                    rg.Interval(0, height / level_count)
                )

                # Convert box to Brep for further manipulation
                brep_box = box.ToBrep()

                # Apply random rotation
                if random.random() > 0.5:
                    center = box.Center
                    rotation_axis = rg.Vector3d(0, 0, 1)  # Rotate around Z-axis
                    angle_rad = math.radians(random.uniform(-max_rotation, max_rotation))
                    rotation_transform = rg.Transform.Rotation(angle_rad, rotation_axis, center)
                    brep_box.Transform(rotation_transform)

                # Add the transformed box to the list of geometries
                geometries.append(brep_box)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_shifted_grid_model(10.0, 15.0, 20.0, 2.0, 1.0, 30.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_shifted_grid_model(12.0, 18.0, 25.0, 3.0, 0.5, 45.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_shifted_grid_model(8.0, 10.0, 15.0, 1.5, 0.8, 60.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_shifted_grid_model(15.0, 20.0, 30.0, 2.5, 1.5, 90.0, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_shifted_grid_model(14.0, 22.0, 18.0, 2.0, 2.0, 15.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
