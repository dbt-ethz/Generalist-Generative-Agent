# Created for 0005_0003_distorted_puzzle.json

""" Summary:
The provided function, `create_distorted_puzzle_model`, generates an architectural concept model based on the "Distorted puzzle" metaphor by creating a series of interconnected geometric elements that are slightly twisted and rotated. It takes parameters such as base dimensions, twist factor, and room count to create visual complexity and dynamic imbalance. Each room is represented as a randomized box that undergoes a unique twisting transformation, enhancing the sense of playfulness and exploration. The resulting model maintains coherence through the interdependent arrangement of these forms, evoking a feeling of movement and unexpected transitions within the space."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_length, base_width, base_height, twist_factor, room_count, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Distorted puzzle' metaphor.
    
    The model consists of a series of interconnected geometric elements that are slightly twisted or rotated
    relative to each other, creating a dynamic and visually complex form. The design emphasizes the interplay
    of varying scales and orientations to evoke a sense of exploration and transformation.
    
    Parameters:
    - base_length: float, the base length of the initial geometric block.
    - base_width: float, the base width of the initial geometric block.
    - base_height: float, the base height of the initial geometric block.
    - twist_factor: float, the maximum degree of twisting or rotation applied to the elements.
    - room_count: int, the number of interconnected rooms or blocks in the model.
    - seed: int, the seed for the random generator to ensure replicability.
    
    Returns:
    - list of Brep: A list of 3D geometries representing the distorted puzzle concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    random.seed(seed)
    geometries = []

    for i in range(room_count):
        # Randomize dimensions slightly to create variation
        length = base_length * (0.8 + 0.4 * random.random())
        width = base_width * (0.8 + 0.4 * random.random())
        height = base_height * (0.8 + 0.4 * random.random())

        # Create a base box
        base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))

        # Apply a random twist to the box
        twist_angle = twist_factor * random.uniform(-1, 1)
        twist_axis = rg.Line(base_box.Center, rg.Point3d(base_box.Center.X, base_box.Center.Y, base_box.Center.Z + height))
        twisted_box = rg.Transform.Rotation(math.radians(twist_angle), twist_axis.Direction, twist_axis.From)
        
        brep_box = base_box.ToBrep()
        brep_box.Transform(twisted_box)
        
        # Offset the box position for next iteration
        x_offset = length * random.uniform(0.5, 1.5)
        y_offset = width * random.uniform(0.5, 1.5)
        z_offset = height * random.uniform(0.1, 0.5)
        
        translation = rg.Transform.Translation(x_offset, y_offset, z_offset)
        brep_box.Transform(translation)
        
        # Add the transformed box to the list of geometries
        geometries.append(brep_box)
        
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(10, 5, 3, 45, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(15, 7, 4, 30, 10, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(12, 6, 2, 60, 5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(8, 4, 5, 90, 12, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(20, 10, 6, 15, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
