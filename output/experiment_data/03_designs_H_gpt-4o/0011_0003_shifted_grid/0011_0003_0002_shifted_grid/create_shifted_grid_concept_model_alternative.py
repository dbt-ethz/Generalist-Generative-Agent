# Created for 0011_0003_shifted_grid.json

""" Summary:
The function `create_shifted_grid_concept_model_alternative` generates an architectural concept model inspired by the "Shifted Grid" metaphor by manipulating a base grid structure. It begins with a conventional grid and introduces dynamic shifts and rotations to individual grid elements, resulting in a non-linear arrangement. This approach creates unexpected intersections and layered volumes, enhancing spatial complexity. The model emphasizes varied circulation paths and adapts to different functions, fostering interaction with light and shadow. Ultimately, the generated geometries reflect the metaphor's essence, showcasing fluidity and adaptability within the architectural design."""

#! python 3
function_code = """def create_shifted_grid_concept_model_alternative(base_length=25.0, base_width=15.0, height=3.0, grid_size=5.0, max_shift=1.5, max_rotation=10.0):
    \"""
    Create an architectural Concept Model using the 'Shifted Grid' metaphor with an alternative approach.
    
    This function generates a grid-based structure, applies strategic shifts and rotations to select elements, 
    and emphasizes dynamic reconfiguration with intersecting and overlapping planes. The model focuses on creating 
    varied circulation paths and distinct spatial zones, enhancing adaptability and interaction with light and shadow.
    
    Parameters:
    - base_length (float): The total length of the base grid in meters.
    - base_width (float): The total width of the base grid in meters.
    - height (float): The height of the architectural volumes in meters.
    - grid_size (float): The size of each grid cell in meters.
    - max_shift (float): The maximum shift distance for grid elements in meters.
    - max_rotation (float): The maximum rotation angle for grid elements in degrees.
    
    Returns:
    list: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set a random seed for reproducibility
    random.seed(42)

    # List to store the resulting geometries
    geometries = []

    # Calculate the number of grid elements
    num_x = int(base_length // grid_size)
    num_y = int(base_width // grid_size)

    # Create the base grid with strategic shifts and rotations
    for i in range(num_x):
        for j in range(num_y):
            # Base position of each grid cell
            x = i * grid_size
            y = j * grid_size
            z = 0

            # Create a basic rectangular box for each grid cell
            base_box = rg.Box(
                rg.Plane.WorldXY,
                rg.Interval(x, x + grid_size),
                rg.Interval(y, y + grid_size),
                rg.Interval(z, height)
            )

            # Determine if this box should be shifted or rotated
            apply_shift = random.choice([True, False])
            apply_rotation = random.choice([True, False])
            
            # Apply a shift
            if apply_shift:
                shift_x = random.uniform(-max_shift, max_shift)
                shift_y = random.uniform(-max_shift, max_shift)
                base_box.Transform(rg.Transform.Translation(shift_x, shift_y, 0))

            # Apply a rotation
            if apply_rotation:
                angle_rad = math.radians(random.uniform(-max_rotation, max_rotation))
                rotation_center = base_box.Center
                rotation_axis = rg.Vector3d(0, 0, 1)  # Rotate around Z-axis
                rotation_transform = rg.Transform.Rotation(angle_rad, rotation_axis, rotation_center)
                base_box.Transform(rotation_transform)

            # Convert the box to a Brep and add to the list
            brep = base_box.ToBrep()
            geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model_alternative(base_length=30.0, base_width=20.0, height=4.0, grid_size=6.0, max_shift=2.0, max_rotation=15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model_alternative(base_length=40.0, base_width=25.0, height=5.0, grid_size=7.0, max_shift=1.0, max_rotation=5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model_alternative(base_length=50.0, base_width=35.0, height=6.0, grid_size=8.0, max_shift=3.0, max_rotation=20.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model_alternative(base_length=35.0, base_width=18.0, height=4.5, grid_size=5.5, max_shift=2.5, max_rotation=12.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model_alternative(base_length=28.0, base_width=18.0, height=3.5, grid_size=4.0, max_shift=1.0, max_rotation=8.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
