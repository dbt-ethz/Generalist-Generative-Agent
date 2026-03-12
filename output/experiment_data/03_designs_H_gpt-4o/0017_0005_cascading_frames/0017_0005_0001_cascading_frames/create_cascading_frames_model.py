# Created for 0017_0005_cascading_frames.json

""" Summary:
The function `create_cascading_frames_model` generates an architectural concept model reflecting the "Cascading frames" metaphor by creating a series of frames that vary in scale and orientation. Each frame is progressively smaller and positioned in a tiered arrangement, enhancing the sense of movement and depth. The parameters control frame dimensions, spacing, and random rotations, contributing to a dynamic visual rhythm. This approach allows for an interplay of light and shadow, guiding observers through interconnected spaces. Ultimately, the model emphasizes verticality, connectivity, and engagement with the environment, fulfilling the design task while embodying the metaphor's essence."""

#! python 3
function_code = """def create_cascading_frames_model(base_width, base_height, frame_count, frame_thickness, vertical_step, horizontal_step, rotation_range, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Cascading frames' metaphor.
    
    This model consists of a series of frames that vary in scale and orientation, creating a stepped or tiered form
    that emphasizes dynamic progression, layered depth, and spatial continuity.

    Parameters:
    - base_width (float): The width of the largest frame in meters.
    - base_height (float): The height of the largest frame in meters.
    - frame_count (int): The number of frames to generate.
    - frame_thickness (float): The thickness of each frame in meters.
    - vertical_step (float): The vertical distance between consecutive frames in meters.
    - horizontal_step (float): The horizontal distance between consecutive frames in meters.
    - rotation_range (float): Maximum random rotation angle for each frame in degrees.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometry of the frames.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    random.seed(seed)
    frames = []

    for i in range(frame_count):
        # Scale down the frame size progressively
        scale_factor = 1 - (i / frame_count) * 0.5
        current_width = base_width * scale_factor
        current_height = base_height * scale_factor

        # Create a rectangle for the frame
        plane = rg.Plane.WorldXY
        rect = rg.Rectangle3d(plane, current_width, current_height)

        # Extrude the rectangle to create a frame
        extrusion_vector = rg.Vector3d(0, 0, frame_thickness)
        brep_frame = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(rect.ToNurbsCurve(), extrusion_vector))

        # Calculate the translation for cascading effect
        translation_vector = rg.Vector3d(horizontal_step * i, 0, vertical_step * i)
        brep_frame.Translate(translation_vector)
        
        # Apply a random rotation
        rotation_angle = random.uniform(-rotation_range, rotation_range)
        rotation_transform = rg.Transform.Rotation(math.radians(rotation_angle), rg.Vector3d.ZAxis, plane.Origin)
        brep_frame.Transform(rotation_transform)

        frames.append(brep_frame)

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(5.0, 3.0, 10, 0.2, 1.0, 0.5, 15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(4.0, 2.5, 8, 0.15, 0.8, 0.4, 20.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(6.0, 4.0, 12, 0.3, 1.5, 0.6, 10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(3.5, 2.0, 6, 0.1, 0.7, 0.3, 25.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(7.0, 5.0, 15, 0.25, 1.2, 0.75, 30.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
