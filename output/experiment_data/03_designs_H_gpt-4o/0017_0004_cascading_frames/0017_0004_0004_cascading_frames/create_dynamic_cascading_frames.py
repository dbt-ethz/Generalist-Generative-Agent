# Created for 0017_0004_cascading_frames.json

""" Summary:
The function `create_dynamic_cascading_frames` generates an architectural concept model based on the metaphor "Cascading frames." It creates a series of frames that progressively change in scale and orientation, establishing a rhythmic and dynamic architectural form. Each frame's design emphasizes vertical and horizontal connectivity, allowing for a vibrant interplay of light and shadows through translucent materials. The function iteratively constructs frames, adjusting their dimensions and angles to enhance the cascading effect and spatial continuity. This process results in a visually engaging structure that fosters the interaction between interior spaces and their surroundings, embodying the metaphor's essence."""

#! python 3
function_code = """def create_dynamic_cascading_frames(base_height, frame_count, base_width, frame_thickness, frame_rotation_angle, seed=42):
    \"""
    Generate an architectural Concept Model embodying the 'Cascading frames' metaphor.

    This function creates a series of dynamically cascading frames that shift in both scale and orientation,
    creating a rhythmic and visually engaging form. Each frame is designed to emphasize vertical and horizontal
    connectivity, allowing for a vibrant interplay of light and shadow.

    Parameters:
    base_height (float): The height of the base frame in meters.
    frame_count (int): The number of frames in the cascading sequence.
    base_width (float): The width of the base frame in meters.
    frame_thickness (float): The thickness of the frame elements in meters.
    frame_rotation_angle (float): The rotation angle in degrees for each successive frame.
    seed (int): Random seed for replicable results. Default is 42.

    Returns:
    List[Rhino.Geometry.Brep]: A list of Brep geometries representing the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)

    frames = []
    current_height = 0
    current_width = base_width
    angle_rad = math.radians(frame_rotation_angle)

    for i in range(frame_count):
        # Create a rectangular frame
        base_corners = [
            rg.Point3d(-current_width / 2, 0, current_height),
            rg.Point3d(current_width / 2, 0, current_height),
            rg.Point3d(current_width / 2, frame_thickness, current_height),
            rg.Point3d(-current_width / 2, frame_thickness, current_height)
        ]

        # Create the surfaces of the frame
        top_surface = rg.NurbsSurface.CreateFromCorners(base_corners[0], base_corners[1], base_corners[2], base_corners[3])
        # Translate the top_surface to create the bottom_surface
        bottom_surface = top_surface.Duplicate()
        bottom_surface.Translate(rg.Vector3d(0, 0, base_height))

        # Create the side surfaces to complete the frame
        side_surfaces = []
        for j in range(4):
            next_j = (j + 1) % 4
            side_surfaces.append(rg.NurbsSurface.CreateFromCorners(
                base_corners[j],
                base_corners[next_j],
                rg.Point3d(base_corners[next_j].X, base_corners[next_j].Y, base_corners[next_j].Z + base_height),
                rg.Point3d(base_corners[j].X, base_corners[j].Y, base_corners[j].Z + base_height)
            ))

        # Create a brep from surfaces
        brep_pieces = [top_surface.ToBrep(), bottom_surface.ToBrep()] + [s.ToBrep() for s in side_surfaces]

        # Join surfaces to create a closed brep
        brep = rg.Brep.JoinBreps(brep_pieces, 0.01)
        if brep and len(brep) > 0:
            frames.append(brep[0])

        # Update parameters for the next frame
        current_height += base_height * 0.9
        current_width *= 0.95
        # Rotate the frame
        transform = rg.Transform.Rotation(angle_rad * i, rg.Vector3d(0, 0, 1), rg.Point3d(0, 0, current_height))
        frames[-1].Transform(transform)

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dynamic_cascading_frames(3.0, 10, 2.0, 0.1, 15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dynamic_cascading_frames(2.5, 8, 1.5, 0.05, 10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dynamic_cascading_frames(4.0, 5, 3.0, 0.2, 20.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dynamic_cascading_frames(1.5, 12, 2.5, 0.15, 30.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dynamic_cascading_frames(5.0, 6, 4.0, 0.2, 25.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
