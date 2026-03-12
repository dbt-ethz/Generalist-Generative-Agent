# Created for 0017_0002_cascading_frames.json

""" Summary:
The function `create_dynamic_cascading_frames` generates an architectural concept model inspired by the metaphor "Cascading frames." It constructs a series of interlocking frames that vary in rotation and horizontal shift, embodying fluidity and dynamic progression. Each frame is defined by specific dimensions and thickness, emphasizing vertical continuity. The function employs randomization to create rhythmic patterns and an interplay of light and shadow, enhancing the visual complexity of the design. By organizing these frames in a layered manner, the model guides viewers through interconnected spaces, reinforcing the metaphor's themes of movement, connectivity, and architectural depth."""

#! python 3
function_code = """def create_dynamic_cascading_frames(frame_count=8, base_width=8.0, base_height=4.0, frame_thickness=0.3, max_rotation=15.0, max_shift=0.8):
    \"""
    Creates an architectural Concept Model based on the 'Cascading frames' metaphor.
    
    This function generates a series of interlocking frames with varying rotations and shifts,
    emphasizing fluidity and dynamic progression. The frames are designed to create a rhythmic
    pattern with an interplay of light and shadow, enhancing vertical continuity and movement.
    
    Parameters:
    - frame_count (int): The number of cascading frames.
    - base_width (float): The width of the base frame in meters.
    - base_height (float): The height of the base frame in meters.
    - frame_thickness (float): The thickness of each frame in meters.
    - max_rotation (float): The maximum rotation angle in degrees for each frame.
    - max_shift (float): The maximum horizontal shift in meters for each frame.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of brep geometries representing the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    random.seed(42)  # Ensure replicability
    
    frames = []
    current_z = 0
    
    for i in range(frame_count):
        # Define the rotation and shift
        rotation_angle = random.uniform(-max_rotation, max_rotation)
        shift_amount = random.uniform(-max_shift, max_shift)
        
        # Create a basic rectangular frame
        plane = rg.Plane.WorldXY
        plane.OriginZ = current_z
        base_rectangle = rg.Rectangle3d(plane, base_width, base_height)
        
        # Offset the rectangle to create a frame outline
        outer_curve = base_rectangle.ToNurbsCurve()
        inner_curve = outer_curve.Offset(plane, -frame_thickness, 0.01, rg.CurveOffsetCornerStyle.Sharp)[0]
        frame_surface = rg.Brep.CreatePlanarBreps([outer_curve, inner_curve])[0]
        
        # Transformations for rotation and shift
        rotation_radians = math.radians(rotation_angle)
        pivot_point = rg.Point3d(base_width / 2, base_height / 2, current_z)
        rotation_transform = rg.Transform.Rotation(rotation_radians, rg.Vector3d.ZAxis, pivot_point)
        shift_transform = rg.Transform.Translation(shift_amount, 0, 0)
        
        # Apply transformations
        frame_surface.Transform(rotation_transform)
        frame_surface.Transform(shift_transform)
        
        # Add frame to the list
        frames.append(frame_surface)
        
        # Update the z-coordinate for the next frame
        current_z += base_height
    
    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dynamic_cascading_frames(frame_count=10, base_width=5.0, base_height=2.5, frame_thickness=0.2, max_rotation=20.0, max_shift=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dynamic_cascading_frames(frame_count=12, base_width=6.0, base_height=3.0, frame_thickness=0.4, max_rotation=10.0, max_shift=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dynamic_cascading_frames(frame_count=15, base_width=7.0, base_height=3.5, frame_thickness=0.25, max_rotation=12.0, max_shift=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dynamic_cascading_frames(frame_count=5, base_width=4.0, base_height=2.0, frame_thickness=0.15, max_rotation=25.0, max_shift=0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dynamic_cascading_frames(frame_count=9, base_width=9.0, base_height=4.5, frame_thickness=0.35, max_rotation=18.0, max_shift=0.9)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
