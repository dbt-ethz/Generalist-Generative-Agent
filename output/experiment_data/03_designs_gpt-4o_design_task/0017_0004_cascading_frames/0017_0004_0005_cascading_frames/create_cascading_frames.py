# Created for 0017_0004_cascading_frames.json

""" Summary:
The provided function, `create_cascading_frames`, generates an architectural concept model by creating a series of interconnected frames that embody the metaphor of "Cascading frames." Each frame is defined by its height, width, and thickness, while progressively shifting in both vertical and horizontal dimensions to establish a dynamic, layered structure. The use of a shift factor allows for variations in frame size and position, enhancing the visual rhythm and emphasizing vertical movement. This design captures the interplay of light and shadow through the frames, facilitating a narrative flow of space that promotes connectivity and continuity within the architectural model."""

#! python 3
function_code = """def create_cascading_frames(seed: int, base_frame_count: int, frame_height: float, frame_width: float, frame_thickness: float, shift_factor: float) -> list:
    \"""
    Create a series of cascading frames for an architectural Concept Model based on the 'Cascading frames' metaphor.

    Parameters:
    seed (int): Seed for random number generator to ensure replicability.
    base_frame_count (int): Number of frames at the base level.
    frame_height (float): Height of each frame.
    frame_width (float): Width of each frame.
    frame_thickness (float): Thickness of each frame.
    shift_factor (float): Factor by which frames will shift horizontally as they ascend.

    Returns:
    list: A list of Brep objects representing the cascading frames.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Box, Plane, Point3d, Vector3d, Interval

    random.seed(seed)

    frames = []
    current_height = 0
    current_width = frame_width
    current_shift = 0

    for i in range(base_frame_count):
        # Create a frame at the current level
        base_origin = Point3d(current_shift, 0, current_height)
        base_x_interval = Interval(0, current_width)
        base_y_interval = Interval(0, frame_thickness)
        base_z_interval = Interval(0, frame_height)
        
        frame = Box(Plane(base_origin, Vector3d(1, 0, 0), Vector3d(0, 1, 0)), base_x_interval, base_y_interval, base_z_interval)
        frames.append(frame.ToBrep())

        # Update parameters for the next frame
        current_height += frame_height
        current_width *= (1 - shift_factor)  # Reduce the width for cascading effect
        current_shift += frame_width * shift_factor  # Shift the frame for cascading effect

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames(seed=42, base_frame_count=5, frame_height=10.0, frame_width=5.0, frame_thickness=0.5, shift_factor=0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames(seed=7, base_frame_count=3, frame_height=8.0, frame_width=6.0, frame_thickness=0.3, shift_factor=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames(seed=12, base_frame_count=4, frame_height=12.0, frame_width=4.0, frame_thickness=0.4, shift_factor=0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames(seed=21, base_frame_count=6, frame_height=15.0, frame_width=7.0, frame_thickness=0.6, shift_factor=0.05)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames(seed=99, base_frame_count=8, frame_height=9.0, frame_width=10.0, frame_thickness=0.2, shift_factor=0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
