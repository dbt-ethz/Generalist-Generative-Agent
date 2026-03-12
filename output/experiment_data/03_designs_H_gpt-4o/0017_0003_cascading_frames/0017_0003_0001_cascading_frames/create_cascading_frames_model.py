# Created for 0017_0003_cascading_frames.json

""" Summary:
The function `create_cascading_frames_model` generates an architectural concept model inspired by the metaphor "Cascading frames." It creates a series of overlapping frames that vary in size, orientation, and curvature, embodying a dynamic facade. By incrementally adjusting the height and scaling down each successive frame, the model evokes movement and depth. The frames interact through lofting techniques, and transformations like rotation and scaling enhance visual complexity. This approach emphasizes spatial continuity, guiding observers through interconnected spaces while allowing light and shadow to play across the surfaces, thus reinforcing the metaphor's themes of fluidity and layered depth."""

#! python 3
function_code = """def create_cascading_frames_model(num_frames=6, base_size=8.0, height_increment=2.0, frame_thickness=0.4, curvature=0.3):
    \"""
    Creates an architectural Concept Model based on the 'Cascading frames' metaphor.
    This model features a series of overlapping frames that vary in orientation and curvature, 
    creating a dynamic facade with a sense of movement and depth.

    Parameters:
    - num_frames (int): Number of frames to generate.
    - base_size (float): Size of the base frame (width and depth in meters).
    - height_increment (float): Vertical increment between frames in meters.
    - frame_thickness (float): Thickness of each frame in meters.
    - curvature (float): Degree of curvature applied to frames for dynamic effect.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import math

    frames = []

    for i in range(num_frames):
        # Create a curved base frame
        radius = base_size / 2
        arc_angle = math.pi / 3  # 60 degrees
        arc = rg.Arc(rg.Point3d(0, 0, i * height_increment), radius, arc_angle)
        arc_curve = arc.ToNurbsCurve()

        # Offset the arc to create thickness
        offset_curve = arc_curve.Offset(rg.Plane.WorldXY, frame_thickness, 0.01, rg.CurveOffsetCornerStyle.Sharp)[0]

        # Loft between the original and offset curves
        loft = rg.Brep.CreateFromLoft([arc_curve, offset_curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        frame_brep = loft[0] if loft else None

        if frame_brep:
            # Apply curvature transformation
            if curvature != 0:
                curvature_transform = rg.Transform.Scale(rg.Plane.WorldXY, 1, 1, 1 + curvature * (i / num_frames))
                frame_brep.Transform(curvature_transform)
            
            # Rotate each frame slightly for a cascading effect
            rotation_transform = rg.Transform.Rotation(math.radians(10 * i), rg.Vector3d.ZAxis, rg.Point3d.Origin)
            frame_brep.Transform(rotation_transform)

            frames.append(frame_brep)

        # Scale down base size for the next frame
        base_size *= 0.9

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(num_frames=8, base_size=10.0, height_increment=3.0, frame_thickness=0.5, curvature=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(num_frames=5, base_size=12.0, height_increment=1.5, frame_thickness=0.3, curvature=0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(num_frames=10, base_size=15.0, height_increment=2.5, frame_thickness=0.6, curvature=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(num_frames=7, base_size=9.0, height_increment=2.0, frame_thickness=0.5, curvature=0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(num_frames=12, base_size=11.0, height_increment=2.2, frame_thickness=0.45, curvature=0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
