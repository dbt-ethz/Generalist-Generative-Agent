# Created for 0011_0003_shifted_grid.json

""" Summary:
The function `create_shifted_grid_concept_model` generates an architectural concept model based on the 'Shifted Grid' metaphor by starting with a conventional grid structure. It applies random shifts and rotations to grid elements, creating a dynamic arrangement of overlapping and intersecting planes. This process results in varied spatial configurations that promote unique circulation paths and diverse experiences. By manipulating light and shadow through angled surfaces, the model embodies fluidity and adaptability, allowing for multifunctional spaces. Ultimately, the function translates the metaphor into a tangible 3D representation that invites exploration and interaction within the architectural space."""

#! python 3
function_code = """def create_shifted_grid_concept_model(base_size=50, grid_spacing=10, shift_amount=3, rotation_angle=20):
    \"""
    Create an architectural Concept Model using the 'Shifted Grid' metaphor.

    This function generates a grid-based structure and applies strategic shifts and rotations
    to selected grid elements to create a dynamic and fluid arrangement of spaces and volumes.
    The resulting model emphasizes intersecting and overlapping planes, varied circulation paths,
    and a playful interaction with light and shadow.

    Parameters:
    - base_size (float): The overall size of the grid structure in meters.
    - grid_spacing (float): The spacing between grid lines in meters.
    - shift_amount (float): The maximum distance to shift grid elements in meters.
    - rotation_angle (float): The maximum angle in degrees to rotate grid elements.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    # Set a random seed for reproducibility
    random.seed(42)

    # List to store the resulting Breps
    breps = []

    # Calculate the number of grid lines
    num_lines = int(base_size / grid_spacing)

    # Iterate over the grid positions
    for i in range(num_lines):
        for j in range(num_lines):
            # Define the grid point with potential shift
            x = i * grid_spacing + random.uniform(-shift_amount, shift_amount)
            y = j * grid_spacing + random.uniform(-shift_amount, shift_amount)

            # Create a base box at each grid point
            base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(x, x + grid_spacing),
                              rg.Interval(y, y + grid_spacing), rg.Interval(0, grid_spacing))

            # Randomly decide to apply rotation
            if random.choice([True, False]):
                angle_rad = math.radians(random.uniform(-rotation_angle, rotation_angle))
                center = rg.Point3d(x + grid_spacing / 2, y + grid_spacing / 2, grid_spacing / 2)
                rotation_axis = rg.Vector3d(0, 0, 1)
                rotation_transform = rg.Transform.Rotation(angle_rad, rotation_axis, center)
                base_box.Transform(rotation_transform)

            # Convert the box to a Brep and add to the list
            breps.append(base_box.ToBrep())

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(base_size=100, grid_spacing=5, shift_amount=2, rotation_angle=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(base_size=75, grid_spacing=8, shift_amount=5, rotation_angle=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(base_size=60, grid_spacing=12, shift_amount=4, rotation_angle=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(base_size=90, grid_spacing=6, shift_amount=1, rotation_angle=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(base_size=80, grid_spacing=7, shift_amount=3, rotation_angle=45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
