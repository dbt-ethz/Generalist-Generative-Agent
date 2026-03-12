# Created for 0017_0004_cascading_frames.json

""" Summary:
The function `generate_cascading_frames` creates an architectural concept model based on the metaphor of "Cascading frames." It generates a series of frames that vary in width, height, and orientation, simulating a dynamic cascading effect. Each frame is slightly rotated and reduced in size, enhancing visual complexity and emphasizing vertical movement. The use of random angles adds uniqueness to each frame, promoting an interplay of light and shadow as they interact with one another. The result is a structured yet fluid form that guides movement, creating transitional spaces and enhancing the overall architectural narrative."""

#! python 3
function_code = """def generate_cascading_frames(seed: int, frame_count: int, initial_width: float, initial_height: float, frame_thickness: float) -> list:
    \"""
    Create a series of cascading frames for an architectural Concept Model based on the 'Cascading frames' metaphor.

    Parameters:
    seed (int): Seed for random number generator to ensure replicability.
    frame_count (int): Number of frames in the cascading sequence.
    initial_width (float): Width of the base frame.
    initial_height (float): Height of each frame level.
    frame_thickness (float): Thickness of each frame.

    Returns:
    list: A list of Brep objects representing the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)

    frames = []
    current_height = 0
    current_width = initial_width

    for i in range(frame_count):
        # Calculate frame orientation with a slight rotation for dynamic effect
        angle = random.uniform(-5, 5)  # Rotate by a random angle between -5 and 5 degrees
        rotation = rg.Transform.Rotation(math.radians(angle), rg.Vector3d.ZAxis, rg.Point3d(0, 0, current_height))

        # Create a base rectangle for the frame
        base_rect = rg.Rectangle3d(rg.Plane.WorldXY, rg.Interval(-current_width / 2, current_width / 2), rg.Interval(-frame_thickness / 2, frame_thickness / 2))
        
        # Extrude the rectangle to form a frame box
        extrude_vector = rg.Vector3d(0, 0, initial_height)
        brep_frame = rg.Brep.CreateFromBox(rg.Box(base_rect.Plane, base_rect.X, base_rect.Y, rg.Interval(0, initial_height)))
        
        # Apply the rotation transformation
        brep_frame.Transform(rotation)

        # Add the transformed frame to the list
        frames.append(brep_frame)

        # Update width and height for the next frame
        current_width *= 0.9  # Reduce width to create a cascading effect
        current_height += initial_height * 0.8  # Increase height with some overlap

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cascading_frames(42, 5, 10.0, 3.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cascading_frames(7, 8, 15.0, 4.0, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cascading_frames(12, 6, 20.0, 2.5, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cascading_frames(21, 10, 12.0, 5.0, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cascading_frames(99, 7, 25.0, 6.0, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
