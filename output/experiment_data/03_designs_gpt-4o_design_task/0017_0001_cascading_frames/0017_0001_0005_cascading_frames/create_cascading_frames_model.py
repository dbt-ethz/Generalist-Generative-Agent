# Created for 0017_0001_cascading_frames.json

""" Summary:
The function `create_cascading_frames_model` generates an architectural concept model that embodies the metaphor of "Cascading frames." It creates a series of tiered frames that progressively shift in position, reflecting dynamic movement and vertical connectivity. Each layer is designed with decreasing dimensions, forming a staggered silhouette that enhances light and shadow interplay. By adjusting parameters like base dimensions, layer count, and shift factors, the model emphasizes fluid transitions and spatial relationships, guiding observers through a visually engaging sequence. The final output is a list of 3D geometries representing the cascading frames, ready for visualization or further design development."""

#! python 3
function_code = """def create_cascading_frames_model(base_width, base_depth, base_height, num_layers, shift_factor, frame_thickness):
    \"""
    Creates an architectural Concept Model based on the 'Cascading frames' metaphor. The model consists of a series of 
    progressively tiered frames, which shift in position to suggest movement and progression, emphasizing verticality 
    and connectivity. Each tier is offset from the previous one to create a dynamic silhouette.

    Parameters:
        base_width (float): The width of the base frame in meters.
        base_depth (float): The depth of the base frame in meters.
        base_height (float): The height of each frame layer in meters.
        num_layers (int): The number of cascading layers.
        shift_factor (float): The amount each layer is shifted horizontally from the previous one in meters.
        frame_thickness (float): The thickness of each frame in meters.

    Returns:
        List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random

    # Seed for reproducibility
    random.seed(42)

    frames = []

    # Starting position of the base frame
    current_x = 0
    current_y = 0
    current_z = 0

    for i in range(num_layers):
        # Calculate frame dimensions
        width = base_width - (i * shift_factor)
        depth = base_depth - (i * shift_factor)

        # Create a box for the current frame
        base_plane = rg.Plane(rg.Point3d(current_x, current_y, current_z), rg.Vector3d.ZAxis)
        box = rg.Box(base_plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, base_height))

        # Create frame as a hollow box
        outer_brep = box.ToBrep()
        inner_box = rg.Box(base_plane, rg.Interval(frame_thickness, width - frame_thickness),
                           rg.Interval(frame_thickness, depth - frame_thickness),
                           rg.Interval(frame_thickness, base_height - frame_thickness))
        inner_brep = inner_box.ToBrep()
        
        # Fix: Check if result from CreateBooleanDifference is not empty
        frame_brep_difference = rg.Brep.CreateBooleanDifference([outer_brep], [inner_brep], 0.01)
        if frame_brep_difference:
            frame_brep = frame_brep_difference[0]
            frames.append(frame_brep)

        # Update position for the next frame
        current_x += shift_factor / 2
        current_y += shift_factor / 2
        current_z += base_height

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cascading_frames_model(5.0, 3.0, 2.0, 4, 0.5, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cascading_frames_model(10.0, 6.0, 3.0, 5, 1.0, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cascading_frames_model(8.0, 4.0, 2.5, 6, 0.75, 0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cascading_frames_model(7.0, 5.0, 3.0, 3, 0.3, 0.05)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cascading_frames_model(6.0, 4.5, 2.0, 5, 0.4, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
