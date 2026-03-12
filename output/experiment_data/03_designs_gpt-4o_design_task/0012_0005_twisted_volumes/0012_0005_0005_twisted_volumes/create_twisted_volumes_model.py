# Created for 0012_0005_twisted_volumes.json

""" Summary:
The provided function generates an architectural concept model reflecting the metaphor of "Twisted volumes" by creating a series of interwoven geometric shapes. Each segment of the structure is twisted incrementally, simulating fluidity and tension, which aligns with the metaphor's implications. The model's parameters, such as twist angle, height, and segment count, dictate the design's complexity and dynamism. This twisting action fosters unique spatial experiences and circulation paths, while the manipulation of light and shadow is achieved through the various angles of the twisted forms. Ultimately, the model embodies the essence of transformation and movement inherent in the metaphor."""

#! python 3
function_code = """def create_twisted_volumes_model(twist_angle=30, height=10, base_length=5, segments=5):
    \"""
    Creates a Concept Model of 'Twisted Volumes' by generating a series of intertwined and contorted geometric shapes.

    Parameters:
    - twist_angle (float): The angle in degrees by which each segment will be twisted. Default is 30 degrees.
    - height (float): The total height of the structure in meters. Default is 10 meters.
    - base_length (float): The base length of each segment (assumed to be square-based). Default is 5 meters.
    - segments (int): The number of segments to create the twisted volume. Default is 5 segments.

    Returns:
    - List of Rhino.Geometry.Brep: A list of Breps representing the twisted geometric forms.
    \"""
    import Rhino
    import System
    from Rhino.Geometry import Point3d, Vector3d, Plane, Box, Transform, Brep

    breps = []

    # Calculate height per segment
    segment_height = height / segments

    # Create base plane
    base_plane = Plane(Point3d(0, 0, 0), Vector3d.ZAxis)

    for i in range(segments):
        # Create a base box
        base_point = Point3d(0, 0, i * segment_height)
        box = Box(base_plane, Rhino.Geometry.Interval(-base_length/2, base_length/2), Rhino.Geometry.Interval(-base_length/2, base_length/2), Rhino.Geometry.Interval(0, segment_height))
        brep = box.ToBrep()

        # Create a rotation transform
        rotation_axis = base_plane.ZAxis
        rotation_angle = System.Math.PI * twist_angle / 180.0 * (i + 1) / segments
        rotation_transform = Transform.Rotation(rotation_angle, rotation_axis, base_point)

        # Apply transformation
        brep.Transform(rotation_transform)

        # Add to the list of breps
        breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(twist_angle=45, height=15, base_length=3, segments=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(twist_angle=60, height=20, base_length=4, segments=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(twist_angle=15, height=12, base_length=6, segments=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(twist_angle=90, height=8, base_length=7, segments=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(twist_angle=75, height=18, base_length=2, segments=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
