# Created for 0017_0003_cascading_frames.json

""" Summary:
The function `create_cascading_frames_model` generates an architectural concept model reflecting the "Cascading frames" metaphor by creating a series of overlapping frames that vary in size, orientation, and rotation. Each frame is constructed as a 3D extrusion from a rectangle, allowing for depth and dynamic visual effects. The frames are incrementally translated vertically, simulating a cascading effect, while random rotations enhance the sense of movement. This arrangement fosters spatial continuity and connectivity, embodying the metaphor's focus on light interplay and layered depth, ultimately guiding observers through a rich, interconnected architectural experience."""

#! python 3
function_code = """def create_cascading_frames_model(frame_count, frame_width, frame_height, frame_depth, rotation_variation):
    \"""
    Creates an architectural Concept Model embodying the 'Cascading frames' metaphor.
    
    Parameters:
    - frame_count (int): The number of frames to generate.
    - frame_width (float): The width of each frame in meters.
    - frame_height (float): The height of each frame in meters.
    - frame_depth (float): The depth (thickness) of each frame in meters.
    - rotation_variation (float): The maximum angle in degrees by which frames can be rotated.

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometries of the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random
    import System

    # Set a random seed for replicable results
    random.seed(42)

    # Initialize a list to hold the generated frames
    frames = []

    # Starting point for the first frame
    base_point = rg.Point3d(0, 0, 0)

    for i in range(frame_count):
        # Create a base rectangle for the frame
        rectangle = rg.Rectangle3d(rg.Plane.WorldXY, frame_width, frame_height)
        
        # Convert the rectangle to a polyline
        polyline = rectangle.ToPolyline()
        polyline_curve = rg.PolylineCurve(polyline)

        # Extrude the frame to give it depth
        extrusion_path = rg.Line(base_point, rg.Point3d(0, 0, frame_depth))
        extruded_frame = rg.Brep.CreateFromLoft([polyline_curve, polyline_curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)[0]
        extruded_frame.CapPlanarHoles(0.01)

        # Apply a random rotation to the frame
        rotation_angle = random.uniform(-rotation_variation, rotation_variation)
        rotation_axis = rg.Vector3d(0, 0, 1)  # Rotate around the Z-axis
        rotation_transform = rg.Transform.Rotation(System.Math.PI * rotation_angle / 180.0, rotation_axis, base_point)

        extruded_frame.Transform(rotation_transform)

        # Move the frame upwards for cascading effect
        translation_transform = rg.Transform.Translation(0, 0, i * (frame_height * 0.5))
        extruded_frame.Transform(translation_transform)

        # Add the transformed frame to the list
        frames.append(extruded_frame)

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(5, 2.0, 3.0, 0.5, 15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(10, 1.5, 2.5, 0.3, 10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(8, 1.0, 2.0, 0.4, 20.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(6, 2.5, 4.0, 0.6, 25.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(7, 3.0, 5.0, 0.8, 30.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
