# Created for 0009_0002_cantilevering_corners.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "Cantilevering corners" by creating a core structure and a series of interconnected volumes. Each volume is designed to extend outward at varying angles and lengths, embodying the tension between stability and dynamic projection. The function incorporates randomness in the angles, lengths, and widths of the cantilevered elements while maintaining a relationship with the core. By experimenting with layering and stacking, the model evokes a sense of balance and interplay between light, shadow, and space, effectively capturing the metaphors essence of architectural innovation and exploration."""

#! python 3
function_code = """def create_cantilevered_concept_model(base_size=10.0, num_volumes=5, max_cantilever=5.0, seed=42):
    \"""
    Creates an architectural Concept Model based on the metaphor of 'Cantilevering corners'.
    
    The model consists of a series of interconnected volumes where each volume extends outward
    at various angles and lengths, emphasizing the balance and counterbalance between a stable core
    and cantilevered sections. The design explores layering and stacking to create a dynamic interplay
    of volumes, with distinct transitions between core and cantilevered elements.
    
    Parameters:
    - base_size (float): The size of the core base structure in meters.
    - num_volumes (int): The number of cantilevered volumes to generate.
    - max_cantilever (float): The maximum distance a volume can cantilever from the core.
    - seed (int): Seed for randomness to ensure replicability.
    
    Returns:
    - List of Rhino.Geometry.Brep: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    random.seed(seed)
    
    # Create the core base
    core_height = base_size * 0.5
    core_base = rg.Box(rg.Plane.WorldXY, rg.Interval(-base_size/2, base_size/2), rg.Interval(-base_size/2, base_size/2), rg.Interval(0, core_height))
    core_brep = core_base.ToBrep()
    
    geometries = [core_brep]
    
    # Generate cantilevered volumes
    for i in range(num_volumes):
        # Random angles and lengths for cantilevering
        length = random.uniform(base_size * 0.2, max_cantilever)
        width = random.uniform(base_size * 0.1, base_size * 0.3)
        height = random.uniform(base_size * 0.1, base_size * 0.3)
        
        angle_x = random.uniform(-45, 45)
        angle_y = random.uniform(-45, 45)
        
        # Define the cantilevered volume
        volume_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(-width/2, width/2), rg.Interval(0, height))
        
        # Rotate and move the volume
        transform = rg.Transform.Identity
        transform *= rg.Transform.Rotation(math.radians(angle_x), rg.Vector3d.ZAxis, rg.Point3d.Origin)
        transform *= rg.Transform.Rotation(math.radians(angle_y), rg.Vector3d.XAxis, rg.Point3d.Origin)
        
        # Offset the cantilevered box from the core
        offset_x = random.choice([-1, 1]) * (base_size/2 + length/2)
        offset_y = random.choice([-1, 1]) * (base_size/2 + width/2)
        offset_z = random.uniform(core_height, core_height + height)
        
        transform *= rg.Transform.Translation(rg.Vector3d(offset_x, offset_y, offset_z))
        
        # Apply transformation and convert to Brep
        volume_box.Transform(transform)
        cantilevered_brep = volume_box.ToBrep()
        
        geometries.append(cantilevered_brep)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevered_concept_model(base_size=12.0, num_volumes=8, max_cantilever=6.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevered_concept_model(base_size=15.0, num_volumes=10, max_cantilever=7.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevered_concept_model(base_size=8.0, num_volumes=4, max_cantilever=4.0, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevered_concept_model(base_size=20.0, num_volumes=6, max_cantilever=8.0, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevered_concept_model(base_size=11.0, num_volumes=7, max_cantilever=5.5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
