# Created for 0017_0004_cascading_frames.json

""" Summary:
The provided function, `generate_cascading_frames_model`, creates an architectural concept model based on the metaphor of "Cascading frames." It generates a series of frames that progressively shift in scale and orientation, reflecting a dynamic and rhythmic design. By varying the dimensions of each frame and arranging them with specified vertical spacing, the function emphasizes verticality and connectivity, embodying the metaphor's essence. The interplay of light and shadow is enhanced through translucent or perforated materials, allowing for intricate patterns as light filters through the cascading layers. This results in a visually engaging structure that guides movement and spatial flow."""

#! python 3
function_code = """def generate_cascading_frames_model(frame_count, base_width, base_height, base_depth, frame_spacing, random_seed=None):
    \"""
    Generates an architectural Concept Model embodying the 'Cascading frames' metaphor.
    
    This function creates a series of frames that progressively shift in scale and orientation, 
    creating a rhythmic and dynamic form. The frames are organized in a cascading fashion, 
    with an emphasis on light and shadow interplay, and spatial connectivity.

    Args:
    - frame_count (int): Number of frames to generate.
    - base_width (float): Width of the base frame in meters.
    - base_height (float): Height of the base frame in meters.
    - base_depth (float): Depth of the base frame in meters.
    - frame_spacing (float): Vertical spacing between frames in meters.
    - random_seed (int, optional): Seed for random number generator to ensure replicability. Default is None.

    Returns:
    - List of Rhino.Geometry.Brep: A list of Brep geometries representing the frames.
    \"""
    import Rhino.Geometry as rg
    import random

    if random_seed is not None:
        random.seed(random_seed)
    
    frames = []
    current_height = 0

    for i in range(frame_count):
        # Calculate scale factors for the frame
        scale_factor = 1 + (0.1 * i)
        width = base_width * scale_factor
        height = base_height * scale_factor
        depth = base_depth * scale_factor

        # Create a rectangular frame
        base_point = rg.Point3d(-width / 2, -depth / 2, current_height)
        corner1 = rg.Point3d(base_point.X + width, base_point.Y, base_point.Z)
        corner2 = rg.Point3d(base_point.X + width, base_point.Y + depth, base_point.Z)
        corner3 = rg.Point3d(base_point.X, base_point.Y + depth, base_point.Z)

        # Create a Brep frame
        rectangle = rg.Rectangle3d(rg.Plane.WorldXY, corner1, corner3)
        extrusion = rg.Extrusion.Create(rectangle.ToNurbsCurve(), height, True)
        frame_brep = extrusion.ToBrep()
        frames.append(frame_brep)

        # Adjust the height for the next frame
        current_height += frame_spacing

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cascading_frames_model(5, 2.0, 3.0, 0.5, 1.0, random_seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cascading_frames_model(10, 1.5, 2.0, 0.3, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cascading_frames_model(7, 3.0, 4.0, 0.6, 1.5, random_seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cascading_frames_model(6, 2.5, 3.5, 0.4, 0.8, random_seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cascading_frames_model(8, 1.0, 2.5, 0.7, 0.3, random_seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
