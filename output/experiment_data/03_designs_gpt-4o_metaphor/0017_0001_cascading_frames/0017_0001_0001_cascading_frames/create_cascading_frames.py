# Created for 0017_0001_cascading_frames.json

""" Summary:
The provided function, `create_cascading_frames`, generates an architectural concept model based on the metaphor of "cascading frames." It constructs a series of hollow, tiered frames that reflect dynamic progression and layered depth, consistent with the metaphor's emphasis on fluidity and spatial continuity. Each frame is created with diminishing dimensions and offset vertically, enhancing the interplay of light and shadow. By varying the number of frames, their dimensions, and offsets, the function achieves visual complexity and connectivity, guiding the observer's eye through a structured sequence of spaces that embody the essence of cascading movement in architecture."""

#! python 3
function_code = """def create_cascading_frames(base_width, base_depth, height, frame_thickness, num_frames, offset_factor):
    \"""
    Creates a cascading frames concept model representing dynamic progression and layered depth,
    where frames are organized in successive tiers with varying offsets.
    
    Parameters:
    - base_width: float, the width of the largest frame at the base in meters.
    - base_depth: float, the depth of the largest frame at the base in meters.
    - height: float, total height of the cascading frames in meters.
    - frame_thickness: float, thickness of each frame in meters.
    - num_frames: int, the number of frames to create.
    - offset_factor: float, factor by which each subsequent frame is offset from the previous one.
    
    Returns:
    - List of Rhino.Geometry.Brep objects representing the frames.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set a seed for random generation
    random.seed(42)
    
    # Calculate the height of each frame tier
    frame_height = height / num_frames
    
    # Initialize list to store the frame geometries
    frames = []
    
    # Create each frame
    for i in range(num_frames):
        # Calculate dimensions for each frame
        current_width = base_width - i * offset_factor
        current_depth = base_depth - i * offset_factor
        
        # Create the base rectangle
        base_rect = rg.Rectangle3d(rg.Plane.WorldXY, current_width, current_depth)
        
        # Extrude to create the frame volume
        frame_volume = rg.Extrusion.Create(base_rect.ToNurbsCurve(), frame_height, True)
        
        # Define void space inside the frame by scaling down the rectangle
        inner_width = current_width - 2 * frame_thickness
        inner_depth = current_depth - 2 * frame_thickness
        inner_rect = rg.Rectangle3d(rg.Plane.WorldXY, inner_width, inner_depth)
        void_volume = rg.Extrusion.Create(inner_rect.ToNurbsCurve(), frame_height, True)
        
        # Subtract the void from the frame to create a hollow frame
        hollow_frame = rg.Brep.CreateBooleanDifference(frame_volume.ToBrep(), void_volume.ToBrep(), 0.01)
        
        # Move the frame up to its correct position
        move_vector = rg.Vector3d(0, 0, i * frame_height)
        transform = rg.Transform.Translation(move_vector)
        for brep in hollow_frame:
            brep.Transform(transform)
            frames.append(brep)
    
    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames(5.0, 3.0, 10.0, 0.2, 5, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames(4.0, 2.5, 8.0, 0.15, 6, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames(6.0, 4.0, 12.0, 0.25, 4, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames(7.0, 5.0, 15.0, 0.3, 3, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames(8.0, 6.0, 20.0, 0.4, 7, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
