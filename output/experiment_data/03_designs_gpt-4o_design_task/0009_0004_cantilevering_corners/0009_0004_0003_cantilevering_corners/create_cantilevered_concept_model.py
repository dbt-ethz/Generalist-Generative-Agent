# Created for 0009_0004_cantilevering_corners.json

""" Summary:
The function `create_cantilevered_concept_model` generates an architectural concept model based on the metaphor of "Cantilevering corners." It constructs a central core structure and creates cantilevered sections that extend dynamically from this core, embodying the tension between stability and motion. By incorporating random angular variations and asymmetrical extensions, the model captures the essence of bold overhangs and unique spatial relationships. The interplay of solid and void is emphasized through contrasting geometries and materials, while the manipulation of light and shadow enhances the perception of movement, ultimately creating an engaging, exploratory architectural form that aligns with the provided design task."""

#! python 3
function_code = """def create_cantilevered_concept_model(base_length=20, base_width=10, height=10, cantilever_length=5, cantilever_height=7, seed=42):
    \"""
    Creates a series of interlocking volumes to form an architectural Concept Model based on the metaphor of 'Cantilevering corners'.
    
    Parameters:
        base_length (float): Length of the base structure in meters.
        base_width (float): Width of the base structure in meters.
        height (float): Height of the central core structure in meters.
        cantilever_length (float): Length of the cantilevered sections in meters.
        cantilever_height (float): Height of the cantilevered sections in meters.
        seed (int): Seed for random number generation to ensure replicability.
        
    Returns:
        List[Rhino.Geometry.Brep]: A list of breps representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    random.seed(seed)
    
    # Create the core structure
    core = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, height)).ToBrep()
    
    # Create cantilevered sections
    cantilevers = []
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Four possible directions
    
    for i in range(4):
        direction = directions[i]
        angle = random.uniform(-15, 15)  # Adding some angular variation
        
        # Define the cantilever transformation
        translation = rg.Vector3d(direction[0] * (base_length / 2 + cantilever_length), 
                                  direction[1] * (base_width / 2 + cantilever_length), 
                                  random.uniform(-height/2, height/2))
        
        rotation_center = rg.Point3d(base_length / 2, base_width / 2, height / 2)
        rotation = rg.Transform.Rotation(math.radians(angle), rotation_center)
        
        # Create the cantilever box
        cantilever_box = rg.Box(rg.Plane.WorldXY, 
                                rg.Interval(0, cantilever_length), 
                                rg.Interval(0, base_width / 2), 
                                rg.Interval(0, cantilever_height)).ToBrep()

        # Apply transformations
        transformed_cantilever = cantilever_box.Duplicate()
        transformed_cantilever.Transform(rg.Transform.Translation(translation))
        transformed_cantilever.Transform(rotation)
        
        cantilevers.append(transformed_cantilever)
    
    # Combine all geometries
    all_geometries = [core] + cantilevers
    
    return all_geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_concept_model(base_length=30, base_width=15, height=12, cantilever_length=8, cantilever_height=10, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_concept_model(base_length=25, base_width=12, height=15, cantilever_length=6, cantilever_height=9, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_concept_model(base_length=40, base_width=20, height=15, cantilever_length=10, cantilever_height=12, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_concept_model(base_length=35, base_width=18, height=14, cantilever_length=9, cantilever_height=11, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_concept_model(base_length=22, base_width=11, height=13, cantilever_length=7, cantilever_height=8, seed=45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
