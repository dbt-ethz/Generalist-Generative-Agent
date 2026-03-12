# Created for 0011_0001_shifted_grid.json

""" Summary:
The provided function, `create_shifted_grid_concept_model`, generates an architectural concept model by starting with a regular grid pattern and dynamically modifying it based on the "Shifted Grid" metaphor. It selectively shifts and tilts grid elements to create intersecting planes, promoting a sense of movement and fluidity. The function incorporates randomness in shifts and tilts, resulting in varied spatial zones that enhance circulation paths and user interaction. By manipulating light and shadow through angled surfaces, the model embodies adaptability and invites exploration, aligning with the metaphor's emphasis on innovation and diverse spatial experiences in architecture."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size=5, shift_amount=2, tilt_angle=15):
    \"""
    Creates an architectural Concept Model based on the 'Shifted Grid' metaphor.
    
    This function generates a dynamic and non-linear architectural form by starting
    with a regular grid layout and selectively shifting and rotating elements to 
    create intersecting planes and varied spatial zones. The design embodies movement,
    adaptability, and diverse spatial experiences, promoting exploration and 
    engagement with light and shadow.

    Parameters:
    grid_size (int): The number of units in the grid along one dimension. Default is 5.
    shift_amount (float): The maximum amount to shift the elements in the grid in meters. Default is 2.
    tilt_angle (float): The angle in degrees to tilt certain elements to enhance dynamism. Default is 15.

    Returns:
    List[Rhino.Geometry.Brep]: A list of 3D geometries representing the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import math
    import random
    random.seed(42)  # Ensure replicability

    geometries = []
    base_plane = rg.Plane.WorldXY

    for i in range(grid_size):
        for j in range(grid_size):
            x_shift = random.uniform(-shift_amount, shift_amount)
            y_shift = random.uniform(-shift_amount, shift_amount)
            current_plane = base_plane.Clone()
            current_plane.OriginX += i * 5 + x_shift
            current_plane.OriginY += j * 5 + y_shift

            # Create a vertical wall with some tilt
            wall_height = random.uniform(3, 5)
            wall_corners = [
                rg.Point3d(0, 0, 0),
                rg.Point3d(5, 0, 0),
                rg.Point3d(5, 0, wall_height),
                rg.Point3d(0, 0, wall_height)
            ]
            wall = rg.Brep.CreateFromCornerPoints(wall_corners[0], wall_corners[1], wall_corners[2], wall_corners[3], 0.01)
            transform_rotate = rg.Transform.Rotation(math.radians(tilt_angle), current_plane.ZAxis, current_plane.Origin)
            wall.Transform(transform_rotate)
            transform_translate = rg.Transform.Translation(current_plane.Origin - rg.Point3d(0, 0, 0))
            wall.Transform(transform_translate)
            geometries.append(wall)

            # Create a horizontal plane as a floor
            floor = rg.Brep.CreateFromCornerPoints(wall_corners[0], wall_corners[1], wall_corners[1] + rg.Vector3d(0, 5, 0), wall_corners[0] + rg.Vector3d(0, 5, 0), 0.01)
            floor.Transform(transform_translate)
            geometries.append(floor)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(grid_size=7, shift_amount=3, tilt_angle=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(grid_size=6, shift_amount=1.5, tilt_angle=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(grid_size=4, shift_amount=2.5, tilt_angle=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(grid_size=8, shift_amount=4, tilt_angle=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(grid_size=5, shift_amount=2.5, tilt_angle=45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
