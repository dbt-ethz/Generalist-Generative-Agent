# Created for 0017_0002_cascading_frames.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor "Cascading frames" by creating a series of interlocking frames that evoke fluidity and dynamic progression. Each frame is defined by parameters such as width, height, rotation, and horizontal shift. The function iteratively constructs frames, applying transformations that rotate and shift each successive frame to suggest movement and continuity. This design approach emphasizes verticality and creates a rhythmic pattern, allowing for an engaging interplay of light and shadow. Ultimately, the generated model captures the essence of the metaphor, guiding the observer through a sequential spatial experience."""

#! python 3
function_code = """def create_cascading_frames_model(frame_count=5, base_width=10.0, base_height=3.0, frame_rotation=10.0, frame_shift=0.5):
    \"""
    Creates an architectural Concept Model based on the metaphor 'Cascading frames', with a series of interlocking frames
    that suggest fluidity and dynamic progression.

    Parameters:
    - frame_count (int): Number of cascading frames to generate.
    - base_width (float): The width of the base frame in meters.
    - base_height (float): The height of the base frame in meters.
    - frame_rotation (float): The rotation angle in degrees applied to each subsequent frame.
    - frame_shift (float): The horizontal shift applied to each subsequent frame in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the frames.
    \"""
    import Rhino.Geometry as rg
    import math

    frames = []
    for i in range(frame_count):
        # Calculate the transformation for each frame
        rotation_angle_rad = math.radians(i * frame_rotation)
        shift_vector = rg.Vector3d(i * frame_shift, 0, 0)

        # Create the base frame rectangle
        base_rect = rg.Rectangle3d(rg.Plane.WorldXY, base_width, base_height)
        
        # Transform the base rectangle
        transform = rg.Transform.Translation(shift_vector)
        base_rect.Transform(transform)
        
        # Rotate the rectangle around its center
        center = base_rect.Center
        rotate_transform = rg.Transform.Rotation(rotation_angle_rad, center)
        base_rect.Transform(rotate_transform)

        # Extrude the rectangle to create a frame
        extrusion_vector = rg.Vector3d(0, 0, base_height)
        frame_brep = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(base_rect.ToNurbsCurve(), extrusion_vector))
        
        # Add the frame to the list
        if frame_brep:
            frames.append(frame_brep)

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(frame_count=7, base_width=12.0, base_height=4.0, frame_rotation=15.0, frame_shift=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(frame_count=10, base_width=8.0, base_height=2.5, frame_rotation=20.0, frame_shift=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(frame_count=6, base_width=15.0, base_height=5.0, frame_rotation=5.0, frame_shift=0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(frame_count=8, base_width=11.0, base_height=3.5, frame_rotation=12.0, frame_shift=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(frame_count=4, base_width=9.0, base_height=3.0, frame_rotation=25.0, frame_shift=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
