# Created for 0017_0004_cascading_frames.json

""" Summary:
The provided function, `create_cascading_frames`, generates an architectural concept model that embodies the metaphor of "Cascading frames." It constructs a series of interconnected frames that progressively shift in scale and orientation, creating a dynamic architectural form. Each frame's dimensions are adjusted to emphasize vertical movement and spatial continuity, allowing for a rich interplay of light and shadow, as described in the design task. The function systematically creates rectangular frames and uses geometric operations to define their surfaces, ensuring that the resultant structure visually represents a rhythmic flow, guiding observers through a narrative of connected spaces while enhancing outdoor interactions."""

#! python 3
function_code = """def create_cascading_frames(height, frame_count, base_width, frame_depth, frame_thickness, seed=42):
    \"""
    Create an architectural Concept Model embodying the 'Cascading frames' metaphor.

    This function generates a series of interconnected frames that progressively shift in scale and orientation,
    creating a rhythmic and dynamic form. The frames are designed to emphasize vertical movement and spatial continuity,
    allowing for an interplay of light and shadow.

    Parameters:
    height (float): The total height of the structure in meters.
    frame_count (int): The number of frames in the cascading sequence.
    base_width (float): The width of the base frame in meters.
    frame_depth (float): The depth of each frame in meters.
    frame_thickness (float): The thickness of the frame elements in meters.
    seed (int): Random seed for replicable results. Default is 42.

    Returns:
    List[Rhino.Geometry.Brep]: A list of Brep geometries representing the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    frames = []
    level_height = height / frame_count

    current_width = base_width
    current_depth = frame_depth

    for i in range(frame_count):
        # Create a rectangular frame
        frame_corners = [
            rg.Point3d(0, 0, i * level_height),
            rg.Point3d(current_width, 0, i * level_height),
            rg.Point3d(current_width, current_depth, i * level_height),
            rg.Point3d(0, current_depth, i * level_height)
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
            frames.append(brep[0])

        # Update dimensions for the next frame
        current_width *= 0.9
        current_depth *= 0.95
        if random.random() > 0.5:
            current_width, current_depth = current_depth, current_width

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames(height=10.0, frame_count=5, base_width=3.0, frame_depth=2.0, frame_thickness=0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames(height=15.0, frame_count=8, base_width=4.0, frame_depth=3.0, frame_thickness=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames(height=12.0, frame_count=6, base_width=2.5, frame_depth=1.5, frame_thickness=0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames(height=20.0, frame_count=10, base_width=5.0, frame_depth=4.0, frame_thickness=0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames(height=8.0, frame_count=4, base_width=2.0, frame_depth=1.0, frame_thickness=0.05)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
