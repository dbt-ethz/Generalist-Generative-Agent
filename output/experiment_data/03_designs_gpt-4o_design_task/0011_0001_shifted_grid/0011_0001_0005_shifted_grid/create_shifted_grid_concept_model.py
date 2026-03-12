# Created for 0011_0001_shifted_grid.json

""" Summary:
The function `create_shifted_grid_concept_model` generates an architectural concept model based on the 'Shifted Grid' metaphor by constructing a regular grid pattern of 3D elements. It selectively shifts and rotates these elements, introducing dynamic spatial arrangements that deviate from traditional orthogonality. Each element can be altered in position and orientation, creating varied circulation paths and distinct spatial zones. The model emphasizes adaptability and fluidity, allowing for multiple uses and engaging interactions with light and shadow through angled surfaces. This approach fosters exploration and discovery within the design, aligning with the metaphor's implications of movement and flexibility."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size, shift_amount, rotation_angle, element_height):
    \"""
    Creates an architectural Concept Model embodying the 'Shifted Grid' metaphor. 
    The model starts with a regular grid pattern and selectively shifts and rotates elements to 
    create dynamic and non-linear spatial arrangements.

    Parameters:
    - grid_size: Tuple[int, int] specifying the number of elements in the grid (rows, columns).
    - shift_amount: float specifying the maximum distance by which elements can be shifted.
    - rotation_angle: float specifying the maximum angle in degrees by which elements can be rotated.
    - element_height: float specifying the height of each grid element.

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometry of the model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensure replicable results

    breps = []
    base_size = 5.0  # Base size of each grid element in meters

    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            # Create base box for each grid element
            base_point = rg.Point3d(i * base_size, j * base_size, 0)
            box_corners = [base_point,
                           rg.Point3d(base_point.X + base_size, base_point.Y, 0),
                           rg.Point3d(base_point.X + base_size, base_point.Y + base_size, 0),
                           rg.Point3d(base_point.X, base_point.Y + base_size, 0),
                           rg.Point3d(base_point.X, base_point.Y, element_height),
                           rg.Point3d(base_point.X + base_size, base_point.Y, element_height),
                           rg.Point3d(base_point.X + base_size, base_point.Y + base_size, element_height),
                           rg.Point3d(base_point.X, base_point.Y + base_size, element_height)]
            box = rg.Brep.CreateFromBox(box_corners)

            # Randomly shift the box
            shift_vector = rg.Vector3d(random.uniform(-shift_amount, shift_amount),
                                       random.uniform(-shift_amount, shift_amount),
                                       0)
            box.Translate(shift_vector)

            # Randomly rotate the box
            rotation_radians = math.radians(random.uniform(-rotation_angle, rotation_angle))
            rotation_axis = rg.Vector3d(0, 0, 1)  # Rotate around Z-axis
            rotation_center = box.GetBoundingBox(True).Center
            rotation_transform = rg.Transform.Rotation(rotation_radians, rotation_axis, rotation_center)
            box.Transform(rotation_transform)

            breps.append(box)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model((4, 4), 1.0, 30.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model((3, 5), 0.5, 45.0, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model((6, 2), 2.0, 60.0, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model((5, 3), 1.5, 15.0, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model((2, 6), 0.8, 90.0, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
