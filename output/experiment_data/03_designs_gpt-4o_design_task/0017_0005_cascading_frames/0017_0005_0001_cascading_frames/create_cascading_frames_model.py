# Created for 0017_0005_cascading_frames.json

""" Summary:
The function `create_cascading_frames_model` generates an architectural concept model inspired by the metaphor "Cascading frames." It constructs a series of layered frames that vary in scale, orientation, and position, reflecting a stepped design that embodies verticality and connectivity. Each frame acts as a visual and spatial connector, guiding the observer through interconnected spaces. The function utilizes randomization for scale and orientation, enhancing visual dynamism and depth, while also considering the interplay of light and shadow. By incorporating offset parameters, it achieves a cascading effect, simulating movement and fluidity within the architectural model."""

#! python 3
function_code = """def create_cascading_frames_model(base_frame_width, base_frame_height, frame_depth, number_of_frames, vertical_offset, horizontal_offset, random_seed):
    \"""
    Creates an architectural concept model based on the 'Cascading frames' metaphor, generating a series of frames with varying 
    scales and orientations. The frames are constructed in a stepped or tiered form, emphasizing both vertical and horizontal continuity.

    Parameters:
    - base_frame_width (float): The width of the base frame in meters.
    - base_frame_height (float): The height of the base frame in meters.
    - frame_depth (float): The depth/thickness of each frame in meters.
    - number_of_frames (int): The total number of frames to generate.
    - vertical_offset (float): The vertical step offset between consecutive frames in meters.
    - horizontal_offset (float): The horizontal step offset between consecutive frames in meters.
    - random_seed (int): Seed for random variations to ensure reproducibility.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(random_seed)
    
    frames = []
    
    for i in range(number_of_frames):
        # Calculate position offsets
        x_offset = horizontal_offset * i
        z_offset = vertical_offset * i

        # Randomly vary the scale and orientation
        scale_factor = random.uniform(0.8, 1.2)
        orientation_angle = random.uniform(-10, 10)  # in degrees

        # Define the base plane for the frame
        base_plane = rg.Plane(rg.Point3d(x_offset, 0, z_offset), rg.Vector3d(0, 0, 1))

        # Create a rectangle as frame boundary
        frame_rect = rg.Rectangle3d(base_plane, base_frame_width * scale_factor, base_frame_height * scale_factor)

        # Extrude the rectangle to create a frame
        extrusion_vector = rg.Vector3d(0, 0, frame_depth)
        extrusion = rg.Extrusion.Create(frame_rect.ToNurbsCurve(), frame_depth, True)
        frame_brep = extrusion.ToBrep()

        # Rotate frame around vertical axis
        rotation_axis = rg.Line(frame_rect.Corner(0), frame_rect.Corner(0) + rg.Vector3d(0, 0, 1))
        rotation_transform = rg.Transform.Rotation(math.radians(orientation_angle), rotation_axis.Direction, rotation_axis.From)
        frame_brep.Transform(rotation_transform)

        frames.append(frame_brep)
    
    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(2.0, 3.0, 0.1, 10, 0.5, 0.5, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(1.5, 2.5, 0.2, 8, 0.3, 0.4, 24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(3.0, 4.0, 0.15, 12, 0.4, 0.6, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(2.5, 4.0, 0.2, 15, 0.6, 0.7, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(1.0, 1.0, 0.05, 5, 0.2, 0.2, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
