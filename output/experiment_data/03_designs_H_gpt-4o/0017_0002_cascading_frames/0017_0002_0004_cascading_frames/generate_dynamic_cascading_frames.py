# Created for 0017_0002_cascading_frames.json

""" Summary:
The function `generate_dynamic_cascading_frames` creates an architectural concept model by generating a series of interlocking frames that embody the metaphor "Cascading frames." Each frame is designed with variable heights and rotational shifts, promoting a sense of fluidity and dynamic progression. The frames arrangement emphasizes vertical continuity, creating a rhythmic pattern that enhances the visual interplay of light and shadow. By adjusting parameters like frame count, width, depth, and rotation, the function produces a visually engaging model that guides observers through interconnected spaces, reflecting the metaphor's essence of movement and connectivity within the architectural design."""

#! python 3
function_code = """def generate_dynamic_cascading_frames(frame_count=7, base_width=4.0, base_depth=0.3, height_variation=0.8, rotation_seed=15.0):
    \"""
    Generates a dynamic architectural Concept Model based on the 'Cascading frames' metaphor.

    This function creates a series of interlocking frames that cascade with varying rotations and heights,
    suggesting movement and progression. The frames create a complex interplay of light and shadow.

    Parameters:
        frame_count (int): The number of cascading frames to generate.
        base_width (float): The width of each frame in meters.
        base_depth (float): The depth (thickness) of each frame in meters.
        height_variation (float): The maximum variation in height for each frame in meters.
        rotation_seed (float): The seed for rotation angle variation in degrees.

    Returns:
        List[Rhino.Geometry.Brep]: A list of brep geometries representing the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensure replicability

    frames = []
    current_height = 0
    plane = rg.Plane.WorldXY

    for i in range(frame_count):
        # Calculate randomized height and rotation
        frame_height = base_width + random.uniform(-height_variation, height_variation)
        rotation_angle = random.uniform(-rotation_seed, rotation_seed)

        # Create the base rectangle for the frame
        rectangle = rg.Rectangle3d(plane, base_width, frame_height)

        # Extrude the rectangle to create a frame
        extrusion_vector = rg.Vector3d(0, 0, base_depth)
        frame_brep = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(rectangle.ToNurbsCurve(), extrusion_vector))

        # Apply rotation to the frame
        rotation_radians = math.radians(rotation_angle)
        rotation_transform = rg.Transform.Rotation(rotation_radians, rg.Vector3d.ZAxis, plane.Origin)
        frame_brep.Transform(rotation_transform)

        # Move the plane for the next frame
        translate_height = rg.Transform.Translation(rg.Vector3d(0, 0, base_depth + frame_height * 0.2))
        plane.Transform(translate_height)

        # Add the frame to the list
        frames.append(frame_brep)

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_dynamic_cascading_frames(frame_count=10, base_width=5.0, base_depth=0.4, height_variation=1.0, rotation_seed=20.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_dynamic_cascading_frames(frame_count=5, base_width=3.0, base_depth=0.5, height_variation=0.5, rotation_seed=10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_dynamic_cascading_frames(frame_count=8, base_width=6.0, base_depth=0.2, height_variation=0.6, rotation_seed=12.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_dynamic_cascading_frames(frame_count=12, base_width=4.5, base_depth=0.25, height_variation=0.9, rotation_seed=18.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_dynamic_cascading_frames(frame_count=6, base_width=4.0, base_depth=0.3, height_variation=0.7, rotation_seed=25.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
