# Created for 0010_0005_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes_model_v2` generates an architectural concept model based on the metaphor of "Mirrored folded planes." It constructs a series of interlocked, angular forms that reflect across multiple axes, embodying dynamic equilibrium. By defining parameters such as base dimensions, fold angles, and the number of folds, the function creates a base plane, applies transformations to fold and mirror it, and generates Brep objects representing the 3D geometry. This approach facilitates a rhythmic interplay of light and shadow, showcasing complexity and coherence, while inviting exploration of the intricate spatial relationships defined by the metaphor."""

#! python 3
function_code = """def create_mirrored_folded_planes_model_v2(base_length, base_width, height, fold_angle, num_folds, seed=None):
    \"""
    Creates an architectural Concept Model based on the 'Mirrored folded planes' metaphor.
    
    This function generates a series of folded planes interlocked and mirrored to form a cohesive,
    intricate design. The model is characterized by dynamic equilibrium and rhythmic interplay of
    light and shadow through strategic folding and arrangement.

    Parameters:
    - base_length (float): The length of the base plane in meters.
    - base_width (float): The width of the base plane in meters.
    - height (float): The height of the folded planes in meters.
    - fold_angle (float): The angle at which each plane is folded in degrees.
    - num_folds (int): Number of folds to create along the base length.
    - seed (int, optional): Seed for randomness to ensure replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    if seed is not None:
        random.seed(seed)
    
    # Calculate the length of each fold section
    section_length = base_length / num_folds
    fold_angle_rad = math.radians(fold_angle)

    breps = []
    
    # Create the base plane
    for i in range(num_folds):
        # Fold line point calculation
        startPt = rg.Point3d(i * section_length, 0, 0)
        endPt = rg.Point3d((i + 1) * section_length, 0, 0)
        
        # Create a fold plane
        fold_line = rg.Line(startPt, endPt)
        rotation_axis = rg.Vector3d(0, 0, 1)
        fold_transform = rg.Transform.Rotation(fold_angle_rad if i % 2 == 0 else -fold_angle_rad, rotation_axis, startPt)
        
        # Define the corners of the plane before the fold
        corners = [
            startPt,
            rg.Point3d(startPt.X, base_width, 0),
            rg.Point3d(endPt.X, base_width, 0),
            endPt
        ]
        
        # Create and transform the plane
        plane_brep = rg.Brep.CreateFromCornerPoints(corners[0], corners[1], corners[2], corners[3], 0.01)
        plane_brep.Transform(fold_transform)
        
        # Mirror the plane
        mirror_transform = rg.Transform.Mirror(rg.Plane.WorldYZ)
        mirrored_brep = plane_brep.DuplicateBrep()
        mirrored_brep.Transform(mirror_transform)
        
        breps.extend([plane_brep, mirrored_brep])
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model_v2(10.0, 5.0, 3.0, 30.0, 6, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model_v2(8.0, 4.0, 2.5, 45.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model_v2(12.0, 6.0, 4.0, 60.0, 8, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model_v2(15.0, 7.0, 5.0, 22.5, 4, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model_v2(14.0, 3.0, 2.0, 90.0, 7, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
