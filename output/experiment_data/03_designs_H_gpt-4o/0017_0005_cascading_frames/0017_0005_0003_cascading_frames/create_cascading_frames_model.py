# Created for 0017_0005_cascading_frames.json

""" Summary:
The function `create_cascading_frames_model` generates an architectural concept model inspired by the metaphor "Cascading frames." It constructs a series of frames with varying scales and orientations, arranged in a stepped manner to evoke fluidity and depth. Each frame is created by extruding a rectangle and then translated vertically and horizontally to create the cascading effect. Random rotations add visual complexity, enhancing the dynamic character of the design. The model emphasizes continuity and connectivity between spaces, reflecting the metaphor's intent of guiding observers through a progression of interconnected areas while playing with light and shadow."""

#! python 3
function_code = """def create_cascading_frames_model(base_width, base_height, frame_count, frame_thickness, vertical_step, horizontal_step, random_seed):
    \"""
    Generates an architectural Concept Model based on the 'Cascading frames' metaphor.

    This function creates a series of frames that vary in scale, orientation, and position,
    forming a dynamic, stepped arrangement that emphasizes both vertical and horizontal continuity.

    Parameters:
    - base_width (float): The initial width of the frames in meters.
    - base_height (float): The initial height of the frames in meters.
    - frame_count (int): The number of frames to generate.
    - frame_thickness (float): The thickness of each frame in meters.
    - vertical_step (float): The vertical distance between consecutive frames in meters.
    - horizontal_step (float): The horizontal distance between consecutive frames in meters.
    - random_seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometry of the frames.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(random_seed)
    frames = []

    for i in range(frame_count):
        scale_factor = random.uniform(0.9, 1.1)  # Allow small variations in scale
        width = base_width * scale_factor
        height = base_height * scale_factor

        # Create a rectangle for the frame
        plane = rg.Plane.WorldXY
        rect = rg.Rectangle3d(plane, width, height)
        
        # Extrude the rectangle to create a frame
        extrusion_vector = rg.Vector3d(0, 0, frame_thickness)
        brep_frame = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(rect.ToNurbsCurve(), extrusion_vector))

        # Offset the frame in both vertical and horizontal directions
        x_offset = i * horizontal_step
        z_offset = i * vertical_step
        translation_vector = rg.Vector3d(x_offset, 0, z_offset)
        transformed_brep = brep_frame.Duplicate()
        transformed_brep.Translate(translation_vector)

        # Apply a small random rotation around the vertical axis
        angle = random.uniform(-5, 5)  # Random angle in degrees
        rotation_axis = rg.Vector3d(0, 0, 1)  # Rotate around Z-axis
        rotation = rg.Transform.Rotation(math.radians(angle), rotation_axis, plane.Origin)
        transformed_brep.Transform(rotation)
        
        frames.append(transformed_brep)

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(3.0, 2.0, 10, 0.1, 0.5, 0.5, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(5.0, 4.0, 15, 0.2, 0.3, 0.4, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(4.0, 3.0, 8, 0.15, 0.6, 0.7, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(2.5, 1.5, 12, 0.2, 0.4, 0.6, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(6.0, 5.0, 20, 0.25, 0.7, 0.3, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
