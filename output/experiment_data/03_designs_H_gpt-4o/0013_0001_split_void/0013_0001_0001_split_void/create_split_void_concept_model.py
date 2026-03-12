# Created for 0013_0001_split_void.json

""" Summary:
The function `create_split_void_concept_model` generates an architectural model that embodies the "Split void" metaphor by creating a structure with a central void that divides the building into two distinct sections. By defining parameters such as dimensions and orientation, it constructs two contrasting forms on either side of the void, enhancing the sense of separation. The model emphasizes dynamic interactions with natural light and shadow, reflecting the metaphor's themes of duality and movement. Transformations such as scaling and rotation further highlight the visual contrast between the sections, culminating in a cohesive architectural concept that aligns with the design task."""

#! python 3
function_code = """def create_split_void_concept_model(length=25.0, width=15.0, height=10.0, void_length=5.0, void_orientation='vertical'):
    \"""
    Creates an architectural Concept Model embodying the 'Split void' metaphor. This function generates a structure with
    a central void that divides the building into two distinct parts, emphasizing separation through contrasting forms
    and interaction with natural light and shadow.

    Parameters:
    - length (float): The total length of the building in meters.
    - width (float): The total width of the building in meters.
    - height (float): The height of the building in meters.
    - void_length (float): The length of the central void in meters.
    - void_orientation (str): Orientation of the void ('vertical' or 'horizontal').

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the architectural concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Determine the void position based on orientation
    if void_orientation == 'vertical':
        half_width = (width - void_length) / 2
        left_section = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, half_width), rg.Interval(0, height))
        right_section = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(half_width + void_length, width), rg.Interval(0, height))
        void_space = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(half_width, half_width + void_length), rg.Interval(0, height))
    else:
        half_length = (length - void_length) / 2
        left_section = rg.Box(rg.Plane.WorldXY, rg.Interval(0, half_length), rg.Interval(0, width), rg.Interval(0, height))
        right_section = rg.Box(rg.Plane.WorldXY, rg.Interval(half_length + void_length, length), rg.Interval(0, width), rg.Interval(0, height))
        void_space = rg.Box(rg.Plane.WorldXY, rg.Interval(half_length, half_length + void_length), rg.Interval(0, width), rg.Interval(0, height))

    # Convert sections to Breps
    left_brep = left_section.ToBrep()
    right_brep = right_section.ToBrep()
    void_brep = void_space.ToBrep()

    # Apply contrasting transformations to emphasize separation
    scale_transform = rg.Transform.Scale(rg.Plane.WorldXY, 1.1, 1.1, 1)
    left_brep.Transform(scale_transform)
    rotate_transform = rg.Transform.Rotation(math.radians(5), rg.Vector3d.ZAxis, rg.Point3d(length / 2, width / 2, height / 2))
    right_brep.Transform(rotate_transform)

    return [left_brep, right_brep, void_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(length=30.0, width=20.0, height=12.0, void_length=6.0, void_orientation='horizontal')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(length=40.0, width=25.0, height=15.0, void_length=7.0, void_orientation='vertical')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(length=35.0, width=18.0, height=10.0, void_length=4.0, void_orientation='vertical')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(length=50.0, width=30.0, height=20.0, void_length=8.0, void_orientation='horizontal')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(length=45.0, width=22.0, height=18.0, void_length=5.0, void_orientation='vertical')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
