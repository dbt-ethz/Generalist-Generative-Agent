# Created for 0017_0001_cascading_frames.json

""" Summary:
The function `create_cascading_frames_model` generates an architectural concept model based on the metaphor "Cascading frames" by creating a series of tiered, layered frames that shift in position. Each frame is progressively smaller and offset from the previous one, representing movement and progression. This staggered arrangement enhances verticality and connectivity, guiding the observer's eye through the model. The interplay of different materials emphasizes the effects of light and shadow across the frames, contributing to a dynamic silhouette. The design encapsulates the essence of cascading elements, fostering fluid transitions among spaces and visual complexity."""

#! python 3
function_code = """def create_cascading_frames_model(base_width, base_depth, frame_height, num_frames, offset_factor, material_variation):
    \"""
    Create an architectural Concept Model embodying the 'Cascading frames' metaphor.

    This function generates a series of layered frames that progressively shift in position,
    suggesting movement and progression. The design emphasizes verticality and connectivity,
    creating a dynamic silhouette with interplay of light and shadow.

    Parameters:
    - base_width (float): The width of the base frame in meters.
    - base_depth (float): The depth of the base frame in meters.
    - frame_height (float): The height of each frame in meters.
    - num_frames (int): The number of cascading frames.
    - offset_factor (float): The amount by which each frame is offset from the previous one.
    - material_variation (list of str): A list of material names or types to apply to the frames.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the frames.
    \"""
    import Rhino
    import random
    random.seed(42)

    frames = []
    current_width = base_width
    current_depth = base_depth
    current_height = 0
    offset_x = 0
    offset_y = 0

    for i in range(num_frames):
        # Create a base rectangle for the frame
        base_plane = Rhino.Geometry.Plane.WorldXY
        rectangle_corners = [
            Rhino.Geometry.Point3d(offset_x, offset_y, current_height),
            Rhino.Geometry.Point3d(offset_x + current_width, offset_y, current_height),
            Rhino.Geometry.Point3d(offset_x + current_width, offset_y + current_depth, current_height),
            Rhino.Geometry.Point3d(offset_x, offset_y + current_depth, current_height),
            Rhino.Geometry.Point3d(offset_x, offset_y, current_height)  # Close the loop
        ]
        rectangle = Rhino.Geometry.Polyline(rectangle_corners)

        # Create a surface from the rectangle
        frame_surface = Rhino.Geometry.Brep.CreateFromCornerPoints(
            rectangle[0], rectangle[1], rectangle[2], rectangle[3], 0.01)

        if frame_surface:
            frames.append(frame_surface)

        # Update parameters for the next frame
        current_height += frame_height
        offset_x += offset_factor * (0.5 - random.random()) * current_width
        offset_y += offset_factor * (0.5 - random.random()) * current_depth

        # Optionally alter dimensions to emphasize the cascading effect
        current_width *= 0.95
        current_depth *= 0.95

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(5.0, 3.0, 2.0, 10, 0.5, ['wood', 'metal', 'glass'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(4.0, 2.5, 1.5, 8, 0.3, ['concrete', 'acrylic'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(6.0, 4.0, 2.5, 12, 0.4, ['steel', 'fiberglass', 'brick'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(7.0, 5.0, 3.0, 15, 0.6, ['aluminum', 'canvas', 'stone'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(3.5, 2.0, 1.0, 6, 0.2, ['bamboo', 'polycarbonate'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
