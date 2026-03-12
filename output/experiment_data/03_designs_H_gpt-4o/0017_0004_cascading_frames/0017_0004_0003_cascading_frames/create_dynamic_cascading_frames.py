# Created for 0017_0004_cascading_frames.json

""" Summary:
The provided function, `create_dynamic_cascading_frames`, generates an architectural concept model inspired by the metaphor "Cascading frames." It creates a series of interconnected frames that vary in scale and orientation, producing a rhythmic and dynamic architectural form. The function emphasizes vertical movement and spatial continuity, facilitating an interplay of light and shadow through the use of translucent or perforated materials. Each frame serves as a visual and spatial connector, guiding movement within the structure and creating sheltered spaces. The cascading arrangement enhances interaction with the surroundings, reflecting the metaphor's themes of fluidity and connectivity."""

#! python 3
function_code = """def create_dynamic_cascading_frames(total_levels, initial_width, initial_height, frame_thickness, horizontal_shift, vertical_spacing, seed=0):
    \"""
    Creates an architectural Concept Model based on the 'Cascading frames' metaphor.
    
    The function generates a series of frames that progressively shift in both scale and orientation,
    creating a rhythmic and dynamic form. It emphasizes vertical movement and spatial continuity,
    allowing for an interplay of light and shadow. Frames are designed to guide movement within the building,
    with pathways and circulation routes integrated into the cascading structure.
    
    Args:
    - total_levels (int): Number of levels or frames in the model.
    - initial_width (float): Initial width of the base frame in meters.
    - initial_height (float): Initial height of the base frame in meters.
    - frame_thickness (float): Thickness of each frame in meters.
    - horizontal_shift (float): Horizontal shift applied to each subsequent frame to achieve the cascading effect.
    - vertical_spacing (float): Vertical spacing between each frame.
    - seed (int, optional): Seed for random number generator to ensure replicability. Default is 0.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    frames = []
    current_height = 0
    current_width = initial_width
    current_depth = frame_thickness

    for level in range(total_levels):
        # Create a frame for the current level
        base_origin = rg.Point3d(level * horizontal_shift, 0, current_height)
        corner1 = rg.Point3d(base_origin.X + current_width, base_origin.Y, base_origin.Z)
        corner2 = rg.Point3d(base_origin.X + current_width, base_origin.Y + current_depth, base_origin.Z)
        corner3 = rg.Point3d(base_origin.X, base_origin.Y + current_depth, base_origin.Z)
        
        # Create a Brep frame
        rectangle = rg.Rectangle3d(rg.Plane.WorldXY, corner1, corner3)
        extrusion = rg.Extrusion.Create(rectangle.ToNurbsCurve(), initial_height, True)
        frame_brep = extrusion.ToBrep()
        frames.append(frame_brep)
        
        # Adjust dimensions for the next frame
        current_height += vertical_spacing
        current_width *= random.uniform(0.85, 0.95)  # Randomly decrease width for cascading effect
        current_depth *= random.uniform(0.9, 1.1)  # Vary depth slightly for visual interest

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dynamic_cascading_frames(5, 10.0, 3.0, 0.2, 1.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dynamic_cascading_frames(7, 8.0, 4.0, 0.15, 1.5, 0.3, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dynamic_cascading_frames(6, 12.0, 2.5, 0.25, 0.8, 0.4, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dynamic_cascading_frames(4, 15.0, 5.0, 0.3, 2.0, 0.6, seed=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dynamic_cascading_frames(3, 9.0, 3.5, 0.1, 1.2, 0.4, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
