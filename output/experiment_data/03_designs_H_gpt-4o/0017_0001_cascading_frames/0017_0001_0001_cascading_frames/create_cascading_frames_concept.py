# Created for 0017_0001_cascading_frames.json

""" Summary:
The function `create_cascading_frames_concept` generates an architectural concept model based on the metaphor of "Cascading frames." It creates a series of geometrical frames that are progressively tiered, each shifted and rotated to suggest movement and visual interest. By defining parameters such as base dimensions, height increments, and rotation angles, the function produces a dynamic silhouette that emphasizes verticality and connectivity. The staggered arrangement enhances the interplay of light and shadow, inviting observers to experience a flowing sequence of spaces. This design approach captures the essence of cascading elements, guiding spatial transitions and creating a narrative through the structure."""

#! python 3
function_code = """def create_cascading_frames_concept(base_dimensions, height_increment, num_layers, rotation_angle, offset_distance):
    \"""
    Create an architectural Concept Model embodying the 'Cascading frames' metaphor.

    This function generates a series of geometrical frames that are progressively tiered, rotated, and offset,
    creating a dynamic silhouette and visual interest. The design emphasizes verticality, connectivity, and the
    interplay of light and shadow.

    Parameters:
    - base_dimensions (tuple of float): The base (width, depth) dimensions of the initial frame in meters.
    - height_increment (float): The vertical increment between each successive frame in meters.
    - num_layers (int): The number of cascading frames to create.
    - rotation_angle (float): The rotation angle in degrees applied to each frame to create dynamic effect.
    - offset_distance (float): The horizontal offset distance applied to each frame from the previous one in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import math

    frames = []
    base_width, base_depth = base_dimensions
    base_height = 0

    for i in range(num_layers):
        # Calculate transformation for each frame
        x_offset = offset_distance * i
        y_offset = offset_distance * i
        z_offset = height_increment * i

        # Create a base rectangle for the frame
        base_plane = rg.Plane.WorldXY
        rectangle_corners = [
            rg.Point3d(x_offset, y_offset, z_offset),
            rg.Point3d(x_offset + base_width, y_offset, z_offset),
            rg.Point3d(x_offset + base_width, y_offset + base_depth, z_offset),
            rg.Point3d(x_offset, y_offset + base_depth, z_offset)
        ]
        rectangle = rg.Polyline(rectangle_corners)

        # Create a surface from the rectangle
        frame_surface = rg.Brep.CreateFromCornerPoints(
            rectangle[0], rectangle[1], rectangle[2], rectangle[3], 0.01)

        # Apply rotation to the frame
        if frame_surface:
            rotation_center = rg.Point3d(x_offset + base_width / 2, y_offset + base_depth / 2, z_offset)
            rotation_transform = rg.Transform.Rotation(math.radians(rotation_angle * i), rotation_center)
            frame_surface.Transform(rotation_transform)
            frames.append(frame_surface)

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_concept((5.0, 3.0), 2.0, 4, 15.0, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_concept((4.0, 2.5), 1.5, 6, 10.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_concept((6.0, 4.0), 3.0, 5, 20.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_concept((3.0, 2.0), 1.0, 3, 30.0, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_concept((7.0, 5.0), 2.5, 8, 12.0, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
