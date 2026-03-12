# Created for 0017_0005_cascading_frames.json

""" Summary:
The function `create_cascading_frames_model` generates an architectural concept model inspired by the metaphor "Cascading frames." It constructs a series of frames that vary in scale and orientation, creating a dynamic, stepped form that emphasizes both verticality and connectivity. Each frame is designed with a specific base size, thickness, and offset to achieve the cascading effect. Random rotations enhance visual interest, contributing to a complex interplay of light and shadow. The resulting model guides observers through interconnected spaces, promoting interaction with the environment and reinforcing the sense of movement, aligning with the metaphors implications."""

#! python 3
function_code = """def create_cascading_frames_model(base_frame_size, frame_count, frame_thickness, step_offset, rotation_variability):
    \"""
    Creates an architectural Concept Model based on the 'Cascading frames' metaphor, using a series of frames
    varying in scale, orientation, and position to create a stepped, dynamic form. The frames cascade to emphasize
    verticality and lateral connectivity, guiding the observer through a sequence of interconnected spaces.

    Parameters:
    - base_frame_size (float): The size of the first frame, setting a base scale for the model.
    - frame_count (int): The number of frames to generate in the cascading sequence.
    - frame_thickness (float): The thickness of each frame.
    - step_offset (float): The offset distance between successive frames, determining the cascading effect.
    - rotation_variability (float): The maximum angle in degrees by which each frame can be randomly rotated.

    Returns:
    - List of Rhino.Geometry.Brep: A list of 3D brep geometries representing the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    random.seed(42)  # Ensures replicable results

    frames = []

    for i in range(frame_count):
        # Calculate the scale factor for the current frame
        scale_factor = 1 + (i * 0.1)

        # Create the base frame rectangle
        frame_size = base_frame_size * scale_factor
        rectangle = rg.Rectangle3d(rg.Plane.WorldXY, frame_size, frame_size)

        # Convert the rectangle to a surface and then to a brep
        surface = rg.Surface.CreateExtrusion(rectangle.ToNurbsCurve(), rg.Vector3d(0, 0, frame_thickness))
        frame_brep = surface.ToBrep()

        # Apply a random rotation around the Z-axis
        rotation_angle = random.uniform(-rotation_variability, rotation_variability)
        rotation = rg.Transform.Rotation(math.radians(rotation_angle), rg.Vector3d.ZAxis, rg.Point3d.Origin)
        frame_brep.Transform(rotation)

        # Move the frame to its cascading position
        translation = rg.Transform.Translation(0, 0, i * step_offset)
        frame_brep.Transform(translation)

        frames.append(frame_brep)

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(10.0, 5, 2.0, 3.0, 15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(8.0, 7, 1.5, 2.5, 20.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(12.0, 4, 3.0, 4.0, 10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(15.0, 6, 2.5, 3.5, 25.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(9.0, 8, 1.0, 2.0, 30.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
