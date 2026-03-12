# Created for 0010_0004_mirrored_folded_planes.json

""" Summary:
The provided function, `generate_mirrored_folded_planes`, creates an architectural concept model inspired by the metaphor "Mirrored folded planes." It generates a series of angular, folded surfaces organized in either radial or bilateral symmetry, embodying the dynamic interplay of solid and void, light and shadow. By defining parameters like base size, fold height, and the number of planes, the function strategically folds and mirrors geometries to enhance depth and movement. The resulting model reflects a cascading spatial arrangement, promoting exploration and discovery, while balancing visual complexity with structural harmony, effectively translating the metaphor into a physical form."""

#! python 3
function_code = """def generate_mirrored_folded_planes(base_size=10.0, fold_height=4.0, num_planes=5, symmetry_type='radial'):
    \"""
    Generates an architectural Concept Model based on the 'Mirrored folded planes' metaphor.
    
    This function creates a series of angular, folded planes organized in a radial or bilateral symmetry.
    The design aims to create depth and movement through strategic folding and mirroring, emphasizing the 
    interplay of light and shadow and the balance between visual complexity and structural harmony.
    
    Parameters:
    - base_size (float): The base dimension of the folded planes in meters.
    - fold_height (float): The height of each fold in meters.
    - num_planes (int): The number of folded planes in the model.
    - symmetry_type (str): Type of symmetry to apply ('radial' or 'bilateral').
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the folded and mirrored planes.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    # Seed for reproducibility
    random.seed(42)

    # Helper function to create a folded plane
    def create_folded_plane(base_size, fold_height, angle_offset):
        # Define plane points
        p1 = rg.Point3d(0, 0, 0)
        p2 = rg.Point3d(base_size, 0, 0)
        p3 = rg.Point3d(base_size, base_size, fold_height)
        p4 = rg.Point3d(0, base_size, fold_height)

        # Rotate points around Z-axis to create fold
        transform = rg.Transform.Rotation(angle_offset, rg.Point3d(0, 0, 0))
        p1.Transform(transform)
        p2.Transform(transform)
        p3.Transform(transform)
        p4.Transform(transform)

        # Create Brep from corner points
        return rg.Brep.CreateFromCornerPoints(p1, p2, p3, p4, 0.01)

    # Generate folded planes
    folded_planes = []
    angle_step = (math.pi * 2) / num_planes if symmetry_type == 'radial' else math.pi / num_planes
    
    for i in range(num_planes):
        angle_offset = i * angle_step
        folded_plane = create_folded_plane(base_size, fold_height, angle_offset)
        if folded_plane:
            folded_planes.append(folded_plane)

    # Apply symmetry by mirroring or rotating
    mirrored_planes = []
    for plane in folded_planes:
        if symmetry_type == 'radial':
            mirrored_plane = plane.DuplicateBrep()
            mirrored_plane.Transform(rg.Transform.Rotation(math.pi, rg.Point3d(0, 0, 0)))
            mirrored_planes.append(mirrored_plane)
        elif symmetry_type == 'bilateral':
            mirrored_plane = plane.DuplicateBrep()
            mirrored_plane.Transform(rg.Transform.Mirror(rg.Plane.WorldYZ))
            mirrored_planes.append(mirrored_plane)

    # Combine original and mirrored planes
    all_planes = folded_planes + mirrored_planes
    
    return all_planes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_mirrored_folded_planes(base_size=15.0, fold_height=6.0, num_planes=8, symmetry_type='bilateral')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_mirrored_folded_planes(base_size=12.0, fold_height=3.0, num_planes=6, symmetry_type='radial')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_mirrored_folded_planes(base_size=20.0, fold_height=5.0, num_planes=10, symmetry_type='radial')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_mirrored_folded_planes(base_size=18.0, fold_height=7.0, num_planes=4, symmetry_type='bilateral')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_mirrored_folded_planes(base_size=14.0, fold_height=2.0, num_planes=7, symmetry_type='radial')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
