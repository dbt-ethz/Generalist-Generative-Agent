# Created for 0017_0002_cascading_frames.json

""" Summary:
The function `create_dynamic_cascading_frames` generates an architectural concept model based on the metaphor "Cascading frames." It creates a series of interlocking frames that are slightly rotated and vertically shifted, evoking fluidity and dynamic progression. By varying the widths, heights, and angles of the frames, the design emphasizes vertical continuity and movement. Each frame acts as a spatial threshold, guiding the viewer through a sequence of interconnected spaces. The interplay of light and shadow is enhanced through these variations, creating a visually engaging structure that reflects the metaphors essence of dynamic layering and connectivity within architectural form."""

#! python 3
function_code = """def create_dynamic_cascading_frames(num_frames=10, base_width=8.0, base_height=4.0, base_depth=0.5, max_angle_shift=10.0, max_vertical_shift=0.3):
    \"""
    Generates an architectural Concept Model inspired by the 'Cascading frames' metaphor.

    This function creates a series of interlocking frames, each slightly rotated or shifted to evoke 
    fluidity and dynamic progression. The design emphasizes verticality and movement, enhancing the 
    interplay of light and shadow with varied heights and angles in a rhythmic pattern.

    Parameters:
        num_frames (int): The number of cascading frames to create.
        base_width (float): The width of each frame in meters.
        base_height (float): The height of each frame in meters.
        base_depth (float): The depth (thickness) of each frame in meters.
        max_angle_shift (float): The maximum angle in degrees by which each subsequent frame is rotated.
        max_vertical_shift (float): The maximum vertical shift in meters for each subsequent frame.

    Returns:
        List[Rhino.Geometry.Brep]: A list of brep geometries representing the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensure replicability

    frames = []
    current_height = 0
    base_point = rg.Point3d(0, 0, 0)

    for i in range(num_frames):
        # Define the base rectangle for each frame
        plane = rg.Plane(base_point, rg.Vector3d.ZAxis)
        rectangle = rg.Rectangle3d(plane, base_width, base_height)

        # Create the frame as a brep by extruding the rectangle
        extrusion_vector = rg.Vector3d(0, 0, base_depth)
        frame = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(rectangle.ToNurbsCurve(), extrusion_vector))
        
        # Calculate rotation and translation for dynamic effect
        angle_shift = random.uniform(-max_angle_shift, max_angle_shift)
        vertical_shift = random.uniform(0, max_vertical_shift)
        
        angle_rad = math.radians(angle_shift)
        rotation = rg.Transform.Rotation(angle_rad, rg.Vector3d.ZAxis, base_point)
        translation = rg.Transform.Translation(0, 0, current_height + vertical_shift)
        
        frame.Transform(rotation)
        frame.Transform(translation)

        frames.append(frame)
        
        # Update the current height for the next frame
        current_height += base_height + vertical_shift
        base_point.Z += base_height + vertical_shift

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dynamic_cascading_frames(num_frames=15, base_width=10.0, base_height=5.0, base_depth=0.6, max_angle_shift=15.0, max_vertical_shift=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dynamic_cascading_frames(num_frames=12, base_width=9.0, base_height=6.0, base_depth=0.4, max_angle_shift=20.0, max_vertical_shift=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dynamic_cascading_frames(num_frames=20, base_width=7.5, base_height=3.5, base_depth=0.7, max_angle_shift=12.0, max_vertical_shift=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dynamic_cascading_frames(num_frames=8, base_width=11.0, base_height=4.5, base_depth=0.8, max_angle_shift=8.0, max_vertical_shift=0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dynamic_cascading_frames(num_frames=18, base_width=8.5, base_height=4.0, base_depth=0.3, max_angle_shift=25.0, max_vertical_shift=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
