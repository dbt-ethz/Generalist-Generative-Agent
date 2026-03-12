# Created for 0010_0003_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes_model` generates an architectural concept model inspired by the metaphor "Mirrored folded planes." It creates a series of angular, folded geometries that are mirrored across specified axes, emphasizing symmetry and balance. The function constructs folded planes by defining a sequence of points and applying alternating fold angles to create depth. After generating these forms, it mirrors them according to the selected axis, enhancing visual complexity while maintaining coherence. The process results in a dynamic model that captures the intricate play of light and shadow, inviting exploration through its layered geometric design."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(length, width, height, fold_count, mirror_axis):
    \"""
    Creates an architectural Concept Model based on the 'Mirrored folded planes' metaphor.

    This function generates a series of angular, folded forms that are mirrored across specified axes.
    The model emphasizes symmetry and balance through the use of mirrored geometries, creating a 
    dynamic and visually engaging environment.

    Parameters:
    - length (float): The length of each folded plane in meters.
    - width (float): The width of each folded plane in meters.
    - height (float): The maximum height of the folded planes in meters.
    - fold_count (int): The number of folds to create along the plane.
    - mirror_axis (str): The axis along which to mirror the geometry ('x', 'y', or 'z').

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the folded and mirrored planes.
    \"""
    import Rhino.Geometry as rg
    import math

    def create_folded_geometry(length, width, height, fold_count):
        \"""Create a folded geometry with a sequence of planes.\"""
        breps = []
        fold_interval = length / fold_count
        for i in range(fold_count):
            # Define the fold angle alternating for each fold
            fold_angle = math.radians(30 if i % 2 == 0 else -30)
            fold_height = height * math.tan(fold_angle)

            # Create points for the base and fold
            pt1 = rg.Point3d(i * fold_interval, 0, 0)
            pt2 = rg.Point3d((i + 1) * fold_interval, 0, 0)
            pt3 = rg.Point3d((i + 1) * fold_interval, width, fold_height)
            pt4 = rg.Point3d(i * fold_interval, width, fold_height)

            # Create a brep from the points
            brep = rg.Brep.CreateFromCornerPoints(pt1, pt2, pt3, pt4, 1e-6)
            if brep:
                breps.append(brep)
        
        return breps

    def mirror_geometries(breps, axis):
        \"""Mirror the given geometries across the specified axis.\"""
        mirrored_breps = []
        if axis == 'x':
            mirror_plane = rg.Plane.WorldYZ
        elif axis == 'y':
            mirror_plane = rg.Plane.WorldZX
        elif axis == 'z':
            mirror_plane = rg.Plane.WorldXY
        else:
            raise ValueError("Invalid mirror axis. Choose 'x', 'y', or 'z'.")

        for brep in breps:
            mirrored_brep = brep.DuplicateBrep()
            mirrored_brep.Transform(rg.Transform.Mirror(mirror_plane))
            mirrored_breps.append(mirrored_brep)

        return mirrored_breps

    # Generate the folded planes
    folded_planes = create_folded_geometry(length, width, height, fold_count)

    # Mirror the folded planes
    mirrored_planes = mirror_geometries(folded_planes, mirror_axis)

    return folded_planes + mirrored_planes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(10.0, 5.0, 3.0, 6, 'z')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(15.0, 8.0, 4.0, 10, 'y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(12.0, 6.0, 2.5, 8, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(20.0, 10.0, 5.0, 12, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(18.0, 9.0, 3.5, 5, 'y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
