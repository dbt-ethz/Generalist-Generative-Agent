# Created for 0017_0005_cascading_frames.json

""" Summary:
The function `create_cascading_frames_model` generates an architectural concept model inspired by the metaphor "Cascading frames." It constructs a series of layered, hollow frames that vary in scale and orientation, creating a dynamic, stepped structure. Each frame is positioned with specified vertical and horizontal offsets, simulating movement and depth. The frames are designed to enhance light and shadow interplay, reinforcing the metaphor's emphasis on fluidity and connectivity. By guiding the observer through interconnected spaces, the model embodies the layered, progressive essence of the metaphor, promoting engagement with the surrounding environment and fostering a sense of spatial continuity."""

#! python 3
function_code = """def create_cascading_frames_model(frame_count, base_width, base_height, frame_thickness, vertical_step, horizontal_step, random_seed):
    \"""
    Creates an architectural Concept Model inspired by the 'Cascading frames' metaphor, using a series of frames
    that vary in scale and orientation, forming a dynamic stepped pattern emphasizing movement and depth.

    Parameters:
    - frame_count (int): The number of frames in the cascading sequence.
    - base_width (float): The width of the largest frame in meters.
    - base_height (float): The height of the largest frame in meters.
    - frame_thickness (float): The thickness of each frame in meters.
    - vertical_step (float): The vertical distance between consecutive frames in meters.
    - horizontal_step (float): The horizontal distance between consecutive frames in meters.
    - random_seed (int): Seed for random variations to ensure reproducibility.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(random_seed)

    frames = []

    for i in range(frame_count):
        # Calculate position offsets
        x_offset = horizontal_step * i
        z_offset = vertical_step * i

        # Randomly vary the scale and orientation
        scale_factor = random.uniform(0.7, 1.3)
        orientation_angle = random.uniform(-5, 5)  # in degrees

        # Define the base plane for the frame
        base_plane = rg.Plane(rg.Point3d(x_offset, 0, z_offset), rg.Vector3d(0, 0, 1))

        # Create a rectangle as frame boundary
        frame_rect = rg.Rectangle3d(base_plane, base_width * scale_factor, base_height * scale_factor)

        # Create a hollow frame by subtracting an inner rectangle
        inner_scale = 0.8
        inner_rect = rg.Rectangle3d(base_plane, base_width * inner_scale * scale_factor, base_height * inner_scale * scale_factor)
        inner_rect_center = rg.Point3d(
            (frame_rect.Corner(0).X + frame_rect.Corner(2).X) / 2,
            (frame_rect.Corner(0).Y + frame_rect.Corner(2).Y) / 2,
            (frame_rect.Corner(0).Z + frame_rect.Corner(2).Z) / 2
        )
        translation_vector = inner_rect_center - inner_rect.Center
        inner_rect.Transform(rg.Transform.Translation(translation_vector))

        # Create surfaces
        outer_surface = rg.Surface.CreateExtrusion(frame_rect.ToNurbsCurve(), rg.Vector3d(0, 0, frame_thickness))
        inner_surface = rg.Surface.CreateExtrusion(inner_rect.ToNurbsCurve(), rg.Vector3d(0, 0, frame_thickness))

        # Boolean difference to create hollow frame
        frame_brep = rg.Brep.CreateBooleanDifference([outer_surface.ToBrep()], [inner_surface.ToBrep()], 0.001)

        # Rotate frame around vertical axis
        rotation_axis = rg.Line(frame_rect.Corner(0), frame_rect.Corner(0) + rg.Vector3d(0, 0, 1))
        rotation_transform = rg.Transform.Rotation(math.radians(orientation_angle), rotation_axis.Direction, rotation_axis.From)
        for brep in frame_brep:
            brep.Transform(rotation_transform)

        frames.extend(frame_brep)

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(10, 2.0, 3.0, 0.1, 0.5, 0.5, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(5, 1.5, 2.5, 0.2, 0.4, 0.4, 100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(15, 1.0, 1.5, 0.15, 0.3, 0.3, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(8, 2.5, 4.0, 0.15, 0.6, 0.4, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(12, 3.0, 2.0, 0.2, 0.7, 0.3, 56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
