# Created for 0017_0004_cascading_frames.json

""" Summary:
The provided function, `create_dynamic_cascading_frames`, generates an architectural concept model based on the "Cascading frames" metaphor. It creates a series of interconnected frames that shift in scale, orientation, and skew, resulting in a dynamic architectural form. The function emphasizes vertical movement and the interplay of light and shadow through the use of translucent or perforated materials, allowing light to filter through the frames. Each frame serves as a spatial connector, enhancing fluid transitions between levels and creating sheltered outdoor spaces. This process captures the metaphor's essence of layered depth, fluidity, and continuity within the architecture."""

#! python 3
function_code = """def create_dynamic_cascading_frames(frame_count, base_width, base_height, frame_thickness, shift_factor, skew_angle, seed=42):
    \"""
    Generate an architectural Concept Model with a 'Cascading frames' metaphor.

    This function creates a series of frames that progressively change in scale, orientation, and skew,
    forming a dynamic and rhythmic architectural form. The frames cascade downward, emphasizing
    the interplay of light and shadow, and providing a spatial narrative of connectivity and progression.

    Parameters:
    frame_count (int): Number of frames in the cascading sequence.
    base_width (float): Initial width of the base frame in meters.
    base_height (float): Initial height of the base frame in meters.
    frame_thickness (float): Thickness of each frame element in meters.
    shift_factor (float): Horizontal shift factor applied to each subsequent frame.
    skew_angle (float): Angle in degrees to skew each frame for added dynamism.
    seed (int): Random seed for replicable results. Default is 42.

    Returns:
    List[Rhino.Geometry.Brep]: A list of Brep geometries representing the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    random.seed(seed)

    frames = []
    current_height = 0
    current_width = base_width

    for i in range(frame_count):
        # Calculate skew transformation using a 4x4 matrix
        skew_matrix = rg.Transform.Identity
        skew_matrix[0, 1] = math.tan(math.radians(skew_angle))

        # Create a rectangular frame and skew it
        frame_corners = [
            rg.Point3d(-current_width / 2, -frame_thickness / 2, current_height),
            rg.Point3d(current_width / 2, -frame_thickness / 2, current_height),
            rg.Point3d(current_width / 2, frame_thickness / 2, current_height),
            rg.Point3d(-current_width / 2, frame_thickness / 2, current_height)
        ]

        # Apply skew transformation to corners
        for j in range(len(frame_corners)):
            frame_corners[j].Transform(skew_matrix)

        # Create the 3D frame
        frame_curve = rg.Polyline(frame_corners + [frame_corners[0]]).ToNurbsCurve()
        frame_extrusion = rg.Extrusion.Create(frame_curve, base_height, True)
        frame_brep = frame_extrusion.ToBrep()

        if frame_brep:
            frames.append(frame_brep)

        # Update parameters for the next frame
        current_height += base_height
        current_width *= (1 - shift_factor)

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dynamic_cascading_frames(frame_count=10, base_width=5.0, base_height=2.0, frame_thickness=0.1, shift_factor=0.1, skew_angle=15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dynamic_cascading_frames(frame_count=8, base_width=6.0, base_height=1.5, frame_thickness=0.2, shift_factor=0.15, skew_angle=20.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dynamic_cascading_frames(frame_count=12, base_width=4.0, base_height=3.0, frame_thickness=0.15, shift_factor=0.2, skew_angle=10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dynamic_cascading_frames(frame_count=15, base_width=3.5, base_height=2.5, frame_thickness=0.05, shift_factor=0.2, skew_angle=25.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dynamic_cascading_frames(frame_count=5, base_width=7.0, base_height=2.0, frame_thickness=0.3, shift_factor=0.05, skew_angle=30.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
