# Created for 0011_0003_shifted_grid.json

""" Summary:
The provided function generates an architectural concept model inspired by the 'Shifted Grid' metaphor. Initially, it creates a conventional grid of boxes. Each box can be randomly shifted and rotated, introducing dynamic variations that break away from traditional orthogonal layouts. This results in a model characterized by misaligned volumes, varied angles, and unique intersections, enhancing spatial experiences. The function allows for adaptability by enabling different configurations, promoting fluid circulation paths and playful interactions with light and shadow. Ultimately, it produces a complex, layered silhouette that embodies movement and flexibility, inviting exploration within the design."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size=5, grid_spacing=4.0, shift_factor=0.5, rotation_angle=15):
    \"""
    Creates an architectural Concept Model based on the 'Shifted Grid' metaphor. This function generates a grid of 
    volumes and strategically shifts and rotates selected elements to create a dynamic and non-linear arrangement 
    of spaces. The resulting model emphasizes adaptability, unique spatial experiences, and interaction with light 
    and shadow.

    Parameters:
    grid_size (int): The number of grid elements in each direction (x and y).
    grid_spacing (float): The distance between grid elements in meters.
    shift_factor (float): The factor by which elements are shifted from the grid.
    rotation_angle (float): The angle in degrees by which elements are rotated.

    Returns:
    list: A list of RhinoCommon.Brep objects representing the 3D geometries of the model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set a random seed for reproducibility
    random.seed(42)

    # List to store the resulting Breps
    breps = []

    # Create a base grid of boxes
    for i in range(grid_size):
        for j in range(grid_size):
            # Calculate the base position of the box
            base_x = i * grid_spacing
            base_y = j * grid_spacing
            base_z = 0

            # Create a box at the grid position
            base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(base_x, base_x + grid_spacing),
                              rg.Interval(base_y, base_y + grid_spacing), rg.Interval(base_z, grid_spacing))

            # Randomly decide if this box should be shifted or rotated
            should_shift = random.choice([True, False])
            should_rotate = random.choice([True, False])

            # Apply a shift
            if should_shift:
                shift_x = random.uniform(-shift_factor, shift_factor) * grid_spacing
                shift_y = random.uniform(-shift_factor, shift_factor) * grid_spacing
                base_box.Transform(rg.Transform.Translation(shift_x, shift_y, 0))

            # Apply a rotation
            if should_rotate:
                angle_rad = math.radians(random.uniform(-rotation_angle, rotation_angle))
                rotation_center = base_box.Center
                rotation_axis = rg.Vector3d(0, 0, 1)  # Rotate around Z-axis
                rotation_transform = rg.Transform.Rotation(angle_rad, rotation_axis, rotation_center)
                base_box.Transform(rotation_transform)

            # Convert the box to a Brep and add to the list
            brep = base_box.ToBrep()
            breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(grid_size=7, grid_spacing=3.0, shift_factor=0.6, rotation_angle=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(grid_size=4, grid_spacing=5.0, shift_factor=0.4, rotation_angle=45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(grid_size=6, grid_spacing=2.5, shift_factor=0.3, rotation_angle=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(grid_size=5, grid_spacing=6.0, shift_factor=0.2, rotation_angle=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(grid_size=8, grid_spacing=2.0, shift_factor=0.7, rotation_angle=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
