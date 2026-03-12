# Created for 0017_0003_cascading_frames.json

""" Summary:
The function `create_cascading_frames_model` generates an architectural concept model based on the metaphor of "Cascading frames." By creating a series of overlapping frames that vary in size, orientation, and curvature, the model embodies dynamic movement and depth. Each frame is constructed with a progressive reduction in size and a random orientation to enhance visual complexity. The spacing and layering of frames facilitate a fluid transition between interconnected spaces, emphasizing both verticality and horizontal connectivity. Additionally, the interplay of light and shadow is achieved through frame design, reinforcing the metaphor's themes of progression and layered depth in architecture."""

#! python 3
function_code = """def create_cascading_frames_model(frame_count=6, frame_base_size=8.0, frame_height=3.0, frame_thickness=0.2, frame_offset=1.5, curvature_variation=0.5):
    \"""
    Creates an architectural Concept Model based on the 'Cascading frames' metaphor, featuring curved and angled frames
    to enhance the cascading effect, emphasizing dynamic movement and depth.

    Parameters:
    - frame_count (int): The number of frames to generate.
    - frame_base_size (float): The base size of the frames in meters.
    - frame_height (float): The height of each frame in meters.
    - frame_thickness (float): The thickness of each frame in meters.
    - frame_offset (float): The offset distance between successive frames in meters.
    - curvature_variation (float): The maximum curvature variation for each frame in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the frames in 3D space.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensure replicability

    frames = []

    for i in range(frame_count):
        # Create a base rectangle for the frame with a curvature
        scale_factor = 1.0 - (i * 0.1)  # Reduce size progressively
        curve_points = []

        # Define points for a slightly curved frame
        for j in range(5):
            x = (j % 2) * frame_base_size * scale_factor
            y = frame_height * (j // 2)
            z = math.sin(math.pi * y / frame_height) * curvature_variation
            curve_points.append(rg.Point3d(x, y, z))

        # Create a NurbsCurve from the points
        frame_curve = rg.NurbsCurve.Create(False, 3, curve_points)
        
        # Offset the curve to create frame thickness
        inner_curves = frame_curve.Offset(rg.Plane.WorldXY, -frame_thickness, 0.01, rg.CurveOffsetCornerStyle.Sharp)

        # Create the frame as a Brep
        if inner_curves and len(inner_curves) > 0:
            planar_breps = rg.Brep.CreatePlanarBreps([frame_curve, inner_curves[0]])
            if planar_breps:
                frame_surface = planar_breps[0]

                # Transform the frame
                translation = rg.Transform.Translation(0, 0, i * frame_offset)
                angle = random.uniform(-15, 15)  # Random orientation for dynamic effect
                rotation = rg.Transform.Rotation(math.radians(angle), rg.Vector3d(0, 0, 1), rg.Point3d(0, 0, 0))
                frame_surface.Transform(translation * rotation)

                # Add to the list of frames
                frames.append(frame_surface)

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(frame_count=8, frame_base_size=10.0, frame_height=4.0, frame_thickness=0.3, frame_offset=2.0, curvature_variation=0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(frame_count=5, frame_base_size=12.0, frame_height=5.0, frame_thickness=0.25, frame_offset=1.0, curvature_variation=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(frame_count=10, frame_base_size=9.0, frame_height=3.5, frame_thickness=0.15, frame_offset=1.0, curvature_variation=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(frame_count=7, frame_base_size=11.0, frame_height=3.5, frame_thickness=0.2, frame_offset=1.2, curvature_variation=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(frame_count=6, frame_base_size=7.0, frame_height=3.0, frame_thickness=0.1, frame_offset=1.5, curvature_variation=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
