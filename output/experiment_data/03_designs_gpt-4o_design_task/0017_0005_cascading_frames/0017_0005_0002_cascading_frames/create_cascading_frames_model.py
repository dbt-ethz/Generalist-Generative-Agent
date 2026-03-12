# Created for 0017_0005_cascading_frames.json

""" Summary:
The function `create_cascading_frames_model` generates an architectural concept model inspired by the metaphor "Cascading frames." It creates a series of 3D frames that vary in scale and orientation, simulating a layered, stepped arrangement. Each frame is scaled down sequentially, enhancing the cascading effect. The frames are extruded from rectangles, then translated and randomly rotated to create visual dynamism. This design emphasizes verticality and connectivity, facilitating movement through interconnected spaces. The interplay of light and shadow is enhanced by varying depths and orientations, aligning with the metaphor's intention to evoke fluidity and layered depth in architecture."""

#! python 3
function_code = """def create_cascading_frames_model(base_width, base_height, frame_count, frame_depth, frame_offset, seed=42):
    \"""
    Generates a series of cascading frames to create an architectural concept model based on the 'Cascading frames' metaphor.
    
    Parameters:
    - base_width (float): The base width of the largest frame in meters.
    - base_height (float): The base height of the largest frame in meters.
    - frame_count (int): The number of frames to generate.
    - frame_depth (float): The depth of each frame in meters.
    - frame_offset (float): The offset distance between consecutive frames in meters.
    - seed (int): A seed for the random number generator to ensure replicability.
    
    Returns:
    - List of Rhino.Geometry.Brep: A list of breps representing the 3D geometries of the frames.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    random.seed(seed)
    frames = []

    for i in range(frame_count):
        scale_factor = (frame_count - i) / frame_count  # Scale down for cascading effect
        width = base_width * scale_factor
        height = base_height * scale_factor

        # Create a rectangle for the frame
        plane = rg.Plane.WorldXY
        rect = rg.Rectangle3d(plane, width, height)
        
        # Extrude the rectangle to create a frame
        extrusion_vector = rg.Vector3d(0, 0, frame_depth)
        brep_frame = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(rect.ToNurbsCurve(), extrusion_vector))

        # Offset the frame
        translation_vector = rg.Vector3d(frame_offset * i, frame_offset * i, frame_offset * i)
        translated_brep = brep_frame.Duplicate()  # Ensure brep is duplicated before transformation
        translated_brep.Translate(translation_vector)
        
        # Apply a random rotation for dynamic orientation
        angle = random.uniform(-15, 15)  # Random angle in degrees
        rotation_axis = rg.Vector3d(0, 0, 1)  # Rotate around Z-axis
        rotation = rg.Transform.Rotation(math.radians(angle), rotation_axis, plane.Origin)
        translated_brep.Transform(rotation)
        
        frames.append(translated_brep)

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(10.0, 5.0, 7, 1.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(12.0, 6.0, 5, 0.8, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(15.0, 7.0, 10, 1.5, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(8.0, 4.0, 6, 1.2, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(9.0, 4.5, 8, 1.0, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
