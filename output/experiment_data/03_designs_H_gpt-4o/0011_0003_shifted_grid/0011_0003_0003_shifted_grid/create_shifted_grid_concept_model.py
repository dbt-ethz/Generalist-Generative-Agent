# Created for 0011_0003_shifted_grid.json

""" Summary:
The provided function, `create_shifted_grid_concept_model`, generates an architectural concept model inspired by the 'Shifted Grid' metaphor. It begins with a conventional grid layout, creating a base of 3D boxes. Each box is then randomly shifted and rotated to break the orthogonal uniformity, embodying the metaphor's essence of dynamic reconfiguration. This results in varied volumes that intersect and overlap, promoting unique spatial experiences and circulation paths. The model highlights adaptability through its adjustable components, allowing for different configurations. Additionally, the manipulation of angles enhances interactions with light and shadow, enriching the occupant's journey through the space."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_rows=4, grid_cols=4, base_length=4.0, base_width=4.0, height_variation=2.0):
    \"""
    Creates an architectural Concept Model based on the 'Shifted Grid' metaphor. 
    This function generates a grid of volumes and applies strategic shifts and rotations 
    to create dynamic and non-linear spatial arrangements. The model emphasizes 
    adaptability, unique spatial experiences, and interaction with light and shadow.

    Parameters:
    grid_rows (int): The number of rows in the grid.
    grid_cols (int): The number of columns in the grid.
    base_length (float): The base length of each grid cell in meters.
    base_width (float): The base width of each grid cell in meters.
    height_variation (float): The maximum variation in height for each grid element in meters.

    Returns:
    list: A list of RhinoCommon.Brep objects representing the 3D geometries of the model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set random seed for reproducibility
    random.seed(42)

    # List to store the resulting Breps
    breps = []

    # Create a base grid of boxes
    for i in range(grid_rows):
        for j in range(grid_cols):
            # Calculate the base position of the box
            base_x = i * base_length
            base_y = j * base_width

            # Determine the height with some variation
            height = base_length + random.uniform(-height_variation, height_variation)

            # Create a box at the grid position
            corners = [rg.Point3d(base_x, base_y, 0),
                       rg.Point3d(base_x + base_length, base_y, 0),
                       rg.Point3d(base_x + base_length, base_y + base_width, 0),
                       rg.Point3d(base_x, base_y + base_width, 0),
                       rg.Point3d(base_x, base_y, height),
                       rg.Point3d(base_x + base_length, base_y, height),
                       rg.Point3d(base_x + base_length, base_y + base_width, height),
                       rg.Point3d(base_x, base_y + base_width, height)]
            box = rg.Brep.CreateFromBox(corners)

            # Randomly apply a shift and rotation
            shift_x = random.uniform(-0.5, 0.5) * base_length
            shift_y = random.uniform(-0.5, 0.5) * base_width
            box.Transform(rg.Transform.Translation(shift_x, shift_y, 0))

            # Apply a small rotation around the center
            rotation_center = rg.Point3d(base_x + base_length / 2, base_y + base_width / 2, height / 2)
            rotation_angle = random.uniform(-10, 10)
            rotation_transform = rg.Transform.Rotation(math.radians(rotation_angle), rg.Vector3d(0, 0, 1), rotation_center)
            box.Transform(rotation_transform)

            # Add the box to the list of geometries
            breps.append(box)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(grid_rows=5, grid_cols=5, base_length=3.0, base_width=3.0, height_variation=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(grid_rows=6, grid_cols=4, base_length=5.0, base_width=2.0, height_variation=3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(grid_rows=3, grid_cols=3, base_length=2.0, base_width=2.0, height_variation=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(grid_rows=4, grid_cols=6, base_length=4.5, base_width=4.5, height_variation=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(grid_rows=7, grid_cols=7, base_length=2.5, base_width=2.5, height_variation=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
