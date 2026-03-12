# Created for 0017_0001_cascading_frames.json

""" Summary:
The function `create_cascading_frames_model` generates an architectural concept model inspired by the metaphor of "Cascading frames." It constructs a series of vertically stacked frames, each representing a tier in the design. The parameters allow for variability in width, height, spacing, and randomness, enhancing visual complexity. This cascading arrangement facilitates dynamic progression, creating layered depth that emphasizes light and shadow interplay. Each frame guides the viewers eye through a sequence of spaces, reinforcing verticality and spatial continuity. The output is a collection of 3D geometries that embodies the metaphor's essence in architectural form."""

#! python 3
function_code = """def create_cascading_frames_model(base_width, base_height, frame_count, frame_thickness, frame_spacing, randomness_seed):
    \"""
    Generate a conceptual architectural model using the "Cascading frames" metaphor.
    
    This function creates a series of frames that cascade vertically, with each frame 
    being a tier in the structure. The frames are organized to create a dynamic sense 
    of progression and layered depth, allowing for interplay of light and shadow.

    Parameters:
    - base_width: The width of the base frame (meters).
    - base_height: The height of the base frame (meters).
    - frame_count: The number of cascading frames.
    - frame_thickness: The thickness of each frame (meters).
    - frame_spacing: The vertical spacing between frames (meters).
    - randomness_seed: Seed for random variation in frame dimensions for visual complexity.
    
    Returns:
    - A list of 3D Brep geometries representing the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the randomness seed for reproducibility
    random.seed(randomness_seed)

    # List to store the frames
    frames = []

    # Calculate the initial position of the base frame
    current_z = 0

    for i in range(frame_count):
        # Introduce some randomness to the frame dimensions for complexity
        width_variation = base_width * (0.9 + 0.2 * random.random())
        height_variation = base_height * (0.9 + 0.2 * random.random())

        # Create a rectangle for the current frame
        corner1 = rg.Point3d(-width_variation / 2, -frame_thickness / 2, current_z)
        corner2 = rg.Point3d(width_variation / 2, frame_thickness / 2, current_z + height_variation)

        # Create a 3D box using a BoundingBox
        bbox = rg.BoundingBox(corner1, corner2)
        frame = rg.Box(bbox)

        # Convert the box to a Brep
        frame_brep = frame.ToBrep()

        # Append the Brep to the frames list
        frames.append(frame_brep)

        # Update the z-position for the next frame
        current_z += height_variation + frame_spacing

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(5, 3, 10, 0.2, 0.5, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(4, 2.5, 8, 0.15, 0.4, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(6, 4, 12, 0.25, 0.6, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(7, 5, 15, 0.3, 0.7, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(3, 2, 5, 0.1, 0.3, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
