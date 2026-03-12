# Created for 0017_0002_cascading_frames.json

""" Summary:
The function `create_dynamic_cascading_frames` generates an architectural concept model inspired by the metaphor "Cascading frames." It creates a series of interlocking frames, each with unique variations in height, depth, and rotation, to embody fluidity and dynamic progression. The frames are arranged in a rhythmic pattern, emphasizing verticality and movement while allowing for an engaging interplay of light and shadow. Each frame acts as a spatial threshold, guiding the viewer through interconnected spaces. By manipulating parameters like rotation and depth, the model captures the metaphor's essence, showcasing architectural complexity and connectivity."""

#! python 3
function_code = """def create_dynamic_cascading_frames(frame_count=8, base_width=5.0, base_height=3.0, depth_variation=1.0, max_rotation=15.0, shift_step=2.0):
    \"""
    Creates a dynamic architectural Concept Model based on the 'Cascading frames' metaphor.
    
    This function generates a series of interlocking frames, each with slight variations in height, depth, and rotation to 
    create a fluid, dynamic progression. The frames form a rhythmic pattern of repetition and variation, emphasizing verticality
    and movement. The model aims to enhance light and shadow interplay through varied geometries.
    
    Parameters:
    - frame_count (int): Number of cascading frames to generate.
    - base_width (float): The width of the base frame in meters.
    - base_height (float): The average height of the frames in meters.
    - depth_variation (float): The maximum variation in depth for the frames in meters.
    - max_rotation (float): The maximum rotation angle in degrees for each frame.
    - shift_step (float): The step distance in meters for shifting each subsequent frame.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensure replicability

    frames = []
    current_shift = 0.0

    for i in range(frame_count):
        # Calculate random variations
        height_variation = random.uniform(-0.5, 0.5) * base_height
        current_height = base_height + height_variation
        current_depth = random.uniform(0.5, depth_variation)
        rotation_angle = random.uniform(-max_rotation, max_rotation)

        # Create a base rectangle for the frame
        plane = rg.Plane.WorldXY
        plane.OriginZ = i * (base_height + 0.5)  # Add space between frames
        rect = rg.Rectangle3d(plane, base_width, current_height)

        # Extrude the rectangle to create a frame
        extrusion_vector = rg.Vector3d(0, 0, current_depth)
        frame_brep = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(rect.ToNurbsCurve(), extrusion_vector))
        
        # Apply rotation
        rotation_center = rg.Point3d(base_width / 2, current_height / 2, plane.OriginZ)
        rotation_transform = rg.Transform.Rotation(math.radians(rotation_angle), rg.Vector3d.ZAxis, rotation_center)
        frame_brep.Transform(rotation_transform)

        # Apply shift
        current_shift += shift_step
        shift_transform = rg.Transform.Translation(current_shift, 0, 0)
        frame_brep.Transform(shift_transform)

        frames.append(frame_brep)

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dynamic_cascading_frames(frame_count=10, base_width=6.0, base_height=4.0, depth_variation=2.0, max_rotation=20.0, shift_step=3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dynamic_cascading_frames(frame_count=5, base_width=4.0, base_height=2.5, depth_variation=1.5, max_rotation=10.0, shift_step=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dynamic_cascading_frames(frame_count=12, base_width=7.0, base_height=5.0, depth_variation=1.2, max_rotation=25.0, shift_step=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dynamic_cascading_frames(frame_count=15, base_width=5.5, base_height=3.5, depth_variation=1.0, max_rotation=18.0, shift_step=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dynamic_cascading_frames(frame_count=6, base_width=8.0, base_height=4.5, depth_variation=3.0, max_rotation=12.0, shift_step=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
