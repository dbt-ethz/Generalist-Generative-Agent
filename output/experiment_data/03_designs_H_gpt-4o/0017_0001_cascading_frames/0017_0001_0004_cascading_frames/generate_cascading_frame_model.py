# Created for 0017_0001_cascading_frames.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "Cascading frames" by creating a series of tiered, hollow box-like frames. Each layer is progressively smaller and shifted in position, suggesting movement and fluidity, while enhancing verticality and connectivity. The function utilizes parameters such as base size, height increments, and offset variations to define the size and arrangement of each layer, ensuring a dynamic silhouette. This tiered design emphasizes light and shadow interplay, guiding the observers eye through the structure and creating a visual narrative that embodies the metaphor's essence."""

#! python 3
function_code = """def generate_cascading_frame_model(base_size, height_increment, num_layers, offset_variation, seed=42):
    \"""
    Generate an architectural Concept Model based on the "Cascading frames" metaphor.

    This function creates a series of progressively tiered frames that suggest movement and progression.
    The frames shift in position and size, creating a dynamic silhouette that enhances verticality and
    connectivity, with an emphasis on light and shadow interplay.

    Parameters:
    - base_size (tuple of float): The base size (width, depth) of the initial frame in meters.
    - height_increment (float): The height increment for each successive frame layer in meters.
    - num_layers (int): The number of cascading frame layers.
    - offset_variation (float): The maximum offset variation for the frames in meters.
    - seed (int, optional): The seed for randomness to ensure replicability. Default is 42.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    frames = []
    
    base_width, base_depth = base_size
    current_height = 0

    for i in range(num_layers):
        # Calculate frame dimensions and position
        width = base_width * (1 - 0.1 * i)
        depth = base_depth * (1 - 0.1 * i)
        x_offset = random.uniform(-offset_variation, offset_variation)
        y_offset = random.uniform(-offset_variation, offset_variation)
        
        # Define the plane for the frame
        base_plane = rg.Plane(rg.Point3d(x_offset, y_offset, current_height), rg.Vector3d.ZAxis)

        # Create frame as a hollow box
        outer_box = rg.Box(base_plane, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height_increment))
        inner_box = rg.Box(base_plane, rg.Interval(width * 0.1, width * 0.9), rg.Interval(depth * 0.1, depth * 0.9), rg.Interval(height_increment * 0.1, height_increment * 0.9))

        outer_brep = outer_box.ToBrep()
        inner_brep = inner_box.ToBrep()

        # Create the frame by subtracting the inner volume from the outer volume
        frame_brep_difference = rg.Brep.CreateBooleanDifference([outer_brep], [inner_brep], 0.01)
        if frame_brep_difference:
            frames.append(frame_brep_difference[0])

        # Update height for the next frame
        current_height += height_increment

    return frames"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cascading_frame_model((5, 3), 2, 4, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cascading_frame_model((10, 5), 3, 5, 2.0, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cascading_frame_model((7, 4), 1.5, 6, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cascading_frame_model((4, 2), 1, 3, 0.5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cascading_frame_model((6, 4), 2.5, 7, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
