# Created for 0005_0005_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_concept_model` generates an architectural concept model based on the 'Distorted Puzzle' metaphor by creating an array of fragmented, interlocking volumes. Each volume is randomly positioned and varies in dimensions, contributing to a dynamic play of light and shadow. The use of asymmetric shapes and varying heights aligns with the metaphor's essence, evoking tension and equilibrium. The model promotes a balance between individuality and unity, allowing for diverse spatial experiences that transition between open and enclosed areas. This results in a visually complex structure that reflects the interconnectedness of a distorted puzzle."""

#! python 3
function_code = """def create_distorted_puzzle_concept_model(base_center, num_volumes, base_size, max_height, random_seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Distorted Puzzle' metaphor.
    
    The model consists of fragmented, interlocking volumes with varying heights and forms.
    These volumes are assembled to create a dynamic play of light and shadow, reflecting the 
    metaphor of a distorted puzzle where each piece is distinct yet part of a cohesive whole.

    Parameters:
    - base_center: tuple of floats (x, y, z), representing the center point of the base plane.
    - num_volumes: int, the number of volumes to generate.
    - base_size: float, the base size of the volumes footprint.
    - max_height: float, the maximum height of any volume.
    - random_seed: int, seed for the random number generator to ensure replicable results.

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometries of the model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(random_seed)
    volumes = []

    for i in range(num_volumes):
        # Randomize position
        x_offset = random.uniform(-base_size, base_size)
        y_offset = random.uniform(-base_size, base_size)
        base_point = rg.Point3d(base_center[0] + x_offset, base_center[1] + y_offset, base_center[2])
        
        # Randomize dimensions
        width = random.uniform(base_size * 0.5, base_size)
        depth = random.uniform(base_size * 0.5, base_size)
        height = random.uniform(max_height * 0.3, max_height)
        
        # Create base plane
        base_plane = rg.Plane(base_point, rg.Vector3d.ZAxis)
        
        # Create a distorted box
        box_corners = [
            base_plane.PointAt(-width/2, -depth/2, 0),
            base_plane.PointAt(width/2, -depth/2, 0),
            base_plane.PointAt(width/2, depth/2, 0),
            base_plane.PointAt(-width/2, depth/2, 0),
            base_plane.PointAt(random.uniform(-width/2, width/2), random.uniform(-depth/2, depth/2), height)
        ]
        
        # Create a Brep from the corner points
        box_brep = rg.Brep.CreateFromCornerPoints(box_corners[0], box_corners[1], box_corners[2], box_corners[3], 0.001)
        if box_brep:
            volumes.append(box_brep)
        
    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_concept_model((0, 0, 0), 10, 5, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_concept_model((1, 1, 0), 8, 4, 10, random_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_concept_model((-5, 3, 0), 15, 6, 20, random_seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_concept_model((2, -2, 0), 12, 7, 25, random_seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_concept_model((3, 3, 0), 20, 8, 30, random_seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
