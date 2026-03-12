# Created for 0005_0001_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_model` generates an architectural concept model inspired by the metaphor of a "Distorted puzzle." It creates a collection of interlocking 3D geometries that are intentionally misaligned and irregularly shaped, embodying the metaphor's key traits of complexity and dynamism. By introducing random distortions in position and dimensions for each element, the function ensures a unique arrangement that reflects unexpected fits, enhancing visual interest and movement. The overall structure maintains coherence, resembling a puzzle where pieces connect despite their distortions, effectively translating the metaphor into a tangible architectural representation."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_size, num_elements, max_distortion):
    \"""
    Creates an architectural Concept Model based on the "Distorted puzzle" metaphor.
    
    The function generates a collection of interlocking forms or spaces that are slightly
    misaligned or irregularly shaped, creating a dynamic interplay of parts that fit together
    in unexpected ways.
    
    Parameters:
    - base_size (float): The base size of the elements in meters.
    - num_elements (int): The number of elements to create in the model.
    - max_distortion (float): The maximum distortion applied to each element in meters.
    
    Returns:
    - List[Brep]: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a seed for reproducibility
    random.seed(42)
    
    geometries = []
    
    # Create a basic grid layout for the puzzle pieces
    grid_size = int(num_elements ** 0.5) + 1  # Ensure a sufficient grid size
    spacing = base_size * 1.5  # Spacing between elements
    
    for i in range(num_elements):
        # Calculate grid position
        row = i // grid_size
        col = i % grid_size
        
        # Base position for the element
        base_x = col * spacing
        base_y = row * spacing
        
        # Introduce a random distortion for each element
        distortion_x = random.uniform(-max_distortion, max_distortion)
        distortion_y = random.uniform(-max_distortion, max_distortion)
        
        # Create a distorted box as a puzzle piece
        base_point = rg.Point3d(base_x + distortion_x, base_y + distortion_y, 0)
        
        # Dimensional distortions
        distort_w = random.uniform(base_size * 0.8, base_size * 1.2)
        distort_d = random.uniform(base_size * 0.8, base_size * 1.2)
        distort_h = random.uniform(base_size * 0.8, base_size * 1.2)
        
        # Create distorted box
        box = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), rg.Interval(0, distort_w), rg.Interval(0, distort_d), rg.Interval(0, distort_h))
        
        # Add to geometries list
        geometries.append(box.ToBrep())
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(2.0, 10, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(1.5, 20, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(3.0, 15, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(1.0, 25, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(2.5, 12, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
