# Created for 0013_0001_split_void.json

""" Summary:
The function generates an architectural concept model based on the 'Split void' metaphor by creating a structure divided by a central void. It defines dimensions for the building and the void, then constructs two solid halves, incorporating a rotation to enhance visual dynamism. The void serves as a spatial divider, fostering distinct areas and guiding movement. By manipulating light through the void, it creates dynamic patterns and shadows, emphasizing the contrast between the two sides. The model visually embodies the duality and structural identity suggested by the metaphor, facilitating varied interactions within the architectural space."""

#! python 3
function_code = """def create_split_void_concept_model(length=25.0, width=15.0, height=12.0, void_width=4.0, void_height=10.0, rotation_angle=15.0):
    \"""
    Creates an architectural Concept Model embodying the 'Split void' metaphor. This model features a central void
    that divides the building into two distinct parts, with a slight rotation to enhance dynamic flow and interaction
    with light and shadow.

    Parameters:
    - length (float): The total length of the building in meters.
    - width (float): The total width of the building in meters.
    - height (float): The height of the building in meters.
    - void_width (float): The width of the central void in meters.
    - void_height (float): The height of the central void in meters.
    - rotation_angle (float): The angle to rotate one part of the building for dynamic contrast in degrees.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the architectural concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Calculate the positions for the void and the two halves
    half_width = (width - void_width) / 2

    # Create the left and right solid parts of the building
    left_solid = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, half_width), rg.Interval(0, height))
    right_solid = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(half_width + void_width, width), rg.Interval(0, height))

    # Create the central void
    central_void = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(half_width, half_width + void_width), rg.Interval(0, void_height))

    # Convert solids to Breps
    left_brep = left_solid.ToBrep()
    right_brep = right_solid.ToBrep()
    void_brep = central_void.ToBrep()

    # Apply rotation to the right part to enhance the dynamic contrast
    rotation_center = rg.Point3d(length / 2, width / 2, height / 2)
    rotation_axis = rg.Vector3d(0, 0, 1)  # Rotate around the vertical axis (Z-axis)
    rotation_transform = rg.Transform.Rotation(math.radians(rotation_angle), rotation_axis, rotation_center)
    right_brep.Transform(rotation_transform)

    # Return a list of Breps representing the concept model
    return [left_brep, right_brep, void_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(length=30.0, width=20.0, height=15.0, void_width=5.0, void_height=12.0, rotation_angle=20.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(length=40.0, width=25.0, height=18.0, void_width=6.0, void_height=10.0, rotation_angle=30.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(length=35.0, width=22.0, height=14.0, void_width=7.0, void_height=11.0, rotation_angle=25.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(length=28.0, width=18.0, height=16.0, void_width=4.5, void_height=9.0, rotation_angle=10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(length=32.0, width=21.0, height=17.0, void_width=5.5, void_height=8.0, rotation_angle=12.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
