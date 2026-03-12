# Created for 0017_0002_cascading_frames.json

""" Summary:
The function `create_cascading_frames` generates an architectural concept model based on the metaphor of "Cascading frames" by producing a series of interlocking frames. Each frame is slightly rotated and shifted upwards, creating a dynamic sense of movement and continuity. This arrangement establishes a rhythmic pattern while emphasizing verticality and the play of light and shadow. By allowing for variations in frame dimensions and rotational angles, the model captures the metaphor's essence, guiding viewers through interconnected spaces. Ultimately, this process reflects the metaphors themes of fluidity, depth, and spatial connectivity within the architectural design."""

#! python 3
function_code = """def create_cascading_frames(num_frames=10, frame_width=2.0, frame_height=5.0, frame_depth=0.5, rotation_angle=5.0, shift_amount=1.0):
    \"""
    Creates an architectural concept model based on the 'Cascading frames' metaphor.
    
    This function generates a series of interlocking frames, each slightly rotated or shifted to suggest fluidity 
    and dynamic progression. The frames create a rhythmic pattern of repetition and variation, emphasizing vertical 
    continuity and movement. The interplay of light and shadow is enhanced by varying heights and angles.
    
    Inputs:
        num_frames (int): The number of cascading frames to create.
        frame_width (float): The width of each frame in meters.
        frame_height (float): The height of each frame in meters.
        frame_depth (float): The depth (thickness) of each frame in meters.
        rotation_angle (float): The angle in degrees by which each subsequent frame is rotated.
        shift_amount (float): The amount in meters by which each subsequent frame is shifted vertically.
    
    Returns:
        List[Rhino.Geometry.Brep]: A list of brep geometries representing the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    random.seed(42)  # Ensure replicability
    
    frames = []
    base_point = rg.Point3d(0, 0, 0)
    
    for i in range(num_frames):
        # Create a base rectangle to represent the frame
        plane = rg.Plane(base_point, rg.Vector3d.ZAxis)
        rectangle = rg.Rectangle3d(plane, frame_width, frame_height)
        
        # Create the frame as a brep (extruded rectangle)
        extrusion_vector = rg.Vector3d(0, 0, frame_depth)
        frame = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(rectangle.ToNurbsCurve(), extrusion_vector))
        
        # Apply rotation and translation to create cascading effect
        angle_rad = math.radians(rotation_angle * i)
        rotation = rg.Transform.Rotation(angle_rad, rg.Vector3d.ZAxis, base_point)
        translation = rg.Transform.Translation(0, 0, shift_amount * i)
        
        frame.Transform(rotation)
        frame.Transform(translation)
        
        frames.append(frame)
        
        # Move the base point for the next frame
        base_point.Z += shift_amount
    
    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames(num_frames=15, frame_width=3.0, frame_height=6.0, frame_depth=0.5, rotation_angle=10.0, shift_amount=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames(num_frames=8, frame_width=1.5, frame_height=4.0, frame_depth=0.3, rotation_angle=7.0, shift_amount=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames(num_frames=12, frame_width=2.5, frame_height=5.5, frame_depth=0.4, rotation_angle=8.0, shift_amount=1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames(num_frames=20, frame_width=2.0, frame_height=7.0, frame_depth=0.6, rotation_angle=15.0, shift_amount=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames(num_frames=10, frame_width=2.5, frame_height=5.0, frame_depth=0.7, rotation_angle=12.0, shift_amount=1.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
