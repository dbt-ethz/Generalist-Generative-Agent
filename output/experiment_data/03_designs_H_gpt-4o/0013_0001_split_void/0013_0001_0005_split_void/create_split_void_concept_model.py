# Created for 0013_0001_split_void.json

""" Summary:
The function `create_split_void_concept_model` generates an architectural model based on the "Split void" metaphor by creating two distinct building masses divided by a central void. It defines parameters such as dimensions and void characteristics to ensure the model reflects the metaphor's essence. The void serves as a spatial axis, facilitating movement and visual connections. The function also incorporates a rotation of one building mass to enhance dynamic tension and light interaction, emphasizing separation and contrast. This approach captures the duality of function and experience, aligning with the metaphor's implications of openness and movement."""

#! python 3
function_code = """def create_split_void_concept_model(length=25.0, width=15.0, height=12.0, void_width=3.0, void_offset=2.0, rotation_angle=15):
    \"""
    Creates an architectural Concept Model based on the 'Split void' metaphor, featuring a central void that divides
    the building into two distinct parts. The model emphasizes separation using rotation to create dynamic spatial
    tension and light interaction.

    Parameters:
    - length (float): The total length of the building in meters.
    - width (float): The total width of the building in meters.
    - height (float): The height of the building in meters.
    - void_width (float): The width of the central void in meters.
    - void_offset (float): Offset distance to shift the void from the center, in meters.
    - rotation_angle (float): Rotation angle for one of the building parts, in degrees.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the architectural concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Calculate half width and offsets
    half_width = (width - void_width) / 2
    left_offset = half_width + void_offset
    right_offset = width - left_offset

    # Create left and right building masses
    left_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(left_offset, 0, 0),
        rg.Point3d(left_offset, length, 0),
        rg.Point3d(0, length, 0),
        rg.Point3d(0, 0, height),
        rg.Point3d(left_offset, 0, height),
        rg.Point3d(left_offset, length, height),
        rg.Point3d(0, length, height)
    ]
    left_brep = rg.Brep.CreateFromBox(left_corners)

    right_corners = [
        rg.Point3d(right_offset, 0, 0),
        rg.Point3d(width, 0, 0),
        rg.Point3d(width, length, 0),
        rg.Point3d(right_offset, length, 0),
        rg.Point3d(right_offset, 0, height),
        rg.Point3d(width, 0, height),
        rg.Point3d(width, length, height),
        rg.Point3d(right_offset, length, height)
    ]
    right_brep = rg.Brep.CreateFromBox(right_corners)

    # Rotate the right part around the void axis
    rotation_center = rg.Point3d(left_offset + void_width / 2, length / 2, height / 2)
    rotation_axis = rg.Line(rotation_center, rg.Vector3d(0, 0, 1))
    rotation_transform = rg.Transform.Rotation(math.radians(rotation_angle), rotation_axis.Direction, rotation_center)
    right_brep.Transform(rotation_transform)

    # Create the central void
    void_corners = [
        rg.Point3d(left_offset, 0, 0),
        rg.Point3d(left_offset + void_width, 0, 0),
        rg.Point3d(left_offset + void_width, length, 0),
        rg.Point3d(left_offset, length, 0),
        rg.Point3d(left_offset, 0, height),
        rg.Point3d(left_offset + void_width, 0, height),
        rg.Point3d(left_offset + void_width, length, height),
        rg.Point3d(left_offset, length, height)
    ]
    void_brep = rg.Brep.CreateFromBox(void_corners)

    # Return the list of Breps representing the concept model
    return [left_brep, right_brep, void_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(length=30.0, width=20.0, height=10.0, void_width=4.0, void_offset=3.0, rotation_angle=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(length=40.0, width=25.0, height=15.0, void_width=5.0, void_offset=4.0, rotation_angle=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(length=35.0, width=18.0, height=12.0, void_width=2.5, void_offset=1.5, rotation_angle=45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(length=28.0, width=22.0, height=14.0, void_width=3.5, void_offset=2.5, rotation_angle=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(length=32.0, width=19.0, height=11.0, void_width=3.0, void_offset=2.0, rotation_angle=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
