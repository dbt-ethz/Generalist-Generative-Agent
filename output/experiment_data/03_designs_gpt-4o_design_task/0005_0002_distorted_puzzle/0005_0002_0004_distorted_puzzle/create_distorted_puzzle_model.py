# Created for 0005_0002_distorted_puzzle.json

""" Summary:
The provided function, `create_distorted_puzzle_model`, generates an architectural concept model inspired by the "Distorted puzzle" metaphor. It creates a series of fragmented, interconnected modules that are stacked and overlapped, embodying the metaphor's themes of tension and cohesion. Parameters, such as base size and overlap factor, dictate the dimensions and arrangement of each module, while random height variations and slight rotations introduce unpredictability. The resulting spatial arrangement is labyrinthine, promoting exploration through varied perspectives and unexpected transitions, ultimately evoking curiosity and interaction. This approach encapsulates the metaphor's essence, merging complexity with coherence in the design."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_size, num_modules, overlap_factor, height_variation):
    \"""
    Creates an architectural Concept Model based on the 'Distorted puzzle' metaphor.
    
    The function generates a series of fragmented yet interconnected modules that are stacked
    and overlapped to form a cohesive and labyrinthine spatial arrangement. The design explores 
    the interplay of movement, tension, and varied perspectives, challenging traditional notions of order.
    
    Parameters:
    - base_size: float, the base size of individual modules in meters.
    - num_modules: int, the number of modules to create and stack.
    - overlap_factor: float, a factor determining the amount of overlap between modules.
                       Value should be between 0 (no overlap) and 1 (full overlap).
    - height_variation: float, maximum variation in height for each module to introduce randomness.
    
    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math  # Added import for math module
    
    random.seed(42)  # Ensure reproducibility
    
    breps = []
    current_height = 0
    
    for i in range(num_modules):
        # Create a base box module
        base_plane = rg.Plane.WorldXY
        module_width = base_size * (1 + random.uniform(-0.1, 0.1))  # Slight variation in size
        module_depth = base_size * (1 + random.uniform(-0.1, 0.1))
        module_height = base_size * random.uniform(0.5, 1.5) + random.uniform(0, height_variation)
        
        # Define the 3D box
        box_corners = [
            rg.Point3d(0, 0, current_height),
            rg.Point3d(module_width, 0, current_height),
            rg.Point3d(module_width, module_depth, current_height),
            rg.Point3d(0, module_depth, current_height),
            rg.Point3d(0, 0, current_height + module_height),
            rg.Point3d(module_width, 0, current_height + module_height),
            rg.Point3d(module_width, module_depth, current_height + module_height),
            rg.Point3d(0, module_depth, current_height + module_height)
        ]
        
        box = rg.Box(base_plane, box_corners)
        brep = box.ToBrep()
        
        # Add a slight rotation and translation to create the 'distorted puzzle' effect
        angle = random.uniform(-10, 10)  # degrees
        rotation_axis = rg.Vector3d(0, 0, 1)  # Rotate around Z-axis
        center_point = rg.Point3d(module_width/2, module_depth/2, current_height + module_height/2)
        transform_rotation = rg.Transform.Rotation(math.radians(angle), rotation_axis, center_point)
        brep.Transform(transform_rotation)
        
        translation_vector = rg.Vector3d(random.uniform(-overlap_factor, overlap_factor) * base_size,
                                         random.uniform(-overlap_factor, overlap_factor) * base_size,
                                         0)
        transform_translation = rg.Transform.Translation(translation_vector)
        brep.Transform(transform_translation)
        
        # Update current height for next module
        current_height += module_height * (1 - overlap_factor)
        
        breps.append(brep)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(2.0, 5, 0.3, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(1.5, 10, 0.2, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(3.0, 8, 0.4, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(2.5, 6, 0.25, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(1.0, 4, 0.1, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
