# Created for 0010_0004_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes_model_v2` generates an architectural concept model that embodies the metaphor of "Mirrored folded planes." By creating a series of angular, folded surfaces with bilateral or radial symmetry, the function captures the essence of dynamic movement and depth. Each layer of folds is strategically designed to reflect and cascade, enhancing the spatial organization and creating a rhythmic interplay of solid and void. The model emphasizes light and shadow through the choice of materials and geometric configurations, resulting in a visually complex yet harmonious structure that invites exploration and progression through its layered geometries."""

#! python 3
function_code = """def create_mirrored_folded_planes_model_v2(base_length=10.0, base_width=5.0, fold_height=3.0, num_layers=4, symmetry_axis='y'):
    \"""
    Creates an architectural Concept Model embodying the 'Mirrored folded planes' metaphor.

    This function generates a series of angular, folded surfaces with bilateral symmetry,
    designed to create a cascading organization of spaces that unfold in layers.
    The model emphasizes light and shadow interplay and the balance between visual complexity and structural harmony.

    Parameters:
    - base_length (float): The length of the base plane in meters.
    - base_width (float): The width of the base plane in meters.
    - fold_height (float): The height of each fold in meters.
    - num_layers (int): The number of mirrored folded layers.
    - symmetry_axis (str): The axis along which the structure will be mirrored ('x' or 'y').

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the folded and mirrored planes.
    \"""
    import Rhino.Geometry as rg
    import math

    # Helper function to create a single folded plane
    def create_folded_plane(center, length, width, height):
        half_length = length / 2
        half_width = width / 2
        points = [
            rg.Point3d(center.X - half_length, center.Y - half_width, center.Z),
            rg.Point3d(center.X + half_length, center.Y - half_width, center.Z),
            rg.Point3d(center.X + half_length, center.Y + half_width, center.Z + height),
            rg.Point3d(center.X - half_length, center.Y + half_width, center.Z + height)
        ]
        return rg.Brep.CreateFromCornerPoints(points[0], points[1], points[2], points[3], 0.01)

    # Calculate layer spacing and initialize geometries list
    layer_spacing = fold_height * 1.5
    geometries = []

    for i in range(num_layers):
        # Calculate the center of each layer
        center_x = 0 if symmetry_axis == 'y' else i * layer_spacing
        center_y = i * layer_spacing if symmetry_axis == 'y' else 0
        center = rg.Point3d(center_x, center_y, 0)

        # Create folded plane and add to geometries
        folded_plane = create_folded_plane(center, base_length, base_width, fold_height)
        if folded_plane:
            geometries.append(folded_plane)

            # Mirror the plane
            mirror_plane = rg.Plane.WorldYZ if symmetry_axis == 'x' else rg.Plane.WorldXY
            mirrored_plane = folded_plane.DuplicateBrep()
            mirrored_plane.Transform(rg.Transform.Mirror(mirror_plane))
            geometries.append(mirrored_plane)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model_v2(base_length=15.0, base_width=7.0, fold_height=4.0, num_layers=5, symmetry_axis='x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model_v2(base_length=12.0, base_width=6.0, fold_height=2.5, num_layers=3, symmetry_axis='y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model_v2(base_length=20.0, base_width=10.0, fold_height=5.0, num_layers=6, symmetry_axis='x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model_v2(base_length=18.0, base_width=9.0, fold_height=3.5, num_layers=4, symmetry_axis='y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model_v2(base_length=25.0, base_width=12.0, fold_height=6.0, num_layers=2, symmetry_axis='x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
