# Created for 0017_0003_cascading_frames.json

""" Summary:
The provided function, `create_cascading_frames`, generates an architectural concept model based on the metaphor "Cascading frames." It creates a series of overlapping frames that vary in size, orientation, and depth, reflecting dynamic movement and layered depth. By adjusting parameters like frame count, width, height, depth variation, and angle variation, the function generates a complex, multi-dimensional facade. Each frame is positioned to enhance verticality and horizontal connectivity, guiding the observers journey through interconnected spaces. The interplay of light and shadow is emphasized through frame design, including perforations, resulting in a visually engaging structure that embodies the metaphor's essence."""

#! python 3
function_code = """def create_cascading_frames(frame_count=5, base_width=10.0, base_height=5.0, depth_variation=2.0, angle_variation=15.0):
    \"""
    Creates an architectural Concept Model embodying the "Cascading frames" metaphor. This function generates a series of overlapping frames that vary in size and orientation to create a sense of movement and depth. The frames are organized in a layered composition to emphasize verticality and horizontal connectivity.

    Parameters:
    - frame_count: int, number of frames to create.
    - base_width: float, width of the base frame in meters.
    - base_height: float, height of the base frame in meters.
    - depth_variation: float, maximum variation in depth between consecutive frames in meters.
    - angle_variation: float, maximum angle variation in degrees for the orientation of consecutive frames.

    Returns:
    - A list of Brep objects representing the 3D geometries of the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensure replicable randomness

    frames = []
    current_position = rg.Point3d(0, 0, 0)

    for i in range(frame_count):
        # Create a base rectangle for the frame
        width = base_width + random.uniform(-depth_variation, depth_variation)
        height = base_height + random.uniform(-depth_variation, depth_variation)
        rectangle_corners = [
            rg.Point3d(current_position.X, current_position.Y, current_position.Z),
            rg.Point3d(current_position.X + width, current_position.Y, current_position.Z),
            rg.Point3d(current_position.X + width, current_position.Y, current_position.Z + height),
            rg.Point3d(current_position.X, current_position.Y, current_position.Z + height),
            rg.Point3d(current_position.X, current_position.Y, current_position.Z)  # Closing the polyline
        ]
        rectangle = rg.Polyline(rectangle_corners)

        # Create frame thickness by offsetting
        outer_curve = rectangle.ToNurbsCurve()
        inner_curve = outer_curve.Offset(rg.Plane.WorldXY, -0.3, 0.01, rg.CurveOffsetCornerStyle.Sharp)[0]  # 0.3m thickness

        # Create a surface between the curves and extrude
        loft = rg.Brep.CreateFromLoft([inner_curve, outer_curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Straight, False)
        frame_surface = loft[0]
        frame_brep = frame_surface.CapPlanarHoles(0.01)

        # Rotate the frame
        angle = random.uniform(-angle_variation, angle_variation)
        rotation = rg.Transform.Rotation(math.radians(angle), current_position)
        frame_brep.Transform(rotation)

        # Add frame to the collection
        frames.append(frame_brep)

        # Update the current position for the next frame
        current_position += rg.Vector3d(random.uniform(0.5, 1.5), 0, height / 2)

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames(frame_count=10, base_width=8.0, base_height=4.0, depth_variation=1.5, angle_variation=20.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames(frame_count=7, base_width=12.0, base_height=6.0, depth_variation=3.0, angle_variation=10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames(frame_count=6, base_width=15.0, base_height=7.0, depth_variation=2.5, angle_variation=25.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames(frame_count=8, base_width=9.0, base_height=5.5, depth_variation=2.0, angle_variation=30.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames(frame_count=12, base_width=11.0, base_height=5.0, depth_variation=2.0, angle_variation=15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
