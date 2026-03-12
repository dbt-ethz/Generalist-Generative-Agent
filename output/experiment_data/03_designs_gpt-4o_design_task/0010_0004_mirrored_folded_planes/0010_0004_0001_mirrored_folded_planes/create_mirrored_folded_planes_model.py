# Created for 0010_0004_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes_model` generates an architectural concept model inspired by the metaphor of "Mirrored folded planes." By defining a base plane and a specified number of folds, it creates a series of angular, reflective surfaces that embody bilateral symmetry. The function constructs points for folded planes, generates lofted surfaces to represent folds, and mirrors these surfaces to enhance the visual complexity. This process creates dynamic geometries that interplay with light and shadow, while layering spaces to evoke a sense of depth and discovery, aligning with the design task's requirements for spatial organization and aesthetic balance."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(base_length=10, base_width=5, fold_height=3, num_folds=3):
    \"""
    Creates an architectural Concept Model based on the 'Mirrored folded planes' metaphor.
    
    Parameters:
    - base_length (float): The length of the base plane (in meters).
    - base_width (float): The width of the base plane (in meters).
    - fold_height (float): The height of each fold (in meters).
    - num_folds (int): The number of folds to create on one side.
    
    Returns:
    - List[Brep]: A list of Brep objects representing the folded and mirrored planes.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set seed for reproducibility
    random.seed(42)
    
    # Create base plane
    base_plane = rg.Plane.WorldXY

    # Define the points for the folded planes
    points = []
    fold_step = base_length / num_folds

    for i in range(num_folds + 1):
        x = i * fold_step
        y = base_width / 2
        z = 0 if i % 2 == 0 else fold_height
        points.append(rg.Point3d(x, y, z))

    # Create folds using lines and loft them into surfaces
    folds = []
    for i in range(len(points) - 1):
        line1 = rg.Line(points[i], rg.Point3d(points[i].X, -points[i].Y, points[i].Z))
        line2 = rg.Line(points[i + 1], rg.Point3d(points[i + 1].X, -points[i + 1].Y, points[i + 1].Z))
        loft = rg.Brep.CreateFromLoft([line1.ToNurbsCurve(), line2.ToNurbsCurve()], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        if loft:
            folds.extend(loft)
    
    # Mirror the folds about the YZ plane
    for fold in folds[:]:
        mirrored_fold = fold.DuplicateBrep()
        mirrored_fold.Transform(rg.Transform.Mirror(rg.Plane.WorldYZ))
        folds.append(mirrored_fold)

    # Return the list of Brep objects
    return folds"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(base_length=15, base_width=7, fold_height=4, num_folds=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(base_length=12, base_width=6, fold_height=2, num_folds=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(base_length=8, base_width=4, fold_height=2, num_folds=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(base_length=20, base_width=10, fold_height=5, num_folds=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(base_length=18, base_width=9, fold_height=3, num_folds=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
