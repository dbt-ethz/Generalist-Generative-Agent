# Created for 0017_0001_cascading_frames.json

""" Summary:
The provided function, `create_cascading_frames_model`, generates an architectural concept model based on the metaphor of "Cascading frames." By stacking a specified number of frames, each with defined dimensions and offsets, the model embodies dynamic progression and layered depth. The frames are designed to create visual complexity, emphasizing verticality and connectivity, as suggested by the metaphor. The use of offsets introduces fluidity, guiding the viewer's gaze through the structure while allowing for interplay between light and shadow. The output is a collection of geometries that represent these cascading frames in a coherent architectural form."""

#! python 3
function_code = """def create_cascading_frames_model(frame_count=5, frame_height=3.0, frame_width=4.0, frame_depth=0.1, offset=0.5):
    \"""
    Creates an architectural Concept Model using the "Cascading frames" metaphor. This model features a stack of frames
    that suggest dynamic progression and layered depth, emphasizing verticality and connectivity.

    Parameters:
    - frame_count (int): The number of frames in the model.
    - frame_height (float): The height of each frame in meters.
    - frame_width (float): The width of each frame in meters.
    - frame_depth (float): The thickness of each frame in meters.
    - offset (float): The horizontal and vertical offset of each successive frame in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the frames.
    \"""
    import Rhino.Geometry as rg
    
    frames = []
    for i in range(frame_count):
        # Calculate the origin for each frame
        x_origin = i * offset
        y_origin = i * offset
        z_origin = i * frame_height
        
        # Create a planar surface for the frame
        plane = rg.Plane.WorldXY
        plane.Origin = rg.Point3d(x_origin, y_origin, z_origin)
        
        # Define the corners of the frame
        p1 = rg.Point3d(x_origin, y_origin, z_origin)
        p2 = rg.Point3d(x_origin + frame_width, y_origin, z_origin)
        p3 = rg.Point3d(x_origin + frame_width, y_origin + frame_height, z_origin)
        p4 = rg.Point3d(x_origin, y_origin + frame_height, z_origin)
        
        # Create a rectangle for the main frame
        outer_rect = rg.Rectangle3d(plane, p2, p3).ToNurbsCurve()
        
        # Define the inner rectangle to create the frame effect
        inner_p1 = rg.Point3d(x_origin + frame_depth, y_origin + frame_depth, z_origin)
        inner_p2 = rg.Point3d(x_origin + frame_width - frame_depth, y_origin + frame_depth, z_origin)
        inner_p3 = rg.Point3d(x_origin + frame_width - frame_depth, y_origin + frame_height - frame_depth, z_origin)
        inner_p4 = rg.Point3d(x_origin + frame_depth, y_origin + frame_height - frame_depth, z_origin)
       
        inner_rect = rg.Rectangle3d(plane, inner_p2, inner_p3).ToNurbsCurve()
        
        # Create the frame by lofting the outer and inner curves
        loft = rg.Brep.CreateFromLoft([outer_rect, inner_rect], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        
        if loft and len(loft) > 0:
            frames.append(loft[0])
    
    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(frame_count=7, frame_height=2.5, frame_width=3.0, frame_depth=0.15, offset=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(frame_count=10, frame_height=4.0, frame_width=5.0, frame_depth=0.2, offset=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(frame_count=6, frame_height=3.5, frame_width=2.5, frame_depth=0.1, offset=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(frame_count=8, frame_height=3.0, frame_width=4.5, frame_depth=0.2, offset=0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(frame_count=9, frame_height=2.0, frame_width=4.0, frame_depth=0.2, offset=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
