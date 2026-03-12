# Created for 0017_0002_cascading_frames.json

""" Summary:
The provided function generates an architectural concept model that embodies the "Cascading frames" metaphor by creating a series of interlocking frames that vary in height and rotation. Each frame is designed to evoke fluidity and dynamic progression, mimicking the layered, rhythmic patterns suggested by the metaphor. By adjusting parameters like height and rotation, the function emphasizes vertical continuity and enhances the interplay of light and shadow, creating a visually engaging structure. The resulting model guides the observer's journey through interconnected spaces, with each frame acting as a threshold that fosters movement and connectivity within the architectural design."""

#! python 3
function_code = """def create_dynamic_cascading_frames(frame_count=10, base_size=5.0, height_variation=2.0, rotation_variation=10.0):
    \"""
    Creates an architectural Concept Model based on the 'Cascading frames' metaphor, emphasizing dynamic progression and fluidity.

    This function generates a series of interlocking frames, each with variations in height and rotation to suggest a sense of movement and depth.
    The frames create a rhythmic pattern of repetition and variation, enhancing vertical continuity and the play of light and shadow.

    Parameters:
        frame_count (int): The number of cascading frames to create.
        base_size (float): The base size (width and depth) of each frame in meters.
        height_variation (float): The maximum variation in height for each frame in meters.
        rotation_variation (float): The maximum rotation angle in degrees for each frame.

    Returns:
        List[Rhino.Geometry.Brep]: A list of brep geometries representing the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensure replicability

    frames = []
    base_point = rg.Point3d(0, 0, 0)
    current_height = base_size

    for i in range(frame_count):
        # Determine random height and rotation for dynamic effect
        height = base_size + random.uniform(-height_variation, height_variation)
        rotation_angle = random.uniform(-rotation_variation, rotation_variation)

        # Create a base plane and rectangle
        plane = rg.Plane(base_point, rg.Vector3d.ZAxis)
        rectangle = rg.Rectangle3d(plane, base_size, height)

        # Create the frame as a brep (extruded rectangle)
        extrusion_vector = rg.Vector3d(0, 0, 0.5)  # Constant depth for each frame
        frame = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(rectangle.ToNurbsCurve(), extrusion_vector))

        # Apply rotation to create a dynamic cascading effect
        angle_rad = math.radians(rotation_angle)
        rotation = rg.Transform.Rotation(angle_rad, rg.Vector3d.ZAxis, base_point)
        frame.Transform(rotation)

        frames.append(frame)

        # Move the base point upwards for the next frame
        base_point.Z += height

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dynamic_cascading_frames(frame_count=15, base_size=6.0, height_variation=3.0, rotation_variation=15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dynamic_cascading_frames(frame_count=20, base_size=4.0, height_variation=1.5, rotation_variation=20.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dynamic_cascading_frames(frame_count=12, base_size=7.0, height_variation=2.5, rotation_variation=5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dynamic_cascading_frames(frame_count=8, base_size=5.5, height_variation=4.0, rotation_variation=12.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dynamic_cascading_frames(frame_count=10, base_size=5.0, height_variation=2.0, rotation_variation=8.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
