# Created for 0005_0001_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_model` generates an architectural concept model reflecting the "Distorted Puzzle" metaphor by creating interlocking geometries that are slightly misaligned and irregularly shaped. It uses parameters like base size, number of pieces, and distortion factor to define the model's characteristics. Each piece is distorted randomly, introducing unpredictability while retaining coherence through their interconnected nature. This dynamic interplay results in a visually intriguing structure, embodying movement and tension, appropriate for architectural exploration. The function outputs a list of 3D geometries, enabling further manipulation and visualization in design software like Rhino and Grasshopper."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_size, num_pieces, distortion_factor, seed):
    \"""
    Creates an architectural Concept Model based on the metaphor 'Distorted Puzzle'.
    
    This function generates a model characterized by a complex, interlocking arrangement of forms
    that are slightly misaligned or irregularly shaped. It reflects a dynamic interplay of parts
    that fit together in unexpected ways, creating a sense of movement and tension.

    Parameters:
    - base_size: float, the base size of each puzzle piece (in meters).
    - num_pieces: int, the number of puzzle pieces to generate.
    - distortion_factor: float, a factor that controls the degree of distortion applied to each piece.
    - seed: int, seed for random number generation to ensure replicability.
    
    Returns:
    - list of Rhino.Geometry.Brep: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    pieces = []
    offset_distance = base_size * 0.1  # Offset for creating interlocking nature

    for i in range(num_pieces):
        # Calculate a random position for the base of the piece
        x = random.uniform(-base_size, base_size)
        y = random.uniform(-base_size, base_size)
        z = random.uniform(0, base_size * 0.5)
        
        # Create a base box
        box = rg.Box(rg.Plane.WorldXY, rg.Interval(x, x + base_size), rg.Interval(y, y + base_size), rg.Interval(z, z + base_size))
        
        # Distort the box by moving its corners
        pts = list(box.GetCorners())
        for pt in pts:
            distortion = rg.Vector3d(
                random.uniform(-distortion_factor, distortion_factor),
                random.uniform(-distortion_factor, distortion_factor),
                random.uniform(-distortion_factor, distortion_factor)
            )
            pt.Transform(rg.Transform.Translation(distortion))
        
        # Create a Brep from the distorted box
        distorted_box = rg.Brep.CreateFromCornerPoints(pts[0], pts[1], pts[2], pts[4], 0.01)
        
        if distorted_box:  # Ensure the Brep creation is successful
            pieces.append(distorted_box)
        
    return pieces"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(2.0, 10, 0.5, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(1.5, 20, 0.3, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(3.0, 15, 0.8, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(1.0, 5, 0.2, 12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(2.5, 12, 0.4, 88)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
