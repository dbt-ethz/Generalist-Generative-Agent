# Created for 0010_0004_mirrored_folded_planes.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "Mirrored folded planes" by creating a series of angular, folded surfaces that embody bilateral or radial symmetry. It defines a base plane and iteratively generates multiple layers of folded geometries, each reflecting light and shadow dynamics. Each layer is created through specified parameters like length, width, height, and fold angle, which guide the folding and mirroring process. This results in a cascading organization of spaces, where layers mirror each other, promoting exploration and a sense of depth while achieving structural harmony and visual complexity."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(base_length=12, base_width=6, fold_height=4, num_layers=4, fold_angle=20):
    \"""
    Generates an architectural Concept Model based on the 'Mirrored folded planes' metaphor.

    This function creates a series of folded, angular planes with radial symmetry, designed to reflect 
    a cascading organization of spaces that unfold in layers. The model emphasizes dynamic interplay 
    of light and shadow, along with structural harmony.

    Parameters:
    - base_length (float): Length of the base plane in meters.
    - base_width (float): Width of the base plane in meters.
    - fold_height (float): Height of each fold in meters.
    - num_layers (int): Number of layered folds to generate.
    - fold_angle (float): Angle of folding in degrees.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the folded and mirrored planes.
    \"""
    import Rhino.Geometry as rg
    import math
    
    # Convert fold angle to radians
    fold_angle_rad = math.radians(fold_angle)

    # Create the base plane
    base_plane = rg.Plane.WorldXY

    # Function to create a folded layer
    def create_folded_layer(center, base_length, base_width, fold_height, fold_angle_rad):
        half_length = base_length / 2
        half_width = base_width / 2

        # Define the corner points of the folded plane
        points = [
            rg.Point3d(center.X - half_length, center.Y - half_width, center.Z),
            rg.Point3d(center.X + half_length, center.Y - half_width, center.Z),
            rg.Point3d(center.X + half_length * math.cos(fold_angle_rad), center.Y + half_width, center.Z + fold_height),
            rg.Point3d(center.X - half_length * math.cos(fold_angle_rad), center.Y + half_width, center.Z + fold_height)
        ]

        # Create a Brep from corner points
        return rg.Brep.CreateFromCornerPoints(points[0], points[1], points[2], points[3], 0.01)

    geometries = []
    layer_spacing = fold_height * 1.5

    for i in range(num_layers):
        # Calculate the center for each layer
        center_z = i * layer_spacing
        folded_layer = create_folded_layer(rg.Point3d(0, 0, center_z), base_length, base_width, fold_height, fold_angle_rad)
        if folded_layer:
            geometries.append(folded_layer)
        
            # Create mirrored version around YZ plane
            mirrored_layer = folded_layer.DuplicateBrep()
            mirrored_layer.Transform(rg.Transform.Mirror(rg.Plane.WorldYZ))
            geometries.append(mirrored_layer)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(base_length=10, base_width=5, fold_height=3, num_layers=5, fold_angle=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(base_length=15, base_width=7, fold_height=5, num_layers=3, fold_angle=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(base_length=8, base_width=4, fold_height=2, num_layers=6, fold_angle=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(base_length=14, base_width=7, fold_height=6, num_layers=4, fold_angle=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(base_length=20, base_width=10, fold_height=8, num_layers=2, fold_angle=45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
