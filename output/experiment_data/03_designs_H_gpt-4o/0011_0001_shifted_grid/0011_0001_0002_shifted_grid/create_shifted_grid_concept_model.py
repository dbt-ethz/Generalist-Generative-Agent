# Created for 0011_0001_shifted_grid.json

""" Summary:
The function `create_shifted_grid_concept_model` generates an architectural concept model that embodies the "Shifted Grid" metaphor by manipulating a regular grid. It begins with a grid of specified size and base dimensions, then selectively applies random shifts and rotations to each grid element, creating intersecting planes and varied spatial zones. This approach fosters a dynamic reconfiguration of the grid, promoting movement and exploration, while allowing for diverse circulation paths. The resulting model emphasizes adaptability and interaction with light and shadow through angled surfaces, aligning with the metaphor's essence of fluidity and unexpected spatial arrangements."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size=6, base_size=5, shift_amount=1.5, rotation_angle=20):
    \"""
    Creates an architectural Concept Model embodying the 'Shifted Grid' metaphor.

    This function generates a dynamic architectural form by starting with a regular grid pattern
    and selectively shifting and rotating elements to create intersecting planes and varied spatial zones.
    The design embodies movement and adaptability, promoting exploration and engagement with light and shadow.

    Parameters:
    grid_size (int): The number of units in the grid along one dimension. Default is 6.
    base_size (float): The base size of each grid unit in meters. Default is 5.
    shift_amount (float): The maximum amount to shift the elements in the grid in meters. Default is 1.5.
    rotation_angle (float): The maximum angle in degrees to rotate elements to enhance dynamism. Default is 20.

    Returns:
    List[Rhino.Geometry.Brep]: A list of 3D geometries representing the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensure replicability

    geometries = []

    for i in range(grid_size):
        for j in range(grid_size):
            # Determine the random shift and rotation
            x_shift = random.uniform(-shift_amount, shift_amount)
            y_shift = random.uniform(-shift_amount, shift_amount)
            rotation = random.uniform(-rotation_angle, rotation_angle)

            # Create a base plane for each grid cell
            base_point = rg.Point3d(i * base_size, j * base_size, 0)
            base_plane = rg.Plane(base_point, rg.Vector3d.ZAxis)

            # Create a vertical element (e.g., a wall)
            wall_height = random.uniform(3, 6)
            wall_corners = [
                rg.Point3d(0, 0, 0),
                rg.Point3d(base_size, 0, 0),
                rg.Point3d(base_size, 0, wall_height),
                rg.Point3d(0, 0, wall_height)
            ]
            wall = rg.Brep.CreateFromCornerPoints(wall_corners[0], wall_corners[1], wall_corners[2], wall_corners[3], 0.01)

            # Apply shift and rotation transformations
            transform_translate = rg.Transform.Translation(x_shift, y_shift, 0)
            wall.Transform(transform_translate)

            transform_rotate = rg.Transform.Rotation(math.radians(rotation), base_plane.ZAxis, base_plane.Origin)
            wall.Transform(transform_rotate)

            geometries.append(wall)

            # Create a rotated and shifted floor plate
            floor_corners = [
                rg.Point3d(0, 0, 0),
                rg.Point3d(base_size, 0, 0),
                rg.Point3d(base_size, base_size, 0),
                rg.Point3d(0, base_size, 0)
            ]
            floor = rg.Brep.CreateFromCornerPoints(floor_corners[0], floor_corners[1], floor_corners[2], floor_corners[3], 0.01)
            floor.Transform(transform_translate)
            floor.Transform(transform_rotate)

            geometries.append(floor)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(grid_size=8, base_size=4, shift_amount=2, rotation_angle=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(grid_size=5, base_size=6, shift_amount=1, rotation_angle=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(grid_size=7, base_size=3, shift_amount=2.5, rotation_angle=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(grid_size=10, base_size=7, shift_amount=1, rotation_angle=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(grid_size=4, base_size=8, shift_amount=1, rotation_angle=45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
