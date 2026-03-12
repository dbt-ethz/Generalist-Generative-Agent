# Created for 0017_0003_cascading_frames.json

""" Summary:
The function `create_cascading_frames_model` generates an architectural concept model based on the metaphor "Cascading frames" by creating a series of overlapping frames that vary in size and orientation. It employs transformations to position each frame vertically and rotate them, producing a dynamic, multi-layered facade that emphasizes verticality and connectivity. The frames are created using randomized dimensions, enhancing visual complexity while maintaining a fluid transition between spaces. This model responds to the metaphor's themes of movement and depth, allowing for interplay between light and shadow, thus enriching the observer's experience as they navigate through the architectural space."""

#! python 3
function_code = """def create_cascading_frames_model(frame_count=5, frame_width=2.0, height_increment=1.5, rotation_angle=15, base_width=10.0, base_depth=5.0):
    \"""
    Creates an architectural Concept Model embodying the 'Cascading frames' metaphor.
    
    Parameters:
    - frame_count (int): The number of frames to create.
    - frame_width (float): The width of each frame.
    - height_increment (float): The vertical increment between each cascading frame.
    - rotation_angle (float): The angle by which each subsequent frame is rotated.
    - base_width (float): The width of the base frame.
    - base_depth (float): The depth of the base frame.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the frames.
    \"""
    import Rhino
    import Rhino.Geometry as rg
    import random
    import math
    random.seed(42)
    
    frames = []
    base_plane = rg.Plane.WorldXY
    
    for i in range(frame_count):
        # Calculate the transformation for the current frame
        translation = rg.Transform.Translation(0, 0, i * height_increment)
        rotation = rg.Transform.Rotation(math.radians(i * rotation_angle), base_plane.ZAxis, base_plane.Origin)
        
        # Apply transformations to the base plane
        current_plane = base_plane.Clone()
        current_plane.Transform(translation)
        current_plane.Transform(rotation)
        
        # Create the frame boundary
        frame_corners = [
            rg.Point3d(-base_width/2, -base_depth/2, 0),
            rg.Point3d(base_width/2, -base_depth/2, 0),
            rg.Point3d(base_width/2, base_depth/2, 0),
            rg.Point3d(-base_width/2, base_depth/2, 0),
            rg.Point3d(-base_width/2, -base_depth/2, 0)  # Close the loop
        ]
        
        # Transform corners to the current frame's orientation
        transform = rg.Transform.PlaneToPlane(rg.Plane.WorldXY, current_plane)
        transformed_corners = [pt.Transform(transform) or pt for pt in frame_corners]
        
        # Create a polyline curve from the corners
        polyline = rg.Polyline(transformed_corners)
        polyline_curve = polyline.ToNurbsCurve()
        
        # Offset the curve to create a frame
        offset_curve = polyline_curve.Offset(current_plane, -frame_width, 0.01, rg.CurveOffsetCornerStyle.Sharp)
        
        if offset_curve and len(offset_curve) > 0:
            # Create a brep from the frame
            outer_brep = rg.Brep.CreatePlanarBreps(polyline_curve)[0]
            inner_brep = rg.Brep.CreatePlanarBreps(offset_curve[0])[0]
            frame_brep = outer_brep.Trim(inner_brep, 0.01)
            
            if frame_brep:
                frames.append(frame_brep)
        
        # Randomly adjust dimensions for the next frame
        base_width *= random.uniform(0.8, 1.2)
        base_depth *= random.uniform(0.8, 1.2)
    
    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(frame_count=7, frame_width=1.5, height_increment=2.0, rotation_angle=10, base_width=12.0, base_depth=6.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(frame_count=6, frame_width=2.5, height_increment=1.0, rotation_angle=20, base_width=15.0, base_depth=7.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(frame_count=4, frame_width=3.0, height_increment=2.5, rotation_angle=30, base_width=8.0, base_depth=4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(frame_count=5, frame_width=2.0, height_increment=1.0, rotation_angle=25, base_width=10.0, base_depth=5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(frame_count=8, frame_width=1.0, height_increment=1.2, rotation_angle=15, base_width=9.0, base_depth=3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
