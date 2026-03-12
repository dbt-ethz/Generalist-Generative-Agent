# Created for 0011_0003_shifted_grid.json

""" Summary:
The provided function generates an architectural concept model based on the "Shifted Grid" metaphor by creating a grid structure and introducing strategic shifts and rotations to its elements. It initiates with a conventional grid, where each cell is represented as a box. Through random transformations, boxes are shifted and rotated, resulting in a dynamic arrangement that deviates from traditional layouts. This process creates intersecting and overlapping planes, fostering varied circulation paths and unique spatial experiences. The model emphasizes adaptability, allowing reconfiguration of spaces to accommodate diverse functions, while also enhancing interactions with light and shadow, promoting exploration."""

#! python 3
function_code = """def create_shifted_grid_concept_model(base_length=30.0, base_width=20.0, base_height=10.0, grid_size=5.0, shift_amount=2.0, rotation_angle=15.0):
    \"""
    Create an architectural Concept Model using the 'Shifted Grid' metaphor.
    
    This function generates a grid-based structure and applies shifts and rotations to select elements, 
    resulting in a dynamic and fluid arrangement of spaces and volumes. The model emphasizes intersecting 
    and overlapping planes, creating varied circulation paths and zones with unique purposes.
    
    Inputs:
    - base_length: The length of the base grid in meters.
    - base_width: The width of the base grid in meters.
    - base_height: The height of the structure in meters.
    - grid_size: The size of each grid cell in meters.
    - shift_amount: The amount by which grid elements are shifted in meters.
    - rotation_angle: The angle in degrees by which grid elements are rotated.
    
    Outputs:
    - A list of 3D brep geometries representing the concept model.
    \"""

    import Rhino.Geometry as rg
    import math
    import random
    random.seed(42)

    geometries = []

    # Create the base grid
    num_x = int(base_length // grid_size)
    num_y = int(base_width // grid_size)

    for i in range(num_x):
        for j in range(num_y):
            # Determine the base position of each grid cell
            x = i * grid_size
            y = j * grid_size
            z = 0

            # Create a basic box for each grid cell
            box_corners = [
                rg.Point3d(x, y, z),
                rg.Point3d(x + grid_size, y, z),
                rg.Point3d(x + grid_size, y + grid_size, z),
                rg.Point3d(x, y + grid_size, z),
                rg.Point3d(x, y, z + base_height),
                rg.Point3d(x + grid_size, y, z + base_height),
                rg.Point3d(x + grid_size, y + grid_size, z + base_height),
                rg.Point3d(x, y + grid_size, z + base_height)
            ]

            box = rg.Brep.CreateFromBox(box_corners)
            
            # Randomly apply shift and rotation
            if random.random() > 0.5:
                shift_vector = rg.Vector3d(random.choice([shift_amount, -shift_amount]), 
                                           random.choice([shift_amount, -shift_amount]), 0)
                transformation_shift = rg.Transform.Translation(shift_vector)
                box.Transform(transformation_shift)

            if random.random() > 0.5:
                center_point = rg.Point3d(x + grid_size / 2, y + grid_size / 2, z + base_height / 2)
                transformation_rotate = rg.Transform.Rotation(math.radians(random.choice([rotation_angle, -rotation_angle])), center_point)
                box.Transform(transformation_rotate)

            geometries.append(box)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(base_length=50.0, base_width=30.0, base_height=15.0, grid_size=10.0, shift_amount=3.0, rotation_angle=20.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(base_length=40.0, base_width=25.0, base_height=12.0, grid_size=6.0, shift_amount=4.0, rotation_angle=10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(base_length=60.0, base_width=40.0, base_height=20.0, grid_size=8.0, shift_amount=5.0, rotation_angle=30.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(base_length=45.0, base_width=35.0, base_height=18.0, grid_size=7.0, shift_amount=2.5, rotation_angle=25.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(base_length=55.0, base_width=32.0, base_height=17.0, grid_size=9.0, shift_amount=3.5, rotation_angle=12.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
