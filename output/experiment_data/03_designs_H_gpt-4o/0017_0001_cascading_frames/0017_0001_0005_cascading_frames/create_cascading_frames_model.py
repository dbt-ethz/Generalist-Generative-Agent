# Created for 0017_0001_cascading_frames.json

""" Summary:
The function `create_cascading_frames_model` generates an architectural concept model inspired by the metaphor "Cascading frames" by creating a series of tiered volumes that shift both horizontally and vertically. Each frame's dimensions are progressively reduced to enhance the cascading effect, emphasizing verticality and connectivity. The parameters, such as base dimensions and offset factors, guide the arrangement of frames, allowing for dynamic silhouettes and an interplay of light and shadow. The resulting model visually narrates a sequence of linked spaces, embodying the metaphor's essence of movement and spatial continuity through its layered design."""

#! python 3
function_code = """def create_cascading_frames_model(base_width, base_depth, frame_height, num_frames, offset_factor, vertical_shift):
    \"""
    Create an architectural Concept Model embodying the 'Cascading frames' metaphor.

    This function generates a series of tiered volumes that shift horizontally and vertically,
    suggesting movement and progression. The design emphasizes verticality and connectivity,
    creating a dynamic silhouette with interplay of light and shadow.

    Parameters:
    - base_width (float): The width of the base frame in meters.
    - base_depth (float): The depth of the base frame in meters.
    - frame_height (float): The height of each frame in meters.
    - num_frames (int): The number of cascading frames.
    - offset_factor (float): The horizontal offset factor for each frame.
    - vertical_shift (float): The vertical shift for each subsequent frame.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the frames.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(42)
    frames = []

    current_width = base_width
    current_depth = base_depth
    current_height = 0
    offset_x = 0
    offset_y = 0

    for i in range(num_frames):
        # Create a base rectangle for the frame
        base_plane = rg.Plane(rg.Point3d(offset_x, offset_y, current_height), rg.Vector3d.ZAxis)
        width_interval = rg.Interval(0, current_width)
        depth_interval = rg.Interval(0, current_depth)
        height_interval = rg.Interval(0, frame_height)

        # Create a box for the current frame
        box = rg.Box(base_plane, width_interval, depth_interval, height_interval)
        frame_brep = box.ToBrep()

        if frame_brep:
            frames.append(frame_brep)

        # Update parameters for the next frame
        current_height += frame_height + vertical_shift
        offset_x += offset_factor * random.uniform(-0.5, 0.5) * current_width
        offset_y += offset_factor * random.uniform(-0.5, 0.5) * current_depth

        # Optionally alter dimensions to emphasize the cascading effect
        current_width *= 0.95
        current_depth *= 0.95

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(5.0, 3.0, 2.0, 10, 0.5, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(4.0, 2.5, 1.5, 8, 0.3, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(6.0, 4.0, 3.0, 12, 0.4, 1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(7.0, 5.0, 2.5, 15, 0.6, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(3.0, 2.0, 1.0, 5, 0.2, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
