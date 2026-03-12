# Created for 0011_0001_shifted_grid.json

""" Summary:
The function `create_shifted_grid_concept_model` generates an architectural concept model inspired by the "Shifted Grid" metaphor. It begins with a regular grid, then selectively shifts and rotates elements while varying their heights to create intersecting planes and dynamic spatial zones. This approach fosters diverse circulation paths and enhances light interaction through angled surfaces. The model emphasizes adaptability, allowing for reconfiguration to accommodate various functions, thereby encouraging exploration. By manipulating parameters like shift amount, rotation angle, and height variation, the function captures the essence of movement and fluidity, resulting in a unique architectural form."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size=(5, 5), base_size=5.0, shift_amount=2.0, rotation_angle=15.0, height_variation=2.0):
    \"""
    Creates an architectural Concept Model embodying the 'Shifted Grid' metaphor.

    This function generates a dynamic architectural form by starting with a regular grid pattern,
    selectively shifting, rotating, and varying the height of elements to create intersecting planes and
    distinct spatial zones. The design promotes diverse circulation paths and playful interaction with light and shadow.

    Parameters:
    - grid_size: Tuple[int, int] defining the number of grid elements in x and y directions.
    - base_size: float, the base size of each grid element in meters.
    - shift_amount: float, maximum distance in meters by which elements can be shifted.
    - rotation_angle: float, maximum rotation angle in degrees for grid elements.
    - height_variation: float, maximum deviation in height for elements in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensure replicable randomness

    breps = []

    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            # Base position of the current grid element
            base_point = rg.Point3d(i * base_size, j * base_size, 0)

            # Randomly determine shift and rotation
            shift_x = random.uniform(-shift_amount, shift_amount)
            shift_y = random.uniform(-shift_amount, shift_amount)
            shift_vector = rg.Vector3d(shift_x, shift_y, 0)

            # Random rotation
            rotation_radians = math.radians(random.uniform(-rotation_angle, rotation_angle))
            rotation_center = base_point + shift_vector + rg.Vector3d(base_size / 2, base_size / 2, 0)
            rotation_axis = rg.Vector3d(0, 0, 1)

            # Random height variation
            height = base_size + random.uniform(-height_variation, height_variation)

            # Create and transform the box
            box_corners = [
                base_point + shift_vector,
                base_point + shift_vector + rg.Vector3d(base_size, 0, 0),
                base_point + shift_vector + rg.Vector3d(base_size, base_size, 0),
                base_point + shift_vector + rg.Vector3d(0, base_size, 0),
                base_point + shift_vector + rg.Vector3d(0, 0, height),
                base_point + shift_vector + rg.Vector3d(base_size, 0, height),
                base_point + shift_vector + rg.Vector3d(base_size, base_size, height),
                base_point + shift_vector + rg.Vector3d(0, base_size, height)
            ]
            box = rg.Brep.CreateFromBox(box_corners)

            # Apply rotation
            rotation_transform = rg.Transform.Rotation(rotation_radians, rotation_axis, rotation_center)
            box.Transform(rotation_transform)

            # Add the transformed box to the list
            breps.append(box)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(grid_size=(6, 6), base_size=4.0, shift_amount=1.5, rotation_angle=30.0, height_variation=3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(grid_size=(4, 4), base_size=6.0, shift_amount=3.0, rotation_angle=45.0, height_variation=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(grid_size=(3, 5), base_size=7.0, shift_amount=2.5, rotation_angle=20.0, height_variation=4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(grid_size=(5, 3), base_size=5.0, shift_amount=2.0, rotation_angle=25.0, height_variation=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(grid_size=(7, 7), base_size=3.0, shift_amount=4.0, rotation_angle=10.0, height_variation=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
