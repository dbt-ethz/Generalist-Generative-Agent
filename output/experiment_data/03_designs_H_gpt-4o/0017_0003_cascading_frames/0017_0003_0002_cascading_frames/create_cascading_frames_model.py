# Created for 0017_0003_cascading_frames.json

""" Summary:
The provided function generates an architectural concept model reflecting the "Cascading frames" metaphor by creating a series of overlapping frames that vary in size, orientation, and spacing. Each frame represents a layer in the design, emphasizing dynamic movement and depth. The function systematically reduces the size of each subsequent frame, while applying transformations such as translation and rotation to enhance visual complexity and suggest fluidity. By organizing these frames vertically and horizontally, the model promotes spatial connectivity and guides the observer's journey, capturing the metaphor's essence of layered depth and interplay of light and shadow."""

#! python 3
function_code = """def create_cascading_frames_model(frame_count, base_size, frame_thickness, vertical_spacing, rotation_angle):
    \"""
    Creates an architectural Concept Model based on the 'Cascading frames' metaphor. This function generates a series of 
    overlapping frames that vary in size and orientation to create a sense of movement and depth.

    Parameters:
    - frame_count (int): The number of frames to generate.
    - base_size (tuple): A tuple (width, height) representing the base size of the frames in meters.
    - frame_thickness (float): The thickness of each frame in meters.
    - vertical_spacing (float): The vertical distance between successive frames in meters.
    - rotation_angle (float): The angle by which each subsequent frame is rotated around its vertical axis in degrees.

    Returns:
    - List of Rhino.Geometry.Brep: A list of Brep objects representing the 3D geometries of the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import math

    frames = []

    width, height = base_size
    current_position = rg.Point3d(0, 0, 0)

    for i in range(frame_count):
        # Create a base rectangle for the frame
        corners = [
            rg.Point3d(-width / 2, -height / 2, 0),
            rg.Point3d(width / 2, -height / 2, 0),
            rg.Point3d(width / 2, height / 2, 0),
            rg.Point3d(-width / 2, height / 2, 0),
            rg.Point3d(-width / 2, -height / 2, 0)  # Closing the polyline
        ]
        polyline = rg.Polyline(corners)
        outer_curve = polyline.ToNurbsCurve()

        # Offset to create frame thickness
        inner_curve = rg.Curve.Offset(outer_curve, rg.Plane.WorldXY, -frame_thickness, 0.01, rg.CurveOffsetCornerStyle.Sharp)[0]

        # Create the frame surface
        frame_surface = rg.Brep.CreatePlanarBreps([outer_curve, inner_curve])[0]

        # Apply transformations
        translation = rg.Transform.Translation(current_position)
        rotation = rg.Transform.Rotation(math.radians(i * rotation_angle), rg.Vector3d(0, 0, 1), current_position)
        transform = translation * rotation
        frame_surface.Transform(transform)

        # Append to list
        frames.append(frame_surface)

        # Update position for the next frame
        current_position.Z += vertical_spacing

        # Reduce the frame size for cascading effect
        width *= 0.9
        height *= 0.9

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(10, (2.0, 1.0), 0.1, 0.5, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(5, (3.0, 2.0), 0.2, 0.4, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(8, (1.5, 1.5), 0.15, 0.3, 20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(6, (4.0, 2.5), 0.25, 0.6, 30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(12, (2.5, 1.8), 0.2, 0.7, 25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
