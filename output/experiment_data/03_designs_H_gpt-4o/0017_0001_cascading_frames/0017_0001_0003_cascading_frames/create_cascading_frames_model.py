# Created for 0017_0001_cascading_frames.json

""" Summary:
The function `create_cascading_frames_model` generates an architectural concept model inspired by the metaphor "Cascading frames." It creates a series of tiered frames, each progressively higher and rotated to suggest movement and fluidity. By adjusting dimensions and materials, the design emphasizes verticality, connectivity, and the interplay of light and shadow. The staggered arrangement of frames creates a dynamic silhouette that guides the observer's view, reflecting the metaphor's essence of layered depth and spatial continuity. This approach also facilitates a visual narrative, enhancing the architectural experience by fostering fluid transitions between spaces."""

#! python 3
function_code = """def create_cascading_frames_model(base_width, base_depth, frame_height, num_frames, rotation_angle, material_variation):
    \"""
    Create an architectural Concept Model embodying the 'Cascading frames' metaphor.

    This function generates a series of frames arranged in a cascading manner, with each frame 
    rotated slightly to suggest movement and progression. The design emphasizes verticality and 
    connectivity, creating a dynamic silhouette with an interplay of light and shadow.

    Parameters:
    - base_width (float): The width of the base frame in meters.
    - base_depth (float): The depth of the base frame in meters.
    - frame_height (float): The height of each frame in meters.
    - num_frames (int): The number of cascading frames.
    - rotation_angle (float): The angle by which each successive frame is rotated, in degrees.
    - material_variation (list of str): A list of material names or types to apply to the frames.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the frames.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)
    frames = []
    current_height = 0

    for i in range(num_frames):
        # Create a base rectangle for the frame
        base_plane = rg.Plane.WorldXY
        rectangle_corners = [
            rg.Point3d(0, 0, current_height),
            rg.Point3d(base_width, 0, current_height),
            rg.Point3d(base_width, base_depth, current_height),
            rg.Point3d(0, base_depth, current_height),
            rg.Point3d(0, 0, current_height)  # Close the loop
        ]
        rectangle = rg.Polyline(rectangle_corners)

        # Create a surface from the rectangle
        frame_surface = rg.Brep.CreateFromCornerPoints(
            rectangle[0], rectangle[1], rectangle[2], rectangle[3], 0.01)

        if frame_surface:
            # Rotate the frame around the Z-axis
            center_point = rg.Point3d(base_width / 2, base_depth / 2, current_height)
            rotation = rg.Transform.Rotation(math.radians(rotation_angle * i), rg.Vector3d.ZAxis, center_point)
            frame_surface.Transform(rotation)
            frames.append(frame_surface)

        # Update parameters for the next frame
        current_height += frame_height
    
    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(5.0, 3.0, 2.0, 10, 15, ['Steel', 'Glass', 'Concrete'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(4.0, 2.5, 1.5, 8, 10, ['Wood', 'Aluminum', 'Plastic'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(6.0, 4.0, 3.0, 12, 20, ['Brick', 'Stone', 'Fiber'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(3.5, 2.0, 1.0, 15, 12, ['Copper', 'Acrylic', 'Marble'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(7.0, 5.0, 2.5, 6, 30, ['Fiberglass', 'Bamboo', 'Recycled Plastic'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
