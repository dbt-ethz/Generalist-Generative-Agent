# Created for 0011_0005_shifted_grid.json

""" Summary:
The provided function generates an architectural concept model based on the "Shifted Grid" metaphor by systematically altering a standard grid framework. It creates a dynamic form by applying shifts and rotations to grid cells, resulting in staggered and misaligned volumes that evoke movement and fluidity. Each cell's position is adjusted using defined shift distances and random rotations, fostering unexpected intersections and creating diverse spatial arrangements. This approach not only enhances visual complexity and interaction with light and shadow but also ensures adaptability in the design, allowing spaces to serve multiple functions while inviting exploration and discovery."""

#! python 3
function_code = """def create_shifted_grid_concept_alternative(grid_dim=5, base_cell_size=4, shift_distance=2, rotation_max=20):
    \"""
    Generates an architectural Concept Model based on the 'Shifted Grid' metaphor using an alternative approach.

    This function begins with a grid of base cells and applies systematic shifts and rotations to create a dynamic
    and interactive form. The result is a structure with staggered and rotated volumes that reflect movement and fluidity.

    Parameters:
    - grid_dim (int): Number of cells per side of the grid (e.g., 5 means a 5x5 grid).
    - base_cell_size (float): The size of each grid cell in meters.
    - shift_distance (float): Maximum distance each cell can be shifted in meters.
    - rotation_max (float): Maximum rotation angle for each cell in degrees.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set a seed for random generation for consistent results
    random.seed(42)

    # List to collect the resulting geometries
    geometries = []

    # Create the grid and apply shifts and rotations
    for i in range(grid_dim):
        for j in range(grid_dim):
            # Base position for each cell
            x = i * base_cell_size
            y = j * base_cell_size

            # Calculate shifts
            shift_x = (i % 2) * shift_distance - shift_distance / 2
            shift_y = (j % 2) * shift_distance - shift_distance / 2

            # Apply shifts
            x_shifted = x + shift_x
            y_shifted = y + shift_y

            # Define the base box
            box = rg.Box(
                rg.Plane.WorldXY,
                rg.Interval(x_shifted, x_shifted + base_cell_size),
                rg.Interval(y_shifted, y_shifted + base_cell_size),
                rg.Interval(0, base_cell_size)
            )

            # Rotate the box around its center
            center = box.Center
            rotation_rad = math.radians(random.uniform(-rotation_max, rotation_max))
            rotation_axis = rg.Vector3d(0, 0, 1)  # Rotate around the Z-axis
            rotation_transform = rg.Transform.Rotation(rotation_rad, rotation_axis, center)
            box.Transform(rotation_transform)

            # Convert the box to a Brep and add to the list
            brep = box.ToBrep()
            geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_alternative(grid_dim=6, base_cell_size=3, shift_distance=1.5, rotation_max=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_alternative(grid_dim=4, base_cell_size=5, shift_distance=3, rotation_max=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_alternative(grid_dim=8, base_cell_size=2, shift_distance=2.5, rotation_max=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_alternative(grid_dim=7, base_cell_size=6, shift_distance=4, rotation_max=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_alternative(grid_dim=3, base_cell_size=7, shift_distance=2, rotation_max=12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
