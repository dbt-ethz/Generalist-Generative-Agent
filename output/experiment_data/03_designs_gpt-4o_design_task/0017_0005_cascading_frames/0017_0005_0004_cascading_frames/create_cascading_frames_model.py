# Created for 0017_0005_cascading_frames.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor "Cascading frames." It creates a series of 3D frames that vary in size and orientation, arranged in a sequential, tiered formation to evoke dynamic movement and depth. Each frame is generated with random scaling factors and is positioned using translation vectors, reinforcing the idea of layers and connectivity between spaces. The design emphasizes verticality and horizontal continuity, allowing for light and shadow interplay, while guiding the observer through a sequence of interconnected spaces. This model visually embodies the metaphor, enhancing engagement with the environment."""

#! python 3
function_code = """def create_cascading_frames_model(base_frame_count=5, frame_distance=3.0, frame_size_variation=1.5, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'Cascading frames' metaphor.
    
    The model consists of a series of frames that vary in scale and orientation, creating a stepped or tiered form.
    This design emphasizes dynamic progression, layered depth, and spatial continuity.

    Parameters:
    - base_frame_count (int): The number of initial frames to generate.
    - frame_distance (float): The average distance between successive frames.
    - frame_size_variation (float): The factor by which frame sizes vary.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometry of the frames.
    \"""
    import random
    import Rhino.Geometry as rg

    # Set seed for randomness
    random.seed(seed)

    # Initialize list to store frame geometries
    frames = []

    # Base dimensions for the frames
    base_width = 4.0
    base_height = 3.0
    base_depth = 0.2

    # Generate each frame
    for i in range(base_frame_count):
        # Calculate random scale factors
        width_scale = 1.0 + (random.random() - 0.5) * frame_size_variation
        height_scale = 1.0 + (random.random() - 0.5) * frame_size_variation

        # Calculate frame dimensions
        width = base_width * width_scale
        height = base_height * height_scale

        # Create corner points for the frame
        p0 = rg.Point3d(0, 0, 0)
        p1 = rg.Point3d(width, 0, 0)
        p2 = rg.Point3d(width, height, 0)
        p3 = rg.Point3d(0, height, 0)

        # Create base rectangle
        base_rect = rg.Polyline([p0, p1, p2, p3, p0])

        # Create extrusion vector
        extrusion_vector = rg.Vector3d(0, 0, base_depth)

        # Offset the frame based on its index
        translate_vector = rg.Vector3d(i * frame_distance, i * frame_distance * 0.5, i * frame_distance * 0.3)
        base_rect.Transform(rg.Transform.Translation(translate_vector))

        # Create the frame by extruding the base rectangle
        frame_brep = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(base_rect.ToNurbsCurve(), extrusion_vector))
        frames.append(frame_brep)
    
    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(base_frame_count=7, frame_distance=2.5, frame_size_variation=1.0, seed=12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(base_frame_count=10, frame_distance=4.0, frame_size_variation=2.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(base_frame_count=6, frame_distance=3.5, frame_size_variation=1.2, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(base_frame_count=8, frame_distance=2.0, frame_size_variation=1.8, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(base_frame_count=5, frame_distance=3.0, frame_size_variation=1.5, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
