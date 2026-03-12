# Created for 0009_0002_cantilevering_corners.json

""" Summary:
The provided function, `create_cantilevered_concept_model`, generates an architectural concept model inspired by the metaphor of "Cantilevering corners." It creates a central base volume and a specified number of cantilevered sections that extend outward at various angles, embodying dynamic tension and stability. The function employs parameters to define the dimensions and characteristics of both the base and cantilevers. Using randomization for angles, it introduces varied projections that enhance spatial intrigue and interaction with light and shadow. Ultimately, the model reflects the metaphor's essence, showcasing a balance between grounded structure and daring extensions."""

#! python 3
function_code = """def create_cantilevered_concept_model(base_length=10, base_width=10, base_height=3, num_cantilevers=4, cantilever_length=5, cantilever_height=2, seed=42):
    \"""
    Creates an architectural Concept Model based on the metaphor of 'Cantilevering corners'.
    
    This function generates a central base volume with cantilevered sections projecting
    outward at various angles, creating a balance between stability and dynamic tension.
    
    Parameters:
    - base_length (float): Length of the central base volume in meters.
    - base_width (float): Width of the central base volume in meters.
    - base_height (float): Height of the central base volume in meters.
    - num_cantilevers (int): Number of cantilevered sections to create.
    - cantilever_length (float): Length of each cantilevered section in meters.
    - cantilever_height (float): Height of each cantilevered section in meters.
    - seed (int): Seed for random generation to ensure replicability.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    import Rhino
    import random
    from math import radians, sin, cos
    
    random.seed(seed)
    
    # Create the central base volume
    base_plane = Rhino.Geometry.Plane.WorldXY
    base_corners = [
        base_plane.Origin,
        base_plane.Origin + Rhino.Geometry.Vector3d(base_length, 0, 0),
        base_plane.Origin + Rhino.Geometry.Vector3d(base_length, base_width, 0),
        base_plane.Origin + Rhino.Geometry.Vector3d(0, base_width, 0)
    ]
    base_surface = Rhino.Geometry.Brep.CreateFromCornerPoints(base_corners[0], base_corners[1], base_corners[2], base_corners[3], 0.01)
    base_solid = base_surface.CapPlanarHoles(Rhino.RhinoDoc.ActiveDoc.ModelAbsoluteTolerance)
    
    geometries = [base_solid]
    
    # Create cantilevered sections
    for i in range(num_cantilevers):
        angle = random.uniform(0, 360)  # Cantilever angle
        translation_vector = Rhino.Geometry.Vector3d(
            cantilever_length * cos(radians(angle)), 
            cantilever_length * sin(radians(angle)), 
            0)
        
        cantilever_corners = [
            base_plane.Origin + translation_vector,
            base_plane.Origin + translation_vector + Rhino.Geometry.Vector3d(cantilever_length, 0, 0),
            base_plane.Origin + translation_vector + Rhino.Geometry.Vector3d(cantilever_length, cantilever_length, 0),
            base_plane.Origin + translation_vector + Rhino.Geometry.Vector3d(0, cantilever_length, 0)
        ]
        cantilever_surface = Rhino.Geometry.Brep.CreateFromCornerPoints(cantilever_corners[0], cantilever_corners[1], cantilever_corners[2], cantilever_corners[3], 0.01)
        cantilever_solid = cantilever_surface.CapPlanarHoles(Rhino.RhinoDoc.ActiveDoc.ModelAbsoluteTolerance)
        
        if cantilever_solid is not None:
            # Move the cantilever to be above the base
            translation_up = Rhino.Geometry.Vector3d(0, 0, base_height + (i * cantilever_height / num_cantilevers))
            cantilever_solid.Translate(translation_up)
            geometries.append(cantilever_solid)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_concept_model(base_length=15, base_width=10, base_height=4, num_cantilevers=3, cantilever_length=6, cantilever_height=3, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_concept_model(base_length=12, base_width=8, base_height=5, num_cantilevers=5, cantilever_length=4, cantilever_height=2, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_concept_model(base_length=20, base_width=15, base_height=6, num_cantilevers=6, cantilever_length=7, cantilever_height=4, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_concept_model(base_length=18, base_width=12, base_height=4, num_cantilevers=2, cantilever_length=8, cantilever_height=3, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_concept_model(base_length=14, base_width=10, base_height=5, num_cantilevers=4, cantilever_length=5, cantilever_height=3, seed=33)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
