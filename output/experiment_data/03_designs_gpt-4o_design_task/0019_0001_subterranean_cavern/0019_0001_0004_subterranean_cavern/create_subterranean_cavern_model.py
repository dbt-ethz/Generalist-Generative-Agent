# Created for 0019_0001_subterranean_cavern.json

""" Summary:
The provided function, `create_subterranean_cavern_model`, generates an architectural concept model inspired by the metaphor of a subterranean cavern. It creates a series of interconnected, organic volumes that reflect the cavern's natural forms and spatial qualities. By defining parameters such as base dimensions, height variations, and the number of chambers, the function produces varied geometries that embody exploration and mystery. The model features undulating shapes and strategic connections, simulating intimate alcoves and open spaces. This design approach captures the essence of a secluded environment, enhancing the immersive experience through dynamic lighting and spatial relationships."""

#! python 3
function_code = """def create_subterranean_cavern_model(base_length, base_width, height_variation, num_chambers, random_seed=42):
    \"""
    Creates an architectural Concept Model that embodies the 'subterranean cavern' metaphor.
    
    This function generates a series of interconnected organic volumes representing a subterranean cavern.
    The model focuses on creating spaces that invoke a sense of exploration, mystery, and refuge through varied
    ceiling heights, floor levels, and organic forms. The design suggests a balance between openness and enclosure,
    using strategic openings to explore lighting effects.

    Parameters:
    - base_length (float): The base length of the model in meters.
    - base_width (float): The base width of the model in meters.
    - height_variation (float): The maximum variation in height levels to simulate undulating surfaces.
    - num_chambers (int): The number of chambers or main spaces within the cavern.
    - random_seed (int): Seed for the random number generator to ensure replicability. Default is 42.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the cavern model.
    \"""
    import Rhino.Geometry as rg
    import random
    random.seed(random_seed)

    # Create a base surface as the ground plane
    ground = rg.Plane.WorldXY
    base_surface = rg.Rectangle3d(ground, base_length, base_width).ToNurbsCurve()
    
    # Create varied heights and organic shapes for chambers
    chambers = []
    for i in range(num_chambers):
        # Randomly position chambers within the base area
        center_x = random.uniform(0.2 * base_length, 0.8 * base_length)
        center_y = random.uniform(0.2 * base_width, 0.8 * base_width)
        
        # Create an organic, undulating form for each chamber
        height = random.uniform(0.1 * height_variation, height_variation)
        radius = random.uniform(0.1 * min(base_length, base_width), 0.3 * min(base_length, base_width))
        
        # Create a spherical shape as a chamber
        sphere = rg.Sphere(rg.Point3d(center_x, center_y, height / 2), radius)
        chamber_brep = rg.Brep.CreateFromSphere(sphere)
        
        if chamber_brep:
            chambers.append(chamber_brep)
    
    # Create connections between chambers
    connections = []
    for i in range(len(chambers) - 1):
        start = chambers[i].GetBoundingBox(True).Center
        end = chambers[i + 1].GetBoundingBox(True).Center
        path = rg.Line(start, end).ToNurbsCurve()
        
        # Create a pipe (tunnel) along the path
        pipe = rg.Brep.CreatePipe(path, random.uniform(0.1, 0.3), True, rg.PipeCapMode.Flat, True, 0.01, 0.1)
        
        if pipe:
            connections.extend(pipe)
    
    # Combine chambers and connections into a single geometry list
    model_breps = chambers + connections
    
    return model_breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(50, 30, 10, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(40, 25, 15, 8, random_seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(60, 40, 20, 6, random_seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(70, 50, 25, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(80, 60, 30, 10, random_seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
