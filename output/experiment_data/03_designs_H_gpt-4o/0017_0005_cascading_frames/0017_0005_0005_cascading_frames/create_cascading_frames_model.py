# Created for 0017_0005_cascading_frames.json

""" Summary:
The provided function creates an architectural concept model based on the "Cascading frames" metaphor by generating a series of 3D frames that vary in scale, orientation, and positioning. Each frame is created by scaling a base rectangle and extruding it into a three-dimensional shape. The function applies a rotation and translation to each frame, producing a dynamic, stepped formation that emphasizes verticality and connectivity. This design approach allows for the interplay of light and shadow, enhancing the perception of depth and movement. Ultimately, the model embodies the metaphor's essence, guiding observers through a sequence of interconnected spaces."""

#! python 3
function_code = """def create_cascading_frames_model(frame_base_size, frame_count, frame_thickness, frame_step, rotation_angle, seed=42):
    \"""
    Creates an architectural Concept Model inspired by the 'Cascading frames' metaphor. The model consists of a series
    of frames that vary in scale and orientation, creating a dynamic stepped form emphasizing verticality and connectivity.

    Parameters:
    - frame_base_size (float): The base size of the initial frame in meters.
    - frame_count (int): The number of frames to generate.
    - frame_thickness (float): The thickness of each frame in meters.
    - frame_step (float): The distance between successive frames in meters.
    - rotation_angle (float): The fixed angle in degrees for frame rotation to create dynamic orientation.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometry of the frames.
    \"""
    import Rhino.Geometry as rg
    import math

    frames = []

    for i in range(frame_count):
        # Calculate the scale factor for current frame
        scale_factor = 1 - (i * 0.1)

        # Create the base frame rectangle
        frame_size = frame_base_size * scale_factor
        rectangle = rg.Rectangle3d(rg.Plane.WorldXY, frame_size, frame_size)

        # Create frame by extruding the rectangle
        surface = rg.Surface.CreateExtrusion(rectangle.ToNurbsCurve(), rg.Vector3d(0, 0, frame_thickness))
        frame_brep = surface.ToBrep()

        # Rotate each frame around the Z-axis
        angle_radians = math.radians(rotation_angle * i)
        rotation = rg.Transform.Rotation(angle_radians, rg.Vector3d.ZAxis, rg.Point3d.Origin)
        frame_brep.Transform(rotation)

        # Translate the frame to its cascading position
        translation = rg.Transform.Translation(i * frame_step, 0, i * frame_step)
        frame_brep.Transform(translation)

        frames.append(frame_brep)

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(5.0, 10, 0.2, 1.0, 15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(3.0, 8, 0.15, 0.8, 10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(4.0, 12, 0.25, 0.5, 20.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(6.0, 15, 0.3, 1.5, 25.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(7.0, 5, 0.1, 0.5, 30.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
