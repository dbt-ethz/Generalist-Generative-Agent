# Created for 0011_0001_shifted_grid.json

""" Summary:
The function `create_shifted_grid_concept_model` generates an architectural concept model based on the 'Shifted Grid' metaphor by manipulating a regular grid. It systematically creates grid elements, which are boxes, and applies random shifts and rotations to these elements to break conventional orthogonal layouts. This results in a dynamic arrangement of intersecting planes and varied spatial zones that enhance circulation and spatial experience. The model emphasizes adaptability and interaction with light and shadow through angled surfaces, fostering exploration within the design. Overall, it embodies the metaphor's essence by promoting fluidity and innovative spatial configurations."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size=8, shift_amount=1.5, rotation_angle=10, element_height=4):
    \"""
    Creates an architectural Concept Model embodying the 'Shifted Grid' metaphor.

    This function generates a dynamic architectural form by starting with a regular grid and
    selectively shifting and rotating elements to create intersecting planes and varied spatial zones.
    The design promotes diverse spatial experiences through varied circulation paths and adaptable spaces.

    Parameters:
    grid_size (int): The number of units in the grid along one dimension. Default is 8.
    shift_amount (float): The maximum distance by which elements in the grid can be shifted, in meters. Default is 1.5.
    rotation_angle (float): The maximum angle in degrees by which elements can be rotated. Default is 10.
    element_height (float): The height of the volumes created, in meters. Default is 4.

    Returns:
    List[Rhino.Geometry.Brep]: A list of 3D geometries representing the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensure replicability

    geometries = []
    base_spacing = 7.0  # Base spacing between grid elements in meters

    for i in range(grid_size):
        for j in range(grid_size):
            # Base point for the current grid element
            base_point = rg.Point3d(i * base_spacing, j * base_spacing, 0)

            # Create a box base element
            box_corners = [
                base_point,
                rg.Point3d(base_point.X + base_spacing, base_point.Y, 0),
                rg.Point3d(base_point.X + base_spacing, base_point.Y + base_spacing, 0),
                rg.Point3d(base_point.X, base_point.Y + base_spacing, 0),
                rg.Point3d(base_point.X, base_point.Y, element_height),
                rg.Point3d(base_point.X + base_spacing, base_point.Y, element_height),
                rg.Point3d(base_point.X + base_spacing, base_point.Y + base_spacing, element_height),
                rg.Point3d(base_point.X, base_point.Y + base_spacing, element_height)
            ]
            box = rg.Brep.CreateFromBox(box_corners)

            # Randomly shift the box
            shift_vector = rg.Vector3d(
                random.uniform(-shift_amount, shift_amount),
                random.uniform(-shift_amount, shift_amount),
                0
            )
            box.Translate(shift_vector)

            # Randomly rotate the box
            rotation_radians = math.radians(random.uniform(-rotation_angle, rotation_angle))
            rotation_axis = rg.Vector3d(0, 0, 1)  # Rotate around Z-axis
            rotation_center = box.GetBoundingBox(True).Center
            rotation_transform = rg.Transform.Rotation(rotation_radians, rotation_axis, rotation_center)
            box.Transform(rotation_transform)

            geometries.append(box)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(grid_size=10, shift_amount=2.0, rotation_angle=15, element_height=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(grid_size=6, shift_amount=2.5, rotation_angle=20, element_height=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(grid_size=12, shift_amount=1.0, rotation_angle=5, element_height=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(grid_size=5, shift_amount=1.0, rotation_angle=30, element_height=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(grid_size=4, shift_amount=3.0, rotation_angle=25, element_height=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
