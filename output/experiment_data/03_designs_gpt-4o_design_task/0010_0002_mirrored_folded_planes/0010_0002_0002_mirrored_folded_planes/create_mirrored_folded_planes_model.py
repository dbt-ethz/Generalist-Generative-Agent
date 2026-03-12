# Created for 0010_0002_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes_model` generates an architectural concept model based on the "Mirrored folded planes" metaphor by creating a series of angular, folded elements that are mirrored across specified axes. It begins by defining a base plane and then introduces folds of random lengths and heights, reflecting the dynamic and complex nature of the design task. The folds are duplicated and mirrored, reinforcing a sense of symmetry and movement. By varying the dimensions and orientations, the function produces a coherent yet intricate spatial narrative, ensuring the model captures the interplay of light and form, as envisioned in the metaphor."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(base_length=30, base_width=20, fold_height=10, mirror_axis='x'):
    \"""
    Creates a Concept Model inspired by the 'Mirrored folded planes' metaphor using a composition of angular, folded elements.
    
    Parameters:
    - base_length: The length of the base plane in meters.
    - base_width: The width of the base plane in meters.
    - fold_height: The height of the folds in meters.
    - mirror_axis: The axis along which the geometry will be mirrored ('x' or 'y').

    Returns:
    - A list of RhinoCommon Brep objects representing the folded planes and mirrored forms.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set seed for replicability
    random.seed(42)

    # Create the base plane
    base_plane = rg.Plane.WorldXY
    base_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(base_length, 0, 0),
        rg.Point3d(base_length, base_width, 0),
        rg.Point3d(0, base_width, 0)
    ]
    base_surface = rg.Brep.CreateFromCornerPoints(base_corners[0], base_corners[1], base_corners[2], base_corners[3], 0.01)

    # Create folds
    folds = []
    for i in range(5):
        fold_length = base_length * (random.uniform(0.1, 0.3))
        fold_start = random.uniform(0, base_length - fold_length)
        fold_plane = rg.Plane(base_corners[0] + rg.Vector3d(fold_start, 0, 0), rg.Vector3d(fold_length, 0, 0), rg.Vector3d(0, 0, 1))
        fold_curve = rg.LineCurve(rg.Point3d(fold_start, 0, 0), rg.Point3d(fold_start + fold_length, 0, fold_height))
        fold_surface = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(fold_curve, rg.Vector3d(0, base_width, 0)))
        folds.append(fold_surface)

    # Mirror the folds
    mirrored_folds = []
    mirror_plane = rg.Plane.WorldYZ if mirror_axis == 'x' else rg.Plane.WorldXY
    for fold in folds:
        mirrored_fold = fold.Duplicate()
        mirrored_fold.Transform(rg.Transform.Mirror(mirror_plane))
        mirrored_folds.append(mirrored_fold)

    # Combine all geometry
    geometry = [base_surface] + folds + mirrored_folds

    return geometry"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(base_length=40, base_width=25, fold_height=15, mirror_axis='y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(base_length=50, base_width=30, fold_height=20, mirror_axis='x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(base_length=35, base_width=22, fold_height=12, mirror_axis='y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(base_length=45, base_width=28, fold_height=18, mirror_axis='x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(base_length=60, base_width=35, fold_height=25, mirror_axis='y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
