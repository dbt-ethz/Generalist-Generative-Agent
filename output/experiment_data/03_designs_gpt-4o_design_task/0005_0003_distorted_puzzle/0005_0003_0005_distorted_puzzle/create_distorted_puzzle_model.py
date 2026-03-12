# Created for 0005_0003_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_model` generates an architectural concept model inspired by the "Distorted puzzle" metaphor. It creates a series of interdependent rooms, each defined by random dimensions and angles, reflecting the metaphor's themes of playful complexity and dynamic imbalance. Each room is represented as a 3D box, which is twisted and rotated based on specified parameters, enhancing visual tension. The rooms are positioned to form a cohesive network of pathways, guiding exploration through a space that evokes transformation. This approach captures the essence of the metaphor by balancing disorder with structural coherence, reminiscent of an intricate puzzle."""

#! python 3
function_code = """def create_distorted_puzzle_model(seed, room_count, min_size, max_size, twist_angle):
    \"""
    Creates an architectural Concept Model based on the 'Distorted puzzle' metaphor.
    
    Args:
        seed (int): Seed for random number generator to ensure replicability.
        room_count (int): Number of interdependent rooms to create in the model.
        min_size (float): Minimum dimension for the rooms (in meters).
        max_size (float): Maximum dimension for the rooms (in meters).
        twist_angle (float): Maximum angle for twisting or rotating each room element (in degrees).
        
    Returns:
        list: A list of RhinoCommon Breps representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    random.seed(seed)
    
    geometries = []
    current_position = rg.Point3d(0, 0, 0)
    
    for _ in range(room_count):
        # Randomly determine room size
        width = random.uniform(min_size, max_size)
        length = random.uniform(min_size, max_size)
        height = random.uniform(min_size, max_size)
        
        # Create a box representing the room
        room_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, width), rg.Interval(0, length), rg.Interval(0, height))
        brep_room = room_box.ToBrep()
        
        # Apply random rotation to the room
        rotation_axis = rg.Vector3d(random.choice([1, 0, 0]), random.choice([0, 1, 0]), random.choice([0, 0, 1]))
        rotation_angle = random.uniform(-twist_angle, twist_angle)
        rotation_transform = rg.Transform.Rotation(math.radians(rotation_angle), rotation_axis, current_position)
        
        brep_room.Transform(rotation_transform)
        
        # Translate to current position
        translation_transform = rg.Transform.Translation(current_position - rg.Point3d(0, 0, 0))
        brep_room.Transform(translation_transform)
        
        # Store the geometry
        geometries.append(brep_room)
        
        # Update current position for the next room, creating a path-like connection
        current_position += rg.Vector3d(width * 0.5, length * 0.5, height * 0.5)
        
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(seed=42, room_count=5, min_size=3.0, max_size=10.0, twist_angle=45.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(seed=7, room_count=10, min_size=2.0, max_size=8.0, twist_angle=30.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(seed=12, room_count=8, min_size=4.0, max_size=12.0, twist_angle=60.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(seed=99, room_count=6, min_size=5.0, max_size=15.0, twist_angle=90.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(seed=21, room_count=7, min_size=2.5, max_size=9.5, twist_angle=75.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
