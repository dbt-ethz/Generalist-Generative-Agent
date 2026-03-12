# Created for 0017_0003_cascading_frames.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "Cascading frames" by creating a series of overlapping frames that vary in size, orientation, and height. It constructs each frame as a three-dimensional box with specific dimensions, applying random transformations to introduce dynamic movement and depth. The parameters allow control over frame attributes, such as thickness and height variation, enhancing the visual complexity and fluidity. The resulting model emphasizes verticality and horizontal connectivity, guiding the observer's experience through interconnected spaces while allowing light and shadow to interplay across the cascading layers."""

#! python 3
function_code = """def create_cascading_frames_model(num_frames=6, initial_width=12.0, initial_height=6.0, thickness=0.3, height_variation=1.0, angle_variation=10.0):
    \"""
    Creates an architectural Concept Model embodying the 'Cascading frames' metaphor by constructing a series of overlapping frames that vary in size and orientation.

    Parameters:
    - num_frames (int): Number of cascading frames to generate.
    - initial_width (float): Initial width of the frames in meters.
    - initial_height (float): Initial height of the frames in meters.
    - thickness (float): Thickness of each frame in meters.
    - height_variation (float): Maximum height variation between consecutive frames in meters.
    - angle_variation (float): Maximum angle variation for frame rotation in degrees.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # For replicability

    frames = []
    current_height = 0.0
    current_width = initial_width
    current_height_increment = initial_height

    for i in range(num_frames):
        # Create a base rectangle for the frame
        rectangle = rg.Rectangle3d(rg.Plane.WorldXY, current_width, current_height_increment)

        # Create thickness by extruding the rectangle
        extrusion_vector = rg.Vector3d(0, 0, thickness)
        frame_brep = rg.Brep.CreateFromBox(rg.BoundingBox(rectangle.Corner(0), rectangle.Corner(2) + extrusion_vector))

        if frame_brep:
            # Randomly adjust rotation and translation
            angle = random.uniform(-angle_variation, angle_variation)
            height_offset = random.uniform(-height_variation, height_variation)

            # Transformations
            rotation = rg.Transform.Rotation(math.radians(angle), rg.Vector3d.ZAxis, rg.Point3d.Origin)
            translation = rg.Transform.Translation(0, 0, current_height + height_offset)
            frame_brep.Transform(rotation)
            frame_brep.Transform(translation)

            # Add frame to the list
            frames.append(frame_brep)

            # Update for the next frame
            current_height += height_variation
            current_width *= 0.9  # Slight reduction for cascading effect
            current_height_increment *= 0.95  # Slight reduction in height

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(num_frames=8, initial_width=15.0, initial_height=7.0, thickness=0.5, height_variation=1.5, angle_variation=15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(num_frames=5, initial_width=10.0, initial_height=5.0, thickness=0.2, height_variation=0.8, angle_variation=5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(num_frames=10, initial_width=20.0, initial_height=10.0, thickness=0.4, height_variation=2.0, angle_variation=20.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(num_frames=7, initial_width=14.0, initial_height=8.0, thickness=0.6, height_variation=1.2, angle_variation=12.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(num_frames=6, initial_width=18.0, initial_height=9.0, thickness=0.3, height_variation=1.0, angle_variation=8.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
