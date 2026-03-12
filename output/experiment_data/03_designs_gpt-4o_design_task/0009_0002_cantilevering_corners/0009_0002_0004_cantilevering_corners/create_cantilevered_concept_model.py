# Created for 0009_0002_cantilevering_corners.json

""" Summary:
The provided function, `create_cantilevered_concept_model`, generates an architectural concept model based on the metaphor of "Cantilevering corners." It creates a central core structure and adds a series of cantilevered volumes that extend outward at various angles and lengths. This dynamic arrangement reflects the balance between stability and motion, as described in the metaphor. By randomly selecting projection angles and lengths, the model emphasizes the interaction between the core and cantilevered elements, creating intriguing spatial relationships. The result is a visually captivating structure that invites exploration and dialogue with its environment, embodying the essence of the metaphor."""

#! python 3
function_code = """def create_cantilevered_concept_model(base_size, num_cantilevers, max_cantilever_length, max_cantilever_angle):
    \"""
    Creates an architectural Concept Model embodying the metaphor of 'Cantilevering corners'.
    
    This function generates a series of interconnected volumes where each volume projects outward 
    at various angles and lengths from a central core, creating a dynamic balance between stability 
    and motion. The core structure is emphasized by the distinct transition to the cantilevered sections.

    Parameters:
    - base_size (float): The size of the central core structure in meters.
    - num_cantilevers (int): The number of cantilevered volumes to create around the core.
    - max_cantilever_length (float): The maximum length a cantilevered volume can extend in meters.
    - max_cantilever_angle (float): The maximum angle in degrees at which a cantilevered volume can project from the core.

    Returns:
    - list: A list of RhinoCommon Breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    # Set a seed for reproducibility
    random.seed(42)
    
    # Create the central core as a cube
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-base_size/2, base_size/2), rg.Interval(-base_size/2, base_size/2), rg.Interval(0, base_size))
    core = core_box.ToBrep()
    concept_model = [core]
    
    # Function to create a cantilevered volume
    def create_cantilever(base, length, angle):
        # Get the faces of the base Brep
        faces = base.Faces
        # Randomly choose a face of the base Brep to project from
        face_index = random.randint(0, faces.Count - 1)
        face = faces[face_index]
        face_center = face.PointAt(face.Domain(0).Mid, face.Domain(1).Mid)
        
        # Calculate the projection direction
        direction = rg.Vector3d(face.NormalAt(face.Domain(0).Mid, face.Domain(1).Mid))
        direction.Rotate(math.radians(random.uniform(-angle, angle)), rg.Vector3d.ZAxis)
        
        # Create the cantilever geometry
        offset_point = face_center + direction * length
        cantilever_box = rg.Box(rg.Plane(offset_point, direction), rg.Interval(-base_size/4, base_size/4), rg.Interval(-base_size/4, base_size/4), rg.Interval(0, base_size/2))
        cantilever_brep = cantilever_box.ToBrep()
        
        return cantilever_brep
    
    # Add cantilevered volumes
    for _ in range(num_cantilevers):
        length = random.uniform(base_size/2, max_cantilever_length)
        angle = random.uniform(0, max_cantilever_angle)
        cantilever = create_cantilever(core, length, angle)
        concept_model.append(cantilever)
    
    return concept_model"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_concept_model(5.0, 10, 3.0, 45.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_concept_model(10.0, 5, 4.0, 30.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_concept_model(7.5, 8, 2.5, 60.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_concept_model(6.0, 12, 5.0, 50.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_concept_model(8.0, 15, 6.0, 40.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
