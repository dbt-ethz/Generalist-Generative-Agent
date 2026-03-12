# Created for 0017_0001_cascading_frames.json

""" Summary:
The function `create_cascading_frames_model` generates an architectural concept model inspired by the metaphor of "cascading frames." It constructs a series of 3D frames, each tier slightly smaller and offset, evoking a sense of layered depth and dynamic progression. The parameters allow for customization of frame dimensions, thickness, and heights, enabling the design to embody fluidity and movement. As frames stack, they create intricate interactions of light and shadow, enhancing visual complexity and spatial continuity. The resulting geometries are suitable for architectural visualization, emphasizing verticality and connectivity, thereby aligning with the metaphor's essence."""

#! python 3
function_code = """def create_cascading_frames_model(base_width=8, base_depth=6, num_frames=5, frame_thickness=0.3, frame_height=3):
    \"""
    Creates a cascading frames architectural concept model.

    Parameters:
    - base_width (float): The width of the base frame in meters.
    - base_depth (float): The depth of the base frame in meters.
    - num_frames (int): The number of cascading frames to create.
    - frame_thickness (float): The thickness of each frame.
    - frame_height (float): The height of each frame tier.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the cascading frames.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Point3d, Box, Brep, Interval, Plane

    # Set a seed for randomness
    random.seed(42)
    
    # List to hold the breps
    breps = []

    # Base point for the first frame
    base_point = Point3d(0, 0, 0)

    # Create each frame
    for i in range(num_frames):
        # Calculate frame dimensions
        width = base_width - (i * frame_thickness * 0.5)
        depth = base_depth - (i * frame_thickness * 0.5)
        height = frame_height
        
        # Random offset for cascading effect
        offset_x = random.uniform(-0.5, 0.5) * frame_thickness
        offset_y = random.uniform(-0.5, 0.5) * frame_thickness
        
        # Create the bounding box for the frame
        corner1 = Point3d(base_point.X + offset_x, base_point.Y + offset_y, base_point.Z + i * height)
        corner2 = Point3d(corner1.X + width, corner1.Y + depth, corner1.Z + height)
        
        # Create a box as a frame
        box = Box(Plane.WorldXY,
                  Interval(corner1.X, corner2.X),
                  Interval(corner1.Y, corner2.Y),
                  Interval(corner1.Z, corner2.Z))
        
        # Create Brep from the box
        brep = box.ToBrep()
        breps.append(brep)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(base_width=10, base_depth=7, num_frames=4, frame_thickness=0.2, frame_height=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(base_width=12, base_depth=8, num_frames=6, frame_thickness=0.4, frame_height=3.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(base_width=9, base_depth=5, num_frames=3, frame_thickness=0.25, frame_height=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(base_width=11, base_depth=9, num_frames=7, frame_thickness=0.35, frame_height=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(base_width=15, base_depth=10, num_frames=8, frame_thickness=0.5, frame_height=3.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
