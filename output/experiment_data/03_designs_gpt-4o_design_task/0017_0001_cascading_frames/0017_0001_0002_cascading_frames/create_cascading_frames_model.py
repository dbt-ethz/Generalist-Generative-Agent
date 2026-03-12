# Created for 0017_0001_cascading_frames.json

""" Summary:
The provided function, `create_cascading_frames_model`, generates an architectural concept model inspired by the metaphor "Cascading frames." It creates a series of 3D geometrical frames that are arranged in a tiered fashion, with each frame progressively offset to suggest movement and dynamism. The parameters control the dimensions and number of frames, while randomization introduces variation for visual interest. This design emphasizes verticality and connectivity, guiding the observer's eye through a sequence of layers, enhancing the perception of light and shadow interplay. The result is a visually compelling model that embodies the metaphor's essence of fluidity and depth."""

#! python 3
function_code = """def create_cascading_frames_model(base_width, base_depth, base_height, num_frames, frame_offset, frame_height, seed=42):
    \"""
    Creates a 3D architectural Concept Model embodying the 'Cascading frames' metaphor.
    
    This function generates a series of geometrical frames that are progressively tiered and offset,
    creating a sense of dynamic progression and layered depth. It emphasizes verticality and connectivity,
    with each frame leading visually to the next, while playing with light and shadow.

    Parameters:
    - base_width (float): The width of the base frame in meters.
    - base_depth (float): The depth of the base frame in meters.
    - base_height (float): The height of the base frame in meters.
    - num_frames (int): The number of cascading frames to create.
    - frame_offset (float): The offset distance between each successive frame in meters.
    - frame_height (float): The height of each individual frame tier in meters.
    - seed (int, optional): The seed for randomness to ensure replicability. Default is 42.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    frames = []

    for i in range(num_frames):
        # Calculate the transformation for each frame
        x_offset = frame_offset * i
        y_offset = random.uniform(-frame_offset, frame_offset) * 0.5  # Add randomness for dynamic effect
        z_offset = frame_height * i

        # Create a box for the current frame
        base_origin = rg.Point3d(x_offset, y_offset, z_offset)
        base_corners = [
            base_origin,
            rg.Point3d(base_origin.X + base_width, base_origin.Y, base_origin.Z),
            rg.Point3d(base_origin.X + base_width, base_origin.Y + base_depth, base_origin.Z),
            rg.Point3d(base_origin.X, base_origin.Y + base_depth, base_origin.Z),
            rg.Point3d(base_origin.X, base_origin.Y, base_origin.Z + base_height),
            rg.Point3d(base_origin.X + base_width, base_origin.Y, base_origin.Z + base_height),
            rg.Point3d(base_origin.X + base_width, base_origin.Y + base_depth, base_origin.Z + base_height),
            rg.Point3d(base_origin.X, base_origin.Y + base_depth, base_origin.Z + base_height)
        ]

        base_box = rg.Brep.CreateFromBox(base_corners)
        frames.append(base_box)

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(5.0, 3.0, 2.0, 10, 1.0, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(4.0, 2.5, 3.0, 8, 0.8, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(6.0, 4.0, 2.5, 12, 1.2, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(7.0, 5.0, 4.0, 15, 1.5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(3.0, 2.0, 1.5, 5, 0.5, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
