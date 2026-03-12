# Created for 0017_0004_cascading_frames.json

""" Summary:
The function `generate_cascading_frames_with_terraces` creates an architectural concept model based on the metaphor "Cascading frames." It generates a series of interconnected frames that progressively alter in scale and orientation, embodying a dynamic and layered design. Each frame emphasizes vertical movement and spatial continuity, allowing for a rich interplay of light and shadows through translucent or perforated materials. Terraces extend from the frames, enhancing outdoor interaction and guiding movement within the structure. The resulting geometries reflect a rhythmic arrangement that fosters connectivity, depth, and fluid transitions, effectively translating the metaphor into a tangible architectural form."""

#! python 3
function_code = """def generate_cascading_frames_with_terraces(frame_count, initial_width, initial_height, initial_depth, terrace_depth, frame_thickness, seed=42):
    \"""
    Generate an architectural Concept Model embodying the 'Cascading frames' metaphor with integrated terraces.

    This function creates a series of frames that progressively shift in scale and orientation, with terraces incorporated
    into the design. The frames emphasize vertical movement and spatial continuity, allowing for an interplay of light
    and shadow.

    Parameters:
    frame_count (int): The number of frames in the cascading sequence.
    initial_width (float): The width of the base frame in meters.
    initial_height (float): The height of each frame in meters.
    initial_depth (float): The depth of the base frame in meters.
    terrace_depth (float): The depth of the terraces in meters.
    frame_thickness (float): The thickness of the frame elements in meters.
    seed (int): Random seed for replicable results. Default is 42.

    Returns:
    List[Rhino.Geometry.Brep]: A list of Brep geometries representing the cascading frames with terraces.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    frames_with_terraces = []
    current_height = 0
    current_width = initial_width
    current_depth = initial_depth

    for i in range(frame_count):
        # Create a rectangular frame
        frame_corners = [
            rg.Point3d(0, 0, current_height),
            rg.Point3d(current_width, 0, current_height),
            rg.Point3d(current_width, current_depth, current_height),
            rg.Point3d(0, current_depth, current_height)
        ]

        # Create the top and bottom surfaces of the frame
        top_surface = rg.NurbsSurface.CreateFromCorners(frame_corners[0], frame_corners[1], frame_corners[2], frame_corners[3])
        bottom_surface = rg.NurbsSurface.CreateFromCorners(
            rg.Point3d(frame_corners[0].X, frame_corners[0].Y, frame_corners[0].Z + frame_thickness),
            rg.Point3d(frame_corners[1].X, frame_corners[1].Y, frame_corners[1].Z + frame_thickness),
            rg.Point3d(frame_corners[2].X, frame_corners[2].Y, frame_corners[2].Z + frame_thickness),
            rg.Point3d(frame_corners[3].X, frame_corners[3].Y, frame_corners[3].Z + frame_thickness)
        )

        # Create the side surfaces to complete the frame
        side_surfaces = []
        for j in range(4):
            next_j = (j + 1) % 4
            side_surfaces.append(rg.NurbsSurface.CreateFromCorners(
                frame_corners[j],
                frame_corners[next_j],
                rg.Point3d(frame_corners[next_j].X, frame_corners[next_j].Y, frame_corners[next_j].Z + frame_thickness),
                rg.Point3d(frame_corners[j].X, frame_corners[j].Y, frame_corners[j].Z + frame_thickness)
            ))

        # Create a brep from surfaces
        brep_pieces = [top_surface.ToBrep(), bottom_surface.ToBrep()] + [s.ToBrep() for s in side_surfaces]

        # Join surfaces to create a closed brep
        brep = rg.Brep.JoinBreps(brep_pieces, 0.01)
        if brep and len(brep) > 0:
            frames_with_terraces.append(brep[0])

        # Create a terrace extending from the frame
        terrace_corners = [
            rg.Point3d(-terrace_depth, 0, current_height + frame_thickness),
            rg.Point3d(current_width + terrace_depth, 0, current_height + frame_thickness),
            rg.Point3d(current_width + terrace_depth, current_depth, current_height + frame_thickness),
            rg.Point3d(-terrace_depth, current_depth, current_height + frame_thickness)
        ]

        terrace_surface = rg.NurbsSurface.CreateFromCorners(
            terrace_corners[0], terrace_corners[1], terrace_corners[2], terrace_corners[3]
        )

        terrace_brep = terrace_surface.ToBrep()
        frames_with_terraces.append(terrace_brep)

        # Update dimensions for the next frame
        current_height += initial_height
        current_width *= 0.9
        current_depth *= 0.95

    return frames_with_terraces"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cascading_frames_with_terraces(5, 10.0, 3.0, 5.0, 2.0, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cascading_frames_with_terraces(7, 12.0, 4.0, 6.0, 1.5, 0.25, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cascading_frames_with_terraces(10, 8.0, 2.5, 4.0, 1.0, 0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cascading_frames_with_terraces(6, 15.0, 3.5, 7.0, 2.5, 0.3, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cascading_frames_with_terraces(8, 14.0, 5.0, 8.0, 3.0, 0.1, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
