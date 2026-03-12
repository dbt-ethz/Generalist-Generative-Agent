# Created for 0010_0003_mirrored_folded_planes.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "Mirrored folded planes" by creating a series of angular, folded geometries that are mirrored across specified axes. The function takes parameters like dimensions and the number of folds to define the complexity of each plane. It constructs a folded geometry using a defined sequence of points and applies a mirroring transformation to create a reflective symmetry. This results in intricate yet coherent forms that promote fluid transitions between spaces, enhancing visual dynamics, light reflection, and shadow play, effectively embodying the metaphor's key traits."""

#! python 3
function_code = """def create_mirrored_folded_planes_model_v2(length, width, height, num_folds, mirror_axis):
    \"""
    Constructs an architectural Concept Model inspired by the "Mirrored folded planes" metaphor.
    
    This function generates a sequence of folded planes that mirror across specified axes, creating
    a dynamic architectural form with an emphasis on symmetry and complexity. The design achieves
    a balance between intricate forms and unified spaces, promoting fluid transitions.

    Parameters:
    - length (float): The length of each plane in meters.
    - width (float): The width of each plane in meters.
    - height (float): The height of the planes, creating vertical variation.
    - num_folds (int): The number of folds in each plane.
    - mirror_axis (str): The axis to mirror the planes across ('x', 'y', or 'z').

    Returns:
    - List of Rhino.Geometry.Brep: A list of Brep geometries representing the mirrored folded planes.
    \"""
    import Rhino.Geometry as rg
    import math

    breps = []
    
    # Helper function to create a single folded plane
    def create_folded_plane(length, width, height, num_folds):
        fold_points = []
        step_length = length / num_folds
        step_height = height / num_folds

        # Create points for the folded geometry
        for i in range(num_folds + 1):
            x = i * step_length
            z = i * step_height if i % 2 == 0 else -i * step_height
            fold_points.append(rg.Point3d(x, 0, z))
        
        # Add width dimension
        fold_points.extend([rg.Point3d(pt.X, width, pt.Z) for pt in reversed(fold_points)])
        
        # Close the polyline
        fold_points.append(fold_points[0])

        # Create and return a brep from the polyline
        polyline = rg.Polyline(fold_points)
        curve = polyline.ToNurbsCurve()
        loft = rg.Brep.CreateFromLoft([curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        return loft[0] if loft else None

    # Generate and mirror the folded planes
    folded_plane = create_folded_plane(length, width, height, num_folds)
    if folded_plane:
        breps.append(folded_plane)

        # Determine the mirror plane
        if mirror_axis.lower() == 'x':
            mirror_plane = rg.Plane.WorldYZ
        elif mirror_axis.lower() == 'y':
            mirror_plane = rg.Plane.WorldXZ
        elif mirror_axis.lower() == 'z':
            mirror_plane = rg.Plane.WorldXY
        else:
            raise ValueError("Invalid mirror axis. Choose 'x', 'y', or 'z'.")

        mirrored_plane = folded_plane.DuplicateBrep()
        mirrored_plane.Transform(rg.Transform.Mirror(mirror_plane))
        breps.append(mirrored_plane)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model_v2(10.0, 5.0, 3.0, 4, 'y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model_v2(15.0, 7.0, 4.0, 3, 'z')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model_v2(12.0, 6.0, 5.0, 5, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model_v2(8.0, 4.0, 2.0, 6, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model_v2(20.0, 10.0, 8.0, 2, 'z')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
