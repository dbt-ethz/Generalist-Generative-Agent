# Created for 0017_0005_cascading_frames.json

""" Summary:
The function `create_cascading_frames_model_v2` generates an architectural concept model based on the metaphor "Cascading frames" by creating a series of layered frames with varying scales and orientations. It employs parameters like frame height, spacing, and random scaling to produce a stepped form that embodies verticality and continuity. Each frame serves as a spatial connector, guiding the observer through interconnected spaces while enhancing light and shadow interplay. The model emphasizes movement and depth, allowing for dynamic visual rhythms and sheltered outdoor areas, thereby fostering interaction with the environment and responding to contextual factors."""

#! python 3
function_code = """def create_cascading_frames_model_v2(base_plane_size, frame_height, frame_thickness, number_of_frames, vertical_spacing, horizontal_spacing, seed=123):
    \"""
    Creates an architectural concept model based on the 'Cascading frames' metaphor by generating a series of 
    frames with varying scales and orientations. The frames are constructed to create a stepped or tiered form, 
    emphasizing both vertical and horizontal continuity.

    Parameters:
    - base_plane_size (float): The size of the base plane for the frames in meters.
    - frame_height (float): The height of each frame in meters.
    - frame_thickness (float): The thickness of each frame in meters.
    - number_of_frames (int): The total number of frames to generate.
    - vertical_spacing (float): The vertical spacing between frames in meters.
    - horizontal_spacing (float): The horizontal spacing between frames in meters.
    - seed (int): Seed for random variations to ensure reproducibility.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    
    frames = []
    
    for i in range(number_of_frames):
        # Calculate position offsets
        x_offset = horizontal_spacing * i
        z_offset = vertical_spacing * i
        
        # Randomly vary the scale
        scale_factor_x = random.uniform(0.9, 1.1)
        scale_factor_y = random.uniform(0.9, 1.1)
        
        # Define the base plane for the frame
        base_plane = rg.Plane(rg.Point3d(x_offset, 0, z_offset), rg.Vector3d(0, 0, 1))
        
        # Create a rectangle as frame boundary
        frame_rect = rg.Rectangle3d(base_plane, base_plane_size * scale_factor_x, frame_height * scale_factor_y)
        
        # Offset the rectangle to create a frame outline
        offset_curve = frame_rect.ToNurbsCurve().Offset(base_plane, frame_thickness, 0.01, rg.CurveOffsetCornerStyle.Sharp)[0]
        
        # Loft between the original and offset curve to create the frame
        loft = rg.Brep.CreateFromLoft([frame_rect.ToNurbsCurve(), offset_curve], base_plane.Origin, base_plane.Origin, rg.LoftType.Straight, False)
        
        if loft:
            frame_brep = loft[0]
            frames.append(frame_brep)
    
    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model_v2(5.0, 3.0, 0.2, 10, 1.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model_v2(4.0, 2.5, 0.15, 8, 0.8, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model_v2(6.0, 4.0, 0.25, 12, 1.5, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model_v2(7.0, 5.0, 0.3, 15, 2.0, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model_v2(3.0, 2.0, 0.1, 5, 0.5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
