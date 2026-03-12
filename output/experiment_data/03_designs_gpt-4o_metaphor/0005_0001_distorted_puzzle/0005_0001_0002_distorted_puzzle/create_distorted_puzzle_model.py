# Created for 0005_0001_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_model` generates an architectural concept model that embodies the metaphor of a "Distorted puzzle" by creating interlocking 3D geometries. It utilizes parameters such as base size, number of elements, and distortion factor to define the scale and complexity of the model. Each puzzle piece is represented as a box, whose corners are randomly distorted, reflecting the metaphor's essence of irregularity and unexpected alignment. By varying these parameters and introducing randomness, the function produces a coherent yet dynamic arrangement of forms that convey visual tension and interconnectedness, aligning with the design intent."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_size, num_elements, distortion_factor, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Distorted puzzle' metaphor.
    
    Parameters:
    - base_size: float, the base size of the bounding box for each puzzle piece in meters.
    - num_elements: int, the number of puzzle pieces to generate.
    - distortion_factor: float, the factor by which the puzzle pieces are distorted.
    - seed: int, random seed for reproducibility.
    
    Returns:
    - List of Breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set random seed for reproducibility
    random.seed(seed)

    geometries = []

    for i in range(num_elements):
        # Randomly generate position for each element within a defined range
        x = random.uniform(-base_size, base_size)
        y = random.uniform(-base_size, base_size)
        z = random.uniform(-base_size / 2, base_size / 2)

        # Create a base box
        box = rg.Box(rg.Plane.WorldXY, rg.Interval(x, x + base_size), rg.Interval(y, y + base_size), rg.Interval(z, z + base_size / 2))
        
        # Distort the box by moving its corners randomly
        distorted_corners = []
        for corner in box.GetCorners():
            dx = random.uniform(-distortion_factor, distortion_factor)
            dy = random.uniform(-distortion_factor, distortion_factor)
            dz = random.uniform(-distortion_factor, distortion_factor)
            distorted_corners.append(rg.Point3d(corner.X + dx, corner.Y + dy, corner.Z + dz))
        
        # Create a distorted Brep from the distorted corners
        distorted_box = rg.Brep.CreateFromCornerPoints(distorted_corners[0], distorted_corners[1], distorted_corners[2], distorted_corners[4], 0.01)
        
        if distorted_box:  # Ensure the Brep was created successfully
            geometries.append(distorted_box)

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
    geometry = create_distorted_puzzle_model(1.5, 15, 0.3, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(3.0, 20, 1.0, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(2.5, 8, 0.8, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(4.0, 12, 0.6, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
