# Created for 0017_0001_cascading_frames.json

""" Summary:
The function `create_cascading_frames_model_alternative` generates an architectural concept model based on the metaphor of "Cascading frames." It creates a series of tiered frames that visually cascade by shifting each frame horizontally while incrementally increasing their height. This staggered arrangement enhances the sense of movement and progression, embodying the metaphor's essence. The function also emphasizes vertical connectivity and spatial relationships, allowing light to interact with the surfaces, creating dynamic shadows and depth. By varying dimensions and gaps, the model captures the metaphors fluidity and visual complexity, guiding observers through a cohesive narrative of interconnected spaces."""

#! python 3
function_code = """def create_cascading_frames_model_alternative(base_length, base_width, frame_height, num_frames, vertical_gap, shift_variation):
    \"""
    Creates an architectural Concept Model based on the 'Cascading frames' metaphor using a different approach.

    This function generates a series of frames that cascade downward, each frame connected vertically with a gap.
    The frames are slightly shifted horizontally to create a sense of dynamic progression and visual interest.

    Parameters:
    - base_length (float): The length of the base frame in meters.
    - base_width (float): The width of the base frame in meters.
    - frame_height (float): The height of each frame in meters.
    - num_frames (int): The number of cascading frames.
    - vertical_gap (float): Vertical gap between each successive frame in meters.
    - shift_variation (float): The maximum horizontal shift variation for each frame.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the frames.
    \"""
    import Rhino.Geometry as rg
    import random

    # Seed for reproducibility
    random.seed(42)

    frames = []
    current_height = 0
    previous_center = rg.Point3d(0, 0, 0)

    for i in range(num_frames):
        # Calculate random shift
        shift_x = random.uniform(-shift_variation, shift_variation)
        shift_y = random.uniform(-shift_variation, shift_variation)

        # Create the base rectangle for the frame
        base_center = rg.Point3d(previous_center.X + shift_x, previous_center.Y + shift_y, current_height)
        rectangle = rg.Rectangle3d(
            rg.Plane(base_center, rg.Vector3d.ZAxis),
            rg.Interval(-base_length / 2, base_length / 2),
            rg.Interval(-base_width / 2, base_width / 2)
        )

        # Create a frame by extruding the rectangle to frame_height
        extrusion_vector = rg.Vector3d(0, 0, frame_height)
        frame = rg.Extrusion.Create(rectangle.ToNurbsCurve(), frame_height, True)

        # Add frame to the list
        if frame:
            frames.append(frame.ToBrep())

        # Update height for the next frame
        current_height += frame_height + vertical_gap
        previous_center = base_center

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model_alternative(5.0, 3.0, 2.0, 10, 1.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model_alternative(4.0, 2.5, 1.5, 8, 0.5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model_alternative(6.0, 4.0, 2.5, 12, 0.8, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model_alternative(3.0, 2.0, 1.0, 5, 0.2, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model_alternative(7.0, 3.5, 2.0, 15, 1.2, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
