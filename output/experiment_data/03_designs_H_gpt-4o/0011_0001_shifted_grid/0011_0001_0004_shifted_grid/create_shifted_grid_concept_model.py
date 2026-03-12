# Created for 0011_0001_shifted_grid.json

""" Summary:
The provided function creates an architectural concept model based on the 'Shifted Grid' metaphor by starting with a standard grid layout. It selectively shifts and rotates grid elements to generate intersecting planes and varied spatial zones, embodying movement and dynamism. Each element is randomly displaced and rotated, resulting in a non-linear arrangement that encourages diverse circulation paths and adaptable spaces. This dynamic configuration promotes engagement with light and shadow, enhancing the spatial experience. The model's design reflects the metaphors key traits of flexibility and exploration, allowing for a playful interaction with the built environment."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size=5, max_shift=2, max_rotation=20, element_height=4):
    \"""
    Creates an architectural Concept Model based on the 'Shifted Grid' metaphor.
    
    This function generates a dynamic architectural form by starting with a regular grid layout,
    then selectively shifting and rotating elements to create intersecting planes and varied spatial zones.
    The design embodies movement, adaptability, and diverse spatial experiences, promoting exploration
    and engagement with light and shadow.

    Parameters:
    grid_size (int): The number of units in the grid along one dimension. Default is 5.
    max_shift (float): The maximum distance to shift the elements in the grid in meters. Default is 2.
    max_rotation (float): The maximum angle in degrees to rotate certain elements to enhance dynamism. Default is 20.
    element_height (float): The height of each grid element in meters. Default is 4.

    Returns:
    List[Rhino.Geometry.Brep]: A list of 3D geometries representing the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensure replicable randomness

    geometries = []
    base_plane = rg.Plane.WorldXY
    base_size = 5.0  # Base size of each grid element in meters

    for i in range(grid_size):
        for j in range(grid_size):
            # Create a base box for each grid element
            base_origin = rg.Point3d(i * base_size, j * base_size, 0)
            box_corners = [
                base_origin,
                base_origin + rg.Vector3d(base_size, 0, 0),
                base_origin + rg.Vector3d(base_size, base_size, 0),
                base_origin + rg.Vector3d(0, base_size, 0),
                base_origin + rg.Vector3d(0, 0, element_height),
                base_origin + rg.Vector3d(base_size, 0, element_height),
                base_origin + rg.Vector3d(base_size, base_size, element_height),
                base_origin + rg.Vector3d(0, base_size, element_height),
            ]
            box = rg.Brep.CreateFromBox(box_corners)

            # Randomly shift the box
            shift_vector = rg.Vector3d(random.uniform(-max_shift, max_shift),
                                       random.uniform(-max_shift, max_shift),
                                       0)
            box.Translate(shift_vector)

            # Randomly rotate the box
            rotation_angle = math.radians(random.uniform(-max_rotation, max_rotation))
            rotation_axis = rg.Vector3d(0, 0, 1)  # Rotate around Z-axis
            rotation_center = box.GetBoundingBox(True).Center
            rotation_transform = rg.Transform.Rotation(rotation_angle, rotation_axis, rotation_center)
            box.Transform(rotation_transform)

            geometries.append(box)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(grid_size=7, max_shift=3, max_rotation=30, element_height=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(grid_size=6, max_shift=1.5, max_rotation=15, element_height=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(grid_size=4, max_shift=2.5, max_rotation=10, element_height=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(grid_size=8, max_shift=2, max_rotation=25, element_height=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(grid_size=5, max_shift=1, max_rotation=5, element_height=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
