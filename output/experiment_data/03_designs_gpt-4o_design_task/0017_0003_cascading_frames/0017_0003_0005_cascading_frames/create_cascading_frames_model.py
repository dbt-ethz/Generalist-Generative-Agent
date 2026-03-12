# Created for 0017_0003_cascading_frames.json

""" Summary:
The function `create_cascading_frames_model` generates an architectural concept model inspired by the metaphor "Cascading frames." It creates multiple overlapping frames that vary in size, orientation, and offset, simulating movement and depth. Each frame is progressively scaled down, enhancing the sense of dynamic progression. Random rotations add to the visual complexity, while the arrangement of frames emphasizes both verticality and horizontal connectivity. The model incorporates varying sizes and thicknesses, allowing light and shadow to play across the surfaces, thereby reinforcing the metaphor's themes of fluidity and layered depth, which guide the observer through interconnected spaces."""

#! python 3
function_code = """def create_cascading_frames_model(frame_count=5, frame_base_size=5.0, frame_height=3.0, frame_thickness=0.3, frame_offset=1.0):
    \"""
    Creates an architectural Concept Model based on the 'Cascading frames' metaphor. The function generates a series of overlapping frames that vary in size and orientation to create a sense of movement and depth.

    Parameters:
    - frame_count (int): The number of frames to generate.
    - frame_base_size (float): The base size of the frames in meters.
    - frame_height (float): The height of each frame in meters.
    - frame_thickness (float): The thickness of each frame in meters.
    - frame_offset (float): The offset distance between successive frames in meters.

    Returns:
    - List of RhinoCommon Brep objects representing the frames in 3D space.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(42)  # Ensure replicability

    frames = []

    for i in range(frame_count):
        # Calculate the transformation parameters
        scale_factor = 1.0 - (i * 0.1)  # Reduce size progressively
        angle = random.uniform(-10, 10)  # Random orientation for dynamic effect

        # Create a base rectangle for the frame
        base_rect = rg.Rectangle3d(rg.Plane.WorldXY, frame_base_size * scale_factor, frame_height)

        # Extrude the rectangle to create a frame
        extrusion_vector = rg.Vector3d(0, 0, frame_thickness)
        frame_brep = rg.Brep.CreateFromBox(base_rect.BoundingBox)
        if frame_brep:
            frame_brep.Transform(rg.Transform.Translation(0, 0, i * frame_offset))

            # Rotate the frame to create cascading effect
            rotation_transform = rg.Transform.Rotation(rg.RhinoMath.ToRadians(angle), rg.Vector3d.ZAxis, rg.Point3d.Origin)
            frame_brep.Transform(rotation_transform)

            # Add to the list of frames
            frames.append(frame_brep)

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(frame_count=10, frame_base_size=6.0, frame_height=4.0, frame_thickness=0.5, frame_offset=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(frame_count=7, frame_base_size=4.0, frame_height=2.5, frame_thickness=0.2, frame_offset=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(frame_count=8, frame_base_size=5.5, frame_height=3.5, frame_thickness=0.4, frame_offset=1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(frame_count=6, frame_base_size=5.0, frame_height=3.0, frame_thickness=0.25, frame_offset=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(frame_count=9, frame_base_size=7.0, frame_height=5.0, frame_thickness=0.6, frame_offset=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
