# Created for 0009_0003_cantilevering_corners.json

""" Summary:
The function `create_cantilevering_corners_model` generates an architectural concept model based on the metaphor of "Cantilevering corners." It constructs a central mass from specified dimensions and creates multiple cantilevered sections that extend outward at varying heights and lengths. Each cantilever is positioned based on a randomly chosen direction, emphasizing the contrast between the solid core and the projecting elements. Additionally, voids are incorporated beneath these cantilevers to enhance the sense of suspension, creating dynamic interstitial spaces. The resulting model embodies the interplay of stability and motion, inviting exploration and interaction with its surroundings."""

#! python 3
function_code = """def create_cantilevering_corners_model(base_size, cantilever_lengths, cantilever_heights, num_cantilevers, seed=42):
    \"""
    Creates an architectural Concept Model embodying the metaphor of 'Cantilevering corners'.
    
    This function generates a central mass with multiple cantilevered sections extending outward,
    each at different heights and orientations. The design emphasizes the contrast between the stable
    core and lighter projecting sections. Voids are incorporated beneath the cantilevers to enhance the
    sense of suspension and tension.

    Parameters:
    - base_size (tuple): A tuple of three floats (width, depth, height) representing the dimensions of the central mass.
    - cantilever_lengths (list): A list of floats representing the lengths of each cantilevered section.
    - cantilever_heights (list): A list of floats representing the starting heights of each cantilevered section from the base.
    - num_cantilevers (int): The number of cantilevered sections to create.
    - seed (int): The seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(seed)  # Seed for reproducibility
    
    # Create the central base mass
    base_width, base_depth, base_height = base_size
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_width), rg.Interval(0, base_depth), rg.Interval(0, base_height))
    
    geometries = [base_box.ToBrep()]
    
    # Generate cantilevered sections
    for i in range(num_cantilevers):
        length = cantilever_lengths[i % len(cantilever_lengths)]
        height = cantilever_heights[i % len(cantilever_heights)]
        
        # Randomly choose a direction for the cantilever
        direction = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
        
        base_point = rg.Point3d(base_width / 2, base_depth / 2, height)
        
        cantilever_box = rg.Box(
            rg.Plane(base_point, rg.Vector3d.ZAxis),
            rg.Interval(-length / 2, length / 2),
            rg.Interval(-length / 2, length / 2),
            rg.Interval(0, base_height / 4)
        )
        translation = rg.Vector3d(direction[0] * length / 2, direction[1] * length / 2, 0)
        cantilever_box.Transform(rg.Transform.Translation(translation))
        
        geometries.append(cantilever_box.ToBrep())
        
        # Create voids beneath the cantilever
        void_box = rg.Box(
            rg.Plane(base_point, rg.Vector3d.ZAxis),
            rg.Interval(-length / 2, length / 2),
            rg.Interval(-length / 2, length / 2),
            rg.Interval(-base_height / 4, 0)
        )
        void_box.Transform(rg.Transform.Translation(translation))
        
        geometries.append(void_box.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevering_corners_model((10.0, 5.0, 8.0), [3.0, 4.0], [1.0, 2.0], 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevering_corners_model((12.0, 6.0, 10.0), [2.5, 3.5, 4.5], [2.0, 3.0, 1.5], 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevering_corners_model((15.0, 7.0, 9.0), [5.0, 6.0], [0.5, 1.5], 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevering_corners_model((20.0, 10.0, 12.0), [4.0, 5.0, 6.0], [2.5, 3.5], 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevering_corners_model((8.0, 4.0, 6.0), [2.0, 3.0, 5.0], [1.0, 2.0], 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
