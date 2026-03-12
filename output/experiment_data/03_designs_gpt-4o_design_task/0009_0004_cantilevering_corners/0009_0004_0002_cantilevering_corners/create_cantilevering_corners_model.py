# Created for 0009_0004_cantilevering_corners.json

""" Summary:
The provided function, `create_cantilevering_corners_model`, generates an architectural concept model inspired by the metaphor of 'Cantilevering corners'. It constructs a central core structure, from which angular projections extend asymmetrically, embodying the tension between stability and motion. By using a random selection of directions for these projections, the function creates a dynamic arrangement of interlocking volumes that challenge traditional notions of support. This approach allows for innovative spatial relationships and unique areas beneath the cantilevered elements. The interplay of light and shadow enhances the model's aesthetic appeal, inviting exploration and engagement within the designed spaces."""

#! python 3
function_code = """def create_cantilevering_corners_model(core_height, core_width, projection_lengths, seed=42):
    \"""
    Create an architectural Concept Model based on the metaphor of 'Cantilevering corners'.
    
    This function generates a series of angular, interlocking volumes extending from a central core,
    forming cantilevered corners that suggest tension and balance between stability and motion.
    The model aims to explore dynamic spaces beneath and around these cantilevered sections.

    Parameters:
    - core_height (float): The height of the central core structure in meters.
    - core_width (float): The width and depth of the central core structure in meters (assuming a cube).
    - projection_lengths (list of float): A list of lengths in meters for each cantilevered projection.
    - seed (int, optional): Seed for random generation to ensure replicability. Default is 42.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set the random seed
    random.seed(seed)
    
    # Core structure as a cube
    core = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_width), rg.Interval(0, core_height))
    core_brep = core.ToBrep()
    
    # Initialize list for storing geometries
    geometries = [core_brep]
    
    # Define directions for cantilevering projections
    directions = [
        rg.Vector3d(1, 0, 0), rg.Vector3d(-1, 0, 0), 
        rg.Vector3d(0, 1, 0), rg.Vector3d(0, -1, 0),
        rg.Vector3d(1, 1, 0), rg.Vector3d(-1, 1, 0),
        rg.Vector3d(1, -1, 0), rg.Vector3d(-1, -1, 0)
    ]
    
    # Create cantilevered projections
    for length in projection_lengths:
        direction = random.choice(directions)
        # Create a transformation matrix for translation
        translation = rg.Transform.Translation(direction * length)
        
        # Create the projection as a box
        projection = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(core_width, core_width + length),
            rg.Interval(0, core_width),
            rg.Interval(0, core_height * 0.5)  # Half-height for projections
        )
        
        # Transform the projection
        projection.Transform(translation)
        
        # Add the transformed projection to the list
        geometries.append(projection.ToBrep())
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevering_corners_model(10.0, 5.0, [2.0, 3.5, 4.0])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevering_corners_model(8.0, 4.0, [1.5, 2.5, 3.0, 4.5])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevering_corners_model(12.0, 6.0, [2.5, 3.0, 5.0, 6.5])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevering_corners_model(15.0, 7.0, [1.0, 2.0, 3.0, 4.0, 5.0])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevering_corners_model(9.0, 4.5, [2.2, 3.1, 4.8, 5.5])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
