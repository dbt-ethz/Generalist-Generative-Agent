# Created for 0017_0003_cascading_frames.json

""" Summary:
The provided function, `create_cascading_frames_model`, generates an architectural concept model based on the metaphor of "Cascading frames." It creates a series of frames that vary in size, orientation, and height, reflecting the metaphor's emphasis on dynamic movement and layered depth. By using randomized angles and height variations, the function simulates the cascading effect, enhancing visual complexity and spatial continuity. Each frame is transformed to create an interconnected sequence, guiding the observers experience through the design. The model emphasizes both verticality and horizontal connections, while strategically incorporating light and shadow interplays through its layered structure."""

#! python 3
function_code = """def create_cascading_frames_model(base_frame_size, num_frames, frame_thickness, angle_variation, height_variation):
    \"""
    Creates an architectural concept model based on the 'Cascading frames' metaphor.

    Parameters:
    - base_frame_size (float): The initial size of the base frame (width and height in meters).
    - num_frames (int): The number of frames to create in the cascading sequence.
    - frame_thickness (float): The thickness of each frame in meters.
    - angle_variation (float): The maximum angle variation for the orientation of frames in degrees.
    - height_variation (float): The maximum height variation for the vertical offset of frames in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensure replicability

    frames = []
    current_position = rg.Point3d(0, 0, 0)
    
    for i in range(num_frames):
        # Calculate random angle and height variation
        angle = random.uniform(-angle_variation, angle_variation)
        height_offset = random.uniform(-height_variation, height_variation)

        # Create frame profile as a polyline
        half_size = base_frame_size / 2
        corners = [
            rg.Point3d(-half_size, -half_size, 0),
            rg.Point3d(half_size, -half_size, 0),
            rg.Point3d(half_size, half_size, 0),
            rg.Point3d(-half_size, half_size, 0),
            rg.Point3d(-half_size, -half_size, 0)  # Close the loop
        ]
        polyline = rg.Polyline(corners)

        # Offset the polyline to create frame thickness
        outer_curve = polyline.ToNurbsCurve()
        inner_curve = rg.Curve.Offset(outer_curve, rg.Plane.WorldXY, -frame_thickness, 0.01, rg.CurveOffsetCornerStyle.Sharp)[0]

        # Create the frame as a Brep
        frame_surface = rg.Brep.CreatePlanarBreps([outer_curve, inner_curve])[0]

        # Transform the frame
        translation = rg.Transform.Translation(current_position + rg.Point3d(0, 0, height_offset))
        rotation = rg.Transform.Rotation(math.radians(angle), rg.Vector3d(0, 0, 1), current_position)
        transform = translation * rotation
        frame_surface.Transform(transform)

        frames.append(frame_surface)

        # Update position for the next frame
        current_position.Z += height_variation

        # Reduce the base frame size for the cascading effect
        base_frame_size *= 0.9

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(5.0, 10, 0.2, 15.0, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(6.0, 8, 0.3, 20.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(4.0, 12, 0.15, 10.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(7.0, 15, 0.25, 25.0, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(3.0, 5, 0.1, 30.0, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
