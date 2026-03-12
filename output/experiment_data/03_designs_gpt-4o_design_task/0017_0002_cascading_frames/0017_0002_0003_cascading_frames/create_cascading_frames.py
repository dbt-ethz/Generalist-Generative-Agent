# Created for 0017_0002_cascading_frames.json

""" Summary:
The function `create_cascading_frames` generates an architectural concept model based on the metaphor "Cascading frames." It constructs a series of interlocking frames, each with random rotations and shifts, to evoke dynamic progression and layered depth. By adjusting frame dimensions, heights, and spatial relationships, the model emphasizes verticality and movement, creating a rhythmic pattern. The interplay of light and shadow is highlighted through varying angles and materials, guiding observers through interconnected spaces. This approach captures the essence of the metaphor, enabling a visually engaging journey that reflects fluidity and connectivity within the architectural design."""

#! python 3
function_code = """def create_cascading_frames(width, depth, frame_count, max_rotation, max_shift):
    \"""
    Creates an architectural Concept Model of 'Cascading frames', emphasizing dynamic progression and continuity.
    
    Parameters:
    - width (float): The width of each frame.
    - depth (float): The depth of each frame.
    - frame_count (int): The number of frames to generate.
    - max_rotation (float): The maximum rotation angle in degrees for each frame.
    - max_shift (float): The maximum shift distance for each frame.

    Returns:
    - List of RhinoCommon Breps representing the 3D geometries of the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensure replicability

    breps = []
    base_height = 3  # Base height of each frame
    vertical_spacing = 0.5  # Vertical space between frames

    for i in range(frame_count):
        # Calculate rotation and shift
        rotation_angle = random.uniform(-max_rotation, max_rotation)
        shift_distance = random.uniform(0, max_shift)

        # Create a base plane
        plane = rg.Plane.WorldXY
        plane.OriginZ = i * (base_height + vertical_spacing)

        # Create a basic frame as a box
        box = rg.Box(plane, rg.Interval(-width / 2, width / 2), rg.Interval(-depth / 2, depth / 2), rg.Interval(0, base_height))
        
        # Rotate the box
        rotation_radians = math.radians(rotation_angle)
        rotated_box = box.ToBrep()
        rotation_axis = rg.Line(plane.Origin, plane.ZAxis * (base_height + vertical_spacing)).ToNurbsCurve()
        transform_rotation = rg.Transform.Rotation(rotation_radians, plane.ZAxis, plane.Origin)
        rotated_box.Transform(transform_rotation)

        # Shift the box
        transform_translation = rg.Transform.Translation(plane.XAxis * shift_distance)
        rotated_box.Transform(transform_translation)

        # Add to the list of Breps
        breps.append(rotated_box)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames(2.0, 1.0, 10, 30, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames(1.5, 0.8, 5, 45, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames(3.0, 2.0, 8, 60, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames(2.5, 1.2, 6, 50, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames(1.0, 0.5, 12, 20, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
