# Created for 0017_0002_cascading_frames.json

""" Summary:
The function `generate_cascading_frames_model` creates a 3D architectural model inspired by the metaphor "Cascading frames." It generates a series of interlocking frames, each slightly rotated and elevated, to evoke dynamic progression and continuity. The frames are designed with varying heights and angles, enhancing verticality and creating a rhythmic pattern that plays with light and shadow. Each frame serves as a visual and spatial threshold, guiding observers through interconnected spaces. By adjusting parameters like base dimensions and angle variation, the function facilitates the exploration of different configurations, reinforcing the metaphor's themes of movement and connectivity within architecture."""

#! python 3
function_code = """def generate_cascading_frames_model(base_width, base_depth, frame_height, frame_thickness, frame_count, angle_variation):
    \"""
    Generates a 3D architectural Concept Model based on the 'Cascading Frames' metaphor.
    This model consists of a series of interlocking frames that cascade with slight rotations
    and shifts to create a dynamic progression and continuity. The frames emphasize verticality
    and create a rhythmic pattern, enhancing the interplay of light and shadow.

    Parameters:
    - base_width (float): The width of the base frame in meters.
    - base_depth (float): The depth of the base frame in meters.
    - frame_height (float): The height of each frame in meters.
    - frame_thickness (float): The thickness of each frame in meters.
    - frame_count (int): The number of cascading frames to generate.
    - angle_variation (float): The maximum angle in degrees by which each subsequent frame can rotate.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D brep geometries representing the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    random.seed(42)  # Ensure replicability
    
    frames = []
    current_z = 0
    current_angle = 0

    for i in range(frame_count):
        # Create the base rectangle for the frame
        base_corners = [
            rg.Point3d(0, 0, current_z),
            rg.Point3d(base_width, 0, current_z),
            rg.Point3d(base_width, base_depth, current_z),
            rg.Point3d(0, base_depth, current_z)
        ]
        base_curve = rg.Polyline(base_corners + [base_corners[0]]).ToNurbsCurve()

        # Offset the curve inward to create a frame
        offset_curve = base_curve.Offset(rg.Plane.WorldXY, -frame_thickness, 0.01, rg.CurveOffsetCornerStyle.Sharp)[0]
        frame_surface = rg.Brep.CreatePlanarBreps([base_curve, offset_curve])[0]

        # Rotate the frame
        current_angle += random.uniform(-angle_variation, angle_variation)
        rotation_axis = rg.Vector3d(0, 0, 1)
        rotation_center = rg.Point3d(base_width / 2, base_depth / 2, current_z)
        transform = rg.Transform.Rotation(math.radians(current_angle), rotation_axis, rotation_center)
        frame_surface.Transform(transform)

        # Add the frame to the list
        frames.append(frame_surface)

        # Update the position for the next frame
        current_z += frame_height

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cascading_frames_model(5.0, 3.0, 2.0, 0.1, 10, 15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cascading_frames_model(4.0, 2.5, 1.5, 0.05, 8, 10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cascading_frames_model(6.0, 4.0, 3.0, 0.2, 12, 20.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cascading_frames_model(7.0, 5.0, 2.5, 0.15, 15, 12.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cascading_frames_model(3.0, 2.0, 1.0, 0.1, 5, 25.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
