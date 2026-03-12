# Created for 0017_0002_cascading_frames.json

""" Summary:
The function `create_cascading_frames_model` generates an architectural concept model that embodies the metaphor of "Cascading frames." It creates a series of interlocking frames, each uniquely rotated and shifted to evoke a sense of dynamic progression and vertical continuity. By adjusting parameters like the number of frames, their dimensions, rotation angles, and horizontal shifts, the function constructs a rhythmic pattern that enhances the interplay of light and shadow. This model visually guides observers through interconnected spaces, reinforcing the metaphor's themes of fluidity and movement, while presenting a complex, engaging architectural form."""

#! python 3
function_code = """def create_cascading_frames_model(frame_count=5, frame_width=10, frame_height=5, frame_depth=0.5, rotation_angle=5, shift_distance=2):
    \"""
    Creates an architectural Concept Model based on the 'Cascading frames' metaphor. The model consists of a series of interlocking frames, each slightly rotated or shifted to suggest fluidity and dynamic progression.

    Parameters:
    - frame_count (int): The number of frames in the cascading sequence.
    - frame_width (float): The width of each frame in meters.
    - frame_height (float): The height of each frame in meters.
    - frame_depth (float): The depth/thickness of each frame in meters.
    - rotation_angle (float): The angle in degrees by which each consecutive frame is rotated to suggest movement.
    - shift_distance (float): The distance in meters by which each consecutive frame is shifted horizontally to enhance the perception of dynamic progression.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the architectural Concept Model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Initialize an empty list to store the frames
    frames = []

    # Base plane for the first frame
    base_plane = rg.Plane.WorldXY

    # Loop through the number of frames to create each one
    for i in range(frame_count):
        # Calculate the transformation for rotation and translation
        rotation = rg.Transform.Rotation(math.radians(rotation_angle * i), base_plane.Normal, base_plane.Origin)
        translation = rg.Transform.Translation(base_plane.XAxis * shift_distance * i)

        # Create a rectangle for the frame
        rectangle = rg.Rectangle3d(base_plane, frame_width, frame_height)

        # Extrude the rectangle to create a frame (extrusion depth is the frame depth)
        extrude_vector = rg.Vector3d(0, 0, frame_depth)
        brep_frame = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(rectangle.ToNurbsCurve(), extrude_vector))

        # Apply the rotation and translation to the frame
        brep_frame.Transform(rotation)
        brep_frame.Transform(translation)

        # Add the frame to the list
        frames.append(brep_frame)

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(frame_count=10, frame_width=12, frame_height=6, frame_depth=0.4, rotation_angle=7, shift_distance=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(frame_count=8, frame_width=15, frame_height=7, frame_depth=0.6, rotation_angle=10, shift_distance=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(frame_count=6, frame_width=14, frame_height=8, frame_depth=0.3, rotation_angle=6, shift_distance=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(frame_count=12, frame_width=9, frame_height=5, frame_depth=0.7, rotation_angle=4, shift_distance=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(frame_count=7, frame_width=11, frame_height=5.5, frame_depth=0.8, rotation_angle=8, shift_distance=3.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
