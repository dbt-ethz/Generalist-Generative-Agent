# Created for 0011_0005_shifted_grid.json

""" Summary:
The provided function generates an architectural concept model inspired by the 'Shifted Grid' metaphor by manipulating a traditional grid framework. It begins with a specified grid size, then applies random shifts, rotations, and height variations to each grid cell. This creates staggered volumes and intersecting planes that embody fluidity and movement, promoting innovative spatial arrangements. The resulting structure features diverse circulation paths and dynamic light-shadow interactions, enhancing the sense of energy and adaptability. By allowing for flexible spatial configurations, the model encourages exploration and engagement, reflecting the metaphor's core themes of transformation and discovery."""

#! python 3
function_code = """def create_dynamic_shifted_grid_model(grid_size=4, base_cell_size=5, shift_range=1.5, rotation_angle=20, height_variation=2):
    \"""
    Generate an architectural Concept Model based on the 'Shifted Grid' metaphor.
    
    This function starts with a regular grid framework and applies dynamic shifts,
    rotations, and variations in height to create a sense of movement and fluidity.
    It results in staggered volumes and intersecting planes, promoting innovative
    spatial arrangements and unique circulation paths.
    
    Parameters:
    - grid_size (int): Number of cells in one direction of the grid.
    - base_cell_size (float): Size of each grid cell in meters.
    - shift_range (float): Maximum shift distance for the grid points in meters.
    - rotation_angle (float): Maximum rotation angle in degrees for grid elements.
    - height_variation (float): Variation in height for each volume in meters.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the generated volumes.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensuring replicable randomness

    geometries = []

    for i in range(grid_size):
        for j in range(grid_size):
            # Calculate base position for each cell
            base_x = i * base_cell_size
            base_y = j * base_cell_size
            base_z = 0

            # Apply random shift
            shift_x = random.uniform(-shift_range, shift_range)
            shift_y = random.uniform(-shift_range, shift_range)
            shifted_point = rg.Point3d(base_x + shift_x, base_y + shift_y, base_z)

            # Create base plane for the box
            base_plane = rg.Plane(shifted_point, rg.Vector3d.ZAxis)

            # Randomly determine height variation
            height = base_cell_size + random.uniform(-height_variation, height_variation)
            box = rg.Box(base_plane, rg.Interval(0, base_cell_size), rg.Interval(0, base_cell_size), rg.Interval(0, height))

            # Convert box to Brep for further transformations
            brep_box = box.ToBrep()

            # Apply random rotation
            rotation_radians = math.radians(random.uniform(-rotation_angle, rotation_angle))
            rotation_axis = rg.Line(shifted_point, rg.Point3d(shifted_point.X, shifted_point.Y, shifted_point.Z + 1))
            rotation_transform = rg.Transform.Rotation(rotation_radians, rotation_axis.Direction, shifted_point)
            brep_box.Transform(rotation_transform)

            # Append to geometries list
            geometries.append(brep_box)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dynamic_shifted_grid_model(grid_size=6, base_cell_size=4, shift_range=2, rotation_angle=30, height_variation=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dynamic_shifted_grid_model(grid_size=5, base_cell_size=6, shift_range=2.5, rotation_angle=15, height_variation=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dynamic_shifted_grid_model(grid_size=3, base_cell_size=7, shift_range=1, rotation_angle=45, height_variation=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dynamic_shifted_grid_model(grid_size=7, base_cell_size=3, shift_range=2, rotation_angle=25, height_variation=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dynamic_shifted_grid_model(grid_size=4, base_cell_size=5, shift_range=1, rotation_angle=10, height_variation=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
