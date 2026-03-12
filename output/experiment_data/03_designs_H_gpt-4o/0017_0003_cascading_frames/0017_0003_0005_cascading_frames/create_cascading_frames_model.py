# Created for 0017_0003_cascading_frames.json

""" Summary:
The function `create_cascading_frames_model` generates an architectural concept model based on the metaphor "Cascading frames" by creating a series of overlapping frames with varying sizes and orientations to convey movement and depth. It initializes parameters like frame count, width, height, thickness, and height increment. The frames are constructed as 3D boxes, each rotated randomly around the Y-axis and translated vertically to emphasize a cascading effect. This design facilitates a dynamic facade that enhances verticality and connectivity among spaces while allowing for the interplay of light and shadow, aligning with the metaphors themes of progression and layered depth."""

#! python 3
function_code = """def create_cascading_frames_model(frame_count=6, base_width=8.0, base_height=4.0, frame_thickness=0.5, height_increment=2.0):
    \"""
    Creates an architectural Concept Model embodying the 'Cascading frames' metaphor by generating a series of vertical frames
    that overlap and vary in size and orientation. This design emphasizes verticality and connectivity with a focus on dynamic
    progression and layered depth.

    Parameters:
    - frame_count (int): Number of frames to generate.
    - base_width (float): Initial width of the base frame in meters.
    - base_height (float): Initial height of the base frame in meters.
    - frame_thickness (float): Thickness of each frame in meters.
    - height_increment (float): Vertical distance increment between successive frames in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensure replicability

    frames = []
    current_position = rg.Point3d(0, 0, 0)

    for i in range(frame_count):
        # Adjust frame size and position
        frame_width = base_width * (1.2 - 0.1 * i)
        frame_height = base_height * (1.1 - 0.1 * i)
        
        # Create frame as a box
        corner1 = rg.Point3d(-frame_width / 2, -frame_thickness / 2, 0)
        corner2 = rg.Point3d(frame_width / 2, frame_thickness / 2, frame_height)
        box = rg.Box(rg.Plane.WorldXY, rg.Interval(corner1.X, corner2.X), rg.Interval(corner1.Y, corner2.Y), rg.Interval(corner1.Z, corner2.Z))
        frame_brep = box.ToBrep()

        # Apply a random rotation around the Y-axis for a cascading effect
        rotation_angle = random.uniform(-15, 15)
        rotation = rg.Transform.Rotation(math.radians(rotation_angle), rg.Vector3d.YAxis, current_position)
        frame_brep.Transform(rotation)

        # Translate the frame upward for cascading effect
        translation = rg.Transform.Translation(0, 0, height_increment * i)
        frame_brep.Transform(translation)

        # Add the frame to the list
        frames.append(frame_brep)

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(frame_count=5, base_width=10.0, base_height=5.0, frame_thickness=0.6, height_increment=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(frame_count=8, base_width=7.0, base_height=3.5, frame_thickness=0.4, height_increment=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(frame_count=10, base_width=12.0, base_height=6.0, frame_thickness=0.3, height_increment=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(frame_count=7, base_width=9.0, base_height=4.5, frame_thickness=0.7, height_increment=1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(frame_count=6, base_width=11.0, base_height=5.5, frame_thickness=0.5, height_increment=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
